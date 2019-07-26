```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/zh-CN/overview/file-system.md
```
# 文件系统

LittlevGL具有文件系统抽象模块，可以连接任何类型的文件系统
该文件系统由一个字母来标识
例如，如果SD卡和字母`'S'`相关联，则可以像`""S:path/to/file.txt`这样来访问文件

## 添加驱动程序

要添加驱动程序，需要像下面这样初始化 `lv_fs_drv_t`：
```c
lv_fs_drv_t drv; 
lv_fs_drv_init(&drv);                     /*基本初始化*/

drv.letter = 'S';                         /* 用于标识驱动器（原文drive，指存储设备，如磁盘驱动器，硬盘驱动器，闪存驱动器等 — 译者注）的大写字母 */
drv.file_size = sizeof(my_file_object);   /*存储文件对象所需的大小*/
drv.rddir_size = sizeof(my_dir_object);   /*存储目录对象所需的大小 (用于dir_open/close/read)*/ 
drv.ready_cb = my_ready_cb;               /*判断驱动器是否可以使用的回调*/
drv.open_cb = my_open_cb;                 /*打开一个文件的回调 */
drv.close_cb = my_close_cb;               /*关闭一个文件的回调 */
drv.read_cb = my_read_cb;                 /*文件读取回调 */
drv.write_cb = my_write_cb;               /*文件写入回调 */
drv.seek_cb = my_seek_cb;                 /*文件seek回调 (移动文件指针) */
drv.tell_cb = my_tell_cb;                 /*描述当前文件指针位置回调  */
drv.trunc_cb = my_trunc_cb;               /*删除文件回调*/
drv.size_cb = my_size_cb;                 /*描述文件大小回调 */
drv.rename_cb = my_size_cb;               /*重命名文件回调 */


drv.dir_open_cb = my_dir_open_cb;         /*打开目录以读取其内容回调 */
drv.dir_read_cb = my_dir_read_cb;         /*读取目录内容回调*/
drv.dir_close_cb = my_dir_close_cb;       /*关闭目录回调*/

drv.free_space_cb = my_size_cb;           /*描述驱动器上的可用空间 */

drv.user_data = my_user_data;             /*如果需要，可自定义任意数据*/

lv_fs_drv_register(&drv);                 /*最后注册硬盘*/

```

任何回调都可以用 `NULL` 来表明操作不支持

如果你使用 `lv_fs_open(&file, "S:/folder/file.txt", LV_FS_MODE_WR)`， LittlevGL会检查以下内容
1. 是否有以字母`'S'` 的驱动器
2. 检查 `open_cb` 是否被实现 (不为`NULL`)
3. 以`"folder/file.txt"`路径调用 `open_cb` 函数集合

## 用法示例

以下示例展示如何读取一个文件：
```c
lv_fs_file_t f;
lv_fs_res_t res;
res = lv_fs_open(&f, "S:folder/file.txt", LV_FS_MODE_RD);
if(res != LV_FS_RES_OK) my_error_handling();

uint32_t read_num;
uint8_t buf[8];
res = lv_fs_read(&f, buf, 8, &read_num);
if(res != LV_FS_RES_OK || read_num != 8) my_error_handling();

lv_fs_close(&f);
```
*`lv_fs_open` 中的模式可以是 `LV_FS_MODE_WR` 表示打开文件以写入或同时为 `LV_FS_MODE_RD | LV_FS_MODE_WR` 表示读写文件*

此示例展示如何读取目录的内容。在目录名称前插入一个 `'/'` 可能是一个好习惯，这取决于驱动程序如何标记目录
```c
lv_fs_dir_t dir;
lv_fs_res_t res;
res = lv_fs_dir_open(&dir, "S:/folder");
if(res != LV_FS_RES_OK) my_error_handling();

char fn[256];
while(1) {
    res = lv_fs_dir_read(&dir, fn);
    if(res != LV_FS_RES_OK) {
        my_error_handling();
        break;
    }

    /*如果没有更多文件可以读取，fn 将是空的*/
    if(strlen(fn) == 0) {
        break;
    }

    printf("%s\n", fn);
}

lv_fs_dir_close(&dir);
```

## 使用驱动器上的图像

[图像](/object-types/img) 对象也可以从文件中打开 (除了存在flash中的变量)

要初始化图片，需要以下回调：
- open
- close
- read
- seek
- tell


## API 

```eval_rst

.. doxygenfile:: lv_fs.h
  :project: lvgl
        
```



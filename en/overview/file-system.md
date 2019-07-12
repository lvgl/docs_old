# File system

LittlevGL has File system abstraction module which enables to attache any type of file system.
The file system are identified by a letter. 
For example if the SD card is associated with  letter`'S'` a file can be reached like `""S:path/to/file.txt`.

## Add a driver

To add a driver an `lv_fs_drv_t` needs to be initialized like this:
```c
lv_fs_drv_t drv; 
lv_fs_drv_init(&drv);                     /*Basic initialization*/

drv.letter = 'S';                         /*An uppercased letter to identify teh drive */
drv.file_size = sizeof(my_file_object);   /*Size required to store a file object*/
drv.rddir_size = sizeof(my_dir_object);   /*Size required to store a directory object (used by dir_open/close/read)*/ 
drv.ready_cb = my_ready_cb;               /*Callback to tell if the drive is ready to use */
drv.open_cb = my_open_cb;                 /*Callback to open a file */
drv.close_cb = my_close_cb;               /*Callback to close a file */
drv.read_cb = my_read_cb;                 /*Callback to read a file */
drv.write_cb = my_write_cb;               /*Callback to write a file */
drv.seek_cb = my_seek_cb;                 /*Callback to seek in a file (Move cursor) */
drv.tell_cb = my_tell_cb;                 /*Callback to tell the cursor position  */
drv.trunc_cb = my_trunc_cb;               /*Callback to delete a file */
drv.size_cb = my_size_cb;                 /*Callback to tell a file's size */
drv.rename_cb = my_size_cb;               /*Callback to rename a file */


drv.dir_open_cb = my_dir_open_cb;         /*Callback to open directory to read its content */
drv.dir_read_cb = my_dir_read_cb;         /*Callback to read a directory's content */
drv.dir_close_cb = my_dir_close_cb;       /*Callback to close a directory */

drv.free_space_cb = my_size_cb;           /*Callback to tell free space on the drive */

drv.user_data = my_user_data;             /*Any custom data if required*/

lv_fs_drv_register(&drv);                 /*Finally register the drive*/

```

Any of the callbacks can be `NULL` to indicate that operation is not supported.

### Use drivers for images

[Image](/object-types/img) objects can be open from files too (besides variables stored i nteh flash)

To initialize the for images the following callbacks are required:
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



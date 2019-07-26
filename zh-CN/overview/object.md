```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/zh-CN/overview/object.md
```
# 对象

在LittlevGL中用户界面的**基本构件**是对象，也叫做*小部件*
举个例子，一个[按钮](/object-types/btn), [标签](/object-types/label), [图像](/object-types/img), [列表](/object-types/list), [图表](/object-types/chart) 或[文本框](/object-types/ta)

在[对象类型](/object-types/index)这里查看所有对象类型

## 对象属性

### 基本属性

对象具有以下与其类型无关的基本属性：
- 位置(Position)
- 大小(Size)
- 父类(Parent)
- 是否可拖拽(Drag enable)
- 是否可点击(Click enable)等等

你可以使用 `lv_obj_set_...` 和 `lv_obj_get_...` 函数来获取或者设置这些属性，比如：

```c
/*设置对象基本属性*/
lv_obj_set_size(btn1, 100, 50);	 /*按钮大小*/
lv_obj_set_pos(btn1, 20,30);      /*按钮位置*/
```

要查看所有可用函数请访问基本对象的[文档](/object-types/obj).

### 专有属性

对象类型也有本身的专有属性，比如，一个滑动条有：
- 最小最大值(Min. max. values)
- 当前值(Current value)
- 自定义样式(Custom styles)

对于这些属性，每个对象类型都具有专门的API函数，例如对于滑动条：

```c
/*设置滑动条专有属性*/
lv_slider_set_range(slider1, 0, 100);	   /*设置最大最小值*/
lv_slider_set_value(slider1, 40, LV_ANIM_ON);	/*设置当前值（位置）*/
lv_slider_set_action(slider1, my_action);     /*设置回调函数*/
```

这些对象类型的API已经描述在他们的 [文档](/object-types/index)中，但是你也可以在他们各自的头文件中核查 (例如 *lv_objx/lv_slider.h*)

## 对象工作机制

### 父子结构

一个父对象可以被视为他所有子对象的容器。每一个对象都只有一个父对象（除了屏幕对象(screens)），但是一个父对象可以拥有不限数量的子对象
父对象的类型没有限制，但是有一些典型的父对象 (例如按钮) 和典型的子对象(例如标签)

### 一起移动(Moving together)

如果父对象的位置改变了，子对象的位置也会随着父对象改变
因此所有位置是相对于父对象的

(0;0) 坐标表示对象的位置会保持在他们各自父对象的左上角

![](/misc/par_child1.png "Objects are moving together 1")

```c
lv_obj_t * par = lv_obj_create(lv_scr_act(), NULL); /*在当前屏幕上创建一个父对象*/
lv_obj_set_size(par, 100, 80);	                   /*设置父对象大小*/

lv_obj_t * obj1 = lv_obj_create(par, NULL);	         /*在前面创建的父对象上创建一个子对象*/
lv_obj_set_pos(obj1, 10, 10);	                   /*为新的子对象设置位置*/
```

修改父对象的位置：
  
![](/misc/par_child2.png "Graphical objects are moving together 2")  

```c
lv_obj_set_pos(par, 50, 50);	/*移动父对象，子对象也会随之移动*/
```

(为简单演示，例子中没有给出调整对象颜色的代码)

### 只可显示在父对象上

如果子对象部分或全部内容溢出父对象，溢出部分会不可见
  
![](/misc/par_child3.png "A graphical object is visible on its parent")  

```c
lv_obj_set_x(obj1, -30);	/*在父对象移动子对象的位置*/
```

### 创建-删除对象

在LittlevGL中，对象可以在运行时被动态的创建或删除
这意味着当前创建的对象只会消耗RAM
例如，如果你需要一个图表，你可以在需要的时候创建它并在他不可见或不需要的时候删除它

每个对象类型有他自己的**创建(create)**原型统一的函数
它需要两个参数：
- 一个父对象的指针，要创建一个屏幕对象请使用*NULL*作为父对象
- 一个可选指针表示另一个相同类型的对象并复制它，当不需要复制其他对象时可以为 *NULL* 
 
独立于对象类型，使用通用变量类型`lv_obj_t`。 之后可以使用此指针来设置或获取对象的属性

创建函数看起来像这样：

```c
lv_obj_t * lv_ <type>_create(lv_obj_t * parent, lv_obj_t * copy);
```

有一个所有对象类型通用的 **删除** 函数，它会删除一个对象和该对象的所有子对象

```c
void lv_obj_del(lv_obj_t * obj);
```

`lv_obj_del` 会立刻删除对象
如果你有某些原因不想立即删除对象，你可以使用 `lv_obj_del_async(obj)`. 
这有时候会很有用，比如你想在 `LV_EVENT_DELETE` 信号中删除一个对象的父对象

你可以只删除一个父对象的子对象而让父对象自己"存活"：

```c
void lv_obj_clean(lv_obj_t * obj);
```

### 屏幕对象(Screen)–最基本的父对象

屏幕对象是一个特殊的对象，因为他自己没有父对象，所以它以这样的方式来创建：
```c
lv_obj_t * scr1 = lv_obj_create(NULL, NULL);
```

在显示时始终会有一个活动(active)的屏幕对象，默认情况下，库会创建并加载一个屏幕对象
要获取当前活动的屏幕对象，可以使用`lv_scr_act()`函数，要加载新的屏幕对象，可以使用`lv_scr_load(scr1)`函数

屏幕对象可以被创建为任何对象类型。例如，一个 [基本对象](/object-types/obj)或一个用一个图像对象作为壁纸


屏幕对象被创建在*默认显示(default display)*
*默认显示* 是最后一个用 `lv_disp_drv_register` 函数注册的屏幕对象 (如果只有一个屏幕对象则使它) 或者你可以显式地通过 `lv_disp_set_default(disp)`来选择
`lv_scr_act()` 和`lv_scr_load()` 操作在当前默认屏幕对象上

访问[多显示器支持](/overview/display) 获取更多内容


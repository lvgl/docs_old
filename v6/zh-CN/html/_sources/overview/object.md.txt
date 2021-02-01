```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/zh-CN/overview/object.md
```
# 对象

In the LittlevGL the **basic building blocks** of a user interface are the objects, also called *Widgets*.
举个例子，一个[按钮](/object-types/btn), [标签](/object-types/label), [图像](/object-types/img), [列表](/object-types/list), [图表](/object-types/chart) 或[文本框](/object-types/ta)

在[对象类型](/object-types/index)这里查看所有对象类型

## 对象属性

### 基本属性

All object types share some basic attributes:
- 位置(Position)
- 大小(Size)
- 父类(Parent)
- 是否可拖拽(Drag enable)
- 是否可点击(Click enable)等等

You can set/get these attributes with `lv_obj_set_...` and `lv_obj_get_...` functions. For example:

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

For these attributes, every object type have unique API functions. For example for a slider:

```c
/*设置滑动条专有属性*/
lv_slider_set_range(slider1, 0, 100);	   /*设置最大最小值*/
lv_slider_set_value(slider1, 40, LV_ANIM_ON);	/*设置当前值（位置）*/
lv_slider_set_action(slider1, my_action);     /*设置回调函数*/
```

这些对象类型的API已经描述在他们的 [文档](/object-types/index)中，但是你也可以在他们各自的头文件中核查 (例如 *lv_objx/lv_slider.h*)

## 对象工作机制

### 父子结构

A parent object can be considered as the container of its children. Every object has exactly one parent object (except screens), but a parent can have an unlimited number of children.
There is no limitation for the type of the parent but, there are typical parent (e.g. button) and typical child (e.g. label) objects.

### 一起移动(Moving together)

If the position of the parent is changed the children will move with the parent.
Therefore all positions are relative to the parent.

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

If a child is partially or fully out of its parent then the parts outside will not be visible.

![](/misc/par_child3.png "A graphical object is visible on its parent")  

```c
lv_obj_set_x(obj1, -30);	/*在父对象移动子对象的位置*/
```

### 创建-删除对象

In LittlevGL objects can be created and deleted dynamically in run-time.
It means only the currently created objects consume RAM.
For example, if you need a chart, you can create it when required and delete it when it is not visible or necessary.

Every object type has its own **create** function with a unified prototype.
It needs two parameters:
- A pointer to the *parent* object. To create a screen give *NULL* as parent.
- Optionally, a pointer to *copy* object with the same type to copy it. This *copy* object can be *NULL* to avoid the copy operation.

All objects are referenced in C code using an `lv_obj_t` pointer as a handle. This pointer can later be used to set or get the attributes of the object.

创建函数看起来像这样：

```c
lv_obj_t * lv_ <type>_create(lv_obj_t * parent, lv_obj_t * copy);
```

有一个所有对象类型通用的 **删除** 函数，它会删除一个对象和该对象的所有子对象

```c
void lv_obj_del(lv_obj_t * obj);
```

`lv_obj_del` will delete the object immediately.
If for any reason you can't delete the object immediately you can use `lv_obj_del_async(obj)`.
It is useful e.g. if you want to delete the parent of an object in the child's `LV_EVENT_DELETE` signal.

You can remove all the children of an object (but not the object itself) using `lv_obj_clean`:

```c
void lv_obj_clean(lv_obj_t * obj);
```

### 屏幕对象(Screen)–最基本的父对象

屏幕对象是一个特殊的对象，因为他自己没有父对象，所以它以这样的方式来创建：
```c
lv_obj_t * scr1 = lv_obj_create(NULL, NULL);
```

There is always an active screen on each display. By default, the library creates and loads a "Base object" as the screen for each display.  
To get the currently active screen use the `lv_scr_act()` function. To load a new one, use `lv_scr_load(scr1)`.

屏幕对象可以被创建为任何对象类型。例如，一个 [基本对象](/object-types/obj)或一个用一个图像对象作为壁纸


Screens are created on the currently selected *default display*.
The *default screen* is the last registered screen with `lv_disp_drv_register` or you can explicitly select a new default display using `lv_disp_set_default(disp)`.
`lv_scr_act()` and `lv_scr_load()` operate on the currently default screen.

Visit [Multi-display support](/overview/display) to learn more.

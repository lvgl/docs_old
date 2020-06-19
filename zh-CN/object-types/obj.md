```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/zh-CN/object-types/obj.md
```
# 基本对象(lv_obj)

## 概览

The 'Base Object' implements the basic properties of an object on a screen, such as:

-坐标(coordinates)
- 父对象(parent object)
- 子对象(children)
- 主样式(main style)
- 属性如*是否可点击(Click enable)*, *是否可拖拽(Drag enable)*等

In object-oriented thinking, it is the base class which all other objects in LittlevGL inherit from. This, among another things, helps reduce code duplication.

### 坐标(Coordinates)
The object size can be modified on individual axes with `lv_obj_set_width(obj, new_width)` and `lv_obj_set_height(obj, new_height)`, or both axes can be modified at the same time with `lv_obj_set_size(obj, new_width, new_height)`.

You can set the x and y coordinates relative to the parent with `lv_obj_set_x(obj, new_x)` and `lv_obj_set_y(obj, new_y)`, or both at the same time with `lv_obj_set_pos(obj, new_x, new_y)`.

You can align the object to another with `lv_obj_align(obj, obj_ref, LV_ALIGN_..., x_shift, y_shift)`.

- `obj` is the object to align.
- `obj_ref` is a reference object. `obj` will be aligned to it. If `obj_ref = NULL`, then the parent of `obj` will be used.
- The third argument is the *type* of alignment. These are the possible options:
![](/misc/align.png "Alignment types in LittlevGL")

  The alignment types build like `LV_ALIGN_OUT_TOP_MID`.
- The last two arguments allow you to shift the object by a specified number of pixels after aligning it.

For example, to align a text below an image: `lv_obj_align(text, image, LV_ALIGN_OUT_BOTTOM_MID, 0, 10)`.   
Or to align a text in the middle of its parent: `lv_obj_align(text, NULL, LV_ALIGN_CENTER, 0, 0)`.

`lv_obj_align_origo` works similarly to `lv_obj_align` but, it aligns the center of the object rather than the top-left corner.

For example, `lv_obj_align_origo(btn, image, LV_ALIGN_OUT_BOTTOM_MID, 0, 0)` will align the center of the button the bottom of the image.

The parameters of the alignment will be saved in the object if `LV_USE_OBJ_REALIGN` is enabled in *lv_conf.h*. You can then realign the objects simply by calling `lv_obj_realign(obj)`. (It's equivalent to calling `lv_obj_align` again with the same parameters.)

If the alignment happened with `lv_obj_align_origo`, then it will be used when the object is realigned.

If `lv_obj_set_auto_realign(obj, true)` is used the object will be realigned automatically, if its size changes in `lv_obj_set_width/height/size()` functions. It's very useful when size animations are applied to the object and the original position needs to be kept.

**Note that the coordinates of screens can't be changed. Attempting to use these functions on screens will result in undefined behavior.**

### 父对象和子对象
You can set a new parent for an object with `lv_obj_set_parent(obj, new_parent)`. To get the current parent, use `lv_obj_get_parent(obj)`.

To get the children of an object, use `lv_obj_get_child(obj, child_prev)` (from last to first) or `lv_obj_get_child_back(obj, child_prev)` (from first to last).
To get the first child, pass `NULL` as the second parameter and use the return value to iterate through the children. The function will return `NULL` if there are no more children. For example:

```c
lv_obj_t * child;
child = lv_obj_get_child(parent, NULL);
while(child) {
    /*使用"子对象" 做一些事情*/
    child = lv_obj_get_child(parent, child);
}
```

`lv_obj_count_children(obj)` 可以获取一个对象的子对象数量，`lv_obj_count_children_recursive(obj)` 也可以获取子对象数量但他会递归加上子对象的子对象数量

### 屏幕对象(Screens)
When you have created a screen like `lv_obj_create(NULL, NULL)`, you can load it with `lv_scr_load(screen1)`. The `lv_scr_act()` function gives you a pointer to the current screen.

如果你有多个显示设备，那么那将非常重要知道这些函数操作在最后创建或明确选择 (通过 `lv_disp_set_default`) 的显示设备上

To get the screen an object is assigned to, use the `lv_obj_get_screen(obj)` function.

### 图层(Layers)
默认有两个自动生成的图层：
- 顶级图层(top layer)
- 系统图层(system layer)

They are independent of the screens and the same layers will be shown on every screen. The *top layer* is above every object on the screen and the *system layer* is above the *top layer* too.
You can add any pop-up windows to the *top layer* freely. But, the *system layer* is restricted to system-level things (e.g. mouse cursor will be placed here in `lv_indev_set_cursor()`).

 `lv_layer_top()` 和`lv_layer_sys()` 函数给出顶级和系统图层的指针

You can bring an object to the foreground or send it to the background with `lv_obj_move_foreground(obj)` and `lv_obj_move_background(obj)`.

Read the [Layer overview](/overview/layer) section to learn more about layers.

### 样式(Style)
The base object stores the [Main style](/overview/style) of the object. To set a new style, use `lv_obj_set_style(obj, &new_style)` function. If `NULL` is set as style, then the object will inherit its parent's style.

Note that, you should use `lv_obj_set_style` only for "Base objects". Every other object type has its own style set function which should be used for them. For example, a button should use `lv_btn_set_style()`.

If you modify a style, which is already used by objects, in order to refresh the affected objects you can use either `lv_obj_refresh_style(obj)` on each object using it or to notify all objects with a given style use `lv_obj_report_style_mod(&style)`. If the parameter of `lv_obj_report_style_mod` is `NULL`, all objects will be notified.

要学习更多关于样式的知识请阅读 [样式概览](/overview/style)。

### 事件(Events)

To set an event callback for an object, use `lv_obj_set_event_cb(obj, event_cb)`,

To manually send an event to an object, use `lv_event_send(obj, LV_EVENT_..., data)`

要了解更多事件的内幕请阅读 [事件概览](/overview/event) 

### 属性(Attributes)
这里有一些属性可以通过`lv_obj_set_...(obj, true/false)` 来启用/关闭 ：

- **hidden** -  Hide the object. It will not be drawn and will be considered by input devices as if it doesn't exist., Its children will be hidden too.
- **click** -  Allows you to click the object via input devices. If disabled, then click events are passed to the object behind this one. (E.g. [Labels](/object-types/label) are not clickable by default)
- **top** -  If enabled then when this object or any of its children is clicked then this object comes to the foreground.
- **drag** - Enable dragging (moving by an input device)
- **drag_dir** - Enable dragging only in specific directions. Can be `LV_DRAG_DIR_HOR/VER/ALL`.
- **drag_throw** - Enable "throwing" with dragging as if the object would have momentum
- **drag_parent** - If enabled then the object's parent will be moved during dragging. It will look like as if the parent is dragged. Checked recursively, so can propagate to grandparents too.
- **parent_event** - Propagate the events to the parents too. Checked recursively, so can propagate to grandparents too.
- **opa_scale_enable** - Enable opacity scaling. See the [#opa-scale](Opa scale) section.

### 透明度(Opa scale)
If `lv_obj_set_opa_scale_enable(obj, true)` is set for an object, then the object's and all of its children's opacity can be adjusted with `lv_obj_set_opa_scale(obj, LV_OPA_...)`.
储存在透明度在样式中的透明度会被此因素影响

使用 [动画](/overview/animation)对一些子对象的淡入淡出非常有用

A little bit of technical background: during the rendering process, the opacity of the object is decided by searching recursively up the object's family tree to find the first object with opacity scaling (Opa scale) enabled.

If an object is found with an enabled *Opa scale*, then that *Opa scale* will be used by the rendered object too.

Therefore, if you want to disable the Opa scaling for an object when the parent has Opa scale, just enable Opa scaling for the object and set its value to `LV_OPA_COVER`. It will overwrite the parent's settings.

### 保护(Protect)
There are some specific actions which happen automatically in the library.
To prevent one or more that kind of actions, you can protect the object against them. The following protections exists:
- **LV_PROTECT_NONE** 不保护
- **LV_PROTECT_POS**  防止自动定位 (例如 在 [容器](/object-types/cont)的布局)
- **LV_PROTECT_FOLLOW** Prevent the object be followed (make a "line break") in automatic ordering (e.g. Layout in [Containers](/object-types/cont))
- **LV_PROTECT_PARENT** 防止父对象自动改变 (例如 [页面](/object-types/page) 在后台移动创建的子对象使其能够滚动)
- **LV_PROTECT_PRESS_LOST** Prevent losing press when the press is slid out of the objects. (E.g. a [Button](/object-types/btn) can be released out of it if it was being pressed)
- **LV_PROTECT_CLICK_FOCUS**防止对象自动聚焦如果他在一个*群组(Group)*中并打开了点击聚焦
- **LV_PROTECT_CHILD_CHG** 关闭子对象改变信号，被库内部使用

 `lv_obj_set/clear_protect(obj, LV_PROTECT_...)` 设置/清除保护，你也可以使用*'OR'ed*保护类型的值

### 群组(Groups)

Once, an object is added to *group* with `lv_group_add_obj(group, obj)` the object's current group can be get with `lv_obj_get_group(obj)`.

`lv_obj_is_focused(obj)` tells if the object is currently focused on its group or not. If the object is not added to a group, `false` will be returned.

要想了解更多关于*群组*的知识，请阅读[输入设备概览](/overview/indev)

### 拓展点击区域(Extended click area)
By default, the objects can be clicked only on their coordinates, however, this area can be extended with `lv_obj_set_ext_click_area(obj, left, right, top, bottom)`.
`left/right/top/bottom` describes how far the clickable area should extend past the default in each direction.

这个功能需要通过*lv_conf.h*的`LV_USE_EXT_CLICK_AREA`来打开，可能的值有：
- **LV_EXT_CLICK_AREA_FULL**  使用`lv_coord_t`保存 了所有4个坐标
- **LV_EXT_CLICK_AREA_TINY**只保存水平(horizontal )和垂直(vertical )的坐标坐标(比  left/right 和 top/bottom 值更好用) 使用 `uint8_t`
- **LV_EXT_CLICK_AREA_OFF** 关闭该功能

## 样式(Styles)

Use `lv_obj_set_style(obj, &style)` to set a style for a base object.

所有`style.body`  属性将会被使用。 显示对象的默认属性是 `lv_style_scr` ，一般对象的默认属性是`lv_style_plain_color` 


## 事件(Events)
只有[通用事件](/overview/event.html#generic-events) 被对象发送

学习更多关于[事件](/overview/event)的知识

## 键(Keys)
No *Keys* are processed by the object type.

学习更多关于 [键](/overview/indev)的知识


## 例子

```eval_rst

.. include:: /lv_examples/src/lv_ex_obj/index.rst

```

## API

```eval_rst

.. doxygenfile:: lv_obj.h
  :project: lvgl

```

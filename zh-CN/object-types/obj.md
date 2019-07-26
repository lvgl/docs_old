```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/zh-CN/object-types/obj.md
```
# 基本对象(lv_obj)

## 概览

基础对象拥有对象的最基础的属性：

-坐标(coordinates)
- 父对象(parent object)
- 子对象(children)
- 主样式(main style)
- 属性如*是否可点击(Click enable)*, *是否可拖拽(Drag enable)*等

### 坐标(Coordinates)
对象的大小可以通过 `lv_obj_set_width(obj, new_width)` 和`lv_obj_set_height(obj, new_height)` 或单一函数  `lv_obj_set_size(obj, new_width, new_height)`来修改

你可以通过 `lv_obj_set_x(obj, new_x)` 和 `lv_obj_set_y(obj, new_y)` 或单一函数`lv_obj_set_pos(obj, new_x, new_y)`来设置x和y相对父对象的坐标

你可以通过 `lv_obj_align(obj, obj_ref, LV_ALIGN_..., x_shift, y_shift)` 来将一个对象与另一个对象对齐
第二个参数是一个引用对象，表示你要对齐到的`对象`。 如果`obj_ref = NULL`，那么父`对象` 将会被使用
第三个参数是对齐的*类型*，可能的选项有：
![](/misc/align.png "Alignment types in LittlevGL")

对齐类型如同 `LV_ALIGN_OUT_TOP_MID`的构建

最后两个参数表示在对齐后x与y的位移

例如，要对齐一个文本到一个图像之下： `lv_obj_align(text, image, LV_ALIGN_OUT_BOTTOM_MID, 0, 10)`.   
或者将一个文本对齐到它父对象的中间： `lv_obj_align(text, NULL, LV_ALIGN_CENTER, 0, 0)`. 

`lv_obj_align_origo` 的作用类似 `lv_obj_align` ，但它对齐的是对象的中点
例如 `lv_obj_align_origo(btn, image, LV_ALIGN_OUT_BOTTOM_MID, 0, 0)`会对齐按钮的中点到图像的下方

对齐的参数会保存在对象中如果 *lv_conf.h* 的 `LV_USE_OBJ_REALIGN` 被启用，你可以通过函数 `lv_obj_realign(obj)`来手动重新对齐对象
它相当于使用相同的参数再次调用 `lv_obj_align`。

如果对齐是由函数 `lv_obj_align_origo` 产生的，那么当对象重新对齐时该函数会被重新调用

如果 `lv_obj_set_auto_realign(obj, true)` 被使用，对象会自动重新对齐当他的大小在 `lv_obj_set_width/height/size()` 函数中被改变

当将大小相关的动画应用到对象中而需要保持原有位置时，它非常有用

要注意的是，屏幕对象的坐标不能被改变。尝试使用这些函数到屏幕对象总中会造成不明确的结果

### 父对象和子对象
你可用通过函数 `lv_obj_set_parent(obj, new_parent)` 来重新设置新的父对象，要获取当前的父对象可以使用函数 `lv_obj_get_parent(obj)`

要获取一个对象的子对象可以使用`lv_obj_get_child(obj, child_prev)` (从最后一个到第一个) 或 `lv_obj_get_child_back(obj, child_prev)` (从第一个到最后一个).
要获取第一个子对象请传入 `NULL`作为第二个参数并使用返回的值来遍历所有子对象，该函数会返回 `NULL` 如果已经没有更多的子对象，举个栗子：

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
当你以这样的方式创建一个屏幕对象 `lv_obj_create(NULL, NULL)` 时你可以加载它通过`lv_scr_load(screen1)`函数。 `lv_scr_act()`函数会给出当前屏幕对象的一个指针

如果你有多个显示设备，那么那将非常重要知道这些函数操作在最后创建或明确选择 (通过 `lv_disp_set_default`) 的显示设备上

获取一个屏幕对象请使用`lv_obj_get_screen(obj)` 函数

### 图层(Layers)
默认有两个自动生成的图层：
- 顶级图层(top layer)
- 系统图层(system layer)

它们独立于屏幕，相同的图层会显示在每个屏幕对象上，*顶级图层* 在每个对象上，*系统图层*也在*顶级图层*上
你可以自由的添加任何弹出窗口到*顶级图层* 中，但是 *系统图层* 被限制了系统级别的东西 (例如`lv_indev_set_cursor()`中的鼠标光标会放在这里). 

 `lv_layer_top()` 和`lv_layer_sys()` 函数给出顶级和系统图层的指针

你可以将一个对象的层级前置或后置通过函数`lv_obj_move_foreground(obj)` 和`lv_obj_move_background(obj)`

要学习更多关于图层的知识，请阅读 [图层概览](/overview/layer)一章

### 样式(Style)
基本对象存储了对象的 [主样式](/overview/style)，要设置新样式请使用`lv_obj_set_style(obj, &new_style)` 函数。 如果被设置了 `NULL`，对象会继承它父对象的样式

注意你不应该使用 `lv_obj_set_style` 在"非基础对象" 上。每个对象类型有它自己设置样式的方法，你应该使用这些函数
例如函数 `lv_btn_set_style()` 时用来设置按钮对象的(此时不应该使用`lv_obj_set_style`)

如果你修改了一个已经被对象了的样式，要刷新生效，可以使用 `lv_obj_refresh_style(obj)`或给出样式的`lv_obj_report_style_mod(&style)`函数来通知所有对象。如果`lv_obj_report_style_mod` 是 `NULL` 所有对象都会被改变。

要学习更多关于样式的知识请阅读 [样式概览](/overview/style)。

### 事件(Events)

要为对象设置一个事件回调请使用 `lv_obj_set_event_cb(obj, event_cb)`

要手动发送事件到一个对象中，请使用`lv_event_send(obj, LV_EVENT_..., data)`

要了解更多事件的内幕请阅读 [事件概览](/overview/event) 

### 属性(Attributes)
这里有一些属性可以通过`lv_obj_set_...(obj, true/false)` 来启用/关闭 ：

- **hidden** 隐藏对象。对象将不会被画出并可以视对象为不存在的，他的子对象也会被隐藏
- **click** 启用可通过输入设备点击对象，如果被关闭点击功能那么对象和它后面的对象都不能被点击。 (例如 [标签](/object-types/label) 默认不可点击)
- **top** 如果开启了那么当对象或他的任何子对象被点击那么该对象会被前置
- **drag** 使能拖拽 (通过输入设备移动)
- **drag_dir** 在某些特定的方向上使能拖拽，可以为：`LV_DRAG_DIR_HOR/VER/ALL`.
- **drag_throw** 使能拖拽的"抛掷(throwing)" 如果对象有冲量（惯性）
- **drag_parent** 如果被启用那么当拖拽发生时对象的父对象也会被移动。它看起来像父对象被拖拽了，这是递归，因此爷爷对象(grandparents)也会被一定移动
- **parent_event** 传播事件给父对象，递归的，所以也可以传播给爷爷对象
- **opa_scale_enable** 使能透明度，查看 [#opa-scale](Opa scale) 一章

### 透明度(Opa scale)
如果`lv_obj_set_opa_scale_enable(obj, true)` 从一个对象中被设置那么所有它的子对象的 透明度都可以通过 `lv_obj_set_opa_scale(obj, LV_OPA_...)`来设置
储存在透明度在样式中的透明度会被此因素影响

使用 [动画](/overview/animation)对一些子对象的淡入淡出非常有用

一点技术背景：在渲染过程中，为找到一个带有*透明度*的父对象，对象和他的父对象会被递归的检查
如果有一个启用 *透明度* 的对象被找到那么*透明度* 也会被用来渲染对象
因此如果你想为一个对象关闭透明度，当他的父对象的透明度开启了，你可以设置它的值为`LV_OPA_COVER`，这会覆盖父对象的设置

### 保护(Protect)
在库中会自动执行一些特定操作
要防止一种或多种此类操作，您可以保护对象不受其影响。 存在以下保护：
- **LV_PROTECT_NONE** 不保护
- **LV_PROTECT_POS**  防止自动定位 (例如 在 [容器](/object-types/cont)的布局)
- **LV_PROTECT_FOLLOW** Prevent the object be followed (make a "line break") in automatic ordering (e.g. Layout in [Containers](/object-types/cont))
- **LV_PROTECT_PARENT** 防止父对象自动改变 (例如 [页面](/object-types/page) 在后台移动创建的子对象使其能够滚动)
- **LV_PROTECT_PRESS_LOST** Prevent losing press when the press is slid out of the objects. (E.g. a [Button](/object-types/btn) can be released out of it if it was being pressed)
- **LV_PROTECT_CLICK_FOCUS**防止对象自动聚焦如果他在一个*群组(Group)*中并打开了点击聚焦
- **LV_PROTECT_CHILD_CHG** 关闭子对象改变信号，被库内部使用

 `lv_obj_set/clear_protect(obj, LV_PROTECT_...)` 设置/清除保护，你也可以使用*'OR'ed*保护类型的值

### 群组(Groups)

一旦一个对象通过 `lv_group_add_obj(group, obj)`被添加到*群组*中，这个对象的当前群组就可以通过 `lv_obj_get_group(obj)`获得

`lv_obj_is_focused(obj)` 描述了当前对象是否在它的群组中被聚焦，如果对象没有被添加到一个群组中，`false`会被返回

要想了解更多关于*群组*的知识，请阅读[输入设备概览](/overview/indev)

### 拓展点击区域(Extended click area)
默认情况下，对象只可以在他们的坐标区域中被点击，但是这个区域可以通过 `lv_obj_set_ext_click_area(obj, left, right, top, bottom)`被拓展
`left/right/top/bottom` 分别表示方向的具体取值

这个功能需要通过*lv_conf.h*的`LV_USE_EXT_CLICK_AREA`来打开，可能的值有：
- **LV_EXT_CLICK_AREA_FULL**  使用`lv_coord_t`保存 了所有4个坐标
- **LV_EXT_CLICK_AREA_TINY**只保存水平(horizontal )和垂直(vertical )的坐标坐标(比  left/right 和 top/bottom 值更好用) 使用 `uint8_t`
- **LV_EXT_CLICK_AREA_OFF** 关闭该功能

## 样式(Styles)

使用 `lv_obj_set_style(obj, &style)` 为一个基本对象设置样式

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

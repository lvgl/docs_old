_Written for v5.1_

## Overview

The Base Object contains the **most basic attributes** of the objects:

- Coordinates
- Parent object
- Children
- Style
- Attributes like Click enable, Drag enable etc.

You can set the **x and y coordinates** relative to the parent with `lv_obj_set_x(obj, new_x)` and `lv_obj_set_y(obj, new_y)` or in one function with `lv_obj_set_pos(obj, new_x, new_y)`. 

The **object size** can be modified with `lv_obj_set_width(obj, new_width)` and `lv_obj_set_height(obj, new_height)` or in one function with `lv_obj_set_size(obj, new_width, new_height)`. 

You can **align**  the object to an other with `lv_obj_align(obj1, obj2, LV_ALIGN_TYPE, x_shift, y_shift)`. The last two argument means an x and y shift after the alignment. The second argument is another object on which to align the first (`NULL` means: align to the parent). The third argument is the type of alignment:
![Alignment types](http://docs.littlevgl.com/img/align.png)

The alignment types build like: `LV_ALIGN_OUT_TOP_MID`. For example to align a text below an image: `lv_obj_align(text, image, LV_ALIGN_OUT_BOTTOM_MID, 0, 10)`. Or to align a text in the middle of its parent: `lv_obj_align(text, NULL, LV_ALIGN_CENTER, 0, 0)`. 

You can set a **new parent** for an object with `lv_obj_set_parent(obj, new_parent)`.

To get the children of an object use `lv_obj_get_child(obj, child_prev)` (from last to first) or `lv_obj_get_child_back(obj, child_prev)` (from first to last). To get the first child pass _NULL_ as the second parameter and then the previous child (return value). The function will return with _NULL_ when there are no more children.

When you have created a **screen** like `lv_obj_create(NULL, NULL)` you can **load** it with `lv_scr_load(screen1)`. The `lv_scr_act()` function gives you a pointer to the **current screen**.

There are **two layers** automatically generated layers:

- top layer
- system layer

They are independent of the screens so objects created an that layers will be shown on every screen. The _top layer_ is above every object on the screen and  _system layer_ is above top layer too. You can add any pop-up windows _top layer_ freely. But the _system layer_ restricted to system level things (e.g. mouse cursor will be moved here). The `lv_layer_top()` and `lv_layer_sys()` functions gives a pointer to the top or system layer.

You can set a **new style** for an object with the `lv_obj_set_style(obj, &new_style)` function. If `NULL` is set as style then the object will inherit its parent's style. If you **modify a style** you have to **notify the objects** who are using the modified styled. You can use either `lv_obj_refresh_style(obj)` or to notify all object with a given style `lv_obj_report_style_mod(&style)`. Set _lv_obj_report_style_mod_'s parameter to `NULL` to notify all objects. 

There are some attributes which can be enabled/disabled by `lv_obj_set_...(obj, true/false)`:

- **hidden** Hide the object. It will not be drawn and won't occupy space, Its children will be hidden too.
- **click** Enabled to click the object via an input device (e.g. touch pad). If disabled then object behind this one will be checked during the input device click handling (useful with typically not clickable objects like Labels)
- **top** If enabled then when this object or any of its children is clicked then this object comes to the foreground.
- **drag** Enable dragging (moving by an input device)
- **drag_throw** Enable "throwing" with dragging like the object would have momentum
- **drag_parent** If enabled then the object's parent will be moved during dragging. 

There are some specific actions which happen automatically in the library. To prevent one or more that kind of actions you can **protect the object** against them. The following protections exists:

- **LV_PROTECT_NONE** No protection
- **LV_PROTECT_POS**  Prevent automatic positioning (e.g.  Layout in [lv_cont](/Container))
- **LV_PROTECT_FOLLOW** Prevent the object be followed in automatic ordering (e.g. Layout in [lv_cont](/Container))
- **LV_PROTECT_PARENT** Prevent automatic parent change
- **LV_PROTECT_CHILD_CHG** Disable the child change signal. Used by the library

The `lv_obj_set/clr_protect(obj, LV_PROTECT_...)` sets/clears the protection. You can use _'OR'ed_ values of protection types too.

There are **built-in animations** for the objects. The following animation types exist:

- **LV_ANIM_FLOAT_TOP** Float from/to the top
- **LV_ANIM_FLOAT_LEFT** Float from/to the left
- **LV_ANIM_FLOAT_BOTTOM** Float from/to the bottom
- **LV_ANIM_FLOAT_RIGHT** Float from/to the right
- **LV_ANIM_GROW_H** Grow/shrink  horizontally
- **LV_ANIM_GROW_V** Grow/shrink  vertically

The `lv_obj_animate(obj, anim_type, time, delay, callback)` applies an animation on _obj_. To determinate the direction of the animation _OR_ _ANIM_IN_ or _ANIM_OUT_ with the animation type. The default is _ANIM_IN_ if not specified. You can learn more about the [animations](/Animations).

## Style usage

All _style.body_ properties are used. Default for screens  _lv_style_plain_  and _lv_style_plain_color_ for normal objects

## Example
![Base object image](http://docs.littlevgl.com/img/base-obj-lv_obj.png)
```c
/*Create a simple base object*/
lv_obj_t * obj1;
obj1 = lv_obj_create(lv_scr_act(), NULL);
lv_obj_set_size(obj1, 150, 40);
lv_obj_set_style(obj1, &lv_style_plain_color);
lv_obj_align(obj1, NULL, LV_ALIGN_IN_TOP_MID, 0, 40);

/*Copy the previous object and enable drag*/
lv_obj_t * obj2;
obj2 = lv_obj_create(lv_scr_act(), obj1);
lv_obj_set_style(obj2, &lv_style_pretty_color);
lv_obj_set_drag(obj2, true);
lv_obj_align(obj2, NULL, LV_ALIGN_CENTER, 0, 0);

static lv_style_t style_shadow;
lv_style_copy(&style_shadow, &lv_style_pretty);
style_shadow.body.shadow.width = 6;
style_shadow.body.radius = LV_RADIUS_CIRCLE;

/*Copy the previous object (drag is already enabled)*/
lv_obj_t * obj3;
obj3 = lv_obj_create(lv_scr_act(), obj2);
lv_obj_set_style(obj3, &style_shadow);
lv_obj_align(obj3, NULL, LV_ALIGN_IN_BOTTOM_MID, 0, -40);
```

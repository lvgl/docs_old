```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/tr/object-types/obj.md
```
# Base object (lv_obj)

## Overview

The Base Object contains the most basic attributes of the objects:

- coordinates
- parent object
- children
- main style
- attributes like *Click enable*, *Drag enable*, etc.

### Coordinates
The object size can be modified with `lv_obj_set_width(obj, new_width)` and `lv_obj_set_height(obj, new_height)` or in one function with `lv_obj_set_size(obj, new_width, new_height)`. 

You can set the x and y coordinates relative to the parent with `lv_obj_set_x(obj, new_x)` and `lv_obj_set_y(obj, new_y)` or in one function with `lv_obj_set_pos(obj, new_x, new_y)`. 

You can align the object to an other with `lv_obj_align(obj, obj_ref, LV_ALIGN_..., x_shift, y_shift)`. 
The second argument is a reference object, `obj` will be aligned to it. If `obj_ref = NULL` then the parent of `obj` will be used. 
The third argument is the *type* of alignment. These are the possible options:
![](/misc/align.png "Alignment types in LittlevGL")

The alignment types build like `LV_ALIGN_OUT_TOP_MID`. 

The last two argument means an x and y shift after the alignment. 

For example to align a text below an image: `lv_obj_align(text, image, LV_ALIGN_OUT_BOTTOM_MID, 0, 10)`.   
Or to align a text in the middle of its parent: `lv_obj_align(text, NULL, LV_ALIGN_CENTER, 0, 0)`. 

`lv_obj_align_origo` works similarly to `lv_obj_align` but it aligns the middle point of the object. 
For example `lv_obj_align_origo(btn, image, LV_ALIGN_OUT_BOTTOM_MID, 0, 0)` will align the center of the button the bottom of the image.

The parameters of the alignment will be saved in the object if `LV_USE_OBJ_REALIGN` is enabled in *lv_conf.h*. You can realign the objects manually with `lv_obj_realign(obj)`. 
It's equivalent to calling `lv_obj_align` again with the same parameters.

If the alignment happened with `lv_obj_align_origo` then it will be used when the object is realigned.

If `lv_obj_set_auto_realign(obj, true)` is used the object will be realigned automatically if its size changes in `lv_obj_set_width/height/size()` functions. 

It's very useful when size animations are applied to the object and the original position needs to be kept.

Note that, the coordinates of screens can't be changed. Attempting to use these functions on screens will result in undefined behavior.

### Parents and children
You can set a new parent for an object with `lv_obj_set_parent(obj, new_parent)`. To get the current parent use `lv_obj_get_parent(obj)`.

To get the children of an object use `lv_obj_get_child(obj, child_prev)` (from last to first) or `lv_obj_get_child_back(obj, child_prev)` (from first to last). 
To get the first child pass `NULL` as the second parameter and use the return value to iterate through the children. The function will return `NULL` if there is no more children. For example:

```c
lv_obj_t * child;
child = lv_obj_get_child(parent, NULL);
while(child) {
    /*Do something with "child" */
    child = lv_obj_get_child(parent, child);
}
```

`lv_obj_count_children(obj)` tells the number of children on an object. `lv_obj_count_children_recursive(obj)` also tells the number of children but counts children of children recursively.

### Screens
When you have created a screen like `lv_obj_create(NULL, NULL)` you can load it with `lv_scr_load(screen1)`. The `lv_scr_act()` function gives you a pointer to the current screen. 

If you have more display then it's important to know that these functions operate on the lastly created or the explicitly selected (with `lv_disp_set_default`) display.

To get the screen of an object use the `lv_obj_get_screen(obj)` function.

### Layers
There are two  automatically generated layers:
- top layer
- system layer

They are independent of the screens and the same layers will be shown on every screen. The *top layer* is above every object on the screen and  *system layer* is above the *top layer* too. 
You can add any pop-up windows to the *top layer* freely. But the *system layer* is restricted to system level things (e.g. mouse cursor will be placed here in `lv_indev_set_cursor()`). 

The `lv_layer_top()` and `lv_layer_sys()` functions gives a pointer to the top or system layer.

You can bring an object to the foreground or send it to the background with `lv_obj_move_foreground(obj)` and `lv_obj_move_background(obj)`. 

Read the [Layer overview](/overview/layer) section to learn more about layers. 

### Style
The base object stores the [Main style](/overview/style) of the object. To set a new style use `lv_obj_set_style(obj, &new_style)` function. If `NULL` is set as style then the object will inherit its parent's style. 

Note that you shouldn't use `lv_obj_set_style` is for "non Base objects". Every object type has its own style set function which should be used for them. E.g. for button `lv_btn_set_style()`

If you modify a style, which is already used by objects in order to refresh the affected objects you can use either `lv_obj_refresh_style(obj)` or to notify all object with a given style `lv_obj_report_style_mod(&style)`. If the parameter of `lv_obj_report_style_mod` is `NULL` all objects will be notified. 

Read the [Style overview](/overview/style) to learn more about styles.

### Events

To set an event callback for an object use `lv_obj_set_event_cb(obj, event_cb)`,

To manually send an event to an object use `lv_event_send(obj, LV_EVENT_..., data)`

Read the [Event overview](/overview/event) to learn more about the events.

### Attributes
There are some attributes which can be enabled/disabled by `lv_obj_set_...(obj, true/false)`:

- **hidden** Hide the object. It will not be drawn and will be considered as if it doesn't exist., Its children will be hidden too.
- **click** Enabled to click the object via input devices. If disabled then object behind this object will be clicked. (E.g. [Labels](/object-types/label) are not clickable by default)
- **top** If enabled then when this object or any of its children is clicked then this object comes to the foreground.
- **drag** Enable dragging (moving by an input device)
- **drag_dir** Enable dragging only in specific directions. Can be `LV_DRAG_DIR_HOR/VER/ALL`.
- **drag_throw** Enable "throwing" with dragging as if the object would have momentum
- **drag_parent** If enabled then the object's parent will be moved during dragging. It will look like as if the parent is dragged. Checked recursively, so can propagate to grandparents too. 
- **parent_event** Propagate the events to the parents too. Checked recursively, so can propagate to grandparents too. 
- **opa_scale_enable** Enable opacity scaling. See the [#opa-scale](Opa scale) section.

### Opa scale
If `lv_obj_set_opa_scale_enable(obj, true)` is set for an object then the object's and all of its children's opacity can be adjusted with `lv_obj_set_opa_scale(obj, LV_OPA_...)`. 
The opacities stored in the styles will be scaled down by this factor.

It is very useful to fade in/out an object with some children using an [Animation](/overview/animation).

A little bit of technical background: during the rendering process the object and its parents are checked recursively to find a parent with enabled *Opa scale*. 
If an object has found with enabled *Opa scale* then that *Opa scale* will be used by the rendered object too. 
Therefore if you want to disable the Opa scaling for an object when the parent has Opa scale just enable Opa scaling for the object and set its value to `LV_OPA_COVER`. It will overwrite the parent's settings.

### Protect
There are some specific actions which happen automatically in the library. 
To prevent one or more that kind of actions you can protect the object against them. The following protections exists:
- **LV_PROTECT_NONE** No protection
- **LV_PROTECT_POS**  Prevent automatic positioning (e.g.  Layout in [Containers](/object-types/cont))
- **LV_PROTECT_FOLLOW** Prevent the object be followed (make a "line break") in automatic ordering (e.g. Layout in [Containers](/object-types/cont))
- **LV_PROTECT_PARENT** Prevent automatic parent change. (e.g. [Page](/object-types/page) moves the children created on the background to the scrollable)
- **LV_PROTECT_PRESS_LOST** Prevent losing press when the press is slid out of the objects. (E.g. a [Button](/object-types/btn) can be released out of it if it was being pressed)
- **LV_PROTECT_CLICK_FOCUS** Prevent automatically focusing the object if it's in a *Group* and click focus is enabled.
- **LV_PROTECT_CHILD_CHG** Disable the child change signal. Used internally by the library

The `lv_obj_set/clear_protect(obj, LV_PROTECT_...)` sets/clears the protection. You can use *'OR'ed* values of protection types too.

### Groups

Once an object is added to *group* with `lv_group_add_obj(group, obj)` the object's current group can be get with `lv_obj_get_group(obj)`. 

`lv_obj_is_focused(obj)` tells if the object is currently focused in its group or not. If the object is not added to a group `false` will be returned.

Read the [Input devices overview](/overview/indev) to learn more about the *Groups*.

### Extended click area
By default, the objects can be clicked only on their coordinates, however this area can be extended with `lv_obj_set_ext_click_area(obj, left, right, top, bottom)`. 
`left/right/top/bottom` tells extra size the directions respectively.

This feature needs to enabled in *lv_conf.h* with `LV_USE_EXT_CLICK_AREA`. The possible values are:
- **LV_EXT_CLICK_AREA_FULL** store all 4 coordinates as `lv_coord_t`
- **LV_EXT_CLICK_AREA_TINY** store only horizontal and vertical coordinates (use the greater value of left/right and top/bottom) as `uint8_t`
- **LV_EXT_CLICK_AREA_OFF** Disable this feature

## Styles

Use `lv_obj_set_style(obj, &style)` to set a style for a base obejct.

All `style.body`  properties are used. The default style for screens is `lv_style_scr`  and `lv_style_plain_color` for normal objects


## Events
Only the [Generic events](/overview/event.html#generic-events) are sent by the object type.

Learn more about [Events](/overview/event).

## Keys
No *Keys* are processed by the object type.

Learn more about [Keys](/overview/indev).
  

## Example

```eval_rst

.. include:: /lv_examples/src/lv_ex_obj/index.rst

```

## API 

```eval_rst

.. doxygenfile:: lv_obj.h
  :project: lvgl
        
```

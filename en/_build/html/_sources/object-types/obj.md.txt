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

You can align  the object to an other with `lv_obj_align(obj, obj_ref, LV_ALIGN_..., x_shift, y_shift)`. The last two argument means an x and y shift after the alignment. 
The second argument is a reference object, `obj` will be aligned to it. If `obj_ref = NULL` then the parent of `obj` will be used. 
The third argument is the type of alignment. These are possible options:
![](/examples/misc/align.png "Alignment types in LittlevGL")

The alignment types build like `LV_ALIGN_OUT_TOP_MID`. 
For example to align a text below an image: `lv_obj_align(text, image, LV_ALIGN_OUT_BOTTOM_MID, 0, 10)`.    
Or to align a text in the middle of its parent: `lv_obj_align(text, NULL, LV_ALIGN_CENTER, 0, 0)`. 

`lv_obj_align_origo` works similarly to `lv_obj_align_origo` but align the middle point of the object. 
For example `lv_obj_align_origo(btn, image, LV_ALIGN_OUT_BOTTOM_MID, 0, 0)` will align the center of the button the bottom of the image.

The parameters of the alingment will be saved in the object if `LV_USE_OBJ_REALIGN` is enabled in *lv_conf.h*. You can realaign the object manully with `lv_obj_realign(obj)`. 
It's equivalent to calling `lv_obj_align` again with the same parameters.

If the alignment happened with `lv_obj_align_origo` then it will be used when the obejct is realigned.

If `lv_obj_set_auto_realign(obj, true)` is used the object will be reaigned automatically if its size changes in `lv_obj_set_width/height/size()` functions. 

It's very useful when size animations are applied on the object and the original position needs to be kept.


Not that coordinates of screens can't be changed. Attempting to use these functions on screen will result in undefined behavior.

### Parents and children
You can set a new parent for an object with `lv_obj_set_parent(obj, new_parent)`. To get the current parent use `lv_obj_get_parent(obj)`.

To get the children of an object use `lv_obj_get_child(obj, child_prev)` (from last to first) or `lv_obj_get_child_back(obj, child_prev)` (from first to last). 
To get the first child pass `NULL` as the second parameter and then feed the return value to iterate through the clidren. The function will return `NULL` is tehre is no more children. For example:

```c
lv_obj_t child;
child = lv_obj_get_child(parent, NULL);
while(child) {
    /*Do something with "child" */
    child = lv_obj_get_child(parent, child);
}
```

`lv_obj_count_children(obj)` tells the number of children on an object. `lv_obj_count_children_recursive(obj)` also tells the number of the clidren but counts children of children recusrsively.

### Screens
When you have created a screen like `lv_obj_create(NULL, NULL)` you can load it with `lv_scr_load(screen1)`. The `lv_scr_act()` function gives you a pointer to the current screen. 

If you have more display then it's important to know that these functions operates on the lastly created or the explicitly chosen (with `lv_disp_set_default`) display.

To get the screen of an object use the `lv_obj_get_screen(obj)` function.

### Layers
There are two layers automatically generated layers:
- top layer
- system layer

They are independent of the screens and the same layers will be shown on every screen. The *top layer* is above every object on the screen and  *system layer* is above the *top layer* too. 
You can add any pop-up windows to the *top layer* freely. But the *system layer* is restricted to system level things (e.g. mouse cursor will be moved here). 

The `lv_layer_top()` and `lv_layer_sys()` functions gives a pointer to the top or system layer.


You bring an object to teóhe foreground or send it to the background with `lv_obj_move_foreground(obj)` and `lv_obj_move_background(obj)`. 

Read the [Layer overview](/overview/layer) to learn more about layers. 

### Style
The base object stores the [Main style](/overview/style) of the obejct. To seta new style use `lv_obj_set_style(obj, &new_style)` function. If `NULL` is set as style then the object will inherit its parent's style. 

Note that you shouldn't use `lv_obj_set_style` is for "non base objects". Every obejct type has its own style set function which should be used for them. E.g. for button `lv_btn_set_style()`

If you modify a style, which is already used by objects, you have to notify the objects who are using the modified styled. 
You can use either `lv_obj_refresh_style(obj)` or to notify all object with a given style `lv_obj_report_style_mod(&style)`. If the paramter of `lv_obj_report_style_mod` is `NULL` all objects will be notified. 

Read the [Style overview](/overview/style) to learn more about styles.

### Events

To set an event callback for an obejct use `lv_obj_set_event_cb(obj, event_cb)`,

To manually send an event to an object use `lv_event_send(obj, LV_EVENT_..., data)`

Read the [Event overview](/overview/event) to learn more about the events.

### Attributes
There are some attributes which can be enabled/disabled by `lv_obj_set_...(obj, true/false)`:

- **hidden** Hide the object. It will not be drawn and will be considered as if it doesn't exsits., Its children will be hidden too.
- **click** Enabled to click the object via input devices. If disabled then object behind this object will be clicked.(E.g. [Labels](/object-types/label) are not clickable by default)
- **top** If enabled then when this object or any of its children is clicked then this object comes to the foreground.
- **drag** Enable dragging (moving by an input device)
- **drag_dir** Enable dragging only in specific directions. Can be `LV_DRAG_DIR_HOR/VER/ALL`.
- **drag_throw** Enable "throwing" with dragging as if the object would have momentum
- **drag_parent** If enabled then the object's parent will be moved during dragging. It will look like as if the parent is dragged. Checked recursively, so can propagte to grandparents too. 
- **parent_event** Propagate the events to the parents too. Checked recursively, so can propagte to grandparents too. 
- **opa_scale_enable** Enable opa scaling. See the [#opa-scale](Opa scale) section.

### Opa scale
If `lv_obj_set_opa_scale_enable(obj, true)` is set for an object then the object's and al of its children's opacti can be adjusted with `lv_obj_set_opa_scale(obj, LV_OPA_...)`. 
The opacities stored in the styles will be scaled down by this factor.

It is very useful to fade in/out an object with some children using an [Animation](/overview/animation).

A little bit of technical bacground: during the rendering process the object and its parents are checked recursively to find a parent with enabled opa scale. 
If an objec has found then that opa scale will be used by rendered object too. 
Therefore if you want to disable the opa scaleing for an object when the parent has opa scale just enable opa scaling for the object and set its value `LV_OPA_COVER`. It will overwite the parent's settings.

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

The `lv_obj_set/clear_protect(obj, LV_PROTECT_...)` sets/clears the protection. You can use _'OR'ed_ values of protection types too.

### Groups

Once an object is added to *group* with `lv_grouo_add_obj(group, obj)` the object's current group can be get with `lv_obj_get_group(obj)`. 

`lv_obj_is_focused(obj)` tells if the object is currently focused in its group or not. If the object is not added to group `false` will be returned.

Read the [Input devices overview](/overview/indev) to learn more about the *Groups*.

### Extended click area
By deafult the objects can be clciked only on their coordinates, however this area can be extended with `lv_obj_set_ext_click_area(obj, left, right, top, bottom)`. 
`left/right/top/bottom` tells extra size the directions respectively.

This feature needs to enabled in *lv_conf.h* with `LV_USE_EXT_CLICK_AREA`. The possible values are:
- **LV_EXT_CLICK_AREA_FULL** store all 4 coordinates as `lv_coord_t`
- **LV_EXT_CLICK_AREA_TINY** store only horizonal and vertical coordinates (use the greater value) as `uint8_t`
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

### C

![](/examples/obj/obj_1.png "Base object in LittlevGL")


```eval_rst
.. container:: toggle

    .. container:: header
    
      code

    .. literalinclude:: /examples/obj/obj_1.c
      :language: c
 
```

### MicroPython
No examples yet.

## API 

```eval_rst

.. doxygenfile:: lv_obj.h
  :project: lvgl
        
```


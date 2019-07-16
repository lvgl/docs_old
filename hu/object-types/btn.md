```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/hu/object-types/btn.md
```
# Button (lv_btn)

## Overview

Buttons are simple rectangle-like objects, but they change their style and state when they are pressed or released. 

### States
Buttons can be in one of the 5 possible states:
- **LV_BTN_STATE_REL** Released state
- **LV_BTN_STATE_PR** Pressed state
- **LV_BTN_STATE_TGL_REL** Toggled released state 
- **LV_BTN_STATE_TGL_PR** Toggled pressed state 
- **LV_BTN_STATE_INA** Inactive state

The state from `..._REL` to `..._PR` will be changed automatically when the button is pressed and back when released.

You can set the button's state manually with `lv_btn_set_state(btn, LV_BTN_STATE_TGL_REL)`.

### Toggle
You can configure the buttons as *toggle button* with `lv_btn_set_toggle(btn, true)`. In this case on release, the button goes to *toggled released* state.

### Layout and Fit
Similarly to [Containers](/object-types/cont) buttons also have layout and fit attributes.
- `lv_btn_set_layout(btn, LV_LAYOUT_...) `set a layout. The default is `LV_LAYOUT_CENTER`. 
So if you add a label, then it will be automatically aligned to the middle and can't be moved with `lv_obj_set_pos()`. 
You can disable the layout with `lv_btn_set_layout(btn, LV_LAYOUT_OFF)`
- `lv_btn_set_fit/fit2/fit4(btn, LV_FIT_..)` enables to set the button width and/or height automatically according to the children, parent, and fit type.

### Ink effect
You can enable a special animation on buttons: when a button is pressed, the pressed state will be drawn in a growing circle starting from the point of pressing. It's like an ink droplet in the water.
When the button is released, the released state will be reverted by fading. It's like the ink is fully mixed with a lot of water and become no visible in it. 

To control this animation use the following functions:
- `lv_btn_set_ink_in_time(btn, time_ms)` time of circle growing
- `lv_btn_set_ink_wait_time(btn, time_ms)` minim time to keep the fully covering (pressed) state
- `lv_btn_set_ink_out_time(btn, time_ms)` time fade back to releases state

This feature needs to be enabled with `LV_BTN_INK_EFFECT  1` in *lv_conf.h*.


## Styles

A button can have 5 independent styles for the 5 state. You can set them via: `lv_btn_set_style(btn, LV_BTN_STYLE_..., &style)`. The styles use the `style.body` properties.

- **LV_BTN_STYLE_REL** style of the released state. Default: `lv_style_btn_rel`
- **LV_BTN_STYLE_PR** style of the pressed state. Default: `lv_style_btn_pr`
- **LV_BTN_STYLE_TGL_REL** style of the toggled released state. Default: `lv_style_btn_tgl_rel`
- **LV_BTN_STYLE_TGL_PR** style of the toggled pressed state. Default: `lv_style_btn_tgl_pr`
- **LV_BTN_STYLE_INA** style of the inactive state. Default: `lv_style_btn_ina`

When you create a label on a button, it's a good practice to set the button's `style.text` properties too. Because labels have `style = NULL` by default, they inherit the parent's (button) style. 
Hence you don't need to create a new style for the label. 


## Events
Besides the [Generic events](/overview/event.html#generic-events) the following [Special events](/overview/event.html#special-events) are sent by the buttons:
 - **LV_EVENT_VALUE_CHANGED** sent when the button is toggled.

Note that the generic input device-related events (like `LV_EVENT_PRESSED`) are sent in the inactive state too. You need to check the state with `lv_btn_get_state(btn)` to ignore the events from inactive buttons.
 
Learn more about [Events](/overview/event).

## Keys
The following *Keys* are processed by the Buttons:
- **LV_KEY_RIGHT/UP** Go to toggled state if toggling is enabled
- **LV_KEY_LEFT/DOWN** Go to non-toggled state if toggling is  enabled

Note that, as usual, the state of `LV_KEY_ENTER` is translated to `LV_EVENT_PRESSED/PRESSING/RELEASED` etc.

Learn more about [Keys](/overview/indev).
  
## Example
```eval_rst

.. include:: /lv_examples/src/lv_ex_btn/index.rst

```

## API 

```eval_rst

.. doxygenfile:: lv_btn.h
  :project: lvgl
        
```

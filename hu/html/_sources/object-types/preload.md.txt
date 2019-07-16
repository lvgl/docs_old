```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/hu/object-types/preload.md
```
# Preloader (lv_preload)

## Overview
The preloader object is a spinning arc over a border. 

### Arc length
The length of the arc can be adjusted by `lv_preload_set_arc_length(preload, deg)`.

### Spinning speed
The speed of the spinning can be adjusted by `lv_preload_set_spin_time(preload, time_ms)`.

### Spin types
You can choose from more spin types:
- **LV_PRELOAD_TYPE_SPINNING_ARC** spin the arc, slow down on the top
- **LV_PRELOAD_TYPE_FILLSPIN_ARC** spin the arc, slow down on the top but also stretch the arc

To apply one if them use `lv_preload_set_type(preload, LV_PRELOAD_TYPE_...)`

### Spin direction
The direction of spinning can be changed with `lv_preload_set_dir(preload, LV_PRELOAD_DIR_FORWARD/BACKWARD)`.

## Styles
You can set the styles with `lv_preload_set_style(btn, LV_PRELOAD_STYLE_MAIN, &style)`. It describes both the arc and the border style:
- **arc** is described by the `line` properties
- **border** is described by the `body.border` properties including `body.padding.left/top` (the smaller is used) to give a smaller radius for the border.


## Events
Only the [Generic events](/overview/event.html#generic-events) are sent by the object type.

## Keys
No *Keys* are processed by the object type.

Learn more about [Keys](/overview/indev).



## Example

```eval_rst

.. include:: /lv_examples/src/lv_ex_preload/index.rst

```

### MicroPython
No examples yet.

## API 

```eval_rst

.. doxygenfile:: lv_preload.h
  :project: lvgl
        
```

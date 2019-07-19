```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/hu/object-types/lmeter.md
```
# Line meter (lv_lmeter)

## Overview

The Line Meter object consists of some radial lines which draw a scale. 

### Set value
When setting a new value with `lv_lmeter_set_value(lmeter, new_value)` the proportional part of the scale will be recolored. 

### Range and Angles
The `lv_lmeter_set_range(lmeter, min, max)` function sets the range of the line meter. 

You can set the angle of the scale and the number of the lines by: `lv_lmeter_set_scale(lmeter, angle, line_num)`. 
The default angle is 240 and the default line number is 31.

## Styles

The line meter uses one style which can be set by `lv_lmeter_set_style(lmeter, LV_LMETER_STYLE_MAIN, &style)`. The line meter's properties are derived from the following style attributes:

- **line.color** "inactive line's" color which are greater then the current value
- **body.main_color** "active line's" color at the beginning of the scale
- **body.grad_color** "active line's" color at the end of the scale (gradient with main color)
- **body.padding.hor** line length
- **line.width** line width

The default style is `lv_style_pretty_color`.

## Events
Only the [Generic events](/overview/event.html#generic-events) are sent by the object type.

Learn more about [Events](/overview/event).

## Keys
No *Keys* are processed by the object type.

Learn more about [Keys](/overview/indev).

## Example

```eval_rst

.. include:: /lv_examples/src/lv_ex_lmeter/index.rst

```

## API 

```eval_rst

.. doxygenfile:: lv_lmeter.h
  :project: lvgl
        
```


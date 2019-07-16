```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/zh-CN/object-types/line.md
```
# Line (lv_line)

## Overview

The Line object is capable of drawing straight lines between a set of points.

### Set points 
The points has to be stored in an `lv_point_t` array and passed to the object by the `lv_line_set_points(lines, point_array, point_cnt)` function. 

### Auto-size
It is possible to automatically set the size of the line object according to its points. 
You can enable it with the `lv_line_set_auto_size(line, true)` function. 
If enabled then when the points are set the object's width and height will be changed according to the maximal x and y coordinates among the points. The *auto size* is enabled by default.

### Invert y
By deafult, the *y == 0* point is in the top of the object but you can invert the y coordinates with `lv_line_set_y_invert(line, true)`. The *y invert* is disabled by default.

## Styles

The Line uses one style which can be set by `lv_line_set_style(led, LV_LINE_STYLE_MAIN, &style)` and it uses all `style.line` properties.

## Events
Only the [Generic events](/overview/event.html#generic-events) are sent by the object type.

Learn more about [Events](/overview/event).

## Keys
No *Keys* are processed by the object type.

Learn more about [Keys](/overview/indev).

## Example

```eval_rst

.. include:: /lv_examples/src/lv_ex_line/index.rst

```

## API 

```eval_rst

.. doxygenfile:: lv_line.h
  :project: lvgl
        
```

# Line (lv_line)

## Overview

The line object is capable of **drawing straight lines** between a set of points. 
The points has to be stored in an `lv_point_t` array and passed to the object by the `lv_line_set_points(lines, point_array, point_cnt)` function. 

It is possible to **automatically set the size** of the line object according to its points. 
You can enable it with the `lv_line_set_auto_size(line, true)` function. 
If enabled then when the points are set then the object width and height will be changed according to the maximal x and y coordinates among the points. The *auto size* is enabled by default.

By deafult the *y == 0* point is in the top of the object but you can **invert the y coordinates** with `lv_line_set_y_invert(line, true)`. 

## Styles

The Line uses one style which can be set by `lv_line_set_style(led, LV_LINE_STYLE_MAIN, &style)` and it uses all `style.line` properties.

## Events
Only the [Genreric events](/overview/events.html#generic-events) are sent by the object type.

Learn more about [Events](/overview/events).

## Keys
No *Keys* are not processed by the object type.

Learn more about [Keys](/overview/indev).

## Example

### C


![](/examples/line/line_1.png "Line object with LittlevGL")

```eval_rst
.. container:: toggle

    .. container:: header
    
      code

    .. literalinclude:: /examples/line/line_1.c
      :language: c
 
```

### MicroPython
No examples yet.

## API 

```eval_rst

.. doxygenfile:: lv_line.h
  :project: lvgl
        
```


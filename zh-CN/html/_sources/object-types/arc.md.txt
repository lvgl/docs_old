```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/zh-CN/object-types/arc.md
```
# Arc (lv_arc)

## Overview

The *Arc* object **draws an arc** within **start and end angles** and with a given **thickness**.

### Angles

To set the angles use the `lv_arc_set_angles(arc, start_angle, end_angle)` function. The zero degree is at the bottom of the object and the degrees are increasing in a counter-clockwise direction. 
The angles should be in [0;360] range.

### Notes
The **width and height** of the *Arc* should be the **same**.

Currently, the *Arc* object **does not support anti-aliasing**.

## Styles
To set the style of an *Arc* object use `lv_arc_set_style(arc, LV_ARC_STYLE_MAIN, &style)`

- **line.rounded** make the endpoints rounded (opacity won't work properly if set to 1)
- **line.width** the thickness of the arc
- **line.color** the color of the arc.

## Events
Only the [Genreric events](/overview/event.html#generic-events) are sent by the object type.

Learn more about [Events](/overview/event).

## Keys
No *Keys* are processed by the object type.

Learn more about [Keys](/overview/indev).
  

## Example

```eval_rst

.. include:: /lv_examples/src/lv_ex_arc/index.rst

```

## API 

```eval_rst

.. doxygenfile:: lv_arc.h
  :project: lvgl
        
```

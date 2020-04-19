```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/en/widgets/arc.md
```
# Arc (lv_arc)

## Overview

The Arc are consists of a background and a foreground arc. Both can have start and end angles and thickness.

## Parts and Styles
The Arc's main part is called `LV_ARC_PART_MAIN`. It draws a background using the typical background style properties and an arc using the *line* style properties.
The arc's size and position will respect the *padding* style properties.

`LV_ARC_PART_INDIC` is virtual part and it draws an other arc using the *line* style proeprties. It's padding values are interpreted relative to the background arc. 
The radius of the indicator arc will be modified according to the greatest padding value.

## Usage

### Angles

To set the angles of the background, use the `lv_arc_set_bg_angles(arc, start_angle, end_angle)` function or `lv_arc_set_bg_start/end_angle(arc, start_angle)`. 
Zero degree is at the middle right (3 o'clock) of the object and the degrees are increasing in a clockwise direction.
The angles should be in [0;360] range.

Similarly, `lv_arc_set_angles(arc, start_angle, end_angle)` function or `lv_arc_set_start/end_angle(arc, start_angle)` sets the angles of the indicator arc. 

## Events
Only the [Generic events](/overview/event.html#generic-events) are sent by the object type.

Learn more about [Events](/overview/event).

## Keys
No *Keys* are processed by the object type.

Learn more about [Keys](/overview/indev).


## Example

```eval_rst

.. include:: /lv_examples/src/lv_ex_widgets/lv_ex_arc/index.rst

```

## API

```eval_rst

.. doxygenfile:: lv_arc.h
  :project: lvgl

```

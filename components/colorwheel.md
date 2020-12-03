```eval_rst
.. include:: /header.rst 
:github_url: |github_link_base|/components/cpicker.md
```
# Color wheel (lv_colorwheel)

## Overview
As its name implies *Color wheel* allows to select color. The Hue, Saturation and Value of the color can be selected after each other. 

Long pressing the object, the color wheel will change to the next parameter of the color (hue, saturation or value).
Besides, double click will reset the current parameter.

## Parts and Styles
The Color wheel's main part is called `LV_COLORWHEEL_PART_MAIN`. It uses *scale_width* to set the the width of the circle.

The Color wheel has knob which can be accessed via the  `LV_COLORWHEEL_PART_KNOB` part. 
It uses all the rectangle like style properties and padding to make it larger than the width of the circle.

## Usage

A new Color wheel can be created like this:
```c
lv_obj_t * cw =  lv_colorwheel_create(parent, knob_recolor);
```

If `knob_recolor` is `true` the knob's background color will be set automatically to the current color. 

### Set color

The color can be set manually with `lv_colorwheel_set_hue/saturation/value(cw, x)` or all at once with `lv_colorwheelr_set_hsv(cw, hsv)` or `lv_colorwheel_set_color(cpicker, rgb)`

### Color mode

The current color mode can be manually selected with `lv_colorwheel_set_color_mode(cpicker, LV_COLORWHEEL_COLOR_MODE_HUE/SATURATION/VALUE)`.

The current color mode can be fixed (i.e. do not change with long press) using `lv_colorwheel_set_fixed_mode(cw, true)`

## Events
Only the [Generic events](../overview/event.html#generic-events) are sent by the object type.

Learn more about [Events](/overview/event).

## Keys
- **LV_KEY_UP**, **LV_KEY_RIGHT** Increment the current parameter's value by 1
- **LV_KEY_DOWN**, **LV_KEY_LEFT** Decrement the current parameter's by 1
- **LV_KEY_ENTER** By long press the next mode will be shown. By double click the current parameter will be reset.

Learn more about [Keys](/overview/indev).

## Example

```eval_rst

.. include:: /lv_examples/src/lv_ex_components/lv_ex_colorwheel/index.rst

```

## API

```eval_rst

.. doxygenfile:: lv_cpicker.h
  :project: lvgl

```

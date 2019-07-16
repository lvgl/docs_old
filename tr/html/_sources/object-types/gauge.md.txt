```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/tr/object-types/gauge.md
```
# Gauge (lv_gauge)

## Overview

The gauge is a meter with scale labels and needles.

### Scale 
You can use the `lv_gauge_set_scale(gauge, angle, line_num, label_cnt)` function to adjust the scale angle and the number of the scale lines and labels. 
The default settings are 220 degrees, 6 scale labels, and 21 lines.

### Needles
The gauge can show more than one needle. 
Use the `lv_gauge_set_needle_count(gauge, needle_num, color_array)` function to set the number of needles and an array with colors for each needle. The array must be static or global variable because only its pointer is stored.

You can use `lv_gauge_set_value(gauge, needle_id, value)` to set the value of a needle.

### Range
The range of the gauge can be specified by `lv_gauge_set_range(gauge, min, max)`. The default range is 0..100.

### Critical value
To set a critical value use `lv_gauge_set_critical_value(gauge, value)`. The scale color will be changed to `line.color` after this value. (default: 80)

## Styles

The gauge uses one style which can be set by `lv_gauge_set_style(gauge, LV_GAUGE_STYLE_MAIN, &style)`. The gauge's properties are derived from the following style attributes:

- **body.main_color** line's color at the beginning of the scale
- **body.grad_color** line's color at the end of the scale (gradient with main color)
- **body.padding.left** line length
- **body.padding.inner** label distance from the scale lines 
- **body.radius** radius of needle origin circle
- **line.width** line width
- **line.color** line's color after the critical value
- **text.font/color/letter_space** label attributes

## Events
Only the [Generic events](/overview/event.html#generic-events) are sent by the object type.

Learn more about [Events](/overview/event).

## Keys
No *Keys* are processed by the object type.

Learn more about [Keys](/overview/indev).

## Example

```eval_rst

.. include:: /lv_examples/src/lv_ex_gauge/index.rst

```
## API 

```eval_rst

.. doxygenfile:: lv_gauge.h
  :project: lvgl
        
```

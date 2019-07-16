```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/zh-CN/object-types/slider.md
```
# Slider (lv_slider)

## Overview

The Slider object looks like a [Bar](/object-types/bar) supplemented with a knob. The knob can be dragged to set a value. The Slider also can be vertical or horizontal.

## Value and range
To set an initial value use `lv_slider_set_value(slider, new_value, LV_ANIM_ON/OFF)`. 
`lv_slider_set_anim_time(slider, anim_time)` sets the animation time in milliseconds.

To specify the **range** (min, max values) the `lv_slider_set_range(slider, min , max)` can be used.

### Knob placement
The knob can be placed in two ways:
- inside the background
- on the edges on min/max values

Use the `lv_slider_set_knob_in(slider, true/false)` to choose between the modes. (*knob_in = false* is the default)


## Styles
You can modify the slider's styles with `lv_slider_set_style(slider, LV_SLIDER_STYLE_..., &style)`.

- **LV_SLIDER_STYLE_BG** Style of the background. All `style.body` properties are used. The `padding` values make the knob larger than the background. (negative value makes is larger)
- **LV_SLIDER_STYLE_INDIC** Style of the indicator. All `style.body` properties are used. The `padding` values make the indicator smaller than the background. 
- **LV_SLIDER_STYLE_KNOB** Style of the knob.  All `style.body` properties are used except `padding`. 

## Events
Besides the [Generic events](/overview/event.html#generic-events) the following [Special events](/overview/event.html#special-events) are sent by the Slider:
- **LV_EVENT_VALUE_CHANGED** Sent while the slider is being dragged or changed with keys.

## Keys
- **LV_KEY_UP**, **LV_KEY_RIGHT** Increment the slider's value by 1
- **LV_KEY_DOWN**, **LV_KEY_LEFT** Decrement the slider's value by 1

Learn more about [Keys](/overview/indev).

## Example

```eval_rst

.. include:: /lv_examples/src/lv_ex_slider/index.rst

```


## API 

```eval_rst

.. doxygenfile:: lv_slider.h
  :project: lvgl
        
```

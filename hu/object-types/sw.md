```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/hu/object-types/sw.md
```
# Switch (lv_sw)

## Overview

The Switch can be used to turn on/off something. The look like a little slider. 

### Change state
The state of the switch can be changed by
- Clicking on it
- Sliding it
- Using `lv_sw_on(sw, LV_ANIM_ON/OFF)`, `lv_sw_off(sw, LV_ANIM_ON/OFF)` or `lv_sw_toggle(sw, LV_ANOM_ON/OFF)` functions

### Animation time

The time of animations, when the switch changes state, can be adjusted with `lv_sw_set_anim_time(sw, anim_time)`.

## Styles

You can modify the Switch's styles with `lv_sw_set_style(sw, LV_SW_STYLE_..., &style)`.

- **LV_SW_STYLE_BG** Style of the background. All `style.body` properties are used. The `padding` values make the Switch smaller than the knob. (negative value makes is larger)
- **LV_SW_STYLE_INDIC** Style of the indicator. All `style.body` properties are used. The `padding` values make the indicator smaller than the background. 
- **LV_SW_STYLE_KNOB_OFF** Style of the knob when the switch is off.  The `style.body` properties are used except padding.
- **LV_SW_STYLE_KNOB_ON** Style of the knob when the switch is on.  The `style.body` properties are used except padding.




## Events
Besides the [Generic events](/overview/event.html#generic-events) the following [Special events](/overview/event.html#special-events) are sent by the Switch:
- **LV_EVENT_VALUE_CHANGED** Sent when the switch changes state.

## Keys
- **LV_KEY_UP**, **LV_KEY_RIGHT** Turn on the slider
- **LV_KEY_DOWN**, **LV_KEY_LEFT** Turn off the slider

Learn more about [Keys](/overview/indev).

## Example

```eval_rst

.. include:: /lv_examples/src/lv_ex_sw/index.rst

```


## API 

```eval_rst

.. doxygenfile:: lv_sw.h
  :project: lvgl
        
```

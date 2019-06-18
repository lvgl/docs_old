# LED (lv_led)

## Overview

The LEDs are rectangle-like (or circle) object. You can set their **brightness** with `lv_led_set_bright(led, bright)`. The brightness should be between 0 (darkest) and 255 (lightest).

Use `lv_led_on(led)` and `lv_led_off(led)` to set the brightness to a predefined  ON or OFF value.  The `lv_led_toggle(led)` toggles between the ON and OFF state.

## Styles

The LED uses one style which can be set by `lv_led_set_style(led, LV_LED_STYLE_MAIN, &style)`. 
To determine the appearance the `style.body` properties are used. 

The colors are darkened and shadow width is reduced at a lower brightness and gains its original value at brightness 255 to show a lighting effect.  

The default style is: `lv_style_pretty_color`. Not that, the LED doesn't really looks like a LED with the default style so you should creat you own style. See the example below.

## Events
Only the [Genreric events](/overview/events.html#generic-events) are sent by the object type.

Learn more about [Events](/overview/events).

## Keys
No *Keys* are not processed by the object type.

Learn more about [Keys](/overview/indev).

## Example

### C


![](/examples/led/led_1.png "LED object with LittlevGL")

```eval_rst
.. container:: toggle

    .. container:: header
    
      code

    .. literalinclude:: /examples/led/led_1.c
      :language: c
 
```

### MicroPython
No examples yet.

## API 

```eval_rst

.. doxygenfile:: lv_led.h
  :project: lvgl
        
```


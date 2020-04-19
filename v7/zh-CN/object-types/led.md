```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/zh-CN/object-types/led.md
```
LED (lv_led)

## 概述

LED 是长方形 (或圆形) 对象

### 亮度
你可以用 “lv_led_set_bright(led, bright)” 来设置它们的亮度。亮度应该在 0 (最暗) 和 255 (最亮) 之间。

### 切换 (Toggle)
Use `lv_led_on(led)` and `lv_led_off(led)` to set the brightness to a predefined ON or OFF value. The `lv_led_toggle(led)` toggles between the ON and OFF state.

## 样式(Styles)

LED 可以通过 “lv_led_set_style(LED, LV_LED_STYLE_MAIN， & style)” 设置使用一种样式。
To determine the appearance, the `style.body` properties are used. 

颜色变暗，阴影宽度降低，亮度降低。增大值到原始的 255 显示照明效果

The default style is: `lv_style_pretty_color`. Note that, the LED doesn't look like a LED with the default style so you should create your style. See the example below.

## 事件 (Events)
只有 [Generic events](/overview/event.html#generic-events) 事件是被目标样式发送。

了解更多关于  [事件](/overview/event).

## 按键 (Keys)
此对象类型不处理 *按键*

了解更多关于 [按键](/overview/indev).

## 例子

```eval_rst

.. include:: /lv_examples/src/lv_ex_led/index.rst

```

## API 

```eval_rst

.. doxygenfile:: lv_led.h
  :project: lvgl
        
```

```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/zh-CN/object-types/bar.md
```
# 进度条 (lv_bar)

## 概述

The 'Bar' objects have got two main parts:
1. a **background** which is the object itself.
2. an **indicator** which shape is similar to the background but its width/height can be adjusted.

The orientation of the bar can be vertical or horizontal according to the width/height ratio. Logically, on horizontal bars, the indicator's width can be changed. Similarly, on vertical bars, the indicator's height can be changed.

### 数值和范围
A new value can be set by `lv_bar_set_value(bar, new_value, LV_ANIM_ON/OFF)`.
The value is interpreted in a range (minimum and maximum values) which can be modified with `lv_bar_set_range(bar, min, max)`.
默认的范围是 1 - 100

The new value in `lv_bar_set_value` can be set with or without an animation depending on the last parameter (`LV_ANIM_ON/OFF`).
The time of the animation can be adjusted by `lv_bar_set_anim_time(bar, 100)`. The time is in milliseconds unit.

### 对称
The bar can be drawn symmetrical to zero (drawn from zero, left to right), if it's enabled with `lv_bar_set_sym(bar, true)`

## 样式

To set the style of an *Bar* object, use `lv_bar_set_style(arc, LV_BAR_STYLE_MAIN, &style)`:

- **LV_BAR_STYLE_BG** - is a [Base object](/object-types/obj), therefore, it uses its style elements. Its default style is: `lv_style_pretty`.
- **LV_BAR_STYLE_INDIC** - is similar to the background. It uses the *left*, *right*, *top* and *bottom* paddings to keeps some space form the edges of the background. Its default style is: `lv_style_pretty_color`.

## 事件
只有 [Generic events](/overview/event.html#generic-events) 事件是被目标样式发送。

Learn more about [Events](/overview/event).

## 按键
此对象类型不处理 *按键*

了解更多关于 [按键](/overview/indev).

## 例子

```eval_rst

.. include:: /lv_examples/src/lv_ex_bar/index.rst

```

## API

```eval_rst

.. doxygenfile:: lv_bar.h
   project

```

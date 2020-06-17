```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/zh-CN/object-types/bar.md
```
# 进度条 (lv_bar)

## 概述

进度条对象有两个主要部分：
其一 是 **背景** ，它是对象本身
另一是 **指示器**，它的形状与背景相似，但是它的高度和宽度可调

进度条的方向可以是垂直的，也可以是水平的，取决与宽度/高度比。在逻辑上，水平放置的进度条的指示器的宽度，和竖直放置进度条的指示器的高度均可调。

### 数值和范围
可以设定新的数值，通过调用函数 `lv_bar_set_value(bar, new_value, LV_ANIM_ON/OFF)` 
该值需要在一个范围内(最小值和最大值)，使用 ‘lv_bar_set_range(bar, min, max)’ 修改这个范围。
默认的范围是 1 - 100

新的数值可以使用 `lv_bar_set_value` 函数设定，有没有动画效果取决与最后的一个参数 (`LV_ANIM_ON/OFF`)。
动画的时间可以通过 `lv_bar_set_anim_time(bar, 100)` 来调整。时间以毫秒为单位。

### 对称 (Symmetrical)
如果启用了`lv_bar_set_sym(bar, true)`，则进度条可以从左到右对称至0(即从0开始从左到右绘制)。

## 样式(Styles)

设定一个目标进度条的样式使用  lv_bar_set_style(arc, LV_BAR_STYLE_MAIN, & style)

**LV_BAR_STYLE_BG** 是一个[基本对象](/object-types/obj) ，因此它使用它的样式元素。它的默认样式是:' lv_style_pretty ' 。
**LV_BAR_STYLE_INDIC**类似于背景。它使用*左*，*右*，*顶*和*底*来和背景边沿保持空间。它的默认样式是:' lv_style_pretty_color '。

## 事件 (Events)
只有 [Generic events](/overview/event.html#generic-events) 事件是被目标样式发送。

了解更多关于  [事件](/overview/event).

## 按键 (Keys)
此对象类型不处理 *按键*

了解更多关于 [按键](/overview/indev).

## 例子

```eval_rst

.. include:: /lv_examples/src/lv_ex_bar/index.rst

```

## API 

```eval_rst

.. doxygenfile:: lv_bar.h
  :project: lvgl

```

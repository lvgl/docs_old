```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/tr/object-types/bar.md
```
# Bar (lv_bar)

## Giriş

Bar nesnesi iki ana parçaya sahiptir: 
1. Nesnenin kendi **arka planı**
2. Şekli arka planla aynı olan fakat genişliği/yüksekliği ayarlanabilen bir **gösterge** . 

Barın yönü genişlik/yüksek oranına göre dikey veya yatay olarak ayarlanabilir. Mantıken yatay barlarda göstergenin genişliği, dikey barlarda göstergenin yüksekliği değiştirilebilir.

### Değer ve aralık
Yeni değer `lv_bar_set_value(bar, new_value, LV_ANIM_ON/OFF)`vasıtasıyla ayarlanabilir. 
The value is interpreted in a range (minimum and maximum values) which can be modified with `lv_bar_set_range(bar, min, max)`. 
Varsayılan aralık 1..100.

The new value in `lv_bar_set_value` can be set with our without an animation depending on the last parameter (`LV_ANIM_ON/OFF`). 
The time of the animation can be adjusted by `lv_bar_set_anim_time(bar, 100)`. The time is in milliseconds unit. 

### Symmetrical
The bar can be drawn symmetrical to zero (drawn from zero left to right) if it's enabled with `lv_bar_set_sym(bar, true)`

## Styles

To set the style of an *Bar* object use `lv_bar_set_style(arc, LV_BAR_STYLE_MAIN, &style)`

- **LV_BAR_STYLE_BG** is an [Base object](/object-types/obj) therefore it uses its style elements. Its default style is: `lv_style_pretty`. 
- **LV_BAR_STYLE_INDIC** is similar to the background. It uses the *left*, *right*, *top* and *bottom* paddings to keeps some space form the edges of the background. Its default style is: `lv_style_pretty_color`.

## Events
Only the [Generic events](/overview/event.html#generic-events) are sent by the object type.

Learn more about [Events](/overview/event).

## Keys
No *Keys* are processed by the object type.

Learn more about [Keys](/overview/indev).

## Example

```eval_rst

.. include:: /lv_examples/src/lv_ex_bar/index.rst

```

## API 

```eval_rst

.. doxygenfile:: lv_bar.h
  :project: lvgl
        
```

```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/tr/object-types/arc.md
```
# Yay (lv_arc)

## Giriş

*Yay* nesnesi  verilen kalınlıkla **başlangıç ve bitiş açıları** dahilinde   **bir yay çizer** .

### Açılar

To set the angles, use the `lv_arc_set_angles(arc, start_angle, end_angle)` function. The zero degree is at the bottom of the object and the degrees are increasing in a counter-clockwise direction.
Açılar  [0;360] aralığında olmalıdır.

### Notlar
*Yayın*  **genişliği ve yükseliği** **aynı** olmalıdır.

Şu anda , *Yay* nesnesi **antialiasing modu desteklemez**.

## Biçim
To set the style of an *Arc* object, use `lv_arc_set_style(arc, LV_ARC_STYLE_MAIN, &style)`

- **line.rounded** - make the endpoints rounded (opacity won't work properly if set to 1)
- **line.width** - the thickness of the arc
- **line.color** - the color of the arc.

## Olaylar
Only the [Generic events](/overview/event.html#generic-events) are sent by the object type.

[Events](/overview/event) hakkında daha fazlasını öğrenin.

## Keys
Nesne türü tarafından işlenilen *Keys* yok.

[Keys](/overview/indev) hakkında daha fazlasını öğrenin.


## Örnek

```eval_rst

.. include:: /lv_examples/src/lv_ex_arc/index.rst

```

## API

```eval_rst

.. doxygenfile:: lv_arc.h
  :project: lvgl

```

```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/tr/object-types/gauge.md
```
# Gösterge (lv_gauge)

## Giriş

Gösterge ölçekli etiketli ve ibreli bir ölçerdir.

### Scale
You can use the `lv_gauge_set_scale(gauge, angle, line_num, label_cnt)` function to adjust the scale angle and the number of the scale lines and labels.
Varsayılan ayarlar 220 derece, 6 ölçek etiketi  ve 21 satır.

### ibreler
The gauge can show more than one needle.
`lv_gauge_set_needle_count(gauge, needle_num, color_array)` fonksiyonun ibrelerin sayısını ve her ibre için renkli bir dizi renin rengini ayarlamak için kullanabilirsin. Bu dizi statik veya global değişken olmalı çünkü sadece göstericisi saklanır.

İbrenin değeri ayarlamak için`lv_gauge_set_value(gauge, needle_id, value)` kullanabilrisin.

### Aralık
Göstergenin aralığı `lv_gauge_set_range(gauge, min, max)` ile belirtilebilir. Varsayılan aralık 0..100'dür.

### Kritik Değer
To set a critical value, use `lv_gauge_set_critical_value(gauge, value)`. The scale color will be changed to `line.color` after this value. (default: 80)

## Biçimler

The gauge uses one style at a time which can be set by `lv_gauge_set_style(gauge, LV_GAUGE_STYLE_MAIN, &style)`. The gauge's properties are derived from the following style attributes:

- **body.main_color** - Line's color at the beginning of the scale.
- **body.grad_color** - Line's color at the end of the scale (gradient with main color).
- **body.padding.left** - Line length.
- **body.padding.inner** - Label distance from the scale lines.
- **body.radius** - Radius of needle origin circle.
- **line.width** - Line width.
- **line.color** - Line's color after the critical value.
- **text.font/color/letter_space** - Label attributes.

## Olaylar
[Generic events](/overview/event.html#generic-events) sadece nesne çeşidi tarafından gönderilir.

Events](/overview/event) hakkında daha fazlasını öğrenin.

## Anahtarlar
Nesne çeşidi tarafından işlenecek*Keys* yoktur.

[Keys](/overview/indev) hakkında daha fazlasını öğrenin.

## Örnek

```eval_rst

.. include:: /lv_examples/src/lv_ex_gauge/index.rst

```
## API

```eval_rst

.. doxygenfile:: lv_gauge.h
  :project: lvgl

```

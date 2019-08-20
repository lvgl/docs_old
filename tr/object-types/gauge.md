```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/tr/object-types/gauge.md
```
# Gösterge (lv_gauge)

## Giriş

Gösterge ölçekli etiketli ve ibreli bir ölçerdir.

### Ölçek
`lv_gauge_set_scale(gauge, angle, line_num, label_cnt)` fonksiyonunu ölçek açısını ve ölçek satırlarının ve etiketlerinin sayısını ayarlamak için kullanabilirsin.
Varsayılan ayarlar 220 derece, 6 ölçek etiketi  ve 21 satır.

### ibreler
Gösterge birden fazla ibre gösterebilir 
`lv_gauge_set_needle_count(gauge, needle_num, color_array)` fonksiyonun ibrelerin sayısını ve her ibre için renkli bir dizi renin rengini ayarlamak için kullanabilirsin. Bu dizi statik veya global değişken olmalı çünkü sadece göstericisi saklanır.

İbrenin değeri ayarlamak için`lv_gauge_set_value(gauge, needle_id, value)` kullanabilrisin.

### Aralık
Göstergenin aralığı `lv_gauge_set_range(gauge, min, max)` ile belirtilebilir. Varsayılan aralık 0..100'dür.

### Kritik Değer
Kritik değeri ayarlamak için`lv_gauge_set_critical_value(gauge, value)` kullanılır . Bu değerden sonra ölçek rengi (varsayılan: 80)`line.color` değiştirilebilir.

## Biçimler

Gösterge`lv_gauge_set_style(gauge, LV_GAUGE_STYLE_MAIN, &style)` tarafından ayarlanan bir biçim ile kullanılabilir. Göstergenin özellikleri aşağıdaki biçim özelliklerinden türetilir:

- **body.main_color** liölçeğin başındaki çizginin rengi
- **body.grad_color**  ölçeğin sonundaki çizginin rengi(ana renkli gradyan)
- **body.padding.left** çizgi uzunluğu
- **body.padding.inner** ölçek çizgilerinden etiket arası mesafe
- **body.radius** ibrenin kökenli dairenin yarıçapı
- **line.width** çizgi genişliği
- **line.color** Kritik değerden sonraki çizgi rengi
- **text.font/color/letter_space** etiket özellikleri

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

```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/tr/object-types/arc.md
```
# Yay (lv_arc)

## Giriş

*Yay* nesnesi  verilen kalınlıkla **başlangıç ve bitiş açıları** dahilinde   **bir yay çizer** .

### Açılar

Açıları ayarlamak için `lv_arc_set_angles(arc, start_angle, end_angle)` fonksiyonu kullanılır. Sıfır derece nesnenin alt tarafıdır ve bu derece saat yönünün tersi yönünde artmaktadır. 
Açılar  [0;360] aralığında olmalıdır.

### Notlar
*Yayın*  **genişliği ve yükseliği** **aynı** olmalıdır.

Şu anda , *Yay* nesnesi **antialiasing modu desteklemez**.

## Biçim
*Yay* nesnesinin biçimini ayarlamak için `lv_arc_set_style(arc, LV_ARC_STYLE_MAIN, &style)`

- **line.rounded** uç noktaları yuvarlar.(Eğer 1'e set edilir ise opaklık düzgün çalışmaz)
- **line.width** yayın kalınlığı
- **line.color** Yayın rengi.

## Olaylar
Sadece [Genreric events](/overview/event.html#generic-events) nesne türü tarafından gönderilir .

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

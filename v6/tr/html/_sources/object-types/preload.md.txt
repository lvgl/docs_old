```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/tr/object-types/preload.md
```
# Öyükleme lv_preload)

## Giriş
Önyükleme nesnesi  bir sınır üzerinde dönen yaydır. 

### Yay uzunluğu
Yay uzunluğu `lv_preload_set_arc_length(preload, deg)` tarafından ayarlanır.

### Dönme Hızı
Dönme hızı `lv_preload_set_spin_time(preload, time_ms)` tarafından ayarlanır.

### Dönme şekli
Daha fazla dönme şekli seçebilirsiniz:
- **LV_PRELOAD_TYPE_SPINNING_ARC** üstünde  yavaşça, yay dönüşü
- **LV_PRELOAD_TYPE_FILLSPIN_ARC** üstünde yavaşça ama  yayı gerdirerek dönüş

Onlardan biri kullanılırsa  uygulamak için`lv_preload_set_type(preload, LV_PRELOAD_TYPE_...)` kullanılır

### Dönme yönü
Dönme yönü`lv_preload_set_dir(preload, LV_PRELOAD_DIR_FORWARD/BACKWARD)`ile değiştirilebilir.

## Biçim
Biçimi `lv_preload_set_style(btn, LV_PRELOAD_STYLE_MAIN, &style)` ile ayarlayabilirsin. Yay ve sınır biçimini tanımlar:
- **arc** `line` özellikleri tarafından tanımlar
- **border**  `body.padding.left/top` (küçüğü kullanılır)  özelliklerini içeren  sınır için daha küçük yarı çap vermek için `body.border` tarafından tanımlanır .


## Olaylar
 [Generic events](/overview/event.html#generic-events) sadece nesne türü tarafından gönderilir.

## Keys
Nesne türü tarafından işlenecek *Keys* yok.

[Keys](/overview/indev) hakkında daha fazlasını öğrenin.



## Örnek

```eval_rst

.. include:: /lv_examples/src/lv_ex_preload/index.rst

```

### MicroPython
Henüz örnek yok.

## API 

```eval_rst

.. doxygenfile:: lv_preload.h
  :project: lvgl
        
```

```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/tr/object-types/line.md
```
# Çizgi (lv_line)

## Genel Bakış

Çizgi nesnesi bir dizi noktalar arasında düz çizgi çizme yeteneğine sahiptir

### Ayar noktası
Noktalar bir`lv_point_t` dizisinde saklanmalı ve `lv_line_set_points(lines, point_array, point_cnt)` foksiyonu  ile nesneye geçmelidir.  

### Otomatik boyutlandırma
Çizgi nesnesinin boyutunu onun uçlarına  göre boyutunu otomatik ayarlamak  mümkündür.
`lv_line_set_auto_size(line, true)` fonksiyonu ile onu  aktif hale getirebilirsin.
Etkinleştirilirse uçlar ayarlandığından nesnenin genişliği ve yükseliği maksimum x ve y kordinat noktaları arasında değiştirilebilir. *auto size* varsayılan olarak aktiftir.

### Y'yi tersle
Varsayılan olarak nesnenin üst kısmı *y == 0* noktasıdır ama`lv_line_set_y_invert(line, true)` ile y' nin kordinatını tersleyebilirsin. Varsayılan olarak *y invert* pasiftir.

## Biçimler

The Line uses one style which can be set by `lv_line_set_style(led, LV_LINE_STYLE_MAIN, &style)` and it uses all `style.line` properties.

## Olaylar
[Generic events](/overview/event.html#generic-events) sadece nesne türü tarafından gönderilir.

[Events](/overview/event) hakkında daha fazlasını öğren.

## Anahylarlar
Hayır, *Keys* nesne türüne göre işlem görür.

[Keys](/overview/indev) hakkında daha öğrenin.

## Örnek

```eval_rst

.. include:: /lv_examples/src/lv_ex_line/index.rst

```

## API 

```eval_rst

.. doxygenfile:: lv_line.h
  :project: lvgl
        
```

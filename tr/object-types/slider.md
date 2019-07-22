```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/tr/object-types/slider.md
```
# Slider (lv_slider)

## Genel bakış

Kayar buton nesnesi düğme ile desteklenmiş [Bar](/object-types/bar) gibidir. Bir değer ayarlamak için düğme sürüklenebilir. Ayrıca kayar buton dikey veya yatay olabilir. 

## Değer ve aralık
Başlangıç değeri ayarlamak içim `lv_slider_set_value(slider, new_value, LV_ANIM_ON/OFF)` kullanılır. 
`lv_slider_set_anim_time(slider, anim_time)` Animasyon süresini milisaniye cinsinden ayarlar.

**range**  belirtmek için (min, max değerler) `lv_slider_set_range(slider, min , max)` kullanılabilir.

### Düğme yerleştirme
Düğme iki şekilde yerleştirilir:
- arka plan içinde
- kenarlarda min/max değerleri

Modlar(*knob_in = false* is the default) arası seçim yapmak için    `lv_slider_set_knob_in(slider, true/false)` kullanın.


## Biçim
Kayar butonun biçimi `lv_slider_set_style(slider, LV_SLIDER_STYLE_..., &style)` ile ayarlanabilir.

- **LV_SLIDER_STYLE_BG** Arka planın biçimi. Tüm `style.body` özellikleri kullanılır. `padding` değerleri düğmeyi arka plandan daha büyük yapar. (negatif değerler daha büyük yapar)
- **LV_SLIDER_STYLE_INDIC** Gösterge biçimi. Tüm `style.body` özellikleri kullanılır. `padding` değerleri göstergeyi arka plandan daha küçük yapar.
- **LV_SLIDER_STYLE_KNOB** Düğme biçimi.  Tüm `style.body` özellikleri `padding` hariç kullanılır. 

## Olaylar
[Generic events](/overview/event.html#generic-events) yanında devamında [Special events](/overview/event.html#special-events) kayar buton tarafından gönderilir:
- **LV_EVENT_VALUE_CHANGED** Kayar buton sürüklenirken veya düğme ile değiştirilirken gönderir.

## Tuşlar/Anahtarlar
- **LV_KEY_UP**, **LV_KEY_RIGHT** Kayar buton değeri1 arttırılır
- **LV_KEY_DOWN**, **LV_KEY_LEFT** Kayar butonun değerini 1 azaltır.

Daha fazlasını öğrenin [Keys](/overview/indev).

## Örnek

```eval_rst

.. include:: /lv_examples/src/lv_ex_slider/index.rst

```


## API 

```eval_rst

.. doxygenfile:: lv_slider.h
  :project: lvgl
        
```

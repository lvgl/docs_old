```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/tr/object-types/sw.md
```
# Anahtar (lv_sw)

## Giriş

Anahtarlar bir şeyi açmak/kapamak için kullanılabilir. Küçük slider gibidir. 

### Durum değiştirme
Anahtarın durumu aşağıdakiler tarafından değiştirilebilir 
- Üzerine tıklanarak
- Kaydırarak
- `lv_sw_on(sw, LV_ANIM_ON/OFF)`, `lv_sw_off(sw, LV_ANIM_ON/OFF)` veya `lv_sw_toggle(sw, LV_ANOM_ON/OFF)` fonksiyonları kullanılarak

### Animasyon süresi

Anahtar durum değiştirdiği anda, animasyon süresi `lv_sw_set_anim_time(sw, anim_time)` ile ayarlanabilir.

## Biçim

Anahtar biçimini `lv_sw_set_style(sw, LV_SW_STYLE_..., &style)` ile düzenleyebiliriz.

- **LV_SW_STYLE_BG** Arka plan biçimi. Tüm`style.body` özellikleri kullanılır. `padding` değerleri anahtarı düğmeden küçük yapar. (Negatif değer daha büyütür)
- **LV_SW_STYLE_INDIC** Göstericinin biçimi. Tüm`style.body` özellikleri kullanılır. `padding` değerleri göstericiyi arka plandan daha küçük yapar.
- **LV_SW_STYLE_KNOB_OFF** Anaftar off durumda iken düğme biçimi.  Padding(dolgu ) hariç `style.body` özellikleri kullanılır.
- **LV_SW_STYLE_KNOB_ON** Anaftar on durumda iken düğme biçimi.  The `style.body`Padding(dolgu ) hariç `style.body` özellikleri kullanılır..




## Olaylar
[Generic events](/overview/event.html#generic-events) yanında  aşağıdaki [Special events](/overview/event.html#special-events) anaktar tarafından gönderilir:
- **LV_EVENT_VALUE_CHANGED** Anahtar durum değiştirdiğinde gönderir.

## Keys
- **LV_KEY_UP**, **LV_KEY_RIGHT** Slideri açar
- **LV_KEY_DOWN**, **LV_KEY_LEFT** Slideri kapatır

Learn more about [Keys](/overview/indev).

## Örnek

```eval_rst

.. include:: /lv_examples/src/lv_ex_sw/index.rst

```


## API 

```eval_rst

.. doxygenfile:: lv_sw.h
  :project: lvgl
        
```

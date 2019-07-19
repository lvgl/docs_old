```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/tr/object-types/btn.md
```
# Buton (lv_btn)

## Giriş

Butonlar, baskı uygulandığında veya bırakıldığında biçimleri ve durumları değişen basit dikdörtgenimsi nesnelerdir.

### Durumlar
Butonlar 5 olası durumdan birinde olabilir
- **LV_BTN_STATE_REL** Bası uygulanmama durumu
- **LV_BTN_STATE_PR** Bası uygulanma durumu
- **LV_BTN_STATE_TGL_REL** Değiştir basılma uygulanmama durumu
- **LV_BTN_STATE_TGL_PR** Değiştir basılma uygulanma durumu
- **LV_BTN_STATE_INA** Pasif durumu

Buton'a basıldığında veya bırakıldığında, buton `..._REL` to `..._PR` durumları arasındaki değişim otomatik olur.

Buton'un durumu el ile `lv_btn_set_state(btn, LV_BTN_STATE_TGL_REL)` fonksiyonu ile değiştirilebilir.

### Değiştir
Butonları  *toggle button* (değiştir butonu) olarak `lv_btn_set_toggle(btn, true) fonksiyonu ile ayarlanabilir, böyle bir durumda buton *toggled released* (değştir bırakılması) durumuna geçer.

### Yerleşim planı ve Uyum
Butonlar [Taşıyıcı çerçeve](/object-types/cont)'lerde olduğu gibi benzer yerleşim planı ve uyum özelliklerine sahiptir.
- `lv_btn_set_layout(btn, LV_LAYOUT_...) ` fonksiyonu ile yerleşim planı ayarlanır. Varsayılarn yerleşim planı `LV_LAYOUT_CENTER` şeklindedir. 
Bu yüzden eğer butona bir etiket eklendiğinde, etiket otomatik olarak ortaya hizalanır ve `lv_obj_set_pos()` fonksiyonu ile haraket ettirilemez.
`lv_btn_set_layout(btn, LV_LAYOUT_OFF)` fonksiyonu ile yerleşim planı etkisiz hale getirilir.
- `lv_btn_set_fit/fit2/fit4(btn, LV_FIT_..)` fonksiyonu butonun genişlik veya yüksekliğini otomatik olarak bağlı bulunduğu üst birimi veya kendi alt birimleri için aktifleştirir ve şekil uyumunu sağlar.

### Mürekkep Etkisi
Butonlarda özel animasyonu aktifleştirebilirsiniz. Butona bası uygulandığında basıl uygulandığı noktadan büyüyen bir daire şeklinde bası durumu oluşur. Bu durum mürekkebin suya damlaması gibi bir etki oluşturur.
Buton bırakıldğında, bırakılma durumu renk değişimi ile tamamlanır. Bu durum mürekkebin çok fazla su ile tam olarak karşması ve hiçbirşeyin görünmemesi gibidir.

Animasyonu kontrol etmek için aşağıdaki fonksiyonlar kullanılır:
- `lv_btn_set_ink_in_time(btn, time_ms)` time of circle growing
- `lv_btn_set_ink_wait_time(btn, time_ms)` minim time to keep the fully covering (pressed) state
- `lv_btn_set_ink_out_time(btn, time_ms)` time fade back to releases state

This feature needs to be enabled with `LV_BTN_INK_EFFECT  1` in *lv_conf.h*.


## Biçimler

A button can have 5 independent styles for the 5 state. You can set them via: `lv_btn_set_style(btn, LV_BTN_STYLE_..., &style)`. The styles use the `style.body` properties.

- **LV_BTN_STYLE_REL** style of the released state. Default: `lv_style_btn_rel`
- **LV_BTN_STYLE_PR** style of the pressed state. Default: `lv_style_btn_pr`
- **LV_BTN_STYLE_TGL_REL** style of the toggled released state. Default: `lv_style_btn_tgl_rel`
- **LV_BTN_STYLE_TGL_PR** style of the toggled pressed state. Default: `lv_style_btn_tgl_pr`
- **LV_BTN_STYLE_INA** style of the inactive state. Default: `lv_style_btn_ina`

When you create a label on a button, it's a good practice to set the button's `style.text` properties too. Because labels have `style = NULL` by default, they inherit the parent's (button) style. 
Hence you don't need to create a new style for the label. 


## Aksiyonlar
Besides the [Generic events](/overview/event.html#generic-events) the following [Special events](/overview/event.html#special-events) are sent by the buttons:
 - **LV_EVENT_VALUE_CHANGED** sent when the button is toggled.

Note that the generic input device-related events (like `LV_EVENT_PRESSED`) are sent in the inactive state too. You need to check the state with `lv_btn_get_state(btn)` to ignore the events from inactive buttons.
 
Learn more about [Events](/overview/event).

## Anahtarlar
The following *Keys* are processed by the Buttons:
- **LV_KEY_RIGHT/UP** Go to toggled state if toggling is enabled
- **LV_KEY_LEFT/DOWN** Go to non-toggled state if toggling is  enabled

Note that, as usual, the state of `LV_KEY_ENTER` is translated to `LV_EVENT_PRESSED/PRESSING/RELEASED` etc.

Learn more about [Keys](/overview/indev).
  
## Örnek
```eval_rst

.. include:: /lv_examples/src/lv_ex_btn/index.rst

```

## API 

```eval_rst

.. doxygenfile:: lv_btn.h
  :project: lvgl
        
```

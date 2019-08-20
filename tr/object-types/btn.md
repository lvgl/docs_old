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

Butona basıldığında veya bırakıldığında, buton `..._REL` to `..._PR` durumları arasındaki değişim otomatik olur.

Butonun durumu el ile `lv_btn_set_state(btn, LV_BTN_STATE_TGL_REL)` fonksiyonu ile değiştirilebilir.

### Değiştir
Butonları `lv_btn_set_toggle(btn, true) fonksiyonu ile  *toggle button* olarak  ayarlanabilir, bu durumda serbest bırakıldığında  buton *toggled released* durumuna geçer.

### Yerleşim planı ve Uyum
Butonlar [Taşıyıcı çerçeve](/object-types/cont)'lerde olduğu gibi benzer yerleşim planı ve uyum özelliklerine sahiptir.
- `lv_btn_set_layout(btn, LV_LAYOUT_...) ` fonksiyonu ile yerleşim planı ayarlanır. Varsayılarn yerleşim planı `LV_LAYOUT_CENTER` şeklindedir. 
Bu yüzden eğer butona bir etiket eklendiğinde, etiket otomatik olarak ortaya hizalanır ve `lv_obj_set_pos()` fonksiyonu ile haraket ettirilemez.
`lv_btn_set_layout(btn, LV_LAYOUT_OFF)` fonksiyonu ile yerleşim planı etkisiz hale getirilir.
- `lv_btn_set_fit/fit2/fit4(btn, LV_FIT_..)` fonksiyonu butonun genişlik ve/veya yüksekliğini otomatik olarak bağlı bulunduğu üst birimi veya kendi alt birimleri için aktifleştirir ve şekil uyumunu sağlar.

### Mürekkep Etkisi
Butonlarda özel animasyonu aktifleştirebilirsiniz. Bir butona basıldığında bası uygulandığı noktadan başlayarak büyüyen bir daire çizilir. Bu durum mürekkebin suya damlaması gibi bir etki oluşturur.
Buton bırakıldığında, bırakılma durumu sönümleyerek eski haline döndürülmesidir. Bu durum mürekkebin çok fazla su ile tam olarak karışması ve hiçbir şeyin görünmemesi gibidir.

Animasyonu kontrol etmek için aşağıdaki fonksiyonlar kullanılır:
- `lv_btn_set_ink_in_time(btn, time_ms)` dairenin büyüme zamanı
- `lv_btn_set_ink_wait_time(btn, time_ms)` full kaplı(basılı) durumu devam ettirmek için minim süre
- `lv_btn_set_ink_out_time(btn, time_ms)` bırakılma durumuna dönmek için sönümleme süresi

Bu özelliğin `LV_BTN_INK_EFFECT  1` in *lv_conf.h* ile aktifleştirilmesi gerekir.


## Biçimler

Bir buton 5 durum için 5 bağımsız biçime sahip olabilir. Onları `lv_btn_set_style(btn, LV_BTN_STYLE_..., &style)`ile ayarlayabilirsiniz. Bu biçimler `style.body` özelliklerini kullanılır.

- **LV_BTN_STYLE_REL** bırakılma durum biçimi. Varsayılan: `lv_style_btn_rel`
- **LV_BTN_STYLE_PR** basılma durum biçimi. Varsayılan: `lv_style_btn_pr`
- **LV_BTN_STYLE_TGL_REL** değiştir bırakılma durum(toggled released) biçimi . Varsayılan: `lv_style_btn_tgl_rel`
- **LV_BTN_STYLE_TGL_PR** değiştir basılma(toggled pressed) durum biçimi. Varsayılan: `lv_style_btn_tgl_pr`
- **LV_BTN_STYLE_INA** pasif durum biçimi. Varsayılan: `lv_style_btn_ina`

Buton üzerinde bir etiket oluşturduğunuzda, butonun`style.text` özelliklerini de ayarlamak iyi bir pratiktir . Çünkü etiketler varsayılan olarak `style = NULL` sahiptir , üst öğenin(button) biçimini devralırlar. 
Bundan dolayı etiket için yeni bir biçim oluşturmaya gerek yoktur. 


## Aksiyonlar
Buton tarafından [Generic events](/overview/event.html#generic-events) yanında  [Special events](/overview/event.html#special-events) gönderilir:
 - **LV_EVENT_VALUE_CHANGED** buton değiştirildiğinde gönderir.

Genel girdi cihazlarıyla ilgili olayların (`LV_EVENT_PRESSED` gibi) pasif durumda da gönderildiğini dikkate alınız. Pasif butonlardan aksiyonları yok saymak için `lv_btn_get_state(btn)` ile durum kontrol etmek gerekir.
 
[Events](/overview/event) hakkında daha fazlasını öğrenin.

## Anahtarlar
Aşağıdaki *Keys* butonlar tarafından işlenmiştir:
- **LV_KEY_RIGHT/UP** Geçiş aktif ise geçiş(toggled)durumuna gitme
- **LV_KEY_LEFT/DOWN** Geçiş aktif ise  geçiş(non-toggled) yapmayan duruma gitme

Dikkate alınız ki , genel olarak,  `LV_KEY_ENTER` durumu  `LV_EVENT_PRESSED/PRESSING/RELEASED` vs. olarak çevrilir.

[Keys](/overview/indev) hakkında daha fazlasını öğrenin.
  
## Örnek
```eval_rst

.. include:: /lv_examples/src/lv_ex_btn/index.rst

```

## API 

```eval_rst

.. doxygenfile:: lv_btn.h
  :project: lvgl
        
```

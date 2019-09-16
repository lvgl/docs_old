```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/tr/object-types/cb.md
```
# Onay kutusu (lv_cb)
## Giriş

Onay kutusu nesneleri bir Button *imi* ve klasik bir onay kutusu gerçekleştirmek için bir [Label](/object-types/label) içeren bir [Button](/object-types/btn) arka planından oluşturulmuştur   . 

### Metin
`lv_cb_set_text(cb, "New text")` fonksiyonu tarafından değiştirilebilir. Bu fonksiyon dinamik olarak metin tahsis eder. 

Statik metin ayarlamak  için `lv_cb_set_static_text(cb, txt)` kullanın. Bu yolla sadece `txt` nin göstericisi saklanılacak, onay kutusu var iken yer tahsil edilmemelidir. 

### Onay/Onayı Kaldır
`lv_cb_set_checked(cb, true/false)` ile manuel olarak  onay kutusunu onaylayabilirsiniz/ onayı kaldırabilirsiniz.

### Pasif
Onay kutusunu pasif yapmak için `lv_cb_set_inactive(cb, true)` kullanın.

## Biçim

Onay kutusu biçimleri `lv_cb_set_style(cb, LV_CB_STYLE_..., &style)` ile modife edilebilir.

- **LV_CB_STYLE_BG** Arka plan biçimi. Tüm ` style.body`özellikleri kullanılır. Etiket biçimi `style.text` den gelir. Varsayılan: `lv_style_transp`
- **LV_CB_STYLE_BOX_REL** Bırakılmış kutucuk biçimi. `style.body` özellikleri kullanılır. Varsaylan: `lv_style_btn_rel`
- **LV_CB_STYLE_BOX_PR** Basılmış kutucuk biçimi. `style.body` özellikleri kullanılır. Varsayılan: `lv_style_btn_pr`
- **LV_CB_STYLE_BOX_TGL_REL** Onaylanmış bırakılmış kutucuk biçimi. `style.body` özellikleri kullanılır. Varsayılan: `lv_style_btn_tgl_rel`
- **LV_CB_STYLE_BOX_TGL_PR** Onaylanmış basılmış kutucuk içimi. `style.body` özellikleri kullanılır. Varsayılan: `lv_style_btn_tgl_pr`
- **LV_CB_STYLE_BOX_INA** Pasif kutucuk biçimi. `style.body` özellikleri kullanılır. Varsayılan: `lv_style_btn_ina`


## Aksiyonlar
[Generic events](/overview/event.html#generic-events) dışında aşağıdaki  [Special events](/overview/event.html#special-events)  onay kutusu tarafından gönderilir :
 - **LV_EVENT_VALUE_CHANGED** onay kutusu değiştiği zaman gönderilir.

Genel giriş cihazı ile ilgili aksiyonlar (`LV_EVENT_PRESSED` gibi) pasif durumda da gönderilir. Pasif onay kutusundan gelen aksiyonları umursamamak için `lv_cb_is_inactive(cb)` ile durumu kontrol etmelisin.
 
[Events](/overview/event) hakkında daha fazlasını öğrenin.


## Keys
Aşağıdaki *Keys* buton tarafından işlenmiştir:
- **LV_KEY_RIGHT/UP** Değiştir aktif ise değiştirmeli durumuna geçer
- **LV_KEY_LEFT/DOWN** Değiştir aktif ise değiştirmez duruma geçer

Her zaman olduğu gibi `LV_KEY_ENTER`  `LV_EVENT_PRESSED/PRESSING/RELEASED` vs olarak çevrilir.

[Keys](/overview/indev) hakkında daha fazlasını öğrenin.


## Örnek

```eval_rst

.. include:: /lv_examples/src/lv_ex_cb/index.rst

```

## API 

```eval_rst

.. doxygenfile:: lv_cb.h
  :project: lvgl
        
```

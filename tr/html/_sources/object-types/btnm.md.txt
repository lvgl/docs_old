```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/tr/object-types/btnm.md
```
# Buton matris (lv_btnm)

## Giriş

Buton matris nesneleri  satır ve sütunlarda **çoklu butonları**  gösterilebilir. 

### Buton metni
Her butonda bir metin vardır. Tanımlayıcı karakter dizisi belirtmek için   *map* çağrısı kullanılması gerekiyor. 
Map `lv_btnm_set_map(btnm, my_map)` ile ayarlanabilir. 
Map bildirimi  `const char * map[] = {"btn1", "btn2", "btn3", ""}` gibi olmalıdır. 
Unutmayın ki **sonuncu elemanın boş karakter olması gerekir**!  

**Satır sonuna** geçmek için `"\n"` kullanın . Örneğin `{"btn1", "btn2", "\n", "btn3", ""}`. Butonun genişliği tüm satırı alacak şekilde her satırda yeniden hesaplanır.

### Kontrol butonları
**Buton genişliği** aynı satırdaki başa butona göre`lv_btnm_set_btn_width(btnm, btn_id, width)` ile ayarlanabilir. 
Örneğin: Bir satırdaki iki buton ile : *btnA, width = 1* ve *btnB, width = 2*, *btnA* %33 genişğinde ve *btnB* %66 genişliğine sahip olacaktır.

Genişliğe ek olarak her bir buton aşağıdaki parametreler ile özelleştirilebilir:
- **LV_BTNM_CTRL_HIDDEN** bir gizli buton yapar
- **LV_BTNM_CTRL_NO_REPEAT** buton uzun basıldığında  yinelemeyi etkisiz kılar
- **LV_BTNM_CTRL_INACTIVE** bir butonu pasif yapar
- **LV_BTNM_CTRL_TGL_ENABLE** buton değişimini(toggle) aktif yapar 
- **LV_BTNM_CTRL_TGL_STATE** değişim durumunu ayarlar
- **LV_BTNM_CTRL_CLICK_TRIG**  0 ise buton basıldığında tepki verir, 1 ise buton bırakıldığında tepki verir

Bir butonun kontrol özelliğini ayarlamak ve silmek için sırası ile`lv_btnm_set_btn_ctrl(btnm, btn_id, LV_BTNM_CTRL_...)` ve `lv_btnm_clear_btn_ctrl(btnm, btn_id, LV_BTNM_CTRL_...)` kullanın . Daha fazla`LV_BTNM_CTRL_...` değerleri  kullanılabilir.

Bir buton matrisin tüm butonların için aynı kontrol özelliklerini ayarlama/silmede  `lv_btnm_set_btn_ctrl_all(btnm, btn_id, LV_BTNM_CTRL_...)`ve`lv_btnm_clear_btn_ctrl_all(btnm, btn_id, LV_BTNM_CTRL_...)` kullanılır.

Bir buton matrisi için kontrol map'i ayarlamada `lv_btnm_set_ctrl_map(btnm, ctrl_map)` kullanılır.
`ctrl_map`in bir unsuru`ctrl_map[0] = width | LV_BTNM_CTRL_NO_REPEAT |  LV_BTNM_CTRL_TGL_ENABLE` gibi olmalı. Unsurların numarası butonların numarasına(yeni satır karakteri hariç) eşit olmalı.

### Tek geçiş (One toggle)
"Tek geçiş" özellikleri bir seferde sadece bir geçiş butonuna izin vermek için`lv_btnm_set_one_toggle(btnm, true)` ile aktif olabilir.

### Yeniden renklendirme(Recolor)
Buton üzerindeki **metinler**  [Label](/object-types/label) nesnesin yeniden renklenmesine benzer şekilde  **yeniden renklendirilebilir** .Aktif etmek için`lv_btnm_set_recolor(btnm, true)` kullanılır. Ondan sonra  buton`#FF0000 Red#` ile metin kırımızı olacak.

### Notlar
Buton matris objesi çok hafiftir çünkü butonlar sadece o anda sanal olarak çizilmiş şekilde
oluşturulmaz.
Bu yolla  bir buton ~100-150 bayt normal bir  [Button](/object-types/btn) nesnesinin boyutunun yerine sadece 8 ekstra bayt kullanır. 

## Biçimler

Buton matris 6 biçim ile çalışır : Bir arka plan ve her bir durum için 5 buton biçimleri. Biçimleri  `lv_btnm_set_style(btn, LV_BTNM_STYLE_..., &style)` ile ayarlayabilirsin. 
Arka plan ve butonlar `style.body` özelliklerini kullanır. Etiketler `style.text` buton biçimlerinin özelliklerini kullanır.

- **LV_BTNM_STYLE_BG** Arka plan biçimi.  _Padding_  içeren tüm _style.body_ özellikleri kullanılır. Varsayılan: _lv_style_pretty_
- **LV_BTNM_STYLE_BTN_REL** bırakılmış butonların biçimi. Varsayılan: _lv_style_btn_rel_
- **LV_BTNM_STYLE_BTN_PR** basılmış butonların biçimi. Varsayılan: _lv_style_btn_pr_
- **LV_BTNM_STYLE_BTN_TGL_REL** geçiş bırakılmış butonların biçimi. Varsayılan: _lv_style_btn_tgl_rel_
- **LV_BTNM_STYLE_BTN_TGL_PR** geçiş basılmış butonların biçimi. Varsayılan: _lv_style_btn_tgl_pr_
- **LV_BTNM_STYLE_BTN_INA**aktif olmayan butonların biçimi. Varsayılan: _lv_style_btn_ina_

## Olaylar
[Genreric events](/overview/events.html#generic-event) yanında aşağıdaki  [Special events](/overview/event.html#special-events) buton matris tarafından gönderilir:
 -Buton basıldığında/bırakıldığında veya uzun basmadan sonra tekrarladığında **LV_EVENT_VALUE_CHANGED**  gönderir . Olay verisi basılmış/bırakılmış butonun kimliğine(ID) ayarlanır.

[Events](/overview/event) hakkında daha fazlasını öğrenin.

##Keys

Aşağıdaki  *Keys* butonlar tarafından işlenmiş:
- **LV_KEY_RIGHT/UP/LEFT/RIGHT** Butonların arasında dolaşıp birini seçmek için
- **LV_KEY_ENTER**  Seçili butona bamak/bırakmak için

 [Keys](/overview/indev) hakkında daha fazlasını öğrenin.

## Örnek

```eval_rst

.. include:: /lv_examples/src/lv_ex_btnm/index.rst

```

## API 

```eval_rst

.. doxygenfile:: lv_btnm.h
  :project: lvgl
        
```

_Written for v5.1_(rev.2)

## Genel Bakış

Butonlar kullanıcının **basmak**, **bırakmak** veya **uzun basmak** eylemlerine bildiri fonksiyoları (`lv_action_t` fonksiyon işaretçileri) ile reaksiyon gösterir. Bildiri fonksiyonu `lv_btn_set_action(btn, ACTION_TYPE, bildiri_fonk)` ile ayarlanır. Olası aksiyon türleri:

- LV_BTN_ACTION_CLICK: Buton basıldıktan sonra bırakıldı. (tıklandı)
- LV_BTN_ACTION_PR: Buton'a basıldı 
- LV_BTN_ACTION_LONG_PR: Buton'a uzun basıldı
- LV_BTN_ACTION_LONG_PR_REPEAT: Buton'a uzun süre basıldı ve bu aksiyon belirli aralıklarla tetiklendi

Buttons can be in one of the **five possible states**:
Butonlar **beş olası durumlar** dan birinde bulunabilir:

- LV_BTN_STATE_REL Bırakma durumu 
- LV_BTN_STATE_PR Basma durumu 
- LV_BTN_STATE_TGL_REL Bırakma surumuna geç (Dorum açık)
- LV_BTN_STATE_TGL_PR Basma durumuna geç (Basma durumu açık)
- LV_BTN_STATE_INA Pasif durum

Butonlar `lv_btn_set_toggle(btn, true)` fonksiyonu ile **durum butonu** olarak ayarlanabilir. Bu durumda bırakma, buton bırakma durumuna geçer. 

Manuel olarak buton durumunu `lv_btn_set_state(btn, LV_BTN_STATE_TGL_REL)` fonksiyonu ile ayarlanabilir.

Bir buton **Pasif duruma** sadece manuel olarak (_lv_btn_set_state()_) fonksiyonu ile geçebilir. Pasif durumda hiçbir aksiyon çağırılamaz.

[Konteyner](/Container_tr)'a benzer olarak butonlarda **katman** ve **otomatik sığdır** özellikeri vardır:

- `lv_btn_set_layout(btn, LV_LAYOUT_...) `fonksiyonu ile katman ayarlanır. Varsayılan katman LV_LAYOUT_CENTER'dır. Bu sebepten eğer etiket(label) eklenirse, etiket otomatik olarak ortaya yerleşir.
- `lv_btn_set_fit(btn, hor_en, ver_en)` fonksiyonu butonun genişlik ve yüksekliğini alt birimlere bağlı olarak otomatik aktifleştirir.

## Biçim kullanımı

Buton 5 durum için 5 bağımsız biçime sahiptir. `lv_btn_set_style(btn, LV_BTN_STYLE_..., &style)` fonksiyonu ile ayarlanır. Biçimler _style.body_ özellirlerini kullanır.

- **LV_BTN_STYLE_REL** Bırakma durum biçimi. Varsayılan: _lv_style_btn_rel_
- **LV_BTN_STYLE_PR** Basma durum biçimi. Varsayılan: _lv_style_btn_pr_
- **LV_BTN_STYLE_TGL_REL** Bırak geç durum biçimi. Varsayılan: _lv_style_btn_tgl_rel_
- **LV_BTN_STYLE_TGL_PR** Bas geç durum biçimi. Varsayılan: _lv_style_btn_tgl_pr_
- **LV_BTN_STYLE_INA** Pasif durum biçimi. Varsayılan: _lv_style_btn_ina_

## Notlar

- Eğer buton sürüklenirse, butonun tıklama ve uzun basma aksiyonları çağırılamaz
- Eğer buton uzun basıldığında ve butonun uzun basılma aksiyonu ayarlanmış ise butonun tıklama aksiyonu çağırılamaz

## Örneğin
![Buton resmi](http://docs.littlevgl.com/img/button-lv_btn.png)
```c
static lv_res_t btn_click_action(lv_obj_t * btn)
{
    uint8_t id = lv_obj_get_free_num(btn);

    printf("Button %d is released\n", id);

    /* Buton bırakıldı.
     * Birşeyleri burada yap */

    return LV_RES_OK; /*Return OK Eğer buton silinmediyse*/
}

.
.
.

/*Etiket başlığı oluştur*/
lv_obj_t * label = lv_label_create(lv_scr_act(), NULL);
lv_label_set_text(label, "Default buttons");
lv_obj_align(label, NULL, LV_ALIGN_IN_TOP_MID, 0, 5);

/*Normal buton oluştur*/
lv_obj_t * btn1 = lv_btn_create(lv_scr_act(), NULL);
lv_cont_set_fit(btn1, true, true); /*Enable resizing horizontally and vertically*/
lv_obj_align(btn1, label, LV_ALIGN_OUT_BOTTOM_MID, 0, 10);
lv_obj_set_free_num(btn1, 1);   /*Set a unique number for the button*/
lv_btn_set_action(btn1, LV_BTN_ACTION_CLICK, btn_click_action);

/*Buton'a etiket ekle*/
label = lv_label_create(btn1, NULL);
lv_label_set_text(label, "Normal");

/*Butonu kopyala ve değiştir(toggle) durumuna ayarla. (Bırakma aksiyonuda kopyalandı)*/
lv_obj_t * btn2 = lv_btn_create(lv_scr_act(), btn1);
lv_obj_align(btn2, btn1, LV_ALIGN_OUT_BOTTOM_MID, 0, 10);
lv_btn_set_state(btn2, LV_BTN_STATE_TGL_REL);  /*Değiştir durumunu ayarla*/
lv_obj_set_free_num(btn2, 2);               /*Buton için tek-eşsiz sayı ayarla*/

/*Değiştir(toggle) butonuna etiket ekle*/
label = lv_label_create(btn2, NULL);
lv_label_set_text(label, "Toggled");

/*Butonu kopyala ve pasif durumu aktifleştir.*/
lv_obj_t * btn3 = lv_btn_create(lv_scr_act(), btn1);
lv_obj_align(btn3, btn2, LV_ALIGN_OUT_BOTTOM_MID, 0, 10);
lv_btn_set_state(btn3, LV_BTN_STATE_INA);   /*Pasif durumu ayarla*/
lv_obj_set_free_num(btn3, 3);               /*Buton için tek-eşsiz sayı ayarla*/

/*Pasif butona etiket ekle*/
label = lv_label_create(btn3, NULL);
lv_label_set_text(label, "Inactive");
```

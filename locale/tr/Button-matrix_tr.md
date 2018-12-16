_Written for v5.1_ (rev.1)

## Genel Bakış

Buton matris nesneleri metin sıralamasına bağlı tanımlanarak **çoklu butonlar** olarak gösterilir ve _map_(haritalama) şeklinde çağırılır. `lv_btnm_set_map(btnm, my_map)` fonksiyonu ile map belirtilebilir.

**Haritalamanın(map) tanımlanması** `const char * map[] = {"btn1", "btn2", "btn3", ""}` şeklindedir. NOT **Son eleman mutlaka boş bir metin olası gerekir**!

Metin'in ilk karakteri bazı özellikleri belirtmek için **kontrol karakter** olabilir:utes:

- **bit 7..6** Metinsel karakterlerden kontrol byte'ına ayrım yapmak için daima _0b10_
- **bit 5** Pasif buton
- **bit 4** Gizli buton
- **bit 3** Buton için uzun basma yok
- **bit 2..0** Aynı satırdaki butonlar için genişlik ilişki karşılaştırması. [1..7]

**Kontrol byte olarak sekizli sayı** özelliği tavsiye edilir. Örneğin `"\213buton"`. Sekizli sayı daima _2_ (bit 7..6) ile başlar orta bölüm özellikleri (bit 5..3) ve son bölüm genişliği (bit 2..0). Önek 3 birim genişliğinde gizli butonu tanımlıyor.

Haritalamada **satır sonu** yapmak için "\n" kullanmak: `{"btn1", "btn2", "\n", "btn3", ""}`. Butonun genişliği her satırda tekrar hesaplanır.

`lv_btnm_set_action(btnm, btnm_action)` fonksiyonu buton bırakıldığında çağırma aksiyonunu belirtir.

**Butonların değişimi(geçişi)** tıklandığında aktifleşir. Tek seferde sadece bir buton değişimi olur. `lv_btnm_set_toggle(btnm, true, id)` fonksiyonu değişimi aktifleştirir ve id'si verilmiş butonun değişim durumunu ayarlar.

## Biçim Kullanımı

Buton matris 6 biçim ile çalışır: Bir arkaplan ve 5 herbir durum için buton biçimi. `lv_btnm_set_style(btn, LV_BTNM_STYLE_..., &style)` fonksiyonu ile biçim ayarlanabilir. Arkaplan ve butonlar _style.body_ özelliğini kullanır. Etiketler buton biçim özelliklerinden_style.text_'i kullanır.

- **LV_BTNM_STYLE_BG** Arkaplan biçimi. _padding_ ile beraber tüm _style.body_ özelliklerini kullanır. Varsayılan: _lv_style_pretty_
- **LV_BTNM_STYLE_BTN_REL** Bırakma butonların biçimi. Varsayılan: _lv_style_btn_rel_
- **LV_BTNM_STYLE_BTN_PR** Basma butonların biçimi. Varsayılan: _lv_style_btn_pr_
- **LV_BTNM_STYLE_BTN_TGL_REL** Değişim bırakma butonların biçimi. Varsayılan: _lv_style_btn_tgl_rel_
- **LV_BTNM_STYLE_BTN_TGL_PR** Değişim basma butonların biçimi. Varsayılan: _lv_style_btn_tgl_pr_
- **LV_BTNM_STYLE_BTN_INA** Pasif butonların biçimi. Varsayılan: _lv_style_btn_ina_

## Notlar

- Buton matris nesnesi **çok basittir**. Temel nesne arkaplanı oluşturur ve gerçek buton oluşturmak yerine butonları çizer.

## Örnek
![Button matris resmi](http://docs.littlevgl.com/img/button-matrix-lv_btnm.png)
```c
/*Uzun süre basılıp çekildiğinde çağrılır*/
static lv_res_t btnm_action(lv_obj_t * btnm, const char *txt)
{
    printf("Button: %s released\n", txt);

    return LV_RES_OK; /*Return OK, çünkü buton matris silinmedi*/
}


.
.
.

/*Buton tanımlama metin dizisini oluştur*/
static const char * btnm_map[] = {"1", "2", "3", "4", "5", "\n",
                           "6", "7", "8", "9", "0", "\n",
                           "\202Action1", "Action2", ""};




/*Varsayılan buton matris'i oluştur*/
lv_obj_t * btnm1 = lv_btnm_create(lv_scr_act(), NULL);
lv_btnm_set_map(btnm1, btnm_map);
lv_btnm_set_action(btnm1, btnm_action);
lv_obj_set_size(btnm1, LV_HOR_RES, LV_VER_RES / 2);

/*Buton matris arkaplan için yeni biçim oluştur*/
static lv_style_t style_bg;
lv_style_copy(&style_bg, &lv_style_plain);
style_bg.body.main_color = LV_COLOR_SILVER;
style_bg.body.grad_color = LV_COLOR_SILVER;
style_bg.body.padding.hor = 0;
style_bg.body.padding.ver = 0;
style_bg.body.padding.inner = 0;

/*2 buton biçimleri oluştur*/
static lv_style_t style_btn_rel;
static lv_style_t style_btn_pr;
lv_style_copy(&style_btn_rel, &lv_style_btn_rel);
style_btn_rel.body.main_color = LV_COLOR_MAKE(0x30, 0x30, 0x30);
style_btn_rel.body.grad_color = LV_COLOR_BLACK;
style_btn_rel.body.border.color = LV_COLOR_SILVER;
style_btn_rel.body.border.width = 1;
style_btn_rel.body.border.opa = LV_OPA_50;
style_btn_rel.body.radius = 0;

lv_style_copy(&style_btn_pr, &style_btn_rel);
style_btn_pr.body.main_color = LV_COLOR_MAKE(0x55, 0x96, 0xd8);
style_btn_pr.body.grad_color = LV_COLOR_MAKE(0x37, 0x62, 0x90);
style_btn_pr.text.color = LV_COLOR_MAKE(0xbb, 0xd5, 0xf1);

/*Yeni biçim ile ikinci buton matris'i oluştur*/
lv_obj_t * btnm2 = lv_btnm_create(lv_scr_act(), btnm1);
lv_btnm_set_style(btnm2, LV_BTNM_STYLE_BG, &style_bg);
lv_btnm_set_style(btnm2, LV_BTNM_STYLE_BTN_REL, &style_btn_rel);
lv_btnm_set_style(btnm2, LV_BTNM_STYLE_BTN_PR, &style_btn_pr);
lv_obj_align(btnm2, btnm1, LV_ALIGN_OUT_BOTTOM_MID, 0, 0);
```

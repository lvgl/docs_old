_Written for v5.1_ (rev.4)

## Genel Bakış

Pencereler, **en karmaşık** konteyner benzeri nesnelerden biridir. İki ana bölümden oluşur: Üstte bir **başlık** [Konteyner](/Container_tr) ve başlığın altındaki **içerik** için bir [Sayfa](/Page_tr).

Üstbilgi **başlığı** değiştirilebilir: `lv_win_set_title(win, "Yeni Başlık")`. Başlık, üstbilginin biçimini her zaman miraslanır.

Üst bilginin sağına **kontrol butonları** `lv_win_add_btn(win, "U:/close", my_close_action)` fonksiyonu ile eklenebilir. İkinci parametre bir resim dosyası yoludur, üçüncü parametre buton bırakıldığı zaman çağrılan bir fonksiyondur. **Semboller** resim gibi kullanabilir: `lv_win_add_btn(win, SYMBOL_CLOSE, my_close_action)`.  

**Kontrol butonlarının boyutu** `lv_win_set_btn_size(win, yeni_boyut)` fonksiyonuyla değiştirebilir. 

Kaydırma çubuğunun davranışı `lv_win_set_sb_mode(win, LV_SB_MODE_...)` fonksiyonuyla ayarlanabilir. 

İçerik düzenini ayarlamak için `lv_win_set_layout(win, LV_LAYOUT_...)` fonksiyonu kullanılır.

## Biçim kullanımı

Pencerenin öğesine yeni bir stil ayarlamak için `lv_win_set_style(win, LV_WIN_STYLE_...,  &style)` fonksiyonu kullanılır.

- **LV_WIN_STYE_BG** tüm _style.body_ özelliklerini kullanan ana arka plan(üstbilgi ve içerik yer alır) (varsayılan: lv_style_plain)
- **LV_WIN_STYLE_CONTENT_BG** tüm _style.body_ özelliklerini kullanan içerik sayfasının arka planı (varsayılan: lv_style_transp)
- **LV_WIN_STYLE_CONTENT_SCRL** tüm _style.body_ özelliklerini kullanan içerik sayfasının kaydırma çubuğu (varsayılan: lv_style_transp)
- **LV_WIN_STYLE_SB** tüm _style.body_ özelliklerini kullanan kaydırma çubuğunun biçimi. Kaydırma çubuğunun dolgusu sırasıyla yatay/dikey* dolgularıyla ayarlanır ve kaydırma çubuğunun genişliği de iç dolguyla ayarlanır. (varsayılan: lv_style_pretty_color)
- **LV_WIN_STYLE_HEADER** tüm _style.body_ özelliklerini kullanan üstbilgi biçimi (varsayılan: lv_style_plain_color)
- **LV_WIN_STYLE_BTN_REL** tüm _style.body_ özelliklerini kullanan butonu bırakman(üstbilgi) biçimi (varsayılan: lv_style_btn_rel)
- **LV_WIN_STYLE_BTN_PR** tüm _style.body_ özelliklerini kullanan butona basma(üstbilgi) biçimi (default: lv_style_btn_pr)

## Notlar

## Örnek
![Window image](http://docs.littlevgl.com/img/window-lv_win.png)
```c
/*Yeni bir kaydırma çubuğu biçimi oluştur*/
static lv_style_t style_sb;
lv_style_copy(&style_sb, &lv_style_plain);
style_sb.body.main_color = LV_COLOR_BLACK;
style_sb.body.grad_color = LV_COLOR_BLACK;
style_sb.body.border.color = LV_COLOR_WHITE;
style_sb.body.border.width = 1;
style_sb.body.border.opa = LV_OPA_70;
style_sb.body.radius = LV_RADIUS_CIRCLE;
style_sb.body.opa = LV_OPA_60;

/*Yeni bir pencere oluştur*/
lv_obj_t * win = lv_win_create(lv_scr_act(), NULL);
lv_win_set_title(win, "Example window");                        /*Başlığı ayarla*/
lv_win_set_style(win, LV_WIN_STYLE_SB, &style_sb);              /*Kaydırma çubuğunun biçimini ayarla*/


/*Üstbilgiye kontrol butonu ekle*/
lv_win_add_btn(win, SYMBOL_SETTINGS, my_setup_action);            /*Ayar butonu ekle*/
lv_win_add_btn(win, SYMBOL_CLOSE, lv_win_close_action);           /*Kapatma butonu ekle ve kapatma aksiyonunun kullanılması*/


/*İçerik örneği ekle*/
lv_obj_t * txt = lv_label_create(win, NULL);
lv_label_set_text(txt, "This is the content of the window\n\n"
                       "You can add control buttons to\nthe window header\n\n"
                       "You can scroll it\n\n"
                       "See the scroll bar on the right!");
```

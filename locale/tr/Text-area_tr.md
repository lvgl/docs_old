_Written for v5.1_ (rev.3)

## Genel Bakış

Metin alanı, üzerinde **etiket** ve **imleç** bulunan bir **sayfadır.** İmleçin bulunduğu konuma **metin veya karakter girerek** eklenir:

- `lv_ta_add_char(ta, 'c')`
- `lv_ta_add_text(ta, "insert this text")`

`lv_ta_set_text(ta, "New text")` fonksiyonu **tüm metni değiştirir**

Geçerli imleç pozisyonunun solundan **bir karakter silmek** için `lv_ta_del()` kullanılır.

İmleç pozisyonu doğrudan `lv_ta_set_cursor_pos(ta, 10)` fonksiyonuyla ya da adım atılarak değiştirilebilir:

- `lv_ta_cursor_right(ta)`
- `lv_ta_cursor_left(ta)`
- `lv_ta_cursor_up(ta)`
- `lv_ta_cursor_down(ta)`

Birkaç farklı imleç türü vardır. Bunlardan biri şu şekilde ayarlanabilir: `lv_ta_set_cursor_type(ta, LV_CURSOR_...)`

- LV_CURSOR_NONE
- LV_CURSOR_LINE
- LV_CURSOR_BLOCK
- LV_CURSOR_OUTLINE
- LV_CURSOR_UNDERLINE

İmleci gizlemek için 'OR' _LV_CURSOR_HIDDEN_ kullanılabilir.

Metin alanı `lv_ta_set_one_line(ta, true)` fonksiyonu ile çizgili olacak şekilde yapılandırılır.

Metin alanı **şifre modunu** destekler. `lv_ta_set_pwd_mode(ta, true)` fonksiyonu ile etkinleştirilir.

## Biçim kullanımı

Metin alanının bir öğesine yeni bir biçim ayarlamak için `lv_ta_set_style(page, LV_TA_STYLE_...,  &style)` fonksiyonu kullanılır:

- **LV_TA_STYLE_BG** tüm _style.body_ özelliklerini kullanan arka plan biçimi. Ayrıca etiket de _style.label_ 'den bu biçimi kullanır. (varsayılan: lv_style_pretty)
- **LV_TA_STYLE_SB** tüm _style.body_ özelliklerini kullanan kaydırma çubuğunun biçimi (varsayılan: lv_style_transp)
- **LV_TA_STYLE_CURSOR** imleç biçimi. NULL ise kütüphane, etiket rengine ve fontuna göre otomatik olarak biçim ayarlar.

    - LV_CURSOR_LINE: _style.line.width_ geniş bir çizgi ama _style.body_ olarak bir dikdörtgen olarak çizilir. Yatay ve dikey dolgu imleç üzerinde ofset yapar.
    - LV_CURSOR_BLOCK: _style.body_ olarak bir dikdörtgen, yatay ve dikey olarak dolguyla dikdörtgeni büyütür.
    - LV_CURSOR_OUTLINE: _style.body_ olarak boş bir dikdörtgen(sadece kenarlık), yatay ve dikey olarak dolguyla dikdörtgeni büyütür.
    - LV_CURSOR_UNDERLINE: _style.line.width_ geniş çizgi ancak _style.body_ şeklinde bir dikdörtgen çizildiğinde imleç üzerinde ofset yapar.


## Notlar

- Şifre modunda `lv_ta_get_text(ta)` yıldız karakterlerini değil gerçek metni verir.

## Örnek
![Text area image](https://raw.githubusercontent.com/wiki/littlevgl/lvgl/img/text-area-lv_ta.png)
```c
/*Kaydırma çubuğunun biçimini ayarla*/
static lv_style_t style_sb;
lv_style_copy(&style_sb, &lv_style_plain);
style_sb.body.main_color = LV_COLOR_BLACK;
style_sb.body.grad_color = LV_COLOR_BLACK;
style_sb.body.border.color = LV_COLOR_WHITE;
style_sb.body.border.width = 1;
style_sb.body.border.opa = LV_OPA_70;
style_sb.body.radius = LV_RADIUS_CIRCLE;
style_sb.body.opa = LV_OPA_60;

/*Normal metin alanı oluştur*/
lv_obj_t * ta1 = lv_ta_create(lv_scr_act(), NULL);
lv_obj_set_size(ta1, 200, 100);
lv_obj_align(ta1, NULL, LV_ALIGN_CENTER, 0, - LV_DPI / 2);
lv_ta_set_style(ta1,LV_TA_STYLE_SB, &style_sb);                     /*Kaydırma çubuğu biçimini uygula*/
lv_ta_set_cursor_type(ta1, LV_CURSOR_BLOCK);
lv_ta_set_text(ta1, "A text in a Text Area\n"
               "You can scroll it if the text is long enough.");    /*İlk metni ayarla*/
lv_ta_set_cursor_pos(ta1, 2);                                       /*İmleç konumunu ayarla*/
lv_ta_add_text(ta1, "long ");                                       /*Geçerli imleç konumuna bir kelime ekle*/

static lv_style_t style_bg;
lv_style_copy(&style_bg, &lv_style_pretty);
style_bg.body.shadow.width = 8;
style_bg.text.color = LV_COLOR_MAKE(0x30, 0x60, 0xd0);              /*Mavi etiket*/

/*Şifre modu ile tek çizgili bir test oluştur*/
lv_obj_t * ta2 = lv_ta_create(lv_scr_act(), ta1);
lv_obj_align(ta2, ta1, LV_ALIGN_OUT_BOTTOM_MID, 0, 50);
lv_ta_set_style(ta2,LV_TA_STYLE_BG, &style_bg);                     /*Arkaplan biçimini uygula*/
lv_ta_set_one_line(ta2, true);
lv_ta_set_cursor_type(ta2, LV_CURSOR_LINE);
lv_ta_set_pwd_mode(ta2, true);
lv_ta_set_text(ta2, "Password");
```
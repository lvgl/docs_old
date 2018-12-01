_Written for v5.1_ rev(5)

## Genel Bakış

Tabandaki **arka plan** (veya temel) ve üstte **kaydırılabilir** olmak üzere sayfa iki konteyner dan oluşur. Eğer sayfada bir alt birim oluşuturulursa o otomatik olarak kaydırılabilir konteyner'a taşınır. Eğer kaydırılabilir konteyner arka plan dan büyük ise **sürükleyerek kaydırılabilir** (akıllı telefonlardaki listeler gibi).

Varsayılan olarak kaydırılabilir sayfanın _auto fit_ özelliği dikey olarak aktif tir bu yüzden tüm alt birimleri dahil ettiği için yükseklik artar. Kaydırılabilir sayfanın genişliği otomatik olarak arka plan sayfanın genişliğine ayarlanır (eksi(-) arkaplan yatay padding).

Arka plan nesnesi sayfanın kendisi gibi referans edilebilir: `lv_obj_set_width(sayfa, 100)`.

Kaydırma çubuk nesnesine şunlar alınabilir: `lv_page_get_scrl (sayfa)`.

**kaydırma çubukları** dört ilkeye bağlı olarak gösterilir:

- LV_SB_MODE_OFF: Kaydırma çubuklarını asla gösterme
- LV_SB_MODE_ON: Kaydırma çubuklarını daima göster
- LV_SB_MODE_DRAG: Sayfa sürüklendiğinde kaydırma çubuklarını göster
- LV_SB_MODE_AUTO: Kaydırılabilir konteyner kaydırılabilecek kadar büyük olduğunda kaydırma çubuklarını göster

Kaydırma çubuğu gösterisi ilkesini şu şekilde ayarlayabilirsiniz: `lv_page_set_sb_mode (sayfa, SB_MODE)`. Varsayılan değer _LV_PAGE_SB_MODE_ON_;

**Alt birimlere sayfa** yapıştırabilirsiniz. Bu durumda, alt nesneyi sürükleyerek sayfayı kaydırabilirsiniz. `lv_page_glue_obj(child, true)` fonksiyonu ile etkinleştirilebilir.

Sayfada **neneye odaklanma** `lv_page_focus(page, child, anim_time)` ile yapılır.

Bir alt birimi göstermek için kaydırılabilir konteyneri hareket ettiririz. Son parametre sıfır değilse, sayfa bir animasyon ile hareket eder.

**Bırakma ve basma aksiyonu** sayfaya `lv_page_set_rel_action(page, my_rel_action)` ve `lv_page_set_pr_action(page, my_pr_action)` fonksiyonları ile atanabilir. Aksiyonlar arkaplan ve kaydırılabilir nesne ile de tetiklenebilir. 

Doğrudan **Kaydırılabilir sayfanın ayarla/al özellik** fonksiyonları:  

- `lv_page_set_scrl_fit()`
- `lv_page_set_scrl_width()`
- `lv_page_set_scrl_height()`
- `lv_page_set_scrl_layout()`

## Biçim Kullanımı

Sayfa elemanları için `lv_page_set_style(page, LV_PAGE_STYLE_...,  &style)` fonksiyonu kullanarak yeni biçim ayarlama:

- **LV_PAGE_STYLE_BG** Arkaplan sayfa biçimi tüm _style.body_ özelliklerini kullanır (varsayılan: lv_style_pretty_color)
- **LV_PAGE_STYLE_SCRL** kaydırılabilir sayfa biçimi tüm _style.body_ özelliklerini kullanır (varsayılan: lv_style_pretty)
- **LV_PAGE_STYLE_SB** Kaydırma çubuk biçimi tüm _style.body_ özelliklerini kullanır. Kaydırma sayfasının dolgusu sırayla yatay/dikey dolgu olarak ayarlanır ve iç dolgu kaydırma sayfasının genişliğidir. (varsayılan: lv_style_pretty_color)

## Notlar

- Eğer x ve y yönüne karşılık gelen _hor_ veya _ver_ sığdır aktif ise **Alt birimlerin posisyon ayarları** münkün değildir. Çünkü, eğer _y_ koodinatı _ver_ sığdır ile değiştirilirse kaydırılabilir nesne alt nesnenin altında ve üstünde olacak şekilde yeniden boyutlandırılacaktır. Fakar kaydırılabilir parça ortada olamadığı için tekrar geri üst'e taşınır. Bunu önlemek için `lv_obj_align ()` nesnesini birbirine göre yerleştirmek için (biri üst / solda olmak zorundadır) veya `lv_page_set_scrl_fit(sayfa, false, false);` ile sığdırmayı devre dışı bırakın ve boyutunu ayarla `lv_page_set_scrl_width/height(page,  100)`
- Arka plan, kaydırılabilir çizildiğinde sınırını çizer. Kaydırılabilir sayfanın ebeveyni ile aynı renge sahip olsa bile sayfanın her zaman kapalı şekli olmasını sağlar. 


## Örnek
![Sayfa resmi](https://raw.githubusercontent.com/wiki/littlevgl/lvgl/img/page-lv_page.png)
```c
/*Kaydırma çubuk biçimi oluştur*/
static lv_style_t style_sb;
lv_style_copy(&style_sb, &lv_style_plain);
style_sb.body.main_color = LV_COLOR_BLACK;
style_sb.body.grad_color = LV_COLOR_BLACK;
style_sb.body.border.color = LV_COLOR_WHITE;
style_sb.body.border.width = 1;
style_sb.body.border.opa = LV_OPA_70;
style_sb.body.radius = LV_RADIUS_CIRCLE;
style_sb.body.opa = LV_OPA_60;
style_sb.body.padding.hor = 3;          /*Sağda yatay dolgu*/
style_sb.body.padding.inner = 8;        /*Kaydırma çubuk genişliği*/

/*Sayfa oluştur*/
lv_obj_t * page = lv_page_create(lv_scr_act(), NULL);
lv_obj_set_size(page, 150, 200);
lv_obj_align(page, NULL, LV_ALIGN_CENTER, 0, 0);
lv_page_set_style(page, LV_PAGE_STYLE_SB, &style_sb);           /*Kaydırma çubuk biçimi ayarla*/
lv_page_set_sb_mode(page, LV_SB_MODE_AUTO);                     /*Kaydırma mümkün ise kaydırma çubuklarını göster*/

/*Sayfada bir etiket oluştur*/
lv_obj_t * label = lv_label_create(page, NULL);
lv_label_set_long_mode(label, LV_LABEL_LONG_BREAK);             /*Uzun satırları otomatik olarak böl*/
lv_obj_set_width(label, lv_page_get_scrl_width(page));          /*Genişlik ayarla, Satırlar bu genişlikten sonra bölünecek*/
lv_label_set_text(label, "Lorem ipsum dolor sit amet, consectetur adipiscing elit,\n"
                         "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\n"
                         "Ut enim ad minim veniam, quis nostrud exercitation ullamco\n"
                         "laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure\n"
                         "dolor in reprehenderit in voluptate velit esse cillum dolore\n"
                         "eu fugiat nulla pariatur.\n"
                         "Excepteur sint occaecat cupidatat non proident, sunt in culpa\n"
                         "qui officia deserunt mollit anim id est laborum.");
```
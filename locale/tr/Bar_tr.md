_Written for v5.1_

## Genel Bakış

Bar nesnesi **arkaplan** ve **işaretleyici(gösterge)** olmak üzere iki parçadan oluşur. Nesnenin temeli **arkaplan**dır, **işaretleyici(gösterge)** arkaplan ile şekil olarak benzerdir fakat genişlik ve yüksekliği ayarlanabilir. 

Bar'ın yönü genişlik/yükseklik oranına bağlı olarak **dikey veya yatay** olabilir. Mantıksal olarak yatay barlar genişlik, dikey barlar yükseklik değerleri değiştirilerek oluşturulur.

`lv_bar_set_value(bar, new_value)` fonksiyonu ile **yeni değer** atanır. Bu değer `lv_bar_set_range(bar, min, max)` fonksiyonu ile belirlenmiş **aralık** (minimum ve maximum değerler) arasında bir değerdir. Varsayılan aralık değerleri 1..100 arasındadır.

Güncel değerden istenilen değere geçiş **animasyon** lu biçinde olur. Bu durumda `lv_bar_set_value_anim(bar, yeni_deger, animasyon_zamani)` fonksiyonu kullanılır.

## Biçim Kullanımı

- [Nesnenin temeli](Base-object_tr) **arkaplan** bu nedenle biçim elementleri kullanılır. Varsayılan biçin `LV_STYLE_PRETTY` dir.  
- **işaretleyici(gösterge)** arkaplanın benzeridir. Işaretleyici(gösterge) biçimleri `lv_bar_set_style_indic(bar,&style_indic)` fonksiyonu ile ayarlanır ve arkaplan ile arasında mesafe bırakmak için _hpad_ and _vpad_ biçim elementleri kullanılır. Varsayılan biçim olarak `LV_STYLE_PRETTY_COLOR` kullanılır.

## Notlar

- İşaretleyici gerçek bir nesne değildir; sadece bar tarafından çizilmiştir.

## Örnek

![Bar image](http://docs.littlevgl.com/img/bar-lv_bar.png)

```c
/*Varsayılan Bar oluştur*/
lv_obj_t * bar1 = lv_bar_create(lv_scr_act(), NULL);
lv_obj_set_size(bar1, 200, 30);
lv_obj_align(bar1, NULL, LV_ALIGN_IN_TOP_RIGHT, -20, 30);
lv_bar_set_value(bar1, 70);

/*Bar'ın sağında etiket oluştur*/
lv_obj_t * bar1_label = lv_label_create(lv_scr_act(), NULL);
lv_label_set_text(bar1_label, "Default");
lv_obj_align(bar1_label, bar1, LV_ALIGN_OUT_LEFT_MID, -10, 0);

/*Bar ve işaretleyici(gösterge) için biçim oluştur*/
static lv_style_t style_bar;
static lv_style_t style_indic;

lv_style_copy(&style_bar, &lv_style_pretty);
style_bar.body.main_color = LV_COLOR_BLACK;
style_bar.body.grad_color = LV_COLOR_GRAY;
style_bar.body.radius = LV_RADIUS_CIRCLE;
style_bar.body.border.color = LV_COLOR_WHITE;

lv_style_copy(&style_indic, &lv_style_pretty);
style_indic.body.grad_color =  LV_COLOR_GREEN;
style_indic.body.main_color=  LV_COLOR_LIME;
style_indic.body.radius = LV_RADIUS_CIRCLE;
style_indic.body.shadow.width = 10;
style_indic.body.shadow.color = LV_COLOR_LIME;
style_indic.body.padding.hor = 3;           /*İşaretleyici(gösterge)'yi biraz küçüklt*/
style_indic.body.padding.ver = 3;

/*İkinci bar oluştur*/
lv_obj_t * bar2 = lv_bar_create(lv_scr_act(), bar1);
lv_bar_set_style(bar2, LV_BAR_STYLE_BG, &style_bar);
lv_bar_set_style(bar2, LV_BAR_STYLE_INDIC, &style_indic);
lv_obj_align(bar2, bar1, LV_ALIGN_OUT_BOTTOM_MID, 0, 30); /*'Bar1''in altında hizala*/

/*Bar'ın sağında ikinci bir etiket oluştur*/
lv_obj_t * bar2_label = lv_label_create(lv_scr_act(), bar1_label);
lv_label_set_text(bar2_label, "Modified");
lv_obj_align(bar2_label, bar2, LV_ALIGN_OUT_LEFT_MID, -10, 0);
```

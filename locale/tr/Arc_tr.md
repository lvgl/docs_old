_Written for v5.2_

## Genel Bakış

Belirlenen **kalınlık** ile **başlangıç ve bitiş** açıları verilmiş bir **Yay nesnesi** çizilmesi.

Açıların ayarlanması için `lv_arc_set_angles(arc(yay), baslangic_acisi, bitis_acisi)` fonksiyonu kullanılır. Sıfır derece nesnenin altından başlar ve saat tersi yönünde devam eder, açı değerleri [0;360] arasındadır.

Yay nesnesinin biçim(style) ayarlaması için `lv_arc_set_style(arc, LV_ARC_STYLE_MAIN, &style)` fonksiyonu kullanılır.

## Biçim kullanımı
- **line.rounded** bitiş noktasını yuvarlaştırmak için kullanılır (Şeffaflık(opacity) 1 yapılırsa bu özellik çalışmaz)
- **line.width** Yay kalınlığı.
- **line.color** Yay rengi.

## Notlar
-  Yay için **genişlik ve boy** aynı olmalı.
-  Yay **anti-aliasing** i şuan **desteklememektedir**.

## Örnek

![Arc image](http://docs.littlevgl.com/img/arc-lv_arc.png)

```c
/*Yay için biçim oluştur*/
lv_style_t style;
lv_style_copy(&style, &lv_style_plain);
style.line.color = LV_COLOR_BLUE;           /*Yay rengi*/
style.line.width = 8;                       /*Yay kalınlığı*/

/*Yay oluştur*/
lv_obj_t * arc = lv_arc_create(lv_scr_act(), NULL);
lv_arc_set_style(arc, LV_ARC_STYLE_MAIN, &style);          /*Yeni biçim kullanımı*/
lv_arc_set_angles(arc, 90, 60);
lv_obj_set_size(arc, 150, 150);
lv_obj_align(arc, NULL, LV_ALIGN_CENTER, 0, 0);

/*Bir önceki yay'ı kopyalayıp farklı açılarda ve boyutta yay oluştur*/
arc = lv_arc_create(lv_scr_act(), arc);
lv_arc_set_angles(arc, 90, 20);
lv_obj_set_size(arc, 125, 125);
lv_obj_align(arc, NULL, LV_ALIGN_CENTER, 0, 0);

/*Bir önceki yay'ı kopyalayıp farklı açılarda ve boyutta yay oluştur*/
arc = lv_arc_create(lv_scr_act(), arc);
lv_arc_set_angles(arc, 90, 310);
lv_obj_set_size(arc, 100, 100);
lv_obj_align(arc, NULL, LV_ALIGN_CENTER, 0, 0);
```

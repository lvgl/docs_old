_Written for v5.1_ (rev.3)

## Genel Bakış

Konteynerler bazı özel özellirleri ile **dikdörtgen'e benzer nesneler** dir. 

Konteynerlara **katman** uygulandığında alt birimlerede uygulanmış olur. Katman aralığı(mesafe) style.body.padding.hor/ver/inner özelliği ile yapılır. Olası katman seçenekleri:

- LV_LAYOUT_OFF: Alt birimleri hizalama(olumsuz)
- LV_LAYOUT_CENTER: Alt birimleri merkezde sutun şeklinde hizala ve aralarında _pad.inner_ boşluk bırak
- LV_LAYOUT_COL_L: Alt birimleri soldaki bir sütunda hizalayın. Solda _pad.hor_ alanı, üstte _pad.ver_ alanı ve alt birimler arasında _pad.inner_ alanı olsun.
- LV_LAYOUT_COL_M: Alt birimleri ortalanmış sütunla hizalayın. En üstte _pad.ver_ alanını ve alt birimler arasında _pad.inner_ alanını tutun.
- LV_LAYOUT_COL_R: Alt birimleri sağa dayalı bir sütunda hizalayın. Sağ tarafta _pad.hor_ alanı, üstte _pad.ver_ alanı ve alt birimler arasında _pad.inner_ alanı olsun.
- LV_LAYOUT_ROW_T: Alt birimleri en üst sıradaki bir satırda hizalayın. Solda _pad.hor_ alanı, üstte _pad.ver_ alanı ve alt birimler arasında _pad.inner_ alanı olsun.
- LV_LAYOUT_ROW_M: Orta sıradaki alt birimleri hizalayın. Sol tarafta _pad.hor_ alanı ve alt birimler arasında _pad.inner_ boşluk bulundurun.
- LV_LAYOUT_ROW_B: Alttaki bir satırdaki alt birimleri hizalayın. Soldaki _pad.hor_ alanını, alt kısımdaki _pad.ver_ alanını ve alt birirmler arasında _pad.inner_ alanı tutun.
- LV_LAYOUT_PRETTY: Bir satırda olabildiğince çok nesne koyun (en azından _pad.inner_ boşluk ve yanlarda _pad.hor_ boşluk ile) ve yeni bir sıraya başlayın. Her bir çizgideki alanı, alt birimler arasında eşit olarak bölün. Üst kısımda _pad.ver_ alanını ve satırların arasındaki _pad.inner_ alanını tutun.
- LV_LAYOUT_GRID: PRETTY LAYOUT'a benzer, ancak yatay alanı eşit olarak bölmesin, sadece _pad.hor_ boşluğa izin verin.

Tüm alt birimleri dahil etmek için kapsayıcı boyutunu otomatik olarak ayarlayan bir **otomatik sığdır(uyum)** özelliğini etkinleştirebilirsiniz. Solda ve sağda _pad.hor_ alanı ve altta _pad.ver_ alanı olacak. Otomatik yerleştirme, `lv_cont_set_fit(cont, true, true)` işleviyle yatay, dikey veya her iki yönde de etkinleştirilebilir. İkinci parametre yataydır, üçüncü parametre dikey sığdırma etkinliğidir.

## Biçim Kullanımı

- **style.body** özellikleri kullanılır.

## Notlar

- **Alt birim pozisyonunu hor / ver fit etkin iken ayarlayamazsınız**. Ne olduğunu hayal edelim. Uyum sağlandığında tek alt birimin pozisyonunu değiştirirseniz, konteyner yeni pozisyonu "etrafında" hareket ettirir / yerleştirir. Bir konteynerda daha fazla nesneniz varsa, bunları birbirine göre hizalayabilirsiniz. Bir geçici çözüm olarak konteyner üzerinde küçük saydam bir nesne oluşturabilirsiniz. Alt birimleri "takip etmemek" için konteyner'ı düzeltecektir.

## Örnek

![Konteyner resmi](https://raw.githubusercontent.com/wiki/littlevgl/lvgl/img/container-lv_cont.png)
```c
lv_obj_t * box1;
box1 = lv_cont_create(lv_scr_act(), NULL);
lv_obj_set_style(box1, &lv_style_pretty);
lv_cont_set_fit(box1, true, true);

/*Konteyner'a metin ekle*/
lv_obj_t * txt = lv_label_create(box1, NULL);
lv_label_set_text(txt, "Lorem ipsum dolor\n"
                       "sit amet, consectetur\n"
                       "adipiscing elit, sed do\n"
                       "eiusmod tempor incididunt\n"
                       "ut labore et dolore\n"
                       "magna aliqua.");

lv_obj_align(box1, NULL, LV_ALIGN_IN_TOP_LEFT, 10, 10);      /*Konteyner'ı hizala*/

/*Biçim oluştur*/
static lv_style_t style;
lv_style_copy(&style, &lv_style_pretty_color);
style.body.shadow.width = 6;
style.body.padding.hor = 5;                                 /*Büyük bir yatay boşluk oluştur*/

/*Başka bir konteyner oluştur*/
lv_obj_t * box2;
box2 = lv_cont_create(lv_scr_act(), NULL);
lv_obj_set_style(box2, &style);     /*Yeni biçim ayarla*/
lv_cont_set_fit(box2, true, false); /*Dikey sığdırmayı aktif etme*/
lv_obj_set_height(box2, 55);        /*Sabit yükseklik ayarla*/

/*Yeni konteyner'a metin ekle*/
lv_obj_t * txt2 = lv_label_create(box2, NULL);
lv_label_set_text(txt2, "No vertical fit 1...\n"
                        "No vertical fit 2...\n"
                        "No vertical fit 3...\n"
                        "No vertical fit 4...");

/*Konteyner'ı öncekinin altına hizala*/
lv_obj_align(box2, box1, LV_ALIGN_OUT_BOTTOM_MID, 30, -30);
```
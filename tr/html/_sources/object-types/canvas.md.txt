```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/tr/object-types/canvas.md
```
# Tuval (lv_canvas)

## Giriş
Bir tuval kullanıcın her şeyi çizebileceği  [Image](/object-types/img) gibidir.

### Ön Bellek
Tuvalin çizilmiş imajı saklayan bir ön belleğe ihtiyacı vardır.
Tuvale bir ön bellek atamak için`lv_canvas_set_buffer(canvas, buffer, width, height, LV_IMG_CF_...)`kullanın. 
`buffer` tuvalin imajını tutan bir statik ön bellektir(sadece yerel bir değişken değil).
Örneğin
`static lv_color_t buffer[LV_CANVAS_BUF_SIZE_TRUE_COLOR(width, height)]`. `LV_CANVAS_BUF_SIZE_...`  makroları farklı renk formatlarında ki önbellek boyutunu belirlemeye yardım eder.


The canvas supports all the built in color formats like `LV_IMG_CF_TRUE_COLOR` or `LV_IMG_CF_INDEXED_2BIT`. See the full list in the [Color formats](/overview/image.html#color-formats) section.

### Palet
`LV_IMG_CF_INDEXED_...` için bir renk format paleti  `lv_canvas_set_palette(canvas, 3, LV_COLOR_RED)` ile başlatılması gerekir. Pikseli *index=3* ile kırmızı ayarlanır.


### Çizim
Tuvalde bir pikseli ayarlamak için `lv_canvas_set_px(canvas, x, y, LV_COLOR_RED)` kullanılır.
`LV_IMG_CF_INDEXED_...` veya `LV_IMG_CF_ALPHA_...` ile rengin veya alfa değerinin indisi renk olarak geçmesi gerekir. Örneğin  `lv_color_t c; c.full = 3;`

`lv_canvas_fill_bg(canvas, LV_COLOR_BLUE)` tüm tuvali mavi doldurur.

`lv_canvas_copy_buf(canvas, buffer_to_copy, x, y, width, height)` ile piksel dizisi tuvale kopyalanabilir . Ön belleğin ve tuvalin renk formatı eşleşmesi gerekir.

Tuvale bir şeyler çizmek için aşağıdaki fonksiyonlar kullanılır
- `lv_canvas_draw_rect(canvas, x, y, width, heigth, &style)`
- `lv_canvas_draw_text(canvas, x, y, max_width, &style, txt, LV_LABEL_ALIGN_LEFT/CENTER/RIGTH)`
- `lv_canvas_draw_img(canvas, x, y, &img_src, &style)`
- `lv_canvas_draw_line(canvas, point_array, point_cnt, &style)`
- `lv_canvas_draw_polygon(canvas, points_array, point_cnt, &style)`
- `lv_canvas_draw_arc(canvas, x, y, radius, start_angle, end_angle, &style)`

Çizim fonksiyonu sadece `LV_IMG_CF_TURE_COLOR`, `LV_IMG_CF_TRUE_COLOR_CHROMA_KEYED` ve `LV_IMG_CF_TRUE_COLOR_ALPHA` ön belleklerini çizebilir. `LV_IMG_CF_TRUE_COLOR_ALPHA` sadece `LV_COLOR_DEPTH 32` birlikte çalışıyor.

### Döndürme
`lv_canvas_rotate(canvas, &imd_dsc, angle, x, y, pivot_x, pivot_y)` ile tuvale döndürülmüş imaj eklenebilir. 
`img_dsc` tarafından gösterilen imajı verilen eksen etrafında döndürecek ve `canvas`ın  `x`, `y`  kordinatlarında saklar.
`img_dsc` ve başka tuval ön belleğinin yerine`lv_canvas_get_img(canvas)`  de kullanılabilir .

Bir tuvalin kendi üzerinde döndürülemeyeceğini dikkate alınız. Bir kaynağa ve belirlenmiş tuvale veya imaja ihtiyacınız vardır. 

## Biçim
`lv_canvas_set_style(btn, LV_CANVAS_STYLE_MAIN, &style)` ile biçimi ayarlayabilirsiniz. 
`style.image.color` temel rengi  `LV_IMG_CF_ALPHA_...`renk formatı ile anlatmak için kullanılır. 

## Olaylar
Sadece  [Generic events](/overview/event.html#generic-events) nesne tarafından gönderilebilir.

[Events](/overview/event) hakkınad daha fazlasını öğrenin.

## Keys
Nesne türü tarafından *Keys*

[Keys](/overview/indev) hakkında daha fazlasını öğrenin.

## Örnek
```eval_rst

.. include:: /lv_examples/src/lv_ex_canvas/index.rst

```

## API 

```eval_rst

.. doxygenfile:: lv_canvas.h
  :project: lvgl
        
```

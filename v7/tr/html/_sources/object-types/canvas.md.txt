```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/tr/object-types/canvas.md
```
# Tuval (lv_canvas)

## Giriş
A Canvas is like an [Image](/object-types/img) where the user can draw anything.

### Ön Bellek
The Canvas needs a buffer which stores the drawn image.
To assign a buffer to a Canvas, use `lv_canvas_set_buffer(canvas, buffer, width, height, LV_IMG_CF_...)`.
`buffer` is a static buffer (not just a local variable) to hold the image of the canvas.
For example,
`static lv_color_t buffer[LV_CANVAS_BUF_SIZE_TRUE_COLOR(width, height)]`. `LV_CANVAS_BUF_SIZE_...`  makroları farklı renk formatlarında ki önbellek boyutunu belirlemeye yardım eder.


The canvas supports all the built-in color formats like `LV_IMG_CF_TRUE_COLOR` or `LV_IMG_CF_INDEXED_2BIT`. See the full list in the [Color formats](/overview/image.html#color-formats) section.

### Palet
For `LV_IMG_CF_INDEXED_...` color formats, a palette needs to be initialized with  `lv_canvas_set_palette(canvas, 3, LV_COLOR_RED)`. It sets pixels with *index=3* to red.


### Çizim
To set a pixel on the canvas, use `lv_canvas_set_px(canvas, x, y, LV_COLOR_RED)`.
With `LV_IMG_CF_INDEXED_...` or `LV_IMG_CF_ALPHA_...`, the index of the color or the alpha value needs to be passed as color. E.g. `lv_color_t c; c.full = 3;`

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
A rotated image can be added to canvas with `lv_canvas_rotate(canvas, &imd_dsc, angle, x, y, pivot_x, pivot_y)`.
`img_dsc` tarafından gösterilen imajı verilen eksen etrafında döndürecek ve `canvas`ın  `x`, `y`  kordinatlarında saklar.
Instead of `img_dsc`, the buffer of another canvas also can be used by `lv_canvas_get_img(canvas)`.

Bir tuvalin kendi üzerinde döndürülemeyeceğini dikkate alınız. Bir kaynağa ve belirlenmiş tuvale veya imaja ihtiyacınız vardır. 

## Biçim
You can set the styles with `lv_canvas_set_style(btn, LV_CANVAS_STYLE_MAIN, &style)`.
`style.image.color` is used to tell the base color with `LV_IMG_CF_ALPHA_...` color format.

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

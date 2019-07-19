```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/tr/object-types/canvas.md
```
# Tuval (lv_canvas)

## Genel Taslak
[Image](/object-types/img) gibi bir tuval ile kullanıcı herşeyi çizebilir.

### Önbellek
Tuvalin çizilmiş imajı hafızada tutabilmesi için  bir önbelleğe ihtiyacı vardır.
Bir tuvale bir önbellek atamak için `lv_canvas_set_buffer(canvas, buffer, width, height, LV_IMG_CF_TRUE_COLOR_ALPHA)`kullanılır.
`buffer` tuvalin görüntüsünü tutan bir statik önbellektir(sadece yerel bir değişken değil).
Örneğin
`static lv_color_t buffer[LV_CANVAS_BUF_SIZE_TRUE_COLOR(width, height)]`. `LV_CANVAS_BUF_SIZE_...` macros help to determine the size of the buffer with different color formats.

### Palet
`LV_IMG_CF_INDEXED_...` için renk format paleti  `lv_canvas_set_palette(canvas, 3, LV_COLOR_RED)` ile başlatılması gerekir. Pikseli *index=3* ile kırmızı ayarlanır.


### Çizim
Bir pikseli ayarlamak için `lv_canvas_set_px(canvas, x, y, LV_COLOR_RED)` kullanılır.
`LV_IMG_CF_INDEXED_...` veya `LV_IMG_CF_ALPHA_...` ile rengin veya alfa değerinin indisi renk olarak geçmesi gerekir. Örneğin  `lv_color_t c; c.full = 3;`

`lv_canvas_fill_bg(canvas, LV_COLOR_BLUE)` tüm tuvali mavi doldurur

`lv_canvas_copy_buf(canvas, buffer_to_copy, x, y, width, height)` ile piksel dizisi tuvale kopyalanabilir . Ön belleğin ve tuvalin renk formatı eşleşmesi gerekir.

Bir şey çizmek için tuval kullanılır
- `lv_canvas_draw_rect(canvas, x, y, width, heigth, &style)`
- `lv_canvas_draw_text(canvas, x, y, max_width, &style, txt, LV_LABEL_ALIGN_LEFT/CENTER/RIGTH)`
- `lv_canvas_draw_img(canvas, x, y, &img_src, &style)`
- `lv_canvas_draw_line(canvas, point_array, point_cnt, &style)`
- `lv_canvas_draw_polygon(canvas, points_array, point_cnt, &style)`
- `lv_canvas_draw_arc(canvas, x, y, radius, start_angle, end_angle, &style)`

### Rotate
A rotated image can be added to canvas with `lv_canvas_rotate(canvas, &imd_dsc, angle, x, y, pivot_x, pivot_y)`. 
It will rotate the image shown by `img_dsc` around the given pivot and stores it on the `x`, `y` coordinates of `canvas`.
Instead of `img_dsc` and the buffer of an other canvas also can be used by `lv_canvas_get_img(canvas)`.

Note that a canvas can't be rotated on itself.  You need a source and destination canvas or image.

## Styles
You can set the styles with `lv_canvas_set_style(btn, LV_CANVAS_STYLE_MAIN, &style)`. 
`style.image.color` is used to tell the base color with `LV_IMG_CF_ALPHA_...` color format. 

## Events
Only the [Generic events](/overview/event.html#generic-events) are sent by the object type.

Learn more about [Events](/overview/event).

## Keys
No *Keys* are processed by the object type.

Learn more about [Keys](/overview/indev).

## Example
```eval_rst

.. include:: /lv_examples/src/lv_ex_canvas/index.rst

```

## API 

```eval_rst

.. doxygenfile:: lv_canvas.h
  :project: lvgl
        
```

```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/fr/object-types/canvas.md
```
# Canvas (lv_canvas)

## Vue d’ensemble
A Canvas is like an [Image](/object-types/img) where the user can draw anything.

### Tampon
The Canvas needs a buffer which stores the drawn image.
To assign a buffer to a Canvas, use `lv_canvas_set_buffer(canvas, buffer, width, height, LV_IMG_CF_...)`.
`buffer` is a static buffer (not just a local variable) to hold the image of the canvas.
For example,
`static lv_color_t buffer[LV_CANVAS_BUF_SIZE_TRUE_COLOR(width, height)]`.  Les macros `LV_CANVAS_BUF_SIZE_...` aident à calculer la taille du tampon pour différents formats de couleur.


The canvas supports all the built-in color formats like `LV_IMG_CF_TRUE_COLOR` or `LV_IMG_CF_INDEXED_2BIT`. See the full list in the [Color formats](/overview/image.html#color-formats) section.

### Palette
For `LV_IMG_CF_INDEXED_...` color formats, a palette needs to be initialized with  `lv_canvas_set_palette(canvas, 3, LV_COLOR_RED)`. It sets pixels with *index=3* to red.


### Dessin
To set a pixel on the canvas, use `lv_canvas_set_px(canvas, x, y, LV_COLOR_RED)`.
With `LV_IMG_CF_INDEXED_...` or `LV_IMG_CF_ALPHA_...`, the index of the color or the alpha value needs to be passed as color. E.g. `lv_color_t c; c.full = 3;`

`lv_canvas_fill_bg(canvas, LV_COLOR_BLUE)` remplit tout le canvas en bleu.

Un tableau de pixels peut être copié sur le canvas avec `lv_canvas_copy_buf(canvas, buffer_to_copy, x, y, width, height)`. Le format de couleur du tampon et du canevas doivent correspondre.

Pour dessiner sur le canvas, utilisez
- `lv_canvas_draw_rect(canvas, x, y, width, heigth, &style)`,
- `lv_canvas_draw_text(canvas, x, y, max_width, &style, txt, LV_LABEL_ALIGN_LEFT/CENTER/RIGTH)`,
- `lv_canvas_draw_img(canvas, x, y, &img_src, &style)`,
- `lv_canvas_draw_line(canvas, point_array, point_cnt, &style)`,
- `lv_canvas_draw_polygon(canvas, points_array, point_cnt, &style)`,
- `lv_canvas_draw_arc(canvas, x, y, radius, start_angle, end_angle, &style)`.

Ces fonctions ne peuvent dessiner que dans des tampons `LV_IMG_CF_TRUE_COLOR`, `LV_IMG_CF_TRUE_COLOR_CHROMA_KEYED` et `LV_IMG_CF_TRUE_COLOR_ALPHA`. `LV_IMG_CF_TRUE_COLOR_ALPHA` fonctionne uniquement avec `LV_COLOR_DEPTH 32`.

### Rotation
A rotated image can be added to canvas with `lv_canvas_rotate(canvas, &imd_dsc, angle, x, y, pivot_x, pivot_y)`.
L'image spécifiée par `img_dsc` est transformé par rotation autour du pivot puis copiée dans le canvas aux coordonnées `x`, `y`.
Instead of `img_dsc`, the buffer of another canvas also can be used by `lv_canvas_get_img(canvas)`.

Notez que la rotation d'un canvas ne peut se fairesur lui-même. Vous avez besoin d'une source, image ou canevas, et d'un canvas de destination.

## Styles
You can set the styles with `lv_canvas_set_style(btn, LV_CANVAS_STYLE_MAIN, &style)`.
`style.image.color` is used to tell the base color with `LV_IMG_CF_ALPHA_...` color format.

## Evénements
Seuls les [événements génériques](/overview/event.html#generic-events) sont envoyés par ce type d'objet.

Apprenez-en plus sur les [événements](/overview/event).

## Touches
Aucune *touche* n'est traitée par ce type d'objet.

Apprenez-en plus sur les [touches](/overview/indev).

## Exemple
```eval_rst

.. include:: /lv_examples/src/lv_ex_canvas/index.rst

```

## API

```eval_rst

.. doxygenfile:: lv_canvas.h
  :project: lvgl

```

```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/fr/object-types/canvas.md
```
# Canvas (lv_canvas)

## Vue d’ensemble
Un canevas est comme une [image](/object-types/img) où l'utilisateur peut dessiner ce qu'il souhaite.

### Tampon
Le canevas a besoin d’un tampon qui mémorise l’image dessinée.
Pour affecter un tampon à un canevas, utilisez `lv_canvas_set_buffer(canvas, buffer, width, height, LV_IMG_CF_...)`. 
`buffer` est un tampon statique (pas seulement une variable locale) destiné à contenir l'image du canevas.
Par exemple
`static lv_color_t buffer[LV_CANVAS_BUF_SIZE_TRUE_COLOR(width, height)]`.  Les macros `LV_CANVAS_BUF_SIZE_...` aident à calculer la taille du tampon pour différents formats de couleur.


Le canvas prend en charge tous les formats de couleur intégrés tels que `LV_IMG_CF_TURE_COLOR` ou `LV_IMG_CF_INDEXED_2BIT`. Consultez la liste complète dans la section [formats de couleur](/overview/image.html#formats-de-couleur).

### Palette
Pour les formats de couleur `LV_IMG_CF_INDEXED_...` une palette doit être initialisée. Par exemple, `lv_canvas_set_palette(canvas, 3, LV_COLOR_RED)` colore les pixels avec *index = 3* en rouge.


### Dessin
Pour tracer un pixel sur la toile, utilisez `lv_canvas_set_px(canvas, x, y, LV_COLOR_RED)`. 
Avec `LV_IMG_CF_INDEXED_...` ou `LV_IMG_CF_ALPHA_...` l'indice de la couleur ou la valeur alpha doit être passé en tant que couleur. P.ex. `lv_color_t c; c.full = 3;`

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
Une image peut être ajoutée au canvas après rotation avec `lv_canvas_rotate(canvas, &img_dsc, angle, x, y, pivot_x, pivot_y)`. 
L'image spécifiée par `img_dsc` est transformé par rotation autour du pivot puis copiée dans le canvas aux coordonnées `x`, `y`.
Au lieu de `img_dsc`, un autre canevas peut être utilisé par `lv_canvas_get_img(canvas)`.

Notez que la rotation d'un canvas ne peut se fairesur lui-même. Vous avez besoin d'une source, image ou canevas, et d'un canvas de destination.

## Styles
Vous pouvez définir les styles avec `lv_canvas_set_style(btn, LV_CANVAS_STYLE_MAIN, &style)`. 
`style.image.color` est utilisé pour spécifier la couleur de base avec les formats de couleur `LV_IMG_CF_ALPHA_...`. 

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

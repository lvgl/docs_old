```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/en/object-types/canvas.md
```
# Canvas (lv_canvas)

## Overview
A Canvas is like an [Image](/object-types/img) where the user can draw anything. 

### Buffer
The Canvas needs a buffer which stores the drawn image. 
To assign a buffer to a Canvas use `lv_canvas_set_buffer(canvas, buffer, width, height, LV_IMG_CF_TRUE_COLOR_ALPHA)`. 
`buffer` is a static buffer (not just a local variable) to hold the image of the canvas. 
For example 
`static lv_color_t buffer[LV_CANVAS_BUF_SIZE_TRUE_COLOR(width, height)]`. `LV_CANVAS_BUF_SIZE_...` macros help to determine the size of the buffer with different color formats.

### Palette
For `LV_IMG_CF_INDEXED_...` color formats a palette needs to be initialized with  `lv_canvas_set_palette(canvas, 3, LV_COLOR_RED)`. It sets pixels with *index=3* to red.


### Drawing
To set a pixel on the canvas use `lv_canvas_set_px(canvas, x, y, LV_COLOR_RED)`. 
With `LV_IMG_CF_INDEXED_...` or `LV_IMG_CF_ALPHA_...` the index of the color or the alpha value needs to be passed as color. E.g. `lv_color_t c; c.full = 3;`

`lv_canvas_fill_bg(canvas, LV_COLOR_BLUE)` fills the whole canvas to blue.

An array of pixels can be copied to the canvas with `lv_canvas_copy_buf(canvas, buffer_to_copy, x, y, width, height)`. The color format of the buffer and the canvas need to match.

To draw something to the canvas use
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

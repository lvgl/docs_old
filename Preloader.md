_Written for v5.2_

## Overview
The preloader object is **a spinning arc over a border**. 

The **length of the arc** can be adjusted by `lv_preload_set_arc_length(preload, deg)`.

The **speed of the spinning** can be adjusted by `lv_preload_set_spin_time(preload, time_ms)`.


## Style usage
The `LV_PRELOAD_STYLE_MAIN` style describes both the arc and the border style:
- **arc** is described by the `line` properties
- **border** is described by the `body.border` properties including `body.padding.hor/ver` (smaller is used) to give a smaller radius for the border.

## Example

![Preloader image](http://docs.littlevgl.com/img/preloader-lv_preload.png)

```c
/*Create a style for the Preloader*/
static lv_style_t style;
lv_style_copy(&style, &lv_style_plain);
style.line.width = 10;                         /*10 px thick arc*/
style.line.color = LV_COLOR_HEX3(0x258);       /*Blueish arc color*/

style.body.border.color = LV_COLOR_HEX3(0xBBB); /*Gray background color*/
style.body.border.width = 10;
style.body.padding.hor = 0;

/*Create a Preloader object*/
lv_obj_t * preload = lv_preload_create(lv_scr_act(), NULL);
lv_obj_set_size(preload, 100, 100);
lv_obj_align(preload, NULL, LV_ALIGN_CENTER, 0, 0);
lv_preload_set_style(preload, LV_PRELOAD_STYLE_MAIN, &style);
```

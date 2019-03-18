_Written for v5.1_

## Overview

The containers are **rectangle-like object** with some special features. 

You can apply a **layout** on the containers to automatically order their children. The layout spacing comes from style.body.padding.hor/ver/inner properties. The possible layout options:

- LV_LAYOUT_OFF: Do not align the children
- LV_LAYOUT_CENTER: Align children to the center in column and keep _pad.inner_ space between them 
- LV_LAYOUT_COL_L: Align children in a left justified column. Keep _pad.hor_ space on the left, _pad.ver_ space on the top and _pad.inner_ space between the children.
- LV_LAYOUT_COL_M: Align children in centered column. Keep _pad.ver_ space on the top and _pad.inner_ space between the children.
- LV_LAYOUT_COL_R: Align children in a right justified column. Keep _pad.hor_ space on the right, _pad.ver_ space on the top and _pad.inner_ space between the children.
- LV_LAYOUT_ROW_T: Align children in a top justified row. Keep _pad.hor_ space on the left, _pad.ver_ space on the top and _pad.inner_ space between the children.
- LV_LAYOUT_ROW_M: Align children in centered row. Keep _pad.hor_ space on the left and _pad.inner_ space between the children.
- LV_LAYOUT_ROW_B: Align children in a bottom justified row. Keep _pad.hor_ space on the left, _pad.ver_ space on the bottom and _pad.inner_ space between the children.
- LV_LAYOUT_PRETTY: Put as may objects as possible in a row (with at least _pad.inner_ space and _pad.hor_ space on the sides) and begin a new row. Divide the space in each line equally between the children. Keep _pad.ver_ space on the top and _pad.inner_ space between the lines.
- LV_LAYOUT_GRID: Similar to PRETTY LAYOUT but not divide horizontal space equally just let _pad.hor_ space

You can enable an **auto fit** feature which automatically set the container size to include all children. It will keep _pad.hor_ space on the left and right and _pad.ver_ space on the top an bottom. The auto fit can be enable horizontally, vertically or in both direction with `lv_cont_set_fit(cont, true, true)` function. The second parameter is the horizontal, the third parameter is the vertical fit enable.

## Style usage

- **style.body** properties are used.

## Notes

- You **can't set the child position with hor/ver fit enabled**. Let's imagine what happens. If you change the position of the only child when fit is enabled the the container will move/fit "around" the new position. If you have more objects on a container then you can align them relative to each other.  As a workaround you can create a small transparent object on the container. It will fix the container to not "follow" the children.

## Example

![Container image](http://docs.littlevgl.com/img/container-lv_cont.png)
```c
lv_obj_t * box1;
box1 = lv_cont_create(lv_scr_act(), NULL);
lv_obj_set_style(box1, &lv_style_pretty);
lv_cont_set_fit(box1, true, true);

/*Add a text to the container*/
lv_obj_t * txt = lv_label_create(box1, NULL);
lv_label_set_text(txt, "Lorem ipsum dolor\n"
                       "sit amet, consectetur\n"
                       "adipiscing elit, sed do\n"
                       "eiusmod tempor incididunt\n"
                       "ut labore et dolore\n"
                       "magna aliqua.");

lv_obj_align(box1, NULL, LV_ALIGN_IN_TOP_LEFT, 10, 10);      /*Align the container*/

/*Create a style*/
static lv_style_t style;
lv_style_copy(&style, &lv_style_pretty_color);
style.body.shadow.width = 6;
style.body.padding.hor = 5;                                 /*Set a great horizontal padding*/

/*Create an other container*/
lv_obj_t * box2;
box2 = lv_cont_create(lv_scr_act(), NULL);
lv_obj_set_style(box2, &style);     /*Set the new style*/
lv_cont_set_fit(box2, true, false); /*Do not enable the vertical fit */
lv_obj_set_height(box2, 55);        /*Set a fix height*/

/*Add a text to the new container*/
lv_obj_t * txt2 = lv_label_create(box2, NULL);
lv_label_set_text(txt2, "No vertical fit 1...\n"
                        "No vertical fit 2...\n"
                        "No vertical fit 3...\n"
                        "No vertical fit 4...");

/*Align the container to the bottom of the previous*/
lv_obj_align(box2, box1, LV_ALIGN_OUT_BOTTOM_MID, 30, -30);
```

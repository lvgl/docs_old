# Container

## Overview

The containers are **rectangle-like object** with some special features. 

You can apply a **layout** on the containers to automatically order their children. The layout spacing comes from `style.body.padding. ...` properties. The possible layout options:

- **LV_LAYOUT_OFF** Do not align the children
- **LV_LAYOUT_CENTER** Align children to the center in column and keep `padding.inner` space between them 
- **LV_LAYOUT_COL_**: Align children in a left justified column. Keep `padding.left` space on the left, `pad.top` space on the top and `padding.inner` space between the children.
- **LV_LAYOUT_COL_M** Align children in centered column. Keep `padding.top` space on the top and `padding.inner` space between the children.
- **LV_LAYOUT_COL_R** Align children in a right justified column. Keep `padding.right` space on the right, `padding.top` space on the top and `padding.inner` space between the children.
- **LV_LAYOUT_ROW_T** Align children in a top justified row. Keep `padding.left` space on the left, `padding.top` space on the top and `padding.inner` space between the children.
- **LV_LAYOUT_ROW_M** Align children in centered row. Keep `padding.left` space on the left and `padding.inner` space between the children.
- **LV_LAYOUT_ROW_B** Align children in a bottom justified row. Keep `padding.left` space on the left, `padding.bottom` space on the bottom and `padding.inner` space between the children.
- **LV_LAYOUT_PRETTY** Put as may objects as possible in a row (with at least `padding.inner` space and `padding.left/right` space on the sides). Divide the space in each line equally between the children. 
Keep `padding.top` space on the top and `pad.inner` space between the lines.
- **LV_LAYOUT_GRID** Similar to `LV_LAYOUT_PRETTY` but not divide horizontal space equally just let `padding.left/right` on the edges and `padding.inner` space betweenthe elemnts.


Container have an **auto fit** features whcih can automaticall change the size of the Container accoring to its children and/or parent. The following optionas are exist:
- **LV_FIT_NONE** Do not change the size automatically
- **LV_FIT_TIGHT** Set the size to involve all children by keeping `padding.top/bottom/left/right` space on the edges.
- **LV_FIT_FLOOD** Set the size to the parents size by keeping `padding.top/bottom/left/right` (from the parent's style) space.
- **LV_FINT_FILL** Use `LV_FIT_FLOOD` while smaller then the parent and `LV_FIT_TIGHT` when larger.

To set the auto fit use `lv_cont_set_fit(cont, LV_FIT_...)`. It will set the same auto fit in every directions.
To use different auto fit horizontally and vertically use `lv_cont_set_fit2(cont, hor_fit_type, ver_fit_type)`.
To use different auto fit in all 4 directions use `lv_cont_set_fit4(cont, left_fit_type, right_fit_type, top_fit_type, bottom_fit_type)`.

## Styles
You can set the styles with `lv_cont_set_style(btn, LV_CONT_STYLE_MAIN, &style)`. 
- **style.body** properties are used.

## Events
Only the [Genreric events](/overview/events.html#generic-events) are sent by the object type.

Learn more about [Events](/overview/events).

## Keys
No *Keys* are processed by the object type.

Learn more about [Keys](/overview/indev).

## Keys
The following *Keys* are processed by the Buttons:
- **LV_KEY_RIGHT/UP** Go to toggled state if toggling is enabled
- **LV_KEY_LEFT/DOWN** Go to non-toggled state if toggling is  enabled

Note that, as usual, the state of `LV_KEY_ENTER` is translated to `LV_EVENT_PRESSED/PRESSING/RELEASED` etc.


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

# Bar (lv_bar)

## Overview

The Bar objects have got two main parts: 
1. a **background** which is the object itself 
2. an **indicator** which shape is similar to the background but its width/height can be adjusted. 

The orientation of the bar can be **vertical or horizontal** according to the width/height ratio. Logically on horizontal bars the indicator width, on vertical bars the indicator height can be changed. 

A **new value** can be set by: `lv_bar_set_value(bar, new_value, LV_ANIM_ON/OFF)`. 
The value is interpreted in **range** (minimum and maximum values) which can be modified with `lv_bar_set_range(bar, min, max)`. 
The default range is: 1..100.

The new value in `lv_bar_set_value` can be set with our without an **animation** depending on the last paramter (`LV_ANIM_ON/OFF`). 
The the of teh animation can be adjusted by `lv_bar_set_anim_time(bar, 100)`. The time is is  millisecinds unit. 


The bar can be drawn **symmetrical** to zero (drawn from zero left ot right) if it's enabled with `lv_bar_set_sym(bar, true)`

## Styles

To set the style of an *Bar* object use `lv_bar_set_style(arc, LV_BAR_STYLE_MAIN, &style)`

- **LV_BAR_STYLE_BG** is an [Base object](/object-types/obj) therefore it uses its style elements. Its default style is: `lv_style_pretty`. 
- **LV_BAR_STYLE_INDIC** is similar to the background. It uses the *left*, *right*, *top* and *bottom* paddings to keeps some space form the edges of the background. Its default style is: `lv_style_pretty_color`.

## Events
Only the [Genreric events](/overview/events.html#generic-events) are sent by the object type.

Learn more about [Events](/overview/events).

## Keys
No *Keys* are processed by the object type.

Learn more about [Keys](/overview/indev).

## Example

![Bar image](http://docs.littlevgl.com/img/bar-lv_bar.png)

```c
/*Create a default bar*/
lv_obj_t * bar1 = lv_bar_create(lv_scr_act(), NULL);
lv_obj_set_size(bar1, 200, 30);
lv_obj_align(bar1, NULL, LV_ALIGN_IN_TOP_RIGHT, -20, 30);
lv_bar_set_value(bar1, 70);

/*Create a label right to the bar*/
lv_obj_t * bar1_label = lv_label_create(lv_scr_act(), NULL);
lv_label_set_text(bar1_label, "Default");
lv_obj_align(bar1_label, bar1, LV_ALIGN_OUT_LEFT_MID, -10, 0);

/*Create a bar and an indicator style*/
static lv_style_t style_bar;
static lv_style_t style_indic;

lv_style_copy(&style_bar, &lv_style_pretty);
style_bar.body.main_color = LV_COLOR_BLACK;
style_bar.body.grad_color = LV_COLOR_GRAY;
style_bar.body.radius = LV_RADIUS_CIRCLE;
style_bar.body.border.color = LV_COLOR_WHITE;

lv_style_copy(&style_indic, &lv_style_pretty);
style_indic.body.grad_color =  LV_COLOR_GREEN;
style_indic.body.main_color=  LV_COLOR_LIME;
style_indic.body.radius = LV_RADIUS_CIRCLE;
style_indic.body.shadow.width = 10;
style_indic.body.shadow.color = LV_COLOR_LIME;
style_indic.body.padding.hor = 3;           /*Make the indicator a little bit smaller*/
style_indic.body.padding.ver = 3;

/*Create a second bar*/
lv_obj_t * bar2 = lv_bar_create(lv_scr_act(), bar1);
lv_bar_set_style(bar2, LV_BAR_STYLE_BG, &style_bar);
lv_bar_set_style(bar2, LV_BAR_STYLE_INDIC, &style_indic);
lv_obj_align(bar2, bar1, LV_ALIGN_OUT_BOTTOM_MID, 0, 30); /*Align below 'bar1'*/

/*Create a second label*/
lv_obj_t * bar2_label = lv_label_create(lv_scr_act(), bar1_label);
lv_label_set_text(bar2_label, "Modified");
lv_obj_align(bar2_label, bar2, LV_ALIGN_OUT_LEFT_MID, -10, 0);
```

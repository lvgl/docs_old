_Written for v5.1_

## Overview

The Line Meter object consists of some **radial lines** which draw a scale. When setting a new value with `lv_lmeter_set_value(lmeter, new_value)` the proportional part of the scale will be recolored. 

The `lv_lmeter_set_range(lmeter, min, max)` function sets the **range** of the line meter.

You can set the **angle** of the scale and the **number of the lines** by: `lv_lmeter_set_scale(lmeter, angle, line_num)`. The default angle is 240 and the default line number is 31

## Style usage

The line meter uses one style which can be set by `lv_lmeter_set_style(lmeter, &style)`. The line meter's properties are derived from the following style attributes:

- **line.color** "inactive line's" color which are greater then the current value
- **body.main_color** "active line's" color at the beginning of the scale
- **body.grad_color** "active line's" color at the end of the scale (gradient with main color)
- **body.padding.hor** line length
- **line.width** line width

The default style is _lv_style_pretty_color_.

## Notes

- The line meter has no background.
- It is recommended to use **antialiasing** on smaller dpi displays to show smooth lines
- Odd number of scale lines look better
- It looks better if the scale angle is: (line number - 1) * N, where N is an integer

## Example

![Line meter image](http://docs.littlevgl.com/img/line-meter-lv_lmeter.png)
```c
/*******************************
 * Create 3 similar line meter
 *******************************/

/*Create a simple style with ticker line width*/
static lv_style_t style_lmeter1;
lv_style_copy(&style_lmeter1, &lv_style_pretty_color);
style_lmeter1.line.width = 2;
style_lmeter1.line.color = LV_COLOR_SILVER;
style_lmeter1.body.main_color = LV_COLOR_HEX(0x91bfed);         /*Light blue*/
style_lmeter1.body.grad_color = LV_COLOR_HEX(0x04386c);         /*Dark blue*/

/*Create the first line meter */
lv_obj_t * lmeter;
lmeter = lv_lmeter_create(lv_scr_act(), NULL);
lv_lmeter_set_range(lmeter, 0, 100);                   /*Set the range*/
lv_lmeter_set_value(lmeter, 30);                       /*Set the current value*/
lv_lmeter_set_style(lmeter, &style_lmeter1);           /*Apply the new style*/
lv_obj_set_size(lmeter, 80, 80);
lv_obj_align(lmeter, NULL, LV_ALIGN_IN_BOTTOM_LEFT, 20, -20);

/*Add a label to show the current value*/
lv_obj_t * label;
label = lv_label_create(lmeter, NULL);
lv_label_set_text(label, "30%");
lv_label_set_style(label, &lv_style_pretty);
lv_obj_align(label, NULL, LV_ALIGN_CENTER, 0, 0);

/*Create the second line meter and label*/
lmeter = lv_lmeter_create(lv_scr_act(), lmeter);
lv_lmeter_set_value(lmeter, 60);
lv_obj_align(lmeter, NULL, LV_ALIGN_IN_BOTTOM_MID, 0, -20);

label = lv_label_create(lmeter, label);
lv_label_set_text(label, "60%");
lv_obj_align(label, NULL, LV_ALIGN_CENTER, 0, 0);

/*Create the third line meter and label*/
lmeter = lv_lmeter_create(lv_scr_act(), lmeter);
lv_lmeter_set_value(lmeter, 90);
lv_obj_align(lmeter, NULL, LV_ALIGN_IN_BOTTOM_RIGHT, -20, -20);

label = lv_label_create(lmeter, label);
lv_label_set_text(label, "90%");
lv_obj_align(label, NULL, LV_ALIGN_CENTER, 0, 0);

/*********************************
 * Create a greater line meter
 *********************************/

/*Create a new style*/
static lv_style_t style_lmeter2;
lv_style_copy(&style_lmeter2, &lv_style_pretty_color);
style_lmeter2.line.width = 2;
style_lmeter2.line.color = LV_COLOR_SILVER;
style_lmeter2.body.padding.hor = 16;            /*Line length*/
style_lmeter2.body.main_color = LV_COLOR_LIME;
style_lmeter2.body.grad_color = LV_COLOR_ORANGE;

/*Create the line meter*/
lmeter = lv_lmeter_create(lv_scr_act(), lmeter);
lv_obj_set_style(lmeter, &style_lmeter2);
lv_obj_set_size(lmeter, 120, 120);
lv_obj_align(lmeter, NULL, LV_ALIGN_IN_TOP_MID, 0, 20);
lv_lmeter_set_scale(lmeter, 240, 31);
lv_lmeter_set_value(lmeter, 90);

/*Create a label style with greater font*/
static lv_style_t style_label;
lv_style_copy(&style_label, &lv_style_pretty);
style_label.text.font = &lv_font_dejavu_60;
style_label.text.color = LV_COLOR_GRAY;

/*Add a label to show the current value*/
label = lv_label_create(lmeter, label);
lv_label_set_text(label, "90%");
lv_obj_set_style(label, &style_label);
lv_obj_align(label, NULL, LV_ALIGN_CENTER, 0, 0);
```

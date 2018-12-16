_Written for v5.1_
## Overview

The gauge is a meter with **scale labels** and **needles**. You can use the `lv_gauge_set_scale(gauge, angle, line_num, label_cnt)` function to adjust the scale angle and the number of the scale lines and labels. The default settings are:  220 degrees, 6 scale labels and 21 lines.

The gauge can show **more then one needles** . Use the `lv_gauge_set_needle_count(gauge, needle_num, color_array)` function to set the number of needles and an array with colors for each needle. (The array must be static or global variable).

You can use `lv_gauge_set_value(gauge, needle_id, value)` to **set the value of a needle**.

To set a **critical value** use `lv_gauge_set_critical_value(gauge, value)`. The scale color ill be changed to _line.color_ after this value. (default: 80)

The **range** of the gauge can be specified by `lv_gauge_set_range(gauge, min, max)`.

## Style usage

The gauge uses one style which can be set by `lv_gauge_set_style(gauge, &style)`. The gauge's properties are derived from the following style attributes:

- **body.main_color** line's color at the beginning of the scale
- **body.grad_color** line's color at the end of the scale (gradient with main color)
- **body.padding.hor** line length
- **body.padding.inner** label distance from the scale lines 
- **line.width** line width
- **line.color** line's color after the critical value
- **text.font/color/letter_space** label attributes

## Example

![Gauge image](http://docs.littlevgl.com/img/gauge-lv_gauge.png)
```c
/*Create a style*/
static lv_style_t style;
lv_style_copy(&style, &lv_style_pretty_color);
style.body.main_color = LV_COLOR_HEX3(0x666);     /*Line color at the beginning*/
style.body.grad_color =  LV_COLOR_HEX3(0x666);    /*Line color at the end*/
style.body.padding.hor = 10;                      /*Scale line length*/
style.body.padding.inner = 8 ;                    /*Scale label padding*/
style.body.border.color = LV_COLOR_HEX3(0x333);   /*Needle middle circle color*/
style.line.width = 3;
style.text.color = LV_COLOR_HEX3(0x333);
style.line.color = LV_COLOR_RED;                  /*Line color after the critical value*/


/*Describe the color for the needles*/
static lv_color_t needle_colors[] = {LV_COLOR_BLUE, LV_COLOR_ORANGE, LV_COLOR_PURPLE};

/*Create a gauge*/
lv_obj_t * gauge1 = lv_gauge_create(lv_scr_act(), NULL);
lv_gauge_set_style(gauge1, &style);
lv_gauge_set_needle_count(gauge1, 3, needle_colors);
lv_obj_align(gauge1, NULL, LV_ALIGN_CENTER, 0, 20);

/*Set the values*/
lv_gauge_set_value(gauge1, 0, 10);
lv_gauge_set_value(gauge1, 1, 20);
lv_gauge_set_value(gauge1, 2, 30);
```

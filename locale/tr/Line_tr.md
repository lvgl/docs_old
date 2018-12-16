_Written for v5.1_

## Overview

The line object is capable of **drawing straight lines** between a set of points. The points has to be stored in an `lv_point_t` array and passed to the object by the `lv_line_set_points(lines, point_array, point_num)` function. 

It is possible to **automatically set the size** of the line object according to its points. You can enable it with the `lv_line_set_auto_size(line, true)` function. If enabled then when the points are set then the object width and height will be changed according to the max. x and max. y coordinates among the points. The _auto size_ is enabled by default.

Basically the _y == 0_ point is in the top of the object but you can **invert the y coordinates** with `lv_line_set_y_invert(line, true)`. After it the y coordinates will be subtracted from object's height.

## Style usage

- **style.line** properties are used

## Notes

## Example

![Example of Line in LittlevGL Graphics Library ](http://docs.littlevgl.com/img/line-lv_line.png)

```c
/*Create an array for the points of the line*/
static lv_point_t line_points[] = { {5, 5}, {70, 70}, {120, 10}, {180, 60}, {240, 10} };

/*Create line with default style*/
lv_obj_t * line1;
line1 = lv_line_create(lv_scr_act(), NULL);
lv_line_set_points(line1, line_points, 5);     /*Set the points*/
lv_obj_align(line1, NULL, LV_ALIGN_IN_TOP_MID, 0, 20);

/*Create new style (thin light blue)*/
static lv_style_t style_line2;
lv_style_copy(&style_line2, &lv_style_plain);
style_line2.line.color = LV_COLOR_MAKE(0x2e, 0x96, 0xff);
style_line2.line.width = 2;

/*Copy the previous line and apply the new style*/
lv_obj_t * line2 = lv_line_create(lv_scr_act(), line1);
lv_line_set_style(line2, &style_line2);
lv_obj_align(line2, line1, LV_ALIGN_OUT_BOTTOM_MID, 0, -20);

/*Create new style (thick dark blue)*/
static lv_style_t style_line3;
lv_style_copy(&style_line3, &lv_style_plain);
style_line3.line.color = LV_COLOR_MAKE(0x00, 0x3b, 0x75);
style_line3.line.width = 5;

/*Copy the previous line and apply the new style*/
lv_obj_t * line3 = lv_line_create(lv_scr_act(), line1);
lv_line_set_style(line3, &style_line3);
lv_obj_align(line3, line2, LV_ALIGN_OUT_BOTTOM_MID, 0, -20);
```

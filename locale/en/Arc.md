_Written for v5.2_

## Overview

The Arc object **draws an arc** within **start and end angles** and with a given **thickness**.

To set the angles use the `lv_arc_set_angles(arc, start_angle, end_angle)` function. The zero degree is at the bottom of the object and the degrees are increasing in a counter-clockwise direction. The angles should be in [0;360] range.

To **set the style** of an Arc object use `lv_arc_set_style(arc, LV_ARC_STYLE_MAIN, &style)`

## Style usage
- **line.rounded** make the endpoints rounded (opacity won't work properly if set to 1)
- **line.width** the thickness of the arc
- **line.color** the color of the arc.

## Notes
- The **width and height** of the Arc should be the **same**
- Currently the Arc object **does not support anti-aliasing**.

## Example

![Arc image](http://docs.littlevgl.com/img/arc-lv_arc.png)

```c
/*Create style for the Arcs*/
lv_style_t style;
lv_style_copy(&style, &lv_style_plain);
style.line.color = LV_COLOR_BLUE;           /*Arc color*/
style.line.width = 8;                       /*Arc width*/

/*Create an Arc*/
lv_obj_t * arc = lv_arc_create(lv_scr_act(), NULL);
lv_arc_set_style(arc, LV_ARC_STYLE_MAIN, &style);          /*Use the new style*/
lv_arc_set_angles(arc, 90, 60);
lv_obj_set_size(arc, 150, 150);
lv_obj_align(arc, NULL, LV_ALIGN_CENTER, 0, 0);

/*Copy the previous Arc and set different angles and size*/
arc = lv_arc_create(lv_scr_act(), arc);
lv_arc_set_angles(arc, 90, 20);
lv_obj_set_size(arc, 125, 125);
lv_obj_align(arc, NULL, LV_ALIGN_CENTER, 0, 0);

/*Copy the previous Arc and set different angles and size*/
arc = lv_arc_create(lv_scr_act(), arc);
lv_arc_set_angles(arc, 90, 310);
lv_obj_set_size(arc, 100, 100);
lv_obj_align(arc, NULL, LV_ALIGN_CENTER, 0, 0);
```

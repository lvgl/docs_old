_Written for v5.1_

## Overview

Charts have a rectangle-like background with horizontal and vertical division lines. You can add any number of **series** to the charts by `lv_chart_add_series(chart, color)`. It allocates data for a `lv_chart_series_t` structure which contains the chosen _color_ and an array for the data. 

You have several options to set the data of series:

1. Set the values manually in the array like `ser1-&gt;points[3] = 7` and refresh the chart with `lv_chart_refresh(chart)`.
2. Use the `lv_chart_set_next(chart, ser, value)` function to shift all data to left and set a new data on the most right position.
3. Initialize all points to a given value with: `lv_chart_init_points(chart, ser, value)`.
4. Set all points from an array with: `lv_chart_set_points(chart, ser, value_array)`.

There are four **data display types**:

- LV_CHART_TYPE_NONE: do not display the points. It can be used if you would like to add your own draw method.
- LV_CHART_TYPE_LINE: draw lines between the points
- LV_CHART_TYPE_COL: Draw columns
- LV_CHART_TYPE_POINT: Draw points

You can specify the display type with `lv_chart_set_type(chart, TYPE)`. The `LV_CHART_TYPE_LINE | LV_CHART_TYPE_POINT` type is also valid to draw both lines and points.

You can specify a the **min. and max. values in y** directions with `lv_chart_set_range(chart, y_min, y_max)`. The value of the points will be scaled proportionally. The default range is: 0..100.

The **number of points** in the  data lines can be modified by `lv_chart_set_point_count(chart, point_num)`. The default value is 10.

The **number of horizontal and vertical division lines**  can be modified by `lv_chart_set_div_line_count(chart, hdiv_num, vdiv_num)`. The default settings are 3 horizontal and 5 vertical division lines.

To set the **line width** and **point radius** use the `lv_chart_set_series_width(chart, size)` function. The default value is: 2.

The *_opacity of the data lines_ can be specified by `lv_chart_set_series_opa(chart, opa)`. The default value is: OPA_COVER.

You can apply a **dark color fade** on the bottom of columns and points by `lv_chart_set_series_darking(chart, effect)` function. The default dark level is OPA_50.

## Style usage

- **style.body** properties set the background's appearance
- **style.line** properties set the division lines' appearance

The series related parameters can be set directly for each chart with `lv_chart_set_series_width()`, `lv_chart_set_series_opa()` and  `lv_chart_set_series_dark()`.

## Example

![Chart image](http://docs.littlevgl.com/img/chart-lv_chart.png)

```c
/*Create a style for the chart*/
static lv_style_t style;
lv_style_copy(&style, &lv_style_pretty);
style.body.shadow.width = 6;
style.body.shadow.color = LV_COLOR_GRAY;
style.line.color = LV_COLOR_GRAY;

/*Create a chart*/
lv_obj_t * chart;
chart = lv_chart_create(lv_scr_act(), NULL);
lv_obj_set_size(chart, 200, 150);
lv_obj_set_style(chart, &style);
lv_obj_align(chart, NULL, LV_ALIGN_CENTER, 0, 0);
lv_chart_set_type(chart, LV_CHART_TYPE_POINT | LV_CHART_TYPE_LINE);   /*Show lines and points too*/
lv_chart_set_series_opa(chart, LV_OPA_70);                            /*Opacity of the data series*/
lv_chart_set_series_width(chart, 4);                                  /*Line width and point radious*/

lv_chart_set_range(chart, 0, 100);

/*Add two data series*/
lv_chart_series_t * ser1 = lv_chart_add_series(chart, LV_COLOR_RED);
lv_chart_series_t * ser2 = lv_chart_add_series(chart, LV_COLOR_GREEN);

/*Set the next points on 'dl1'*/
lv_chart_set_next(chart, ser1, 10);
lv_chart_set_next(chart, ser1, 50);
lv_chart_set_next(chart, ser1, 70);
lv_chart_set_next(chart, ser1, 90);

/*Directly set points on 'dl2'*/
ser2->points[0] = 90;
ser2->points[1] = 70;
ser2->points[2] = 65;
ser2->points[3] = 65;
ser2->points[4] = 65;
ser2->points[5] = 65;

lv_chart_refresh(chart); /*Required after direct set*/
```

```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/en/widgets/chart.md
```
# Chart (lv_chart)

## Overview


Charts are basic object to visualize data points. 
It support *Line* charts (connect points with lines and/or draw points on them) and *Column* chart.

Chart also support division lines, 2 y axis, axis ticks, and texts on ticks.

## Parts and Styles
The Chart's main part is called `LV_CHART_PART_BG` and it uses all the typical background properties. 
The *text* style properties determine the style of the axis texts and the *line* properties determine ticks' style.
*Padding* values will make `LV_CHART_PART_SERIES` smaller. Padding also can be used to make space for axis texts.

The background of the series is called `LV_CHART_PART_SERIES` and it's placed on the main background. 
The division lines, and series data is drawn on this part. Besides the typical background style properties
the *line* style properties are used by the division lines. The *padding* values tells the space between the this part and the axis texts.  


The style of the series can be referenced by `LV_CHART_PART_SERIES`. In case of column type the following properties are used:
- *radius*: radius of the bars
- *padding_inner*: space between the columns of the same x coordinate

In case of Line type these properties are used:
- *line properties* to describe the lines
- *size* radius of the points
- *bg_opa*: the overall opacity of the area below the lines
- *bg_main_stop*: % of *bg_opa* at the top to create an alpha fade (0: transparent at the top, 255: *bg_opa* at the top)
- *bg_grad_stop*: %  of *bg_opa* at the bottom to create an alpha fade  (0: transparent at the bottom, 255: *bg_opa* at the top)
- *bg_drag_dir*: should be `LV_GRAD_DIR_VER` to allow alpha fading with *bg_main_stop* and *bg_grad_stop*

## Usage

### Data series
You can add any number of series to the charts by `lv_chart_add_series(chart, color)`.
It allocates data for a `lv_chart_series_t` structure which contains the chosen `color` and an array for the data points.

### Series' type
The following **data display types** exist:

- **LV_CHART_TYPE_NONE** - Do not display any data. It can be used to hide a series.
- **LV_CHART_TYPE_LINE** - Draw lines between the points.
- **LV_CHART_TYPE_COLUMN** - Draw columns.

You can specify the display type with `lv_chart_set_type(chart, LV_CHART_TYPE_...)`. The types can be 'OR'ed (like `LV_CHART_TYPE_LINE`).

### Modify the data
You have several options to set the data of series:
1. Set the values manually in the array like `ser1->points[3] = 7` and refresh the chart with `lv_chart_refresh(chart)`.
2. Use the `lv_chart_set_next(chart, ser, value)`.
3. Initialize all points to a given value with: `lv_chart_init_points(chart, ser, value)`.
4. Set all points from an array with: `lv_chart_set_points(chart, ser, value_array)`.

Use `LV_CHART_POINT_DEF` as value to make the library skip drawing that point, column, or line segment.

### Update modes
`lv_chart_set_next` can behave in two ways depending on *update mode*:
- **LV_CHART_UPDATE_MODE_SHIFT** - Shift old data to the left and add the new one o the right.
- **LV_CHART_UPDATE_MODE_CIRCULAR** - Circularly add the new data (Like an ECG diagram).

The update mode can be changed with `lv_chart_set_update_mode(chart, LV_CHART_UPDATE_MODE_...)`.

### Number of points
The number of points in the series can be modified by `lv_chart_set_point_count(chart, point_num)`. The default value is 10.

### Vertical range
You can specify the minimum and maximum values in y-direction with `lv_chart_set_range(chart, y_min, y_max)`. The value of the points will be scaled proportionally. The default range is: 0..100.

### Division lines
The number of horizontal and vertical division lines can be modified by `lv_chart_set_div_line_count(chart, hdiv_num, vdiv_num)`. The default settings are 3 horizontal and 5 vertical division lines.

### Tick marks and labels
Ticks and labels can be added to the axis.

`lv_chart_set_x_tick_text(chart, list_of_values, num_tick_marks, LV_CHART_AXIS_...)` set the ticks and texts on x axis.
`list_of_values` is a string with `'\n'` terminated text (expect the last) with text for the ticks. E.g. `const char * list_of_values = "first\nsec\nthird"`. `list_of_values` can be `NULL`.
If `list_of_values` is set then `num_tick_marks` tells the number of ticks between two labels.  If `list_of_values` is `NULL` then it specifies the total number of ticks.

*Major tick lines* are drawn where text is placed, and *minor tick lines* are drawn elsewhere. `lv_chart_set_x_tick_length(chart, major_tick_len, minor_tick_len)` sets the length of tick lines on the x-axis.

The same functions exists for the y axis too: `lv_chart_set_y_tick_text` and `lv_chart_set_y_tick_length`.

## Events
Only the [Generic events](/overview/event.html#generic-events) are sent by the object type.

Learn more about [Events](/overview/event).

## Keys
No *Keys* are processed by the object type.

Learn more about [Keys](/overview/indev).

## Example

```eval_rst

.. include:: /lv_examples/src/lv_ex_widgets/lv_ex_chart/index.rst

```

## API

```eval_rst

.. doxygenfile:: lv_chart.h
  :project: lvgl

```

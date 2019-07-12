# Chart (lv_chart)

## Overview

Charts have a rectangle-like background with horizontal and vertical division lines and data series drawn from lines, points colums or areas. 

### Data series
You can add any number of series to the charts by `lv_chart_add_series(chart, color)`. 
It allocates data for a `lv_chart_series_t` structure which contains the chosen `color` and an array for the data points. 

### Series' type
The following **data display types** exists:

- **LV_CHART_TYPE_NONE** do not display any data. It can be used to hide a series.
- **LV_CHART_TYPE_LINE** draw lines between the points
- **LV_CHART_TYPE_COL** Draw columns
- **LV_CHART_TYPE_POINT** Draw points
- **LV_CHART_TYPE_AREA** Draw areas (fill the area below the lines)
- **LV_CHART_TYPE_VERTICAL_LINE** Draw only vertical lines to connect the points. Useful if the chart width is equal to the number of points.

You can specify the display type with `lv_chart_set_type(chart, LV_CHART_TYPE_...)`. The types can be 'OR'ed (like `LV_CHART_TYPE_LINE | LV_CHART_TYPE_POINT`).

### Modify the data
You have several options to set the data of series:
1. Set the values manually in the array like `ser1->points[3] = 7` and refresh the chart with `lv_chart_refresh(chart)`.
2. Use the `lv_chart_set_next(chart, ser, value)` 
3. Initialize all points to a given value with: `lv_chart_init_points(chart, ser, value)`.
4. Set all points from an array with: `lv_chart_set_points(chart, ser, value_array)`.

Use `LV_CHART_POINT_DEF` as value to make the library to not draw that point, column, or line segment.

### Update modes
`lv_chart_set_next` can behave in two way depending on *update mode*:
- **LV_CHART_UPDATE_MODE_SHIFT** Shift old data to the left and add the new one o the right
- **LV_CHART_UPDATE_MODE_CIRCULAR** Add the new data in a circular way. (Like an ECG diagram)

To update mode can be changed with `lv_chart_set_update_mode(chart, LV_CHART_UPDATE_MODE_...)`.

### Number of points
The number of points in the series can be modified by `lv_chart_set_point_count(chart, point_num)`. The default value is 10.

### Vertical range
You can specify a the min. and max. values in y directions with `lv_chart_set_range(chart, y_min, y_max)`. The value of the points will be scaled proportionally. The default range is: 0..100.

### Division lines
The number of horizontal and vertical division lines can be modified by `lv_chart_set_div_line_count(chart, hdiv_num, vdiv_num)`. The default settings are 3 horizontal and 5 vertical division lines.

### Series' appearance
To set the **line width** and **point radius** of the series use the `lv_chart_set_series_width(chart, size)` function. The default value is: 2.

The **opacity of the data lines** can be specified by `lv_chart_set_series_opa(chart, opa)`. The default value is: OPA_COVER.

You can apply a **dark color fade** on the bottom of columns and points by `lv_chart_set_series_darking(chart, effect)` function. The default dark level is OPA_50.


### Tick marks and labels
Ticks and texts to ticks can be added.

`lv_chart_set_x_tick_text(chart, list_of_values, num_tick_marks, LV_CHART_AXIS_...)` set the ticks and texts on x axis.
`list_of_values` is a string with `'\n'` terminated text (expect the last) with text for the ticks. E.g. `const char * list_of_values = "first\nseco\nthird"`. `list_of_values` can be `NULL`.
If `list_of_values` is set then `num_tick_marks` tells the number of ticks between two labels.  If `list_of_values` is `NULL` then it specifies the total number of ticks.

Where text are added *major tick lines* are drawn, ot the other places *minor tick lines*. `lv_chart_set_x_tick_length(chart, major_tick_len, minor_tick_len)` sets the length of tick lines on the x axis.

The same functions exists for the y axis too: `lv_chart_set_y_tick_text` and `lv_chart_set_y_tick_length`

`lv_chart_set_margin(chart, 20)` needs to be used to add some extra space around the chart for the ticks and texts.

## Styles
You can set the styles with `lv_chart_set_style(btn, LV_CHART_STYLE_MAIN, &style)`.
- **style.body** properties set the background's appearance
- **style.line** properties set the division lines' appearance
- **style.text** properties set the axis labels' appearance


## Events
Only the [Generic events](/overview/event.html#generic-events) are sent by the object type.

Learn more about [Events](/overview/event).

## Keys
No *Keys* are processed by the object type.

Learn more about [Keys](/overview/indev).

## Example

```eval_rst

.. include:: /lv_examples/src/lv_ex_chart/index.rst

```

## API 

```eval_rst

.. doxygenfile:: lv_chart.h
  :project: lvgl
        
```

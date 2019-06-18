# Chart (lv_chart)

## Overview

Charts have a rectangle-like background with horizontal and vertical division lines. You can add any number of **series** to the charts by `lv_chart_add_series(chart, color)`. 
It allocates data for a `lv_chart_series_t` structure which contains the chosen `color` and an array for the data points. 

You have several options to set the data of series:

1. Set the values manually in the array like `ser1->points[3] = 7` and refresh the chart with `lv_chart_refresh(chart)`.
2. Use the `lv_chart_set_next(chart, ser, value)` 
3. Initialize all points to a given value with: `lv_chart_init_points(chart, ser, value)`.
4. Set all points from an array with: `lv_chart_set_points(chart, ser, value_array)`.

`lv_chart_set_next` can behave in two way depeding on *update mode*:
- **LV_CHART_UPDATE_MODE_SHIFT** Shift old data to the left and add the new one o the right
- **LV_CHART_UPDATE_MODE_CIRCULAR** Add the new data in a cirdclar way. (Like an ECG diagram)

To update mode can be changed with `lv_chart_set_update_mode(chart, LV_CHART_UPDATE_MODE_...)`.

The following **data display types** exists:

- **LV_CHART_TYPE_NONE** do not display any data. It can be used to hide a serie.
- **LV_CHART_TYPE_LINE** draw lines between the points
- **LV_CHART_TYPE_COL** Draw columns
- **LV_CHART_TYPE_POINT** Draw points
- **LV_CHART_TYPE_AREA** Draw areas (fill the area below the lines)
- **LV_CHART_TYPE_VERTICAL_LINE** Draw only vertical lines to connect the points. Useful if the chart width is equal to the numnber of points.

You can specify the display type with `lv_chart_set_type(chart, LV_CHART_TYPE_...)`. The types can be ORed (like `LV_CHART_TYPE_LINE | LV_CHART_TYPE_POINT`).

You can specify a the **min. and max. values in y** directions with `lv_chart_set_range(chart, y_min, y_max)`. The value of the points will be scaled proportionally. The default range is: 0..100.

The **number of points** in the data lines can be modified by `lv_chart_set_point_count(chart, point_num)`. The default value is 10.

The **number of horizontal and vertical division lines**  can be modified by `lv_chart_set_div_line_count(chart, hdiv_num, vdiv_num)`. The default settings are 3 horizontal and 5 vertical division lines.

To set the **line width** and **point radius** of the series use the `lv_chart_set_series_width(chart, size)` function. The default value is: 2.

The ***opacity of the data lines** can be specified by `lv_chart_set_series_opa(chart, opa)`. The default value is: OPA_COVER.

You can apply a **dark color fade** on the bottom of columns and points by `lv_chart_set_series_darking(chart, effect)` function. The default dark level is OPA_50.

**Ticks** and **texts to ticks** can be added with 

```c
lv_chart_set_x_ticks(chart, list_of_values, num_tick_marks, 
                     major_tick_len, minor_tick_len, 
                     LV_CHART_AXIS_DRAW_LAST_TICK);
```
`list_of_values` is an array with `num_tick_marks` `'\n'` termianted text (expect the last) with text for the ticks. E.g. `const char * list_of_values = "first\nseco\nthird"`. 
`major_tick_len` and `min_tick_len` is the length of the tick marks when the tick is on the division line or when it isn respectively. `LV_CHART_AXIS_DRAW_LAST_TICK` is the only supported mode now.

For y axis you can use `lv_chart_set_y_ticks`.

`lv_chart_set_margin(chart, 20)` needs to used to add some extra space arounf the chart for the ticks and texts.

## Styles
You can set the styles with `lv_chart_set_style(btn, LV_CHART_STYLE_MAIN, &style)`.
- **style.body** properties set the background's appearance
- **style.line** properties set the division lines' appearance
- **style.text** properties set the axis labels' appearance


## Events
Only the [Genreric events](/overview/events.html#generic-events) are sent by the object type.

Learn more about [Events](/overview/events).

## Keys
No *Keys* are processed by the object type.

Learn more about [Keys](/overview/indev).



## Example

### C


![Chart image](/examples/chart/chart_1.png)


```eval_rst
.. container:: toggle

    .. container:: header
    
      code

    .. literalinclude:: /examples/chart/chart_1.c
      :language: c
 
```

### MicroPython
No examples yet.

## API 

```eval_rst

.. doxygenfile:: lv_chart.h
  :project: lvgl
        
```

```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/fr/object-types/chart.md
```
# Graphique (lv_chart)

## Vue d’ensemble

Charts consist of the following:

* A background
* Horizontal and vertical division lines
* Data series, which can be represented with points, lines, columns, or filled areas.

### Série de données
You can add any number of series to the charts by `lv_chart_add_series(chart, color)`.
It allocates data for a `lv_chart_series_t` structure which contains the chosen `color` and an array for the data points.

### Type de série
The following **data display types** exist:

- **LV_CHART_TYPE_NONE** - Do not display any data. It can be used to hide a series.
- **LV_CHART_TYPE_LINE** - Draw lines between the points.
- **LV_CHART_TYPE_COL** - Draw columns.
- **LV_CHART_TYPE_POINT** - Draw points.
- **LV_CHART_TYPE_AREA** - Draw areas (fill the area below the lines).
- **LV_CHART_TYPE_VERTICAL_LINE** - Draw only vertical lines to connect the points. Useful if the chart width is equal to the number of points, because it can redraw much faster than the `LV_CHART_TYPE_AREA`.

Vous pouvez spécifier le type de données avec `lv_chart_set_type(chart, LV_CHART_TYPE_...)`. Les types peuvent être combinés par 'OU' (comme `LV_CHART_TYPE_LINE | LV_CHART_TYPE_POINT`).

### Modifier le données
Vous avez plusieurs possibilités pour définir les données de la série :
1. Définir les valeurs manuellement dans le tableau comme `ser1->points[3] = 7` et actualiser le graphique avec `lv_chart_refresh(chart)`.
2. Use the `lv_chart_set_next(chart, ser, value)`.
3. Initialiser tous les points avec une valeur donnée : `lv_chart_init_points(chart, ser, value)`.
4. Définir tous les points à partir d'un tableau : `lv_chart_set_points(chart, ser, value_array)`.

Use `LV_CHART_POINT_DEF` as value to make the library skip drawing that point, column, or line segment.

### Modes de mise à jour
`lv_chart_set_next` can behave in two ways depending on *update mode*:
- **LV_CHART_UPDATE_MODE_SHIFT** - Shift old data to the left and add the new one o the right.
- **LV_CHART_UPDATE_MODE_CIRCULAR** - Circularly add the new data (Like an ECG diagram).

The update mode can be changed with `lv_chart_set_update_mode(chart, LV_CHART_UPDATE_MODE_...)`.

### Nombre de points
Le nombre de points de la série peut être modifié par `lv_chart_set_point_count(chart, point_num)`. La valeur par défaut est 10.

### Plage verticale
You can specify the minimum and maximum values in y-direction with `lv_chart_set_range(chart, y_min, y_max)`. The value of the points will be scaled proportionally. The default range is: 0..100.

### Quadrillage
Le nombre de lignes horizontales et verticales du quadrillage peut être modifié par `lv_chart_set_div_line_count(chart, hdiv_num, vdiv_num)`. Les valeurs par défaut sont 3 lignes horizontales et 5 lignes verticales.

Apparence de la série
To set the **line width** and **point radius** of the series, use the `lv_chart_set_series_width(chart, size)` function. The default value is 2.

The **opacity of the data lines** can be specified by `lv_chart_set_series_opa(chart, opa)`. The default value is `LV_OPA_COVER`.

You can apply a **dark color fade** on the bottom of columns and points by `lv_chart_set_series_darking(chart, effect)` function. The default dark level is `LV_OPA_50`.


### Graduation et étiquettes
Ticks and labels beside them can be added.

**`lv_chart_set_margin(chart, 20)` needs to be used to add some extra space around the chart for the ticks and texts. Otherwise, you will not see them at all. You may need to adjust the number 20 depending on your requirements.**

`lv_chart_set_x_tick_text(chart, list_of_values, num_tick_marks, LV_CHART_AXIS_...)` définit les graduations et les textes sur l'axe des x.
`list_of_values` est une chaîne de textes pour les graduations délimités par des `'\n'` (excepté le dernier). P.ex. `const char * list_of_values = "premier\ndeuxième\ntroisième"`. `list_of_values` peut être `NULL`.
Si `list_of_values` est défini alors `num_tick_marks` indique le nombre de graduations entre deux étiquettes.  Si `list_of_values` est `NULL` alors il spécifie le nombre total de graduations.

*Major tick lines* are drawn where text is placed, and *minor tick lines* are drawn elsewhere. `lv_chart_set_x_tick_length(chart, major_tick_len, minor_tick_len)` sets the length of tick lines on the x-axis.

The same functions exists for the y axis too: `lv_chart_set_y_tick_text` and `lv_chart_set_y_tick_length`.

## Styles
Vous pouvez définir les styles avec `lv_chart_set_style(btn, LV_CHART_STYLE_MAIN, &style)`.
- **style.body** - properties set the background's appearance.
- **style.line** - properties set the division lines' appearance.
- **style.text** - properties set the axis labels' appearance.


## Evénements
Seuls les [événements génériques](/overview/event.html#generic-events) sont envoyés par ce type d'objet.

Apprenez-en plus sur les [événements](/overview/event).

## Touches
Aucune *touche* n'est traitée par ce type d'objet.

Apprenez-en plus sur les [touches](/overview/indev).

## Exemple

```eval_rst

.. include:: /lv_examples/src/lv_ex_chart/index.rst

```

## API

```eval_rst

.. doxygenfile:: lv_chart.h
  :project: lvgl

```

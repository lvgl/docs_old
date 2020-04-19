```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/fr/object-types/line.md
```
# Ligne (lv_line)

## Vue d'ensemble

L'objet ligne sert à tracer des lignes droites entre un ensemble de points.

### Ensemble de points 
Les points doivent être enregistrés dans un tableau `lv_point_t` et transmis à l'objet par la fonction `lv_line_set_points(line, point_array, point_cnt)`.

### Dimensionnement automatique
Il est possible de définir automatiquement les dimensions de l'objet ligne en fonction de ses points.
Vous pouvez l'activer avec la fonction `lv_line_set_auto_size(line, true)`.
Si activé, alors lorsque les points sont définis, la largeur et la hauteur de l'objet seront modifiées en fonction des coordonnées x et y maximales des points. Le *dimensionnement automatique* est activé par défaut.

### Y inversé
Par défaut, le point *y == 0* est en haut de l'objet, mais vous pouvez inverser les coordonnées y avec `lv_line_set_y_invert (line, true)`. Le *y inversé* est désactivé par défaut.

## Styles

La ligne utilise un style qui peut être défini par `lv_line_set_style(line, LV_LINE_STYLE_MAIN, &style)` et utilise toutes les propriétés `style.line`.

## Evénements
Seuls les [événements génériques](/overview/event.html#generic-events) sont envoyés par ce type d'objet.

Apprenez-en plus sur les [événements](/overview/event).

## Touches
Aucune *touche* n'est traitée par ce type d'objet.

Apprenez-en plus sur les [touches](/overview/indev).

## Exemple

```eval_rst

.. include:: /lv_examples/src/lv_ex_line/index.rst

```

## API 

```eval_rst

.. doxygenfile:: lv_line.h
  :project: lvgl
        
```

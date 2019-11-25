```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/fr/object-types/gauge.md
```
# Jauge (lv_gauge)

## Vue d’ensemble

La jauge est semi-circulaire, présente une échelle graduée, des étiquettes et des aiguilles.

### Scale
You can use the `lv_gauge_set_scale(gauge, angle, line_num, label_cnt)` function to adjust the scale angle and the number of the scale lines and labels.
Les paramètres par défaut sont 220 degrés, 21 graduations et 6 étiquettes.

### Aiguilles
The gauge can show more than one needle.
Utilisez la fonction `lv_gauge_set_needle_count(gauge, needle_num, color_array)`pour définir le nombre d’aiguilles et un tableau de couleurs pour chaque aiguille. Le tableau doit être une variable statique ou globale car seul son pointeur est sauvegardé.

Vous pouvez utiliser `lv_gauge_set_value(gauge, needle_id, value)` pour définir une aiguille.

### Plage
La plage de la jauge peut être spécifiée par `lv_gauge_set_range(gauge, min, max)`. La plage par défaut est 0..100.

### Valeur critique
To set a critical value, use `lv_gauge_set_critical_value(gauge, value)`. The scale color will be changed to `line.color` after this value. (default: 80)

## Styles

The gauge uses one style at a time which can be set by `lv_gauge_set_style(gauge, LV_GAUGE_STYLE_MAIN, &style)`. The gauge's properties are derived from the following style attributes:

- **body.main_color** - Line's color at the beginning of the scale.
- **body.grad_color** - Line's color at the end of the scale (gradient with main color).
- **body.padding.left** - Line length.
- **body.padding.inner** - Label distance from the scale lines.
- **body.radius** - Radius of needle origin circle.
- **line.width** - Line width.
- **line.color** - Line's color after the critical value.
- **text.font/color/letter_space** - Label attributes.

## Evénements
Seuls les [événements génériques](/overview/event.html#generic-events) sont envoyés par ce type d'objet.

Apprenez-en plus sur les [événements](/overview/event).

## Touches
Aucune *touche* n'est traitée par ce type d'objet.

Apprenez-en plus sur les [touches](/overview/indev).

## Exemple

```eval_rst

.. include:: /lv_examples/src/lv_ex_gauge/index.rst

```
## API

```eval_rst

.. doxygenfile:: lv_gauge.h
  :project: lvgl

```

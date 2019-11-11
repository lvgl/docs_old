```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/fr/object-types/arc.md
```
# Arc (lv_arc)

## Vue d'ensemble

L'objet *arc*  **trace un arc** entre les **angles de début et de fin** dans une certaine **épaisseur**.

### Angles

To set the angles, use the `lv_arc_set_angles(arc, start_angle, end_angle)` function. The zero degree is at the bottom of the object and the degrees are increasing in a counter-clockwise direction.
Les angles doivent être compris dans l'intervalle [0;360].

### Notes
Les **largeur et hauteur** de l'*arc* doivent être **identiques**.

Actuellement, l'objet *arc* **ne prend pas en charge l'anticrénelage**.

## Styles
To set the style of an *Arc* object, use `lv_arc_set_style(arc, LV_ARC_STYLE_MAIN, &style)`

- **line.rounded** - make the endpoints rounded (opacity won't work properly if set to 1)
- **line.width** - the thickness of the arc
- **line.color** - the color of the arc.

## Evénements
Seuls les [événements génériques](/overview/event.html#generic-events) sont envoyés par ce type d'objet.

Apprenez-en plus sur les [événements](/overview/event).

## Touches
Aucune *touche* n'est traitée par ce type d'objet.

Apprenez-en plus sur les [touches](/overview/indev).


## Exemple

```eval_rst

.. include:: /lv_examples/src/lv_ex_arc/index.rst

```

## API

```eval_rst

.. doxygenfile:: lv_arc.h
  :project: lvgl

```

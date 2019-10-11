```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/fr/object-types/arc.md
```
# Arc (lv_arc)

## Vue d'ensemble

L'objet *arc*  **trace un arc** entre les **angles de début et de fin** dans une certaine **épaisseur**.

### Angles

Pour définir les angles, la fonction `lv_arc_set_angles(arc, start_angle, end_angle)` est utilisée. Le degré zéro est en bas de l'objet et les degrés s'incrémentent dans la direction des aiguilles d'une montre. 
Les angles doivent être compris dans l'intervalle [0;360].

### Notes
Les **largeur et hauteur** de l'*arc* doivent être **identiques**.

Actuellement, l'objet *arc* **ne prend pas en charge l'anticrénelage**.

## Styles
Pour définir le style d'un objet *arc* la fonction `lv_arc_set_style(arc, LV_ARC_STYLE_MAIN, &style)` est utilisée

- **line.rounded** rend les extrémités arrondies (l'opacité ne fonctionnera pas correctement si elle est définie à 1)
- **line.width** l'épaisseur de l'arc
- **line.color** la couleur de l'arc.

## Evénements
Only the [Generic events](/overview/event.html#generic-events) are sent by the object type.

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

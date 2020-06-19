```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/fr/object-types/preload.md
```
# Indicateur de chargement (lv_preload)

## Vue d'ensemble
L'objet indicateur de chargement est un arc en rotation sur une bordure circulaire.

###Longueur de l'arc
La longueur de l'arc peut être ajustée par `lv_preload_set_arc_length(preload, deg)`.

### Vitesse de rotation
La vitesse de rotation peut être ajustée par `lv_preload_set_spin_time(preload, time_ms)`.

### Types de rotation
Vous pouvez choisir parmi plusieurs types de rotation :
- **LV_PRELOAD_TYPE_SPINNING_ARC** rotation de l'arc avec ralentissement au sommet du cercle
- **LV_PRELOAD_TYPE_FILLSPIN_ARC** rotation de l'arc avec ralentissement au sommet du cercle mais étire également l'arc

Pour appliquer un type, utilisez `lv_preload_set_type(preload, LV_PRELOAD_TYPE_...)`

### Direction de rotation
Le sens de rotation peut être changé avec `lv_preload_set_dir(preload, LV_PRELOAD_DIR_FORWARD/BACKWARD)`.

## Styles
Vous pouvez définir les styles avec `lv_preload_set_style(btn, LV_PRELOAD_STYLE_MAIN, &style)`. Il décrit à la fois le style de l'arc et celui de la bordure :
- **arc** est décrit par les propriétés `line`
- **border** est décrit par les propriétés `body.border` notamment `body.padding.left/top` pour donner un rayon plus petit à la bordure (le plus petit est utilisé).


## Evénements
Seuls les [événements génériques](/overview/event.html#generic-events) sont envoyés par ce type d'objet.

## Touches
Aucune *touche* n'est traitée par ce type d'objet.

Apprenez-en plus sur les [touches](/overview/indev).



## Exemple

```eval_rst

.. include:: /lv_examples/src/lv_ex_preload/index.rst

```

### MicroPython
Pas encore d'exemple.

## API 

```eval_rst

.. doxygenfile:: lv_preload.h
  :project: lvgl
        
```

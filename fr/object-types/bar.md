```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/fr/object-types/bar.md
```
# Barre (lv_bar)

## Vue d'ensemble

L'objet barre possède deux parties principales : 
1. un **fond**, l'objet lui-même 
2. un **indicateur** dont la forme est similaire à celle du fond mais dont les largeur et hauteur peuvent être ajustée. 

L'orientation de la barre peut être verticale ou horizontale selon le rapport largeur/hauteur. Logiquement, sur les barres horizontales, la largeur de l'indicateur est modifiable. Sur les barres verticales, c'est la hauteur de l'indicateur qui peut être modifiée. 

### Valeur et intervalle
Une nouvelle valeur peut être définie par `lv_bar_set_value(bar, new_value, LV_ANIM_ON/OFF)`. 
La valeur est comprise dans un intervalle (valeurs minimale et maximale) qui peut être modifié avec `lv_bar_set_range(bar, min, max)`. 
L'intervalle par défaut est 1..100.

La nouvelle valeur définie par `lv_bar_set_value` est affichée avec ou sans animation selon la valeur du dernier paramètre (`LV_ANIM_ON/OFF`). 
La durée de l'animation peut être ajustée par `lv_bar_set_anim_time(bar, 100)`. L'unité de durée est la milliseconde. 

### Symétrique
La barre peut être dessinée symétriquement par rapport à zéro (de zéro vers la gauche ou la droite, le haut ou le bas) si cela est activé par `lv_bar_set_sym(bar, true)`

## Styles

Pour définir le style d'un objet *barre* `lv_bar_set_style(arc, LV_BAR_STYLE_MAIN, &style)` est utilisée.

- **LV_BAR_STYLE_BG** est un [objet de base](/object-types/obj) de ce fait, il utilise ses éléments de style. Son style par défaut est: `lv_style_pretty`.
- **LV_BAR_STYLE_INDIC** est similaire au fond.Il utilise les marges *left*, *right*, *top* et *bottom* pour conserver un peu d'espace sur les bords du fond. Son style par défaut est `lv_style_pretty_color`.

## Evénements
Les [événements génériques](/overview/event.html#generic-events) sont les seuls à être envoyés par ce type d'objet.

Apprenez-en plus sur les [événements](/overview/event).

## Touches
Aucune *touche* n'est traitée par ce type d'objet.

Apprenez-en plus sur les [touches](/overview/indev).

## Exemple

```eval_rst

.. include:: /lv_examples/src/lv_ex_bar/index.rst

```

## API 

```eval_rst

.. doxygenfile:: lv_bar.h
  :project: lvgl
        
```

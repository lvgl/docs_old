```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/fr/object-types/slider.md
```
# Curseur (lv_slider)

## Vue d'ensemble

L'objet curseur ressemble à une [barre](/object-types/bar) complété par un bouton. Le bouton peut être déplacé pour définir une valeur. Le curseur peut également être vertical ou horizontal.

## Valeur et intervalle
Pour définir une valeur initiale, utilisez `lv_slider_set_value(slider, new_value, LV_ANIM_ON/OFF)`. 
`lv_slider_set_anim_time(slider, anim_time)` définit la durée d'animation en millisecondes.

Pour spécifier l'**intervalle** (valeurs minimum et maximum) la fonction `lv_slider_set_range(slider, min , max)` est utilisée.

### Symétrie
Le curseur peut être dessiné symétriquement par rapport à zéro (de zéro vers la gauche ou la droite) si cela est activé par `lv_slider_set_sym(slider, true)`

### Placement du bouton
Le bouton peut être placé de deux manières :
- sur l'arrière-plan
- sur les bords aux valeurs minimum/maximum

Utilisez `lv_slider_set_knob_in(slider, true/false)`choisir entre les modes (*knob_in = false* est la valeur par défaut).


## Styles
Vous pouvez modifier les styles du curseur avec `lv_slider_set_style(slider, LV_SLIDER_STYLE_..., &style)`.

- **LV_SLIDER_STYLE_BG** style de l'arrière plan. Toutes les propriétés `style.body` sont utilisées. Les valeurs `padding` rendent le bouton plus grand que l'arrière-plan (les valeurs négatives le rendent plus grand)
- **LV_SLIDER_STYLE_INDIC** style de l'indicateur. Toutes les propriétés `style.body` sont utilisées. Les valeurs `padding` rendent l'indicateur plus petit que l'arrière-plan.
- **LV_SLIDER_STYLE_KNOB** style du bouton. Toutes les propriétés `style.body` sont utilisées sauf` padding`.

## Evénements
Outre les [événements génériques](/overview/event.html #evenements-generiques), les [événements spéciaux](/overview/event.html#evenements-speciaux) suivants sont envoyés par le curseur :
- **LV_EVENT_VALUE_CHANGED** envoyé quand le curseur est déplacé ou modifié avec les touches.

## Touches
- **LV_KEY_UP**, **LV_KEY_RIGHT** incrémente la valeur du curseur de 1.
- **LV_KEY_DOWN**, **LV_KEY_LEFT** décrémente la valeur du curseur de 1.

Apprenez-en plus sur les [touches](/overview/indev).

## Exemple

```eval_rst

.. include:: /lv_examples/src/lv_ex_slider/index.rst

```


## API 

```eval_rst

.. doxygenfile:: lv_slider.h
  :project: lvgl
        
```

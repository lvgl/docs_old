```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/fr/object-types/sw.md
```
# Commutateur (lv_sw)

## Vue d'ensemble

Le commutateur peut être utilisé pour activer/désactiver quelque chose. Il ressemble à un petit curseur.

### Changer d'état
Pour changer l’état du commutateur 
- Cliquer dessus,
- Le faire glisser,
- Utiliser les fonctions `lv_sw_on(sw, LV_ANIM_ON/OFF)`, `lv_sw_off(sw, LV_ANIM_ON/OFF)` ou `lv_sw_toggle(sw, LV_ANOM_ON/OFF)`.

### Durée d'animation

La durée des animations quand le commutateur change d'état peut être ajusté avec `lv_sw_set_anim_time(sw, anim_time_ms)`.

## Styles

Vous pouvez définir les styles du commutateur avec `lv_sw_set_style(sw, LV_SW_STYLE_..., &style)`.

- **LV_SW_STYLE_BG** style de l'arrière plan. Toutes les propriétés `style.body` sont utilisées. Les valeurs `padding` rendent le commutateur plus petit que le bouton (une valeur négative le rend plus grand).
- **LV_SW_STYLE_INDIC** style de l'indicateur. Toutes les propriétés `style.body` sont utilisées. Les valeurs `padding` rendent l'indicateur plus petit que l'arrière-plan.
- **LV_SW_STYLE_KNOB_OFF** style du bouton lorsque le commutateur est désactivé. Les propriétés `style.body` sont utilisées sauf `padding`.
- **LV_SW_STYLE_KNOB_ON** Style du bouton lorsque le commutateur est activé. Les propriétés `style.body` sont utilisées sauf `padding`.




## Evénements
Outre les [événements génériques](/overview/event.html #evenements-generiques), les [événements spéciaux](/overview/event.html#evenements-speciaux) suivants sont envoyés par les commutateurs :
 - **LV_EVENT_VALUE_CHANGED** envoyé lorsque le commutateur change d'état.

## Touches
- **LV_KEY_UP**, **LV_KEY_RIGHT** active le commutateur.
- **LV_KEY_DOWN**, **LV_KEY_LEFT** désactive le commutateur.

Apprenez-en plus sur les [touches](/overview/indev).

## Exemple

```eval_rst

.. include:: /lv_examples/src/lv_ex_sw/index.rst

```


## API 

```eval_rst

.. doxygenfile:: lv_sw.h
  :project: lvgl
        
```

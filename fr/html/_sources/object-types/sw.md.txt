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

- **LV_SW_STYLE_BG** Style of the background. All `style.body` properties are used. The `padding` values make the Switch smaller than the knob. (negative value makes is larger)
- **LV_SW_STYLE_INDIC** Style of the indicator. All `style.body` properties are used. The `padding` values make the indicator smaller than the background. 
- **LV_SW_STYLE_KNOB_OFF** Style of the knob when the switch is off.  The `style.body` properties are used except padding.
- **LV_SW_STYLE_KNOB_ON** Style of the knob when the switch is on.  The `style.body` properties are used except padding.




## Events
Besides the [Generic events](/overview/event.html#generic-events) the following [Special events](/overview/event.html#special-events) are sent by the Switch:
- **LV_EVENT_VALUE_CHANGED** Sent when the switch changes state.

## Keys
- **LV_KEY_UP**, **LV_KEY_RIGHT** Turn on the slider
- **LV_KEY_DOWN**, **LV_KEY_LEFT** Turn off the slider

Learn more about [Keys](/overview/indev).

## Example

```eval_rst

.. include:: /lv_examples/src/lv_ex_sw/index.rst

```


## API 

```eval_rst

.. doxygenfile:: lv_sw.h
  :project: lvgl
        
```

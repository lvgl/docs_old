```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/fr/object-types/led.md
```
# LED (lv_led)

## Vue d’ensemble

Les LEDs sont des objets rectangulaires (ou circulaires).

### Luminosité
Vous pouvez régler leur luminosité avec `lv_led_set_bright(led, bright)`. La luminosité doit être comprise entre 0 (plus sombre) et 255 (plus clair).

### Bascule
Use `lv_led_on(led)` and `lv_led_off(led)` to set the brightness to a predefined ON or OFF value. The `lv_led_toggle(led)` toggles between the ON and OFF state.

## Styles

Les LEDs utilisent un style qui peut être défini par `lv_led_set_style(led, LV_LED_STYLE_MAIN, &style)`. 
To determine the appearance, the `style.body` properties are used. 

Les couleurs sont assombries et la largeur de l'ombre est réduite lorsque la luminosité est faible et les valeurs nominales sont utilisées à la luminosité 255 afin de simuler un effet d'éclairage.

The default style is: `lv_style_pretty_color`. Note that, the LED doesn't look like a LED with the default style so you should create your style. See the example below.

## Evénements
Seuls les [événements génériques](/overview/event.html#generic-events) sont envoyés par ce type d'objet.

Apprenez-en plus sur les [événements](/overview/event).

## Touches
Aucune *touche* n'est traitée par ce type d'objet.

Apprenez-en plus sur les [touches](/overview/indev).

## Exemple

```eval_rst

.. include:: /lv_examples/src/lv_ex_led/index.rst

```

## API 

```eval_rst

.. doxygenfile:: lv_led.h
  :project: lvgl
        
```

```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/fr/object-types/led.md
```
# LED (lv_led)

## Vue d’ensemble

Les LEDs sont des objets rectangulaires (ou circulaires).

### Luminosité
Vous pouvez régler leur luminosité avec `lv_led_set_bright(led, bright)`. La luminosité doit être comprise entre 0 (plus sombre) et 255 (plus clair).

### Bascule
Utilisez `lv_led_on(led)` et `lv_led_off(led)` pour régler la luminosité sur des valeurs prédéfinies ON ou OFF. La fonction `lv_led_toggle (led)` alterne entre les états ON et OFF.

## Styles

Les LEDs utilisent un style qui peut être défini par `lv_led_set_style(led, LV_LED_STYLE_MAIN, &style)`. 
Pour déterminer l'apparence, les propriétés de `style.body` sont utilisées.

Les couleurs sont assombries et la largeur de l'ombre est réduite lorsque la luminosité est faible et les valeurs nominales sont utilisées à la luminosité 255 afin de simuler un effet d'éclairage.

Le style par défaut est `lv_style_pretty_color`. Notez que la LED ne ressemble pas vraiment à une LED avec le style par défaut, vous devez donc créer votre propre style. Voir l'exemple ci-dessous.

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

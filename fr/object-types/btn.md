```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/fr/object-types/btn.md
```
# Bouton (lv_btn)

## Vue d'ensemble

Les boutons sont de simples objets rectangulaires dont le style et l'état changent quand ils sont pressés ou relâchés. 

### Etats
Les boutons peuvent prendre l'un des 5 états possibles :
- **LV_BTN_STATE_REL** Etat relâché
- **LV_BTN_STATE_PR** Etat  pressé
- **LV_BTN_STATE_TGL_REL** Etat basculé relâché 
- **LV_BTN_STATE_TGL_PR** Etat basculé pressé 
- **LV_BTN_STATE_INA** Etat inactif

L'état passe automatiquement de `..._REL` à `..._PR` quand le bouton est pressé et inversement quand il est relâché.

L'état peut être défini par programmation avec `lv_btn_set_state(btn, LV_BTN_STATE_TGL_REL)`.

### Bascule
Les boutons peuvent être configurés comme *bouton bascule* avec`lv_btn_set_toggle(btn, true)`. Dans ce cas, au relâchement, le bouton prend l'état *basculé relâché*.

### Mise en page et remplissage
De la même manière que les [Conteneurs](/object-types/cont), les boutons ont des attributs de disposition et de mise en page.
- `lv_btn_set_layout(btn, LV_LAYOUT_...) `définit une mise en page. La valeur par défaut est `LV_LAYOUT_CENTER`. 
Donc, si vous ajoutez une étiquette, elle sera automatiquement alignée au milieu et ne pourra pas être déplacée avec `lv_obj_set_pos ()`.
La mise en page peut être désactivée avec `lv_btn_set_layout(btn, LV_LAYOUT_OFF)`
- `lv_btn_set_fit/fit2/fit4(btn, LV_FIT_..)` enables to set the button width and/or height automatically according to the children, parent, and fit type.

### Ink effect
You can enable a special animation on buttons: when a button is pressed, the pressed state will be drawn in a growing circle starting from the point of pressing. It's like an ink droplet in the water.
When the button is released, the released state will be reverted by fading. It's like the ink is fully mixed with a lot of water and become no visible in it. 

To control this animation use the following functions:
- `lv_btn_set_ink_in_time(btn, time_ms)` time of circle growing
- `lv_btn_set_ink_wait_time(btn, time_ms)` minim time to keep the fully covering (pressed) state
- `lv_btn_set_ink_out_time(btn, time_ms)` time fade back to releases state

This feature needs to be enabled with `LV_BTN_INK_EFFECT  1` in *lv_conf.h*.


## Styles

A button can have 5 independent styles for the 5 state. You can set them via: `lv_btn_set_style(btn, LV_BTN_STYLE_..., &style)`. The styles use the `style.body` properties.

- **LV_BTN_STYLE_REL** style of the released state. Default: `lv_style_btn_rel`
- **LV_BTN_STYLE_PR** style of the pressed state. Default: `lv_style_btn_pr`
- **LV_BTN_STYLE_TGL_REL** style of the toggled released state. Default: `lv_style_btn_tgl_rel`
- **LV_BTN_STYLE_TGL_PR** style of the toggled pressed state. Default: `lv_style_btn_tgl_pr`
- **LV_BTN_STYLE_INA** style of the inactive state. Default: `lv_style_btn_ina`

When you create a label on a button, it's a good practice to set the button's `style.text` properties too. Because labels have `style = NULL` by default, they inherit the parent's (button) style. 
Hence you don't need to create a new style for the label. 


## Events
Besides the [Generic events](/overview/event.html#generic-events) the following [Special events](/overview/event.html#special-events) are sent by the buttons:
 - **LV_EVENT_VALUE_CHANGED** sent when the button is toggled.

Note that the generic input device-related events (like `LV_EVENT_PRESSED`) are sent in the inactive state too. You need to check the state with `lv_btn_get_state(btn)` to ignore the events from inactive buttons.
 
Learn more about [Events](/overview/event).

## Keys
The following *Keys* are processed by the Buttons:
- **LV_KEY_RIGHT/UP** Go to toggled state if toggling is enabled
- **LV_KEY_LEFT/DOWN** Go to non-toggled state if toggling is  enabled

Note that, as usual, the state of `LV_KEY_ENTER` is translated to `LV_EVENT_PRESSED/PRESSING/RELEASED` etc.

Learn more about [Keys](/overview/indev).
  
## Example
```eval_rst

.. include:: /lv_examples/src/lv_ex_btn/index.rst

```

## API 

```eval_rst

.. doxygenfile:: lv_btn.h
  :project: lvgl
        
```

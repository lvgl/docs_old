```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/fr/object-types/btnm.md
```
# Matrice de boutons (lv_btnm)

## Vue d’ensemble

The Button Matrix objects can display **multiple buttons** in rows and columns.

The main reasons for wanting to use a button matrix instead of a container and individual button objects are:

* The button matrix is simpler to use for grid-based button layouts.
* The button matrix consumes a lot less memory per button.

### Texte du bouton
There is a text on each button. To specify them a descriptor string array, called *map*, needs to be used.
The map can be set with `lv_btnm_set_map(btnm, my_map)`.
The declaration of a map should look like `const char * map[] = {"btn1", "btn2", "btn3", ""}`.
Notez que **le dernier élément doit être une chaîne vide** !

Use `"\n"` in the map  to make **line break**. E.g. `{"btn1", "btn2", "\n", "btn3", ""}`. Each line's buttons have their width calculated automatically.

### Contrôle des boutons
The **buttons width** can be set relative to the other button in the same line with `lv_btnm_set_btn_width(btnm, btn_id, width)`
E.g. in a line with two buttons: *btnA, width = 1* and *btnB, width = 2*, *btnA* will have 33 % width and *btnB* will have 66 % width. It's similar to how the [`flex-grow`](https://developer.mozilla.org/en-US/docs/Web/CSS/flex-grow) property works in CSS.

In addition to width, each button can be customized with the following parameters:
- **LV_BTNM_CTRL_HIDDEN** - make a button hidden (hidden buttons still take up space in the layout, they are just not visible or clickable)
- **LV_BTNM_CTRL_NO_REPEAT** - disable repeating when the button is long pressed
- **LV_BTNM_CTRL_INACTIVE** - make a button inactive
- **LV_BTNM_CTRL_TGL_ENABLE** - enable toggling of a button
- **LV_BTNM_CTRL_TGL_STATE** - set the toggle state
- **LV_BTNM_CTRL_CLICK_TRIG** - if 0, the button will react on press, if 1, will react on release

The set or clear a button's control attribute, use `lv_btnm_set_btn_ctrl(btnm, btn_id, LV_BTNM_CTRL_...)` and `lv_btnm_clear_btn_ctrl(btnm, btn_id, LV_BTNM_CTRL_...)` respectively. More `LV_BTNM_CTRL_...` values can be *Or*ed

The set/clear the same control attribute for all buttons of a button matrix, use `lv_btnm_set_btn_ctrl_all(btnm, btn_id, LV_BTNM_CTRL_...)` and `lv_btnm_clear_btn_ctrl_all(btnm, btn_id, LV_BTNM_CTRL_...)`.

The set a control map for a button matrix (similarly to the map for the text), use `lv_btnm_set_ctrl_map(btnm, ctrl_map)`.
Un élément de `ctrl_map` devrait ressembler à `ctrl_map[0] = width | LV_BTNM_CTRL_NO_REPEAT | LV_BTNM_CTRL_TGL_ENABLE`. Le nombre d'éléments doit être égal au nombre de boutons (en excluant les caractères de saut de ligne).

### Une bascule
The "One toggle" feature can be enabled with `lv_btnm_set_one_toggle(btnm, true)` to allow only one button to be toggled at once.

### Recolorer
The **texts** on the button can be **recolored** similarly to the recolor feature for [Label](/object-types/label) object. To enable it, use `lv_btnm_set_recolor(btnm, true)`. After that a button with `#FF0000 Red#` text will be red.

### Notes
L'objet Matrice de boutons est très léger, car les boutons ne sont pas créés mais simplement dessinés à la volée.
This way, 1 button use only 8 extra bytes instead of the ~100-150 byte size of a normal [Button](/object-types/btn) object (plus the size of its container and a label for each button).

The disadvantage of this setup is that the ability to style individual buttons to be different from others is limited (aside from the toggling feature). If you require that ability, using individual buttons is very likely to be a better approach.

## Styles

The Button matrix works with 6 styles: a background and 5 button styles for each state. You can set the styles with `lv_btnm_set_style(btn, LV_BTNM_STYLE_..., &style)`.
L'arrière-plan et les boutons utilisent les propriétés `style.body`. Les étiquettes utilisent les propriétés `style.text` des styles de bouton.

- **LV_BTNM_STYLE_BG** - Background style. Uses all _style.body_ properties including _padding_ Default: _lv_style_pretty_
- **LV_BTNM_STYLE_BTN_REL** - style of the released  buttons. Default: _lv_style_btn_rel_
- **LV_BTNM_STYLE_BTN_PR** - style of the pressed buttons. Default: _lv_style_btn_pr_
- **LV_BTNM_STYLE_BTN_TGL_REL** - style of the toggled released  buttons. Default: _lv_style_btn_tgl_rel_
- **LV_BTNM_STYLE_BTN_TGL_PR** - style of the toggled pressed  buttons. Default: _lv_style_btn_tgl_pr_
- **LV_BTNM_STYLE_BTN_INA** - style of the inactive  buttons. Default: _lv_style_btn_ina_

## Evénements
Besides the [Generic events](/overview/events.html#generic-event), the following [Special events](/overview/event.html#special-events) are sent by the button matrices:
 - **LV_EVENT_VALUE_CHANGED** - sent when the button is pressed/released or repeated after long press. The event data is set to the ID of the pressed/released button.

Apprenez-en plus sur les [événements](/overview/event).

## Keys

Les *touches* suivantes sont traitées par les boutons :
- **LV_KEY_RIGHT/UP/LEFT/RIGHT** - To navigate among the buttons to select one
- **LV_KEY_ENTER** - To press/release the selected button

Apprenez-en plus sur les [touches](/overview/indev).

## Exemple

```eval_rst

.. include:: /lv_examples/src/lv_ex_btnm/index.rst

```

## API

```eval_rst

.. doxygenfile:: lv_btnm.h
  :project: lvgl

```

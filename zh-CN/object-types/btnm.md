# Button matrix (lv_btnm)

## Overview

The Button Matrix objects can display **multiple buttons** in rows and columns. 

### Button's text
There is a text on each button. To specify them a descriptor string array, called *map*, needs to be used. 
The map can be set with `lv_btnm_set_map(btnm, my_map)`. 
The declaration of a map should look like `const char * map[] = {"btn1", "btn2", "btn3", ""}`. 
Note that **the last element has to be an empty string**!  

Use `"\n"` in the map  to make **line break**. E.g. `{"btn1", "btn2", "\n", "btn3", ""}`. The button's width is recalculated in every line to will the whole line.

### Control buttons
The **buttons width** can be set relative to the other button in the same line with `lv_btnm_set_btn_width(btnm, btn_id, width)` 
E.g. in a line with two buttons: *btnA, width = 1* and *btnB, width = 2*, *btnA* will have 33 % width adnd *btnB* will have 66 % width.

In addition to width each button can be customized with the following parameters:
- **LV_BTNM_CTRL_HIDDEN** make a button hidden
- **LV_BTNM_CTRL_NO_REPEAT** disable repeating when the button is long pressed 
- **LV_BTNM_CTRL_INACTIVE** make a button inactive
- **LV_BTNM_CTRL_TGL_ENABLE** enable toggling of a button
- **LV_BTNM_CTRL_TGL_STATE** set the toggle state
- **LV_BTNM_CTRL_CLICK_TRIG** if 0 the button will react on press, if 1 will react on release

The set or clear a button's control attribute use `lv_btnm_set_btn_ctrl(btnm, btn_id, LV_BTNM_CTRL_...)` and `lv_btnm_clear_btn_ctrl(btnm, btn_id, LV_BTNM_CTRL_...)` respectively. More `LV_BTNM_CTRL_...` values can be *Or*ed

The set/clear the same control attribute for all buttons of a button matrix use `lv_btnm_set_btn_ctrl_all(btnm, btn_id, LV_BTNM_CTRL_...)` and `lv_btnm_clear_btn_ctrl_all(btnm, btn_id, LV_BTNM_CTRL_...)`.

The set a control map for a button matrix (similarly to the map for the text) use `lv_btnm_set_ctrl_map(btnm, ctrl_map)`. 
An element of `ctrl_map` should look like `ctrl_map[0] = width | LV_BTNM_CTRL_NO_REPEAT |  LV_BTNM_CTRL_TGL_ENABLE`. The number of elements should be equal to the number of buttons (excluding newlines characters).

### One toggle
The "One toggle" feature can be enabled with `lv_btnm_set_one_toggle(btnm, true)` to allow only one toggled button at once.

### Recolor
The **texts** on the button can be **recolored** similarly to the recolor feature for [Label](/object-types/label) object. To enabel it use `lv_btnm_set_recolor(btnm, true)`. After that a button with `#FF0000 Red#` text will be red.

### Notes
The Button matrix object is very light weighted because the buttons are not created just virtually drawn on the fly.
This way 1 button use only 8 extra bytes instead of the ~100-150 byte size of a normal [Button](/object-types/btn) object. 

## Styles

The Button matrix works with 6 styles: a background and 5 button styles for each state. You can set the styles with `lv_btnm_set_style(btn, LV_BTNM_STYLE_..., &style)`. 
The background and the buttons use the `style.body` properties. The labels use the `style.text` properties of the button styles.

- **LV_BTNM_STYLE_BG** Background style. Uses all _style.body_ properties including _padding_ Default: _lv_style_pretty_
- **LV_BTNM_STYLE_BTN_REL** style of the released  buttons. Default: _lv_style_btn_rel_
- **LV_BTNM_STYLE_BTN_PR** style of the pressed buttons. Default: _lv_style_btn_pr_
- **LV_BTNM_STYLE_BTN_TGL_REL** style of the toggled released  buttons. Default: _lv_style_btn_tgl_rel_
- **LV_BTNM_STYLE_BTN_TGL_PR** style of the toggled pressed  buttons. Default: _lv_style_btn_tgl_pr_
- **LV_BTNM_STYLE_BTN_INA** style of the inactive  buttons. Default: _lv_style_btn_ina_

## Events
Besides the [Genreric events](/overview/events.html#generic-event) the following [Special events](/overview/event.html#special-events) are sent by the button matrices:
 - **LV_EVENT_VALUE_CHANGED** sent when the button is pressed/released or repeated after long press. The event data is set to ID of the pressed/released button.

Learn more about [Events](/overview/event).

##Keys

The following *Keys* are processed by the Buttons:
- **LV_KEY_RIGHT/UP/LEFT/RIGHT** To navigate among the buttons to select one
- **LV_KEY_ENTER** To press/release the selected button 

Learn more about [Keys](/overview/indev).

## Example

```eval_rst

.. include:: /lv_examples/src/lv_ex_btnm/index.rst

```

## API 

```eval_rst

.. doxygenfile:: lv_btnm.h
  :project: lvgl
        
```

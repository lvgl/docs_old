_Written for v5.1_

## Overview

As it names shows the **Keyboard** object provides a keyboard to **write text**. You can assign a [Text area](/Text-area_tr) to the Keyboard to put the clicked characters there. To assign the Text area use `lv_kb_set_ta(kb, ta)`.

The keyboard contains an _Ok_ and a _Hide_ button. An ok and a hide action can be specified by `lv_kb_set_ok_action(kb, action)` and `lv_kb_set_hide_action(kb, action)` to add callbacks to Ok/Hide clicks. If no action is specified then the buttons will delete the Keyboard. 

The assigned Text area's **cursor** can be **managed** by the keyboard: when the keyboard is assigned the previous Text area's cursor will be hidden an the new's will be shown. Clicking on _Ok_ or _Hide_  will also hide the cursor. The cursor manager feature is enabled by `lv_kb_set_cursor_manage(kb, true)`. The default is not manage.

The Keyboards have two **modes**:

- LV_KB_MODE_TEXT: display letters, number and special characters
- LV_KB_MODE_NUM: display numbers, +/- sign and dot

To set the mode use `lv_kb_set_mode(kb, mode)`. The default is  _LV_KB_MODE_TEXT_

You can specify a **new map** (layout) for the keyboard with `lv_kb_set_map(kb, map)`. It works like a the [Button matrix](/Button-matrix_tr) so control character can be added to the layout the set button width and other attributes. Keep in mind using following keywords will have the same effect as with the original map:  _SYMBOL_OK_, _SYMBOL_CLOSE_, _SYMBOL_LEFT_, _SYMBOL_RIGHT_, _ABC_, _abc_, _Enter_, _Del_, _#1_, _+/-_ .

## Style usage

The Keyboard works with 6 styles: a background and 5 button styles for each states. You can set the styles with `lv_kb_set_style(btn, LV_KB_STYLE_..., &style)`. The background and the buttons use the _style.body_ properties. The labels use the _style.text_ properties of the button styles.

- **LV_KB_STYLE_BG** Background style. Uses all _style.body_ properties including _padding_ Default: _lv_style_pretty_
- **LV_KB_STYLE_BTN_REL** style of the released  buttons. Default: _lv_style_btn_rel_
- **LV_KB_STYLE_BTN_PR** style of the pressed buttons. Default: _lv_style_btn_pr_
- **LV_KB_STYLE_BTN_TGL_REL** style of the toggled released  buttons. Default: _lv_style_btn_tgl_rel_
- **LV_KB_STYLE_BTN_TGL_PR** style of the toggled pressed  buttons. Default: _lv_style_btn_tgl_pr_
- **LV_KB_STYLE_BTN_INA** style of the inactive  buttons. Default: _lv_style_btn_ina_

## Example
![Keyboard image](http://docs.littlevgl.com/img/keyboard-lv_kb.png)
```c
/*Create styles for the keyboard*/
static lv_style_t rel_style, pr_style;

lv_style_copy(&rel_style, &lv_style_btn_rel);
rel_style.body.radius = 0;

lv_style_copy(&pr_style, &lv_style_btn_pr);
pr_style.body.radius = 0;

/*Create a keyboard and apply the styles*/
lv_obj_t *kb = lv_kb_create(lv_scr_act(), NULL);
lv_kb_set_cursor_manage(kb, true);
lv_kb_set_style(kb, LV_KB_STYLE_BG, &lv_style_transp_tight);
lv_kb_set_style(kb, LV_KB_STYLE_BTN_REL, &rel_style);
lv_kb_set_style(kb, LV_KB_STYLE_BTN_PR, &pr_style);

/*Create a text area. The keyboard will write here*/
lv_obj_t *ta = lv_ta_create(lv_scr_act(), NULL);
lv_obj_align(ta, NULL, LV_ALIGN_IN_TOP_MID, 0, 10);
lv_ta_set_text(ta, "");

/*Assign the text area to the keyboard*/
lv_kb_set_ta(kb, ta);
```

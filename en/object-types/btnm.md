# Button matrix (lv_btnm)

## Overview

The Button Matrix objects can display **multiple buttons** in rows and culomns. 

The Button matrix object is very light weighted becasue the buttons are not really created just drawn on the fly.
This way 1 button uses only 8 extra byte instead of the ~100-150 byte size of a normal [Button](/object-types/btn) object. 

The buttons have texts on them which can be specified a descriptor string array, called *map*. The map can be set with `lv_btnm_set_map(btnm, my_map)`. 

The **declaration of a map** looks like `const char * map[] = {"btn1", "btn2", "btn3", ""}`. Note that **the last element has to be an empty string**!  

Use `"\n"` in the map  to make **line break**. E.g. `{"btn1", "btn2", "\n", "btn3", ""}`. The button's width is recalculated in every line.

The buttons width can be set relative to the other button in the same line with `lv_btnm_set_btn_width(btnm, btn_id, width)` 
E.g. in a line with two buttons: *btn 1 width = 1* and *btn 2 width = 2*, *btn 1* will have 33 % width adnd *btn 2* will have 66 % width.

In addition to width each button can be customized with following paramters:
- **LV_BTNM_CTRL_HIDDEN** make a button hidden
- **LV_BTNM_CTRL_NO_REPEAT** disable repating when the button is long pressed 
- **LV_BTNM_CTRL_INACTIVE** make a button inactive
- **LV_BTNM_CTRL_TGL_ENABLE** enable toggling of a button
- **LV_BTNM_CTRL_TGL_STATE** set the toggle state
- **LV_BTNM_CTRL_CLICK_TRIG** if 0 the button will react on press, if 1 will ract on release

The set or clear a button's control attribute use `lv_btnm_set_btn_ctrl(btnm, btn_id, LV_BTNM_CTRL_...)` and `lv_btnm_clear_btn_ctrl(btnm, btn_id, LV_BTNM_CTRL_...)` respectively. More `LV_BTNM_CTRL_...` values can be *Or*ed

The set/clear the same control attribute for all buttons of a button matrix use `lv_btnm_set_btn_ctrl_all(btnm, btn_id, LV_BTNM_CTRL_...)` and `lv_btnm_clear_btn_ctrl_all(btnm, btn_id, LV_BTNM_CTRL_...)`.

The *"One toggle"* feature can be enable with `lv_btnm_set_one_toggle(btnm, true)` to allow only one toggled button at once.

The set a control map for a butto nmatrix (similarly to the map for the text) use `lv_btnm_set_ctrl_map(btnm, ctrl_map)`. 
An element of `ctrl_map` should look like `ctrl_map[0] = width | LV_BTNM_CTRL_NO_REPEAT |  LV_BTNM_CTRL_TGL_ENABLE`. The number of elemnts should be equal to the number of buttons (excluiding new lines).

The **texts** on the button can be **recolored** similarly to the recolor feature for [Label](/object-types/label) object. To enabel it use `lv_btnm_set_recolor(btnm, true)`. After that a button with `#FF0000 Red#` text will be red.


## Styles

The Button matrix works with 6 styles: a background and 5 button styles for each states. You can set the styles with `lv_btnm_set_style(btn, LV_BTNM_STYLE_..., &style)`. 
The background and the buttons use the `style.body` properties. The labels use the `style.text` properties of the button styles.

- **LV_BTNM_STYLE_BG** Background style. Uses all _style.body_ properties including _padding_ Default: _lv_style_pretty_
- **LV_BTNM_STYLE_BTN_REL** style of the released  buttons. Default: _lv_style_btn_rel_
- **LV_BTNM_STYLE_BTN_PR** style of the pressed buttons. Default: _lv_style_btn_pr_
- **LV_BTNM_STYLE_BTN_TGL_REL** style of the toggled released  buttons. Default: _lv_style_btn_tgl_rel_
- **LV_BTNM_STYLE_BTN_TGL_PR** style of the toggled pressed  buttons. Default: _lv_style_btn_tgl_pr_
- **LV_BTNM_STYLE_BTN_INA** style of the inactive  buttons. Default: _lv_style_btn_ina_


## Events
Besided the [Genreric events](/overview/events.html#generic-events) the following [Special events](/overview/events.html#special-events) are sent by the button matrices:
 - **LV_EVENT_VALUE_CHANGED** sent when the button is pressed/released or repeated after long press. The event data is set to ID of the pressed/released button.

Learn more about [Events](/overview/events).

##Keys

The following *Keys* are processed by the Buttons:
- **LV_KEY_RIGHT/UP/LEFT/RIGHT** To navigate among the buttons and elect one
- **LV_KEY_ENTER** To press/release the selected button 

Learn more about [Keys](/overview/indev).

## Example
![Button matrix image](http://docs.littlevgl.com/img/button-matrix-lv_btnm.png)
```c
/*Called when a button is released ot long pressed*/
static lv_res_t btnm_action(lv_obj_t * btnm, const char *txt)
{
    printf("Button: %s released\n", txt);

    return LV_RES_OK; /*Return OK because the button matrix is not deleted*/
}


.
.
.

/*Create a button descriptor string array*/
static const char * btnm_map[] = {"1", "2", "3", "4", "5", "\n",
                           "6", "7", "8", "9", "0", "\n",
                           "\202Action1", "Action2", ""};




/*Create a default button matrix*/
lv_obj_t * btnm1 = lv_btnm_create(lv_scr_act(), NULL);
lv_btnm_set_map(btnm1, btnm_map);
lv_btnm_set_action(btnm1, btnm_action);
lv_obj_set_size(btnm1, LV_HOR_RES, LV_VER_RES / 2);

/*Create a new style for the button matrix back ground*/
static lv_style_t style_bg;
lv_style_copy(&style_bg, &lv_style_plain);
style_bg.body.main_color = LV_COLOR_SILVER;
style_bg.body.grad_color = LV_COLOR_SILVER;
style_bg.body.padding.hor = 0;
style_bg.body.padding.ver = 0;
style_bg.body.padding.inner = 0;

/*Create 2 button styles*/
static lv_style_t style_btn_rel;
static lv_style_t style_btn_pr;
lv_style_copy(&style_btn_rel, &lv_style_btn_rel);
style_btn_rel.body.main_color = LV_COLOR_MAKE(0x30, 0x30, 0x30);
style_btn_rel.body.grad_color = LV_COLOR_BLACK;
style_btn_rel.body.border.color = LV_COLOR_SILVER;
style_btn_rel.body.border.width = 1;
style_btn_rel.body.border.opa = LV_OPA_50;
style_btn_rel.body.radius = 0;

lv_style_copy(&style_btn_pr, &style_btn_rel);
style_btn_pr.body.main_color = LV_COLOR_MAKE(0x55, 0x96, 0xd8);
style_btn_pr.body.grad_color = LV_COLOR_MAKE(0x37, 0x62, 0x90);
style_btn_pr.text.color = LV_COLOR_MAKE(0xbb, 0xd5, 0xf1);

/*Create a second button matrix with the new styles*/
lv_obj_t * btnm2 = lv_btnm_create(lv_scr_act(), btnm1);
lv_btnm_set_style(btnm2, LV_BTNM_STYLE_BG, &style_bg);
lv_btnm_set_style(btnm2, LV_BTNM_STYLE_BTN_REL, &style_btn_rel);
lv_btnm_set_style(btnm2, LV_BTNM_STYLE_BTN_PR, &style_btn_pr);
lv_obj_align(btnm2, btnm1, LV_ALIGN_OUT_BOTTOM_MID, 0, 0);
```

_Written for v5.1_

## Overview

The Button Matrix objects can display **multiple buttons** according to a descriptor string array, called _map_. You can specify the map with `lv_btnm_set_map(btnm, my_map)`. 

The **declaration of a map** looks like `const char * map[] = {"btn1", "btn2", "btn3", ""}`. Note that **the last element has to be an empty string**!  

The first character of a string can be a **control character** to specify some attributes:

- **bit 7..6** Always _0b10_ to differentiate the control byte from the textual characters
- **bit 5** Inactive button
- **bit 4** Hidden button
- **bit 3** No long press for the button
- **bit 2..0** Relative width compared to the buttons in the same row. [1..7]

It is recommended to specify the **control byte as an octal number**. For example `"\213button"`. The octal number always starts with _2_ (bit 7..6) the middle part is the attributes (bit 5..3) and the last part is the width (bit 2..0). So the example describes a 3 unit wide, hidden button.

Use "\n" in the map  to make **line break**: `{"btn1", "btn2", "\n", "btn3", ""}`. The button's width is recalculated in every line.

The `lv_btnm_set_action(btnm, btnm_action)` specifies an action to call when a button is released. 

You can enable the **buttons to toggle** when they are clicked. There can only be one toggled button at a time. The `lv_btnm_set_toggle(btnm, true, id)` enables the toggling and sets the _id_th button to the toggled state.

## Style usage

The Button matrix works with 6 styles: a background and 5 button styles for each states. You can set the styles with `lv_btnm_set_style(btn, LV_BTNM_STYLE_..., &style)`. The background and the buttons use the _style.body_ properties. The labels use the _style.text_ properties of the button styles.

- **LV_BTNM_STYLE_BG** Background style. Uses all _style.body_ properties including _padding_ Default: _lv_style_pretty_
- **LV_BTNM_STYLE_BTN_REL** style of the released  buttons. Default: _lv_style_btn_rel_
- **LV_BTNM_STYLE_BTN_PR** style of the pressed buttons. Default: _lv_style_btn_pr_
- **LV_BTNM_STYLE_BTN_TGL_REL** style of the toggled released  buttons. Default: _lv_style_btn_tgl_rel_
- **LV_BTNM_STYLE_BTN_TGL_PR** style of the toggled pressed  buttons. Default: _lv_style_btn_tgl_pr_
- **LV_BTNM_STYLE_BTN_INA** style of the inactive  buttons. Default: _lv_style_btn_ina_

## Notes

- The Button matrix object is **very light weighted**. It creates only the Background Base object and draws the buttons on it instead of creating a lot of real button.

## Example
![Button matrix image](https://raw.githubusercontent.com/wiki/littlevgl/lvgl/img/button-matrix-lv_btnm.png)
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
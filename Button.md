_Written for v5.1, revision 2_

## Overview

Buttons can react on user **press**, **release** or **long press** via callback functions (`lv_action_t` function pointers). You can set the callback functions with: `lv_btn_set_action(btn, ACTION_TYPE, callback_func)`. The possible action types are:

- LV_BTN_ACTION_CLICK: the button is released after pressing (clicked) or, when using keypad, after the key `LV_GROUP_KEY_ENTER` is released
- LV_BTN_ACTION_PR: the button is pressed
- LV_BTN_ACTION_LONG_PR: the button is long pressed
- LV_BTN_ACTION_LONG_PR_REPEAT: the button is long pressed and this action is triggered periodically

Buttons can be in one of the **five possible states**:

- LV_BTN_STATE_REL Released state
- LV_BTN_STATE_PR Pressed state
- LV_BTN_STATE_TGL_REL Toggled released state (On state)
- LV_BTN_STATE_TGL_PR Toggled pressed state (On pressed state)
- LV_BTN_STATE_INA Inactive state

The buttons can be configured as **toggle button** with `lv_btn_set_toggle(btn, true)`. In this case on release, the button goes to toggled released state.

You can set the button's state manually by: `lv_btn_set_state(btn, LV_BTN_STATE_TGL_REL)`.

A button can go to **Inactive state** only manually (by _lv_btn_set_state()_). In an Inactive state, none of the action will be called.  

Similarly to [Containers](/Container) buttons also have **layout** and **auto fit**:

- `lv_btn_set_layout(btn, LV_LAYOUT_...) `set a layout. The default is LV_LAYOUT_CENTER. So if you add a label then it will be automatically aligned to the middle.
- `lv_btn_set_fit(btn, hor_en, ver_en)` enables to set the button width and/or height automatically according to the children.

## Style usage

A button can have 5 independent styles for the 5 state. You can set them via: `lv_btn_set_style(btn, LV_BTN_STYLE_..., &style)`. The styles use the _style.body_ properties.

- **LV_BTN_STYLE_REL** style of the released state. Default: _lv_style_btn_rel_
- **LV_BTN_STYLE_PR** style of the pressed state. Default: _lv_style_btn_pr_
- **LV_BTN_STYLE_TGL_REL** style of the toggled released state. Default: _lv_style_btn_tgl_rel_
- **LV_BTN_STYLE_TGL_PR** style of the toggled pressed state. Default: _lv_style_btn_tgl_pr_
- **LV_BTN_STYLE_INA** style of the inactive state. Default: _lv_style_btn_ina_

## Notes

- If a button is dragged its click and long press action will not be called
- If a button was long pressed and its long press action was set then its click action will not be called

## Example
![Button image](http://doc.littlevgl.com/img/button-lv_btn.png)
```c
static lv_res_t btn_click_action(lv_obj_t * btn)
{
    uint8_t id = lv_obj_get_free_num(btn);

    printf("Button %d is released\n", id);

    /* The button is released.
     * Make something here */

    return LV_RES_OK; /*Return OK if the button is not deleted*/
}

.
.
.

/*Create a title label*/
lv_obj_t * label = lv_label_create(lv_scr_act(), NULL);
lv_label_set_text(label, "Default buttons");
lv_obj_align(label, NULL, LV_ALIGN_IN_TOP_MID, 0, 5);

/*Create a normal button*/
lv_obj_t * btn1 = lv_btn_create(lv_scr_act(), NULL);
lv_cont_set_fit(btn1, true, true); /*Enable resizing horizontally and vertically*/
lv_obj_align(btn1, label, LV_ALIGN_OUT_BOTTOM_MID, 0, 10);
lv_obj_set_free_num(btn1, 1);   /*Set a unique number for the button*/
lv_btn_set_action(btn1, LV_BTN_ACTION_CLICK, btn_click_action);

/*Add a label to the button*/
label = lv_label_create(btn1, NULL);
lv_label_set_text(label, "Normal");

/*Copy the button and set toggled state. (The release action is copied too)*/
lv_obj_t * btn2 = lv_btn_create(lv_scr_act(), btn1);
lv_obj_align(btn2, btn1, LV_ALIGN_OUT_BOTTOM_MID, 0, 10);
lv_btn_set_state(btn2, LV_BTN_STATE_TGL_REL);  /*Set toggled state*/
lv_obj_set_free_num(btn2, 2);               /*Set a unique number for the button*/

/*Add a label to the toggled button*/
label = lv_label_create(btn2, NULL);
lv_label_set_text(label, "Toggled");

/*Copy the button and set inactive state.*/
lv_obj_t * btn3 = lv_btn_create(lv_scr_act(), btn1);
lv_obj_align(btn3, btn2, LV_ALIGN_OUT_BOTTOM_MID, 0, 10);
lv_btn_set_state(btn3, LV_BTN_STATE_INA);   /*Set inactive state*/
lv_obj_set_free_num(btn3, 3);               /*Set a unique number for the button*/

/*Add a label to the inactive button*/
label = lv_label_create(btn3, NULL);
lv_label_set_text(label, "Inactive");
```

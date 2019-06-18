# Button (lv_btn)

## Overview

Buttons are simple rectagnle-like objects but they change their style and state when they are pressed or released. 

Buttons can be in one of the **five possible states**:
- **LV_BTN_STATE_REL** Released state
- **LV_BTN_STATE_PR** Pressed state
- **LV_BTN_STATE_TGL_REL** Toggled released state 
- **LV_BTN_STATE_TGL_PR** Toggled pressed state 
- **LV_BTN_STATE_INA** Inactive state

The buttons can be configured as **toggle button** with `lv_btn_set_toggle(btn, true)`. In this case on release, the button goes to toggled released state.

You can set the button's state manually with `lv_btn_set_state(btn, LV_BTN_STATE_TGL_REL)`.

Similarly to [Containers](/object-types/cont) buttons also have **layout** and **fit** attributes.
- `lv_btn_set_layout(btn, LV_LAYOUT_...) `set a layout. The default is `LV_LAYOUT_CENTER`. 
So if you add a label then it will be automatically aligned to the middle and can't be moved with `lv_obj_set_pos()`. 
You can disable the layout with `lv_btn_set_layout(btn, LV_LAYOUT_OFF)`
- `lv_btn_set_fit/fit2/fit4(btn, LV_FIT_..)` enables to set the button width and/or height automatically according to the children, parent and fit type.

## Styles

A button can have 5 independent styles for the 5 state. You can set them via: `lv_btn_set_style(btn, LV_BTN_STYLE_..., &style)`. The styles use the `style.body` properties.

- **LV_BTN_STYLE_REL** style of the released state. Default: `lv_style_btn_rel`
- **LV_BTN_STYLE_PR** style of the pressed state. Default: `lv_style_btn_pr`
- **LV_BTN_STYLE_TGL_REL** style of the toggled released state. Default: `lv_style_btn_tgl_rel`
- **LV_BTN_STYLE_TGL_PR** style of the toggled pressed state. Default: `lv_style_btn_tgl_pr`
- **LV_BTN_STYLE_INA** style of the inactive state. Default: `lv_style_btn_ina`

When labels are created on a button, it's a good practive to set the button's `style.text` properties too. Because labels have `style = NULL` by default they inherit the parent's (button) style. 
Hence you don't need to craete a new style for the label. 


## Events
Besided the [Genreric events](/overview/events.html#generic-events) the following [Special events](/overview/events.html#special-events) are sent by the buttons:
 - **LV_EVENT_VALUE_CHANGED** sent when the button is toggled.

Note that the generic input device related events (like `LV_EVENT_PRESSED`) are sent in inactive state too. You need to check the state with `lv_btn_get_state(btn)` to ignore the events from inactive buttons.
 
Learn more about [Events](/overview/events).

## Keys
The following *Keys* are processed by the Buttons:
- **LV_KEY_RIGHT/UP** Go to toggled state if toggling is enabled
- **LV_KEY_LEFT/DOWN** Go to non-toggled state if toggling is  enabled

Note that, as usual, the state of `LV_KEY_ENTER` is translated to `LV_EVENT_PRESSED/PRESSING/RELEASED` etc.

Learn more about [Keys](/overview/indev).
  
## Example
![Button image](http://docs.littlevgl.com/img/button-lv_btn.png)
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

_Written for v5.1_

## Overview

The message boxes act as **pop-ups**. They are built from a **background**, a **text** and **buttons**. The background is a [Container](/Container) object with enabled vertical fit to ensure that the text and the buttons are always visible.  

To **set the text** use the `lv_mbox_set_text(mbox, "My text")` function.

The buttons are a Button matrix. To **add buttons** use the `lv_mbox_add_btns(mbox, btn_str, action)` function. In this you can specify the button text e.g (`const char * btn_str[] = {"btn1", "btn2", ""}`) and add a callback which is called when a button is released. For more information visit the [Button matrix](https://github.com/littlevgl/lvgl/wiki/Button-matrix)'s documentation.

With `lv_mbox_start_auto_close(mbox, delay)` the message box can be **closed automatically** after _delay_ milliseconds with a long animation. The `lv_mbox_stop_auto_close(mbox)` function will stop a started auto close .

The close animation time can be adjusted by `lv_mbox_set_anim_time(mbox, anim_time)`.

## Style usage

Use `lv_mbox_set_style(mbox, LV_MBOX_STYLE_...,  &style)` to set a new style for an element of the message box:

- **LV_MBOX_STYLE_BG** specifies the background container's style. _style.body_ for background and _style.label_ for the text appearance. Default: lv_style_pretty
- **LV_MBOX_STYLE_BTN_BG** style of the buttons (button matrix) background. Default: lv_style_transp
- **LV_MBOX_STYLE_BTN_REL** style of the released buttons. Default: lv_style_btn_rel
- **LV_MBOX_STYLE_BTN_PR** style of the pressed buttons. Default: lv_style_btn_pr
- **LV_MBOX_STYLE_BTN_TGL_REL** style of the toggled released buttons. Default: lv_style_btn_tgl_rel
- **LV_MBOX_STYLE_BTN_TGL_PR** style of the toggled pressed buttons. Default: lv_style_btn_tgl_pr
- **LV_MBOX_STYLE_BTN_INA** style of the inactive buttons. Default: lv_style_btn_ina

## Notes

- The **height of the buttons** comes from the _font height_ + 2 × _body.vpad_ of _LV_MBOX_STYLE_BTN_REL_

## Example

![Message box image](http://docs.littlevgl.com/img/message-box-lv_mbox.png)
```c
/*Called when a button is clicked*/
static lv_res_t mbox_apply_action(lv_obj_t * mbox, const char * txt)
{
    printf("Mbox button: %s\n", txt);

    return LV_RES_OK; /*Return OK if the message box is not deleted*/
}

.
.
.
.

/*******************************
 * Create a default message box
 *******************************/

lv_obj_t * mbox1 = lv_mbox_create(lv_scr_act(), NULL);
lv_mbox_set_text(mbox1, "Default message box\n"
                        "with buttons");                    /*Set the text*/
/*Add two buttons*/
static const char * btns[] ={"\221Apply", "\221Close", ""}; /*Button description. '\221' lv_btnm like control char*/
lv_mbox_add_btns(mbox1, btns, NULL);
lv_obj_set_width(mbox1, 250);
lv_obj_align(mbox1, NULL, LV_ALIGN_IN_TOP_LEFT, 10, 10); /*Align to the corner*/

/****************************************
 * Create a message box with new styles
 ***************************************/

/*Create a new background style*/
static lv_style_t style_bg;
lv_style_copy(&style_bg, &lv_style_pretty);
style_bg.body.main_color = LV_COLOR_MAKE(0xf5, 0x45, 0x2e);
style_bg.body.grad_color = LV_COLOR_MAKE(0xb9, 0x1d, 0x09);
style_bg.body.border.color = LV_COLOR_MAKE(0x3f, 0x0a, 0x03);
style_bg.text.color = LV_COLOR_WHITE;
style_bg.body.padding.hor = 12;
style_bg.body.padding.ver = 8;
style_bg.body.shadow.width = 8;

/*Create released and pressed button styles*/
static lv_style_t style_btn_rel;
static lv_style_t style_btn_pr;
lv_style_copy(&style_btn_rel, &lv_style_btn_rel);
style_btn_rel.body.empty = 1;                    /*Draw only the border*/
style_btn_rel.body.border.color = LV_COLOR_WHITE;
style_btn_rel.body.border.width = 2;
style_btn_rel.body.border.opa = LV_OPA_70;
style_btn_rel.body.padding.hor = 12;
style_btn_rel.body.padding.ver = 8;

lv_style_copy(&style_btn_pr, &style_btn_rel);
style_btn_pr.body.empty = 0;
style_btn_pr.body.main_color = LV_COLOR_MAKE(0x5d, 0x0f, 0x04);
style_btn_pr.body.grad_color = LV_COLOR_MAKE(0x5d, 0x0f, 0x04);

/*Copy the message box (The buttons will be copied too)*/
lv_obj_t * mbox2 = lv_mbox_create(lv_scr_act(), mbox1);
lv_mbox_set_text(mbox2, "Message box with\n"
                        "with modified styles");
lv_mbox_set_style(mbox2, LV_MBOX_STYLE_BG, &style_bg);
lv_mbox_set_style(mbox2, LV_MBOX_STYLE_BTN_REL, &style_btn_rel);
lv_mbox_set_style(mbox2, LV_MBOX_STYLE_BTN_PR, &style_btn_pr);
lv_obj_align(mbox2, mbox1, LV_ALIGN_OUT_BOTTOM_LEFT, 50, -20);   /*Align according to the previous message box */
```

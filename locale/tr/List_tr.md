_Written for v5.1_

## Overview

The Lists are built from a background **Page** and **Buttons** on it. The Buttons contain an optional icon-like Image (which can be a symbol too) and a Label. When the list become long enough it can be scrolled. The **width of the buttons** is set to maximum according to the object width. The **height** of the buttons are adjusted automatically according to the content (content height + style.body.padding.ver).

You can **add new list element** with `lv_list_add(list, "U:/img", "Text", rel_action)` or with symbol icon `lv_list_add(list, SYMBOL_EDIT, "Edit text")`. If you do no want to add image use `""` as file name. The function returns with a pointer to the created button to allow further configurations.  

You can use `lv_list_get_btn_label(list_btn)` and `lv_list_get_btn_img(list_btn)` to **get the label and the image** of a list button.

In the release action of a button you can get the the **button's text** with `lv_list_get_btn_text(button)`. It helps to identify the released list element. 

To **delete a list element** just use `lv_obj_del()` on the return value of `lv_list_add()`.

You can **navigate manually** in the list with `lv_list_up(list)` and `lv_list_down(list)`.

You can focus on a button directly using `lv_list_focus(btn, anim_en)`.

The **animation time** of up/down/focus movements can be set via: `lv_list_set_anim_time(list, anim_time)`. Zero animation time means not animations. 

## Style usage

The `lv_list_set_style(list, LV_LIST_STYLE_..., &style)` function sets the style of a list. For details explanation of _BG_, _SCRL_ and _SB_ see [Page](/Page_tr)

- **LV_LIST_STYLE_BG** list background style. Default: _lv_style_transp_fit_
- **LV_LIST_STYLE_SCRL** scrollable parts's style. Default:_ lv_style_pretty_
- **LV_LIST_STYLE_SB** scrollbars' style. Default: _lv_style_pretty_color_
- **LV_LIST_STYLE_BTN_REL** button released style. Default: _lv_style_btn_rel_
- **LV_LIST_STYLE_BTN_PR** button pressed style. Default: _lv_style_btn_pr_
- **LV_LIST_STYLE_BTN_TGL_REL** button toggled released style. Default: _lv_style_btn_tgl_rel_
- **LV_LIST_STYLE_BTN_TGL_PR** button toggled pressed style. Default: _lv_style_btn_tgl_pr_
- **LV_LIST_STYLE_BTN_INA** button inactive style. Default: _lv_style_btn_ina_

## Notes

- You can set a transparent background for the list. In this case if you have only a few list buttons the the list will look shorter but become scrollable when more list elements are added.
- The button labels default long mode is `LV_LABEL_LONG_ROLL`. You can modify it manually. Use `lv_list_get_btn_label()` to get buttons's label.
- To **modify the height of the buttons** adjust the _body.padding.ver_ field of the corresponding style (LV_LIST_STYLE_BTN_REL , LV_LIST_STYLE_BTN_PR etc.)

## Example
![List image](http://docs.littlevgl.com/img/list-lv_list.png)
```c
/*Will be called on click of a button of a list*/
static lv_res_t list_release_action(lv_obj_t * list_btn)
{
    printf("List element click:%s\n", lv_list_get_btn_text(list_btn));

    return LV_RES_OK; /*Return OK because the list is not deleted*/
}

.
.
.

/************************
 * Create a default list
 ************************/

/*Crate the list*/
lv_obj_t * list1 = lv_list_create(lv_scr_act(), NULL);
lv_obj_set_size(list1, 130, 170);
lv_obj_align(list1, NULL, LV_ALIGN_IN_TOP_LEFT, 20, 40);

/*Add list elements*/
lv_list_add(list1, SYMBOL_FILE, "New", list_release_action);
lv_list_add(list1, SYMBOL_DIRECTORY, "Open", list_release_action);
lv_list_add(list1, SYMBOL_CLOSE, "Delete", list_release_action);
lv_list_add(list1, SYMBOL_EDIT, "Edit", list_release_action);
lv_list_add(list1, SYMBOL_SAVE, "Save", list_release_action);

/*Create a label above the list*/
lv_obj_t * label;
label = lv_label_create(lv_scr_act(), NULL);
lv_label_set_text(label, "Default");
lv_obj_align(label, list1, LV_ALIGN_OUT_TOP_MID, 0, -10);

/*********************
 * Create new styles
 ********************/
/*Create a scroll bar style*/
static lv_style_t style_sb;
lv_style_copy(&style_sb, &lv_style_plain);
style_sb.body.main_color = LV_COLOR_BLACK;
style_sb.body.grad_color = LV_COLOR_BLACK;
style_sb.body.border.color = LV_COLOR_WHITE;
style_sb.body.border.width = 1;
style_sb.body.border.opa = LV_OPA_70;
style_sb.body.radius = LV_RADIUS_CIRCLE;
style_sb.body.opa = LV_OPA_60;

/*Create styles for the buttons*/
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

/**************************************
 * Create a list with modified styles
 **************************************/

/*Copy the previous list*/
lv_obj_t * list2 = lv_list_create(lv_scr_act(),list1);
lv_obj_align(list2, NULL, LV_ALIGN_IN_TOP_RIGHT, -20, 40);
lv_list_set_sb_mode(list2, LV_SB_MODE_AUTO);
lv_list_set_style(list2, LV_LIST_STYLE_BG, &lv_style_transp_tight);
lv_list_set_style(list2, LV_LIST_STYLE_SCRL, &lv_style_transp_tight);
lv_list_set_style(list2, LV_LIST_STYLE_BTN_REL, &style_btn_rel); /*Set the new button styles*/
lv_list_set_style(list2, LV_LIST_STYLE_BTN_PR, &style_btn_pr);

/*Create a label above the list*/
label = lv_label_create(lv_scr_act(), label);       /*Copy the previous label*/
lv_label_set_text(label, "Modified");
lv_obj_align(label, list2, LV_ALIGN_OUT_TOP_MID, 0, -10);
```

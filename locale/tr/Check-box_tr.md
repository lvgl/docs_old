## Overview

The Check Box objects are built from a Button **background** which contains an also Button **bullet** and a **label** to realize a classical check box. The **text** can be modified by the `lv_cb_set_text(cb, "New text")` function.

An **action** can assigned by `lv_cb_set_action(cb, action)`.

You can manually **check / un-check** the Check box  via `lv_cb_set_checked(cb, state)`.

## Style usage

The Check box styles can be modified with `lv_cb_set_style(cb, LV_CB_STYLE_..., &style)`.

- **LV_CB_STYLE_BG** Background style. Uses all _style.body_ properties. The label's style comes from  _style.text_. Default: _lv_style_transp_
- **LV_CB_STYLE_BOX_REL** Style of the released box. Uses the _style.body_ properties. Default: _lv_style_btn_rel_
- **LV_CB_STYLE_BOX_PR** Style of the pressed box. Uses the _style.body_ properties. Default: _lv_style_btn_pr_
- **LV_CB_STYLE_BOX_TGL_REL** Style of the checked released box. Uses the _style.body_ properties. Default: _lv_style_btn_tgl_rel_
- **LV_CB_STYLE_BOX_TGL_PR** Style of the checked released box. Uses the _style.body_ properties. Default: _lv_style_btn_tgl_pr_

## Example
![Checkbox image](http://docs.littlevgl.com/img/check-box-lv_cb.png)
```c
static lv_res_t cb_release_action(lv_obj_t * cb)
{
    /*A check box is clicked*/
    printf("%s state: %d\n", lv_cb_get_text(cb), lv_cb_is_checked(cb));

    return LV_RES_OK;
}

.
.
.


/********************************************
 * Create a container for the check boxes
 ********************************************/

/*Create  border style*/
static lv_style_t style_border;
lv_style_copy(&style_border, &lv_style_pretty_color);
style_border.glass = 1;
style_border.body.empty = 1;

/*Create a container*/
lv_obj_t * cont;
cont = lv_cont_create(lv_scr_act(), NULL);
lv_cont_set_layout(cont, LV_LAYOUT_COL_L);      /*Arrange the children in a column*/
lv_cont_set_fit(cont, true, true);              /*Fit the size to the content*/
lv_obj_set_style(cont, &style_border);

/**************************
 * Create check boxes
 *************************/

/*Create check box*/
lv_obj_t * cb;
cb = lv_cb_create(cont, NULL);
lv_cb_set_text(cb, "Potato");
lv_cb_set_action(cb, cb_release_action);

/*Copy the previous check box*/
cb = lv_cb_create(cont, cb);
lv_cb_set_text(cb, "Onion");

/*Copy the previous check box*/
cb = lv_cb_create(cont, cb);
lv_cb_set_text(cb, "Carrot");

/*Copy the previous check box*/
cb = lv_cb_create(cont, cb);
lv_cb_set_text(cb, "Salad");

/*Align the container to the middle*/
lv_obj_align(cont, NULL, LV_ALIGN_CENTER, 0, 0);
```

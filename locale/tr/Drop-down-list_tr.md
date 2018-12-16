_Written for v5.3, revision 2_

## Overview

Drop Down Lists allow you to simply **select one option from more**. The Drop Down List is closed by default an show the currently selected text. If you click on it the this list opens and all the options are shown.

The **options** are passed to the Drop Down List as a **string** with `lv_ddlist_set_options(ddlist, options)`. The options should be separated by `\n`. For example: `"First\nSecond\nThird"`.

You can **select an option manually** with `lv_ddlist_set_selected(ddlist, id)`, where _id_ is the index of an option.

A **callback function** can be specified with `lv_ddlist_set_action(ddlist, my_action)` to call when a new option is selected.

By default the list's **height** is adjusted automatically to show all options. The `lv_ddlist_set_fix_height(ddlist, h)` sets a fixed height for the opened list.

The **width** is also adjusted automatically. To prevent this apply `lv_ddlist_set_hor_fit(ddlist, false)` and set the width manually by `lv_obj_set_width(ddlist, width)`.

Similarly to [Page](/Page_tr) with fix height the Drop Down List supports various **scrollbar display modes**. It can be set by `lv_ddlist_set_sb_mode(ddlist, LV_SB_MODE_...)`.

The Drop Down List open/close animation time is adjusted by `lv_ddlist_set_anim_time(ddlist, anim_time)`. Zero animation time means no animation.

**New in v5.3** is the ability to enable an arrow on the side of the drop down list. To use this feature you can call `lv_ddlist_set_draw_arrow(ddlist, true)`.

## Style usage

The `lv_ddlist_set_style(ddlist, LV_DDLIST_STYLE_..., &style)` set the styles of a Drop Down List.

- **LV_DDLIST_STYLE_BG** Style of the background. All _style.body_ properties are used. It is used for the label's style from _style.text_. Default: _lv_style_pretty_
- **LV_DDLIST_STYLE_SEL** Style of the selected option.  The _style.body_ properties are used. The selected option will be recolored with _text.color_. Default: _lv_style_plain_color_
- **LV_DDLIST_STYLE_SB** Style of the scrollbar. The _style.body_ properties are used. Default: _lv_style_plain_color_

## Example
![Drop down list image](http://docs.littlevgl.com/img/drop-down-list-lv_ddlist.png)
```c
static lv_res_t ddlist_action(lv_obj_t * ddlist)
{
    uint8_t id = lv_obj_get_free_num(ddlist);

    char sel_str[32];
    lv_ddlist_get_selected_str(ddlist, sel_str);
    printf("Ddlist %d new option: %s \n", id, sel_str);

    return LV_RES_OK; /*Return OK if the drop down list is not deleted*/
}


.
.
.

/*Create a drop down list*/
lv_obj_t * ddl1 = lv_ddlist_create(lv_scr_act(), NULL);
lv_ddlist_set_options(ddl1, "Apple\n"
                            "Banana\n"
                            "Orange\n"
                            "Melon\n"
                            "Grape\n"
                            "Raspberry");
lv_obj_align(ddl1, NULL, LV_ALIGN_IN_TOP_LEFT, 30, 10);
lv_obj_set_free_num(ddl1, 1);               /*Set a unique ID*/
lv_ddlist_set_action(ddl1, ddlist_action);  /*Set a function to call when anew option is chosen*/

/*Create a style*/
static lv_style_t style_bg;
lv_style_copy(&style_bg, &lv_style_pretty);
style_bg.body.shadow.width = 4; /*Enable the shadow*/
style_bg.text.color = LV_COLOR_MAKE(0x10, 0x20, 0x50);

/*Copy the drop down list and set the new style_bg*/
lv_obj_t * ddl2 = lv_ddlist_create(lv_scr_act(), ddl1);
lv_obj_align(ddl2, NULL, LV_ALIGN_IN_TOP_RIGHT, -30, 10);
lv_obj_set_free_num(ddl2, 2);       /*Set a unique ID*/
lv_obj_set_style(ddl2, &style_bg);
```

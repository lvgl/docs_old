_Written for v5.1_

## Overview

The Text Area is **a page**  with a **label** and a **cursor** on it. You can **insert text or characters**  to the current cursor position with:

- `lv_ta_add_char(ta, 'c')`
- `lv_ta_add_text(ta, "insert this text")`

The `lv_ta_set_text(ta, "New text")` **changes the whole text**.

To **delete a character** from the left of the current cursor position use `lv_ta_del()`.

The cursor position can be modified directly like `lv_ta_set_cursor_pos(ta, 10)` or by stepping it:

- `lv_ta_cursor_right(ta)`
- `lv_ta_cursor_left(ta)`
- `lv_ta_cursor_up(ta)`
- `lv_ta_cursor_down(ta)`

There are several cursor types. You can set one of them with: `lv_ta_set_cursor_type(ta, LV_CURSOR_...)`

- LV_CURSOR_NONE
- LV_CURSOR_LINE
- LV_CURSOR_BLOCK
- LV_CURSOR_OUTLINE
- LV_CURSOR_UNDERLINE

You can 'OR' _LV_CURSOR_HIDDEN_ to any type to hide the cursor.

The Text area can be configures to be one lined with `lv_ta_set_one_line(ta, true)`.

The text area supports **password mode**. It can be enabled with `lv_ta_set_pwd_mode(ta, true)`.

## Style usage

Use `lv_ta_set_style(page, LV_TA_STYLE_...,  &style)` to set a new style for an element of the text area:

- **LV_TA_STYLE_BG** background's style which uses all _style.body_ properties. The label also uses this _style.label_ from this style.  (default: lv_style_pretty)
- **LV_TA_STYLE_SB** scrollbar's style which uses all _style.body_ properties (default: lv_style_transp)
- **LV_TA_STYLE_CURSOR** cursor style. If NULL then the library sets us a style automatically according to the label color and font

    - LV_CURSOR_LINE: a _style.line.width_ wide line but drawn as a rectangle as _style.body_. Hor. and ver. padding makes an offset on the cursor
    - LV_CURSOR_BLOCK: a rectangle as _style.body_  Hor. and ver. padding makes the rectangle larger
    - LV_CURSOR_OUTLINE: an empty rectangle (just a border) as _style.body_  Hor. and ver. padding makes the rectangle larger
    - LV_CURSOR_UNDERLINE: a _style.line.width_ wide line but drawn as a rectangle as _style.body_. Hor. and ver. padding makes an offset on the cursor 

## Notes

- In password mode `lv_ta_get_text(ta)` gives the real text and not the asterisk characters

## Example
![Text area image](http://docs.littlevgl.com/img/text-area-lv_ta.png)
```c
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

/*Create a normal Text area*/
lv_obj_t * ta1 = lv_ta_create(lv_scr_act(), NULL);
lv_obj_set_size(ta1, 200, 100);
lv_obj_align(ta1, NULL, LV_ALIGN_CENTER, 0, - LV_DPI / 2);
lv_ta_set_style(ta1,LV_TA_STYLE_SB, &style_sb);                     /*Apply the scroll bar style*/
lv_ta_set_cursor_type(ta1, LV_CURSOR_BLOCK);
lv_ta_set_text(ta1, "A text in a Text Area\n"
               "You can scroll it if the text is long enough.");    /*Set an initial text*/
lv_ta_set_cursor_pos(ta1, 2);                                       /*Set the cursor position*/
lv_ta_add_text(ta1, "long ");                                       /*Insert a word at the current cursor position*/

static lv_style_t style_bg;
lv_style_copy(&style_bg, &lv_style_pretty);
style_bg.body.shadow.width = 8;
style_bg.text.color = LV_COLOR_MAKE(0x30, 0x60, 0xd0);              /*Blue label*/

/*Create a one lined test are with password mode*/
lv_obj_t * ta2 = lv_ta_create(lv_scr_act(), ta1);
lv_obj_align(ta2, ta1, LV_ALIGN_OUT_BOTTOM_MID, 0, 50);
lv_ta_set_style(ta2,LV_TA_STYLE_BG, &style_bg);                     /*Apply the background style*/
lv_ta_set_one_line(ta2, true);
lv_ta_set_cursor_type(ta2, LV_CURSOR_LINE);
lv_ta_set_pwd_mode(ta2, true);
lv_ta_set_text(ta2, "Password");
```

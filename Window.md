_Written for v5.1_

## Overview

The windows are one of the **most complex** container-like objects. They are built from two main parts: a **header** [Container](/Container) on the top and a [Page](/Page) for the **content** below the header. 

On the header there is **title** which can be modified by: `lv_win_set_title(win, "New title")`. The title always inherits the style of the header.

You can add **control buttons** to the right side of the header with: `lv_win_add_btn(win, "U:/close", my_close_action)`. The second parameter is an image file path, the third parameter is a function to call when the button is released. You can use **symbols** as images as well like: `lv_win_add_btn(win, SYMBOL_CLOSE, my_close_action)`. 

You can modify the **size of the control buttons** with the `lv_win_set_btn_size(win, new_size)` function.

The scrollbar behavior can be set by `lv_win_set_sb_mode(win, LV_SB_MODE_...)`.

To set a layout for the content use `lv_win_set_layout(win, LV_LAYOUT_...)`. 

## Style usage

Use `lv_win_set_style(win, LV_WIN_STYLE_...,  &style)` to set a new style for an element of the window:

- **LV_WIN_STYE_BG** main background which uses all _style.body_ properties (header and content page are placed on it) (default: lv_style_plain)
- **LV_WIN_STYLE_CONTENT_BG** content page's background which uses all _style.body_ properties (default: lv_style_transp)
- **LV_WIN_STYLE_CONTENT_SCRL** content page's scrollable part which uses all _style.body_ properties (default: lv_style_transp)
- **LV_WIN_STYLE_SB** scroll bar's style which uses all _style.body_ properties. hor/ver* padding sets the scrollbars' padding respectively and the inner padding sets the scrollbar's width.  (default: lv_style_pretty_color)
- **LV_WIN_STYLE_HEADER** header's style which uses all _style.body_ properties (default: lv_style_plain_color)
- **LV_WIN_STYLE_BTN_REL** released button's style (on header) which uses all _style.body_ properties (default: lv_style_btn_rel)
- **LV_WIN_STYLE_BTN_PR** released button's style (on header) which uses all _style.body_ properties (default: lv_style_btn_pr)

## Notes

## Example
![Window image](http://docs.littlevgl.com/img/window-lv_win.png)
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

/*Create a window*/
lv_obj_t * win = lv_win_create(lv_scr_act(), NULL);
lv_win_set_title(win, "Example window");                        /*Set the title*/
lv_win_set_style(win, LV_WIN_STYLE_SB, &style_sb);              /*Set the scroll bar style*/


/*Add control button to the header*/
lv_win_add_btn(win, SYMBOL_SETTINGS, my_setup_action);            /*Add a setup button*/
lv_win_add_btn(win, SYMBOL_CLOSE, lv_win_close_action);           /*Add close button and use built-in close action*/


/*Add some dummy content*/
lv_obj_t * txt = lv_label_create(win, NULL);
lv_label_set_text(txt, "This is the content of the window\n\n"
                       "You can add control buttons to\nthe window header\n\n"
                       "You can scroll it\n\n"
                       "See the scroll bar on the right!");
```

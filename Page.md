_Written for v5.1_

## Overview

The Page consist of two containers on each other: the bottom is the **background** (or base) and the top is the **scrollable**. If you create a child on the page it will be automatically moved to the scrollable container. If the scrollable container become greater then the background it **can be scrolled by dragging** (like the lists on smart phones).

By default the scrollable's _auto fit_ attribute is enabled vertically so its height will increased to include all its children. The width of the scrollable is automatically adjusted to the background width (minus the background's horizontal padding).

The background object can be referenced as the page itself like: `lv_obj_set_width(page, 100)`.

The scrollbar object can be retrieved with: `lv_page_get_scrl(page)`.

**Scrollbars** can be shown according to four policies:

- LV_SB_MODE_OFF: Never show scrollbars
- LV_SB_MODE_ON: Always show scrollbars
- LV_SB_MODE_DRAG: Show scrollbars when page is being dragged
- LV_SB_MODE_AUTO: Show scrollbars when the scrollable container is large enough to be scrolled

You can set scroll bar show policy by: `lv_page_set_sb_mode(page, SB_MODE)`. The default value is _LV_PAGE_SB_MODE_ON_;

You can **glue a children** to the page. In this case you can scroll the page with dragging the child object. It can be enabled by the `lv_page_glue_obj(child, true)`.

You can **focus to an object** on a page with: `lv_page_focus(page, child, anim_time)`.

It will moves the scrollable container to show a child. If the last parameter is not zero then the page will move with an animation.

**A release and a press action** can be assigned to the Page with `lv_page_set_rel_action(page, my_rel_action)` and `lv_page_set_pr_action(page, my_pr_action)`. The action can be triggered from the Background and the Scrollable object too.

There are functions to directly **set/get the scrollable's attributes**: 

- `lv_page_set_scrl_fit()`
- `lv_page_set_scrl_width()`
- `lv_page_set_scrl_height()`
- `lv_page_set_scrl_layout()`

## Style usage

Use `lv_page_set_style(page, LV_PAGE_STYLE_...,  &style)` to set a new style for an element of the page:

- **LV_PAGE_STYLE_BG** background's style which uses all _style.body_ properties (default: lv_style_pretty_color)
- **LV_PAGE_STYLE_SCRL** scrollable's style which uses all _style.body_ properties (default: lv_style_pretty)
- **LV_PAGE_STYLE_SB** scroll bar's style which uses all _style.body_ properties. hor/ver* padding sets the scrollbars' padding respectively and the inner padding sets the scrollbar's width.  (default: lv_style_pretty_color)

## Notes

- **Setting the position of children** is not possible in x or y direction if the corresponding _hor_ or _ver_ fit is enabled.  It's because if  the _y_ coordinate is modified  (with _ver fit_ enabled)  the scrollable object will resized to be directly above and below the child. But a scrollable part can't be in the middle so it will be moved back to the top.  To avoid this use `lv_obj_align()` to place object relative to each other (one has to be in to top/left) or disable fit with `lv_page_set_scrl_fit(page, false, false);` and set it's size `lv_page_set_scrl_width/height(page,  100)`.
- The background draws its border when the scrollable is drawn. It ensures that the page always will have closed shape even if the scrollable has the same color as the page's parent.

## Example
![Page image](https://github.com/littlevgl/lvgl/wiki/img/page-lv_page.png)
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
style_sb.body.padding.hor = 3;          /*Horizontal padding on the right*/
style_sb.body.padding.inner = 8;        /*Scrollbar width*/

/*Create a page*/
lv_obj_t * page = lv_page_create(lv_scr_act(), NULL);
lv_obj_set_size(page, 150, 200);
lv_obj_align(page, NULL, LV_ALIGN_CENTER, 0, 0);
lv_page_set_style(page, LV_PAGE_STYLE_SB, &style_sb);           /*Set the scrollbar style*/
lv_page_set_sb_mode(page, LV_SB_MODE_AUTO);                     /*Show scroll bars is scrolling is possible*/

/*Create a label on the page*/
lv_obj_t * label = lv_label_create(page, NULL);
lv_label_set_long_mode(label, LV_LABEL_LONG_BREAK);             /*Automatically break long lines*/
lv_obj_set_width(label, lv_page_get_scrl_width(page));          /*Set the width. Lines will break here*/
lv_label_set_text(label, "Lorem ipsum dolor sit amet, consectetur adipiscing elit,\n"
                         "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\n"
                         "Ut enim ad minim veniam, quis nostrud exercitation ullamco\n"
                         "laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure\n"
                         "dolor in reprehenderit in voluptate velit esse cillum dolore\n"
                         "eu fugiat nulla pariatur.\n"
                         "Excepteur sint occaecat cupidatat non proident, sunt in culpa\n"
                         "qui officia deserunt mollit anim id est laborum.");
```

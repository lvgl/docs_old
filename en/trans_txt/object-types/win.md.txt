# Window (lv_win)

## Overview

The windows are one of the most complex container-like objects. They are built from two main parts: 
1. a header [Container](/object-types/cont) on the top 
2. a [Page](/object-types/page) for the content below the header. 

### Title
On the header, there is a title which can be modified by: `lv_win_set_title(win, "New title")`. The title always inherits the style of the header.

### Control buttons
You can add control buttons to the right side of the header with: `lv_win_add_btn(win, LV_SYMBOL_CLOSE)`. 
The second parameter is an [Image](/object-types/img) source.

`lv_win_close_event_cb` can be used as an event callback to close the Window.

You can modify the size of the control buttons with the `lv_win_set_btn_size(win, new_size)` function.

### Scrollbars

The scrollbar behavior can be set by `lv_win_set_sb_mode(win, LV_SB_MODE_...)`. See [Page](/object-types/page) for details.

### Manual scroll and focus
To scroll the Window directly you can use `lv_win_scroll_hor(win, dist_px)` or `lv_win_scroll_ver(win, dist_px)`.

To make the Window show an object on it use `lv_win_focus(win, child, LV_ANIM_ON/OFF)`.

The time of scroll and focus animations can  be adjusted with `lv_win_set_anim_time(win, anim_time_ms)`

### Layout
To set a layout for the content use `lv_win_set_layout(win, LV_LAYOUT_...)`. See [Container](/object-types/cont) for details.

## Style usage

Use `lv_win_set_style(win, LV_WIN_STYLE_...,  &style)` to set a new style for an element of the Window:

- **LV_WIN_STYE_BG** main background which uses all `style.body` properties (header and content page are placed on it) (default: `lv_style_plain`)
- **LV_WIN_STYLE_CONTENT** content page's scrollable part which uses all `style.body` properties (default: `lv_style_transp`)
- **LV_WIN_STYLE_SB** scroll bar's style which uses all `style.body` properties. `left/top` padding sets the scrollbars' padding respectively and the inner padding sets the scrollbar's width.  (default: `lv_style_pretty_color`)
- **LV_WIN_STYLE_HEADER** header's style which uses all `style.body` properties (default: `lv_style_plain_color`)
- **LV_WIN_STYLE_BTN_REL** released button's style (on header) which uses all `style.body` properties (default: `lv_style_btn_rel`)
- **LV_WIN_STYLE_BTN_PR** released button's style (on header) which uses all `style.body` properties (default: `lv_style_btn_pr`)

## Events
Only the [Generic events](/overview/event.html#generic-events) are sent by the object type.

Learn more about [Events](/overview/event).

## Keys

The following *Keys* are processed by the Page:
- **LV_KEY_RIGHT/LEFT/UP/DOWN** Scroll the page

Learn more about [Keys](/overview/indev).


## Example

```eval_rst

.. include:: /lv_examples/src/lv_ex_win/index.rst

```


## API 

```eval_rst

.. doxygenfile:: lv_win.h
  :project: lvgl
        
```

```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/zh-CN/object-types/ta.md
```
# Text area (lv_ta)

## Overview

The Text Area is a [Page](/object-types/page) with a [Label](/object-types/label) and a cursor on it. Texts or characters can be added to it. Long lines are wrapped and when the text becomes long enough the Text area can be scrolled-

### Add text

You can insert text or characters  to the current cursor's position with:

- `lv_ta_add_char(ta, 'c')`
- `lv_ta_add_text(ta, "insert this text")`

To add wide characters like `'á'`, `'ß'` or CJK characters use `lv_ta_add_text(ta, "á")`.

`lv_ta_set_text(ta, "New text")` changes the whole text.

### Placeholder

A placeholder text can be specified which is displayed when the Text area is empty with `lv_ta_set_placeholder_text(ta, "Placeholder text")`

### Delete character

To delete a character from the left of the current cursor position use `lv_ta_del_char(ta)`. The delete from teh right use `lv_ta_del_char_forward(ta)`

### Move the cursor

The cursor position can be modified directly with `lv_ta_set_cursor_pos(ta, 10)`. The `0` position means "before the first characters", `LV_TA_CURSOR_LAST` means "after the last character"

You can step the cursor with
- `lv_ta_cursor_right(ta)`
- `lv_ta_cursor_left(ta)`
- `lv_ta_cursor_up(ta)`
- `lv_ta_cursor_down(ta)`

If `lv_ta_set_cursor_click_pos(ta, true)` is called the cursor will jump to the position where the Text area was clicked.

### Cursor types

There are several cursor types. You can set one of them with: `lv_ta_set_cursor_type(ta, LV_CURSOR_...)`
- **LV_CURSOR_NONE** No cursor
- **LV_CURSOR_LINE** A simple vertical line
- **LV_CURSOR_BLOCK** A filled rectangle on the current character
- **LV_CURSOR_OUTLINE** A rectangle border around the current character
- **LV_CURSOR_UNDERLINE** Underline the current character

You can 'OR' `LV_CURSOR_HIDDEN` to any type to temporarily hide the cursor.

The blink time of the cursor can be adjusted with `lv_ta_set_cursor_blink_time(ta, time_ms)`.


### One line mode
The Text area can be configures to be one lined with `lv_ta_set_one_line(ta, true)`. In this mode the height is set automatically to show only one line, line break character are ignored, and word wrap is disabled. 

### Password mode
The text area supports password mode which can be enabled with `lv_ta_set_pwd_mode(ta, true)`. In password mode, the enters characters are converted to `*` after some time or when a new character is entered. 

In password mode `lv_ta_get_text(ta)` gives the real text and not the asterisk characters

The visibility time can be adjusted with `lv_ta_set_pwd_show_time(ta, time_ms)`.

### Text align
The text can be aligned to the left, center or right with `lv_ta_set_text_align(ta, LV_LABEL_ALIGN_LET/CENTER/RIGHT)`.

In one line mode, the text can be scrolled horizontally only if the text is left aligned.

### Accepted characters
You can set a list of accepted characters with `lv_ta_set_accepted_chars(ta, "0123456789.+-")`. Other characters will be ignored. 

### Max text length
The maximum number of characters can be limited with `lv_ta_set_max_length(ta, max_char_num)`

### Very long texts
If there is a  very long text in the Text area  (> 20k characters) its scrolling and drawing might be slow. 
However, by enabling `LV_LABEL_LONG_TXT_HINT   1` in *lv_conf.h* it can be hugely improved. 
It will save some info about the label to speed up its drawing. Using `LV_LABEL_LONG_TXT_HINT` the scrolling and drawing will as fast as with "normal" short texts.

### Select text
A part of text can be selected if enabled with `lv_ta_set_text_sel(ta, true)`. It works like when you select a text on your PC with your mouse. 

### Scrollbars
The scrollbars can shown according to different policies set by `lv_ta_set_sb_mode(ta, LV_SB_MODE_...)`. Learn more at the [Page](/object-types/page) object.

### Scroll propagation
When the Text area is scrolled on an other scrollable object (like a Page) and the scrolling has reached the edge of the Text area, the scrolling can be propagated to the parent. 
In other words, when the Text area can be scrolled further, the parent will be scrolled instead.

It can be enabled with `lv_ta_set_scroll_propagation(ta, true)`.

Learn more at the [Page](/object-types/page) object.

### Edge flash
When the Text area is scrolled to edge a circle like flash animation can be shown if it is enabled with `lv_ta_set_edge_flash(ta, true)`

## Style usage

Use `lv_ta_set_style(page, LV_TA_STYLE_...,  &style)` to set a new style for an element of the text area:

- **LV_TA_STYLE_BG** background's style which uses all `style.body` properties. The label uses `style.label` from this style.  (default: `lv_style_pretty`)
- **LV_TA_STYLE_SB** scrollbar's style which uses all `style.body` properties (default: `lv_style_pretty_color`)
- **LV_TA_STYLE_CURSOR** cursor style. If `NULL` then the library sets a style automatically according to the label's color and font
    - *LV_CURSOR_LINE*: a `style.line.width` wide line but drawn as a rectangle as `style.body`. `padding.top/left` makes an offset on the cursor
    - *LV_CURSOR_BLOCK*: a rectangle as `style.body`  `padding` makes the rectangle larger
    - *LV_CURSOR_OUTLINE*: an empty rectangle (just a border) as `style.body` `padding` makes the rectangle larger
    - *LV_CURSOR_UNDERLINE*: a `style.line.width` wide line but drawn as a rectangle as `style.body`. `padding.top/left` makes an offset on the cursor 



## Events
Besides the [Generic events](/overview/event.html#generic-events) the following [Special events](/overview/event.html#special-events) are sent by the Slider:
- **LV_EVENT_INSERT** Sent when a character before a character is inserted. 
The evnet data is the text planned to insert. `lv_ta_set_insert_replace(ta, "New text")` replaces the text to insert. 
The new text can't be in a local variable which is destroyed when the event callback exists. `""` means do not insert anything.
- **LV_EVENT_VALUE_CHANGED** When the content of the text area has been changed. 

## Keys
- **LV_KEY_UP/DOWN/LEFT/RIGHT** Move the cursor
- **Any character** Add the character to the current cursor position

Learn more about [Keys](/overview/indev).

## Example

```eval_rst

.. include:: /lv_examples/src/lv_ex_ta/index.rst

```

## API 

```eval_rst

.. doxygenfile:: lv_ta.h
  :project: lvgl
        
```

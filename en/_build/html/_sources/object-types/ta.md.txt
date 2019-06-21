# Test area

## Overview

The Text Area is a [Page](/object-types/page) with a [Label](/object-types/label) and a cursor on it. Texts or characters can be adde to it. Long lines are wrapped and when the Text become height enouggh the Text area can be scrolled-

### Add text

You can insert text or characters  to the current cursor's position with:

- `lv_ta_add_char(ta, 'c')`
- `lv_ta_add_text(ta, "insert this text")`

`lv_ta_set_text(ta, "New text")` changes the whole text.

### Placeholder

A placheloder text can be specified which is displayed when teh text are is empty with `lv_ta_set_placeholder_text(ta, "Placeholder text")`

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
- **LV_CURSOR_LINE** A smimple vertical line
- **LV_CURSOR_BLOCK** A filled rectangle on the current character
- **LV_CURSOR_OUTLINE** A rectangle border around the current character
- **LV_CURSOR_UNDERLINE** Underline the current character

You can 'OR' `LV_CURSOR_HIDDEN` to any type to temporarly hide the cursor.

The blibk time of the cusor can be adjusted with `lv_ta_set_cursor_blink_time(ta, time_ms)`.


### One line mode
The Text area can be configures to be one lined with `lv_ta_set_one_line(ta, true)`. IN this mode the height is set automaticlly to show only one line, line break character are ignored, and word wrap is disabled. 

### Password mode
The text area supports password mode whcih can be enabled with `lv_ta_set_pwd_mode(ta, true)`. In password mode the enters characters are covnerted to `*` after some time or shen a new character is eneterd. 

In password mode `lv_ta_get_text(ta)` gives the real text and not the asterisk characters

The visibilty time can be adjusted with `lv_ta_set_pwd_show_time(ta, time_ms)`.

### Text align
The txt can be alinged to the left, center or right with `lv_ta_set_text_align(ta, LV_LABEL_ALIGN_LET/CENTER/RIGHT)`.

In one line mode the text can be scrolled horizontally onle if the text is left aligned.

### Accepted characters
You can set a list of accepted characters with `lv_ta_set_accepted_chars(ta, "0123456789.+-")`. Other character will be ignored. 

### Max text length
THe maximum number of characters can be limited with `lv_ta_set_max_length(ta, max_char_num)`

### Select text
A part of text can be selected if enabled with `lv_ta_set_text_sel(ta, true)`. It work like wen you select a text on your PC with your mouse. 

### Scrollbars
The scrollbars can shown according to different policies set by `lv_ta_set_sb_mode(ta, LV_SB_MODE_...)`. Learn more at the [Page](/object-types/page) object.

### Scroll propagation
When the Text area is scrolled and its on an other scrollable object (like a Page) and the scrolling has reached the edge of the Text area, the scrolling can can be propagated to the parent. 
In other words when the Text area can be scrolled further, the parent wil be scrolled instead.

It can be enabled with `lv_ta_set_scroll_propagation(ta, true)`.

Learn more at the [Page](/object-types/page) object.

### Edge flash
When the Text are is scrolled to edge a circle like flash animation can be shown if it is enabled with `lv_ta_set_edge_flash(ta, true)`

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
Besided the [Genreric events](/overview/event.html#generic-events) the following [Special events](/overview/event.html#special-events) are sent by the Slider:
- **LV_EVENT_INSERT** Sent when a chracer before a chacter is inserted. 
The evnet data is the text planned to insert. `lv_ta_set_insert_replace(ta, "New text")` replaces the text to insert. 
The new text can't be in a local variable which is destroyed when the event callback exists. `""` means do not insert anything.
- **LV_EVENT_VALUE_CHANGED** When the content of the text area has been changed. 

## Keys
- **LV_KEY_UP/DOWN/LEFT/RIGHT** Move the cursor
- **Any chacter** Add the chacter to the current cursor position

Learn more about [Keys](/overview/indev).

## Example

### C

![](/examples/ta/ta_1.png "Text area in LittlevGL")

```eval_rst
.. container:: toggle

    .. container:: header
    
      code

    .. literalinclude:: /examples/ta/ta_1.c
      :language: c
 
```

### MicroPython
No examples yet.

## API 

```eval_rst

.. doxygenfile:: lv_ta.h
  :project: lvgl
        
```


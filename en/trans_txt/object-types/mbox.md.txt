# Message box (lv_mbox)

## Overview

The Message boxes act as pop-ups. They are built from a background [Container](/object-types/cont), a [Label](/object-types/label) and a [Button matrix](/object-types/btnm) for buttons. 


The text will be broken into multiple lines automatically (has `LV_LABEL_LONG_MODE_BREAK`) and the height will be set automatically to involve the text and the buttons (`LV_FIT_TIGHT` auto fit vertically)-

### Set text
To set the text use the `lv_mbox_set_text(mbox, "My text")` function.

### Add buttons
 To add buttons use the `lv_mbox_add_btns(mbox, btn_str)` function. You need specify the button's text like `const char * btn_str[] = {"Apply", "Close", ""}`. 
 For more information visit the [Button matrix](/object-types/btnm) documentation.

### Auto-close
With `lv_mbox_start_auto_close(mbox, delay)` the message box can be closed automatically after `delay` milliseconds with an animation. The `lv_mbox_stop_auto_close(mbox)` function stops a started auto close.

The duration of the close animation can be set by `lv_mbox_set_anim_time(mbox, anim_time)`.

## Styles

Use `lv_mbox_set_style(mbox, LV_MBOX_STYLE_...,  &style)` to set a new style for an element of the Message box:

- **LV_MBOX_STYLE_BG** specifies the background container's style. `style.body` sets the background and`_style.label` sets the text appearance. Default: `lv_style_pretty`
- **LV_MBOX_STYLE_BTN_BG** style of the Button matrix background. Default: `lv_style_trans`
- **LV_MBOX_STYLE_BTN_REL** style of the released buttons. Default: `lv_style_btn_rel`
- **LV_MBOX_STYLE_BTN_PR** style of the pressed buttons. Default: `lv_style_btn_pr`
- **LV_MBOX_STYLE_BTN_TGL_REL** style of the toggled released buttons. Default: `lv_style_btn_tgl_rel`
- **LV_MBOX_STYLE_BTN_TGL_PR** style of the toggled pressed buttons. Default: `lv_style_btn_tgl_pr`
- **LV_MBOX_STYLE_BTN_INA** style of the inactive buttons. Default: `lv_style_btn_ina`

The height of the button area comes from *font height + padding.top + padding.bottom* of `LV_MBOX_STYLE_BTN_REL`.

## Events
Besides the [Generic events](/overview/event.html#generic-events) the following [Special events](/overview/event.html#special-events) are sent by the Message boxes:
 - **LV_EVENT_VALUE_CHANGED** sent when the button is clicked. The event data is set to ID of the clicked button.

The Message box has a default event callback which closes itself when a button is clicked.

Learn more about [Events](/overview/event).

##Keys

The following *Keys* are processed by the Buttons:
- **LV_KEY_RIGHT/DOWN** Select the next button
- **LV_KEY_LEFT/TOP** Select the previous button
- **LV_KEY_ENTER** Clicks the selected button 

Learn more about [Keys](/overview/indev).


## Example

```eval_rst

.. include:: /lv_examples/src/lv_ex_mbox/index.rst

```

## API 

```eval_rst

.. doxygenfile:: lv_mbox.h
  :project: lvgl
        
```

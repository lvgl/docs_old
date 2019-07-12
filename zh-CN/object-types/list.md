# List (lv_list)

## Overview

The Lists are built from a background [Page](/object-types/page) and [Buttons](/object-types/btn) on it. 
The Buttons contain an optional icon-like [Image](/object-types/img) (which can be a symbol too) and a [Label](/object-types/label). 
When the list becomes long enough it can be scrolled. 

### Add buttons
You can add new list elements with `lv_list_add_btn(list, &icon_img, "Text", event_cb)` or with symbol `lv_list_add_btn(list, SYMBOL_EDIT, "Edit text")`. 
If you do not want to add image use `NULL` as image source. The function returns with a pointer to the created button to allow further configurations.

The width of the buttons is set to maximum according to the object width. 
The height of the buttons are adjusted automatically according to the content. (*content height* + *padding.top* + *padding.bottom*).

The labels are created with `LV_LABEL_LONG_SROLL_CIRC` long mode to automatically scroll the long labels circularly.

You can use `lv_list_get_btn_label(list_btn)` and `lv_list_get_btn_img(list_btn)` to get the label and the image of a list button. You can get the text directly with `lv_list_get_btn_text(list_btn)`.

### Delete buttons
To delete a list element just use `lv_obj_del(btn)` on the return value of `lv_list_add_btn()`. 

To clean the list (remove all buttons) use `lv_list_clean(list)`


### Manual navigation
You can navigate manually in the list with `lv_list_up(list)` and `lv_list_down(list)`.

You can focus on a button directly using `lv_list_focus(btn, LV_ANIM_ON/OFF)`.

The **animation time** of up/down/focus movements can be set via: `lv_list_set_anim_time(list, anim_time)`. Zero animation time means not animations. 

### Edge flash
A circle-like effect can be shown when the list reaches the most top or bottom position. 
`lv_list_set_edge_flash(list, en)` enables this feature.

### Scroll propagation
If the list is created on an other scrollable element (like a [Page](/object-types/page)) and the list can't be scrolled further the **scrolling can be propagated to the parent**. 
This way the scroll will be continued on the parent. It can be enabled with `lv_list_set_scroll_propagation(list, true)`

If the buttons have `lv_btn_set_toggle` enabled then `lv_list_set_single_mode(list, true)` can be used to ensure that only one button can be in toggled state at the same time.

## Style usage

The `lv_list_set_style(list, LV_LIST_STYLE_..., &style)` function sets the style of a list. 
- **LV_LIST_STYLE_BG** list background style. Default: `lv_style_transp_fit`
- **LV_LIST_STYLE_SCRL** scrollable part's style. Default: `lv_style_pretty`
- **LV_LIST_STYLE_SB** scrollbars' style. Default: `lv_style_pretty_color`. For details see [Page](/object-types/page) 
- **LV_LIST_STYLE_BTN_REL** button released style. Default: `lv_style_btn_rel`
- **LV_LIST_STYLE_BTN_PR** button pressed style. Default: `lv_style_btn_pr`
- **LV_LIST_STYLE_BTN_TGL_REL** button toggled released style. Default: `lv_style_btn_tgl_rel`
- **LV_LIST_STYLE_BTN_TGL_PR** button toggled pressed style. Default: `lv_style_btn_tgl_pr`
- **LV_LIST_STYLE_BTN_INA** button inactive style. Default: `lv_style_btn_ina`

Because *BG* has a transparent style by default if there is only a few buttons the list will look shorter but become scrollable when more list elements are added.

To modify the height of the buttons adjust the `body.padding.top/bottom` fields of the corresponding styles (`LV_LIST_STYLE_BTN_REL/PR/...`)


## Events
Only the [Generic events](/overview/event.html#generic-events) are sent by the object type.

Learn more about [Events](/overview/event).

## Keys
The following *Keys* are processed by the Lists:
- **LV_KEY_RIGHT/DOWN** Select the next button
- **LV_KEY_LEFT/UP** Select the previous button

Note that, as usual, the state of `LV_KEY_ENTER` is translated to `LV_EVENT_PRESSED/PRESSING/RELEASED` etc.

The Selected buttons are in `LV_BTN_STATE_PR/TG_PR` state.

To manually select a button use `lv_list_set_btn_selected(list, btn)`. When the list is defocused and focused again it will restore the last selected button.

Learn more about [Keys](/overview/indev).


## Example

```eval_rst

.. include:: /lv_examples/src/lv_ex_list/index.rst

```

## API 

```eval_rst

.. doxygenfile:: lv_list.h
  :project: lvgl
        
```

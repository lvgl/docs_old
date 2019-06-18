# List (lv_list)

## Overview

The Lists are built from a background [Page](/object-types/page) and [Buttons](/object-types/btn) on it. 
The Buttons contain an optional icon-like [Image](/object-types/img) (which can be a symbol too) and a [Label](/object-types/label). 
When the list become long enough it can be scrolled. 

The **width of the buttons** is set to maximum according to the object width. 
The **height** of the buttons are adjusted automatically according to the content. (*content height* + *padding.top* + *padding.bottom*).

You can **add new list element** with `lv_list_add(list, &icon_img, "Text", event_cb)` or with symbol `lv_list_add(list, SYMBOL_EDIT, "Edit text")`. 
If you do no want to add image use `NULL` as file name. The function returns with a pointer to the created button to allow further configurations.

The labels are created with `LV_LABEL_LONG_SROLL_CIRC` long mode.

You can use `lv_list_get_btn_label(list_btn)` and `lv_list_get_btn_img(list_btn)` to **get the label and the image** of a list button. You can get text directly with `lv_list_get_btn_text(list_btn)`.

To **delete a list element** just use `lv_obj_del()` on the return value of `lv_list_add()`. The clean the list (remove all buttons) use `lv_list_clean(list)`

You can **navigate manually** in the list with `lv_list_up(list)` and `lv_list_down(list)`.

You can focus on a button directly using `lv_list_focus(btn, LV_ANIM_ON/OFF)`.

A **circle-like effect** can be shown if the list **reached the most top or bottom** position. `lv_list_set_edge_flash(list, en)` enables this feature.

If the list is created on an other scrollable element (like a [Page](/object-types/page)) and the list can't be scrolled further the **scrolling can be propagated to the parent**. 
This way the scroll will be continued on the parent. It can be enebaled with `lv_list_set_scroll_propagation(list, true)`

The **animation time** of up/down/focus movements can be set via: `lv_list_set_anim_time(list, anim_time)`. Zero animation time means not animations. 

If the buttons have `lv_btn_set_toggle` enabled then `lv_list_set_single_mode(list, true)` can be used to ensure that only one button can be in toggleg state at the same time.

If the list is **added to a group** then a button be selected which will receive the *PRESS/CLICK/...* events when `LV_KEY_ENTER` is pressed. 
To change the seelceted button `LV_KEY_LEFT/RIGHT/UP/DOWN` or the `lv_list_set_btn_selected(list, btn)` can be used. When the list is defocused and focused again it will restore the last selected button.

## Style usage

The `lv_list_set_style(list, LV_LIST_STYLE_..., &style)` function sets the style of a list. 
- **LV_LIST_STYLE_BG** list background style. Default: `lv_style_transp_fit`
- **LV_LIST_STYLE_SCRL** scrollable parts's style. Default: `lv_style_pretty`
- **LV_LIST_STYLE_SB** scrollbars' style. Default: `lv_style_pretty_color`. For detailes see [Page](/object-types/page) 
- **LV_LIST_STYLE_BTN_REL** button released style. Default: `lv_style_btn_rel`
- **LV_LIST_STYLE_BTN_PR** button pressed style. Default: `lv_style_btn_pr`
- **LV_LIST_STYLE_BTN_TGL_REL** button toggled released style. Default: `lv_style_btn_tgl_rel`
- **LV_LIST_STYLE_BTN_TGL_PR** button toggled pressed style. Default: `lv_style_btn_tgl_pr`
- **LV_LIST_STYLE_BTN_INA** button inactive style. Default: `lv_style_btn_ina`

Because *BG* has a transparent style by default if there is only a few buttons the list will look shorter but become scrollable when more list elements are added.

To modify the height of the buttons adjust the `body.padding.top/bottom` fields of the corresponding styles (`LV_LIST_STYLE_BTN_REL/PR/...`)


## Events
Only the [Genreric events](/overview/events.html#generic-events) are sent by the object type.

Learn more about [Events](/overview/events).

## Keys
The following *Keys* are processed by the Lists:
- **LV_KEY_RIGHT/DOWN** Select he next button
- **LV_KEY_LEFT/UP** Select the previous button

Note that, as usual, the state of `LV_KEY_ENTER` is translated to `LV_EVENT_PRESSED/PRESSING/RELEASED` etc.

The Selected buttons are in `LV_BTN_STATE_PR/TG_PR` state.

Learn more about [Keys](/overview/indev).

## Example

### C


![](/examples/list/list_1.png "List object with LittlevGL")

```eval_rst
.. container:: toggle

    .. container:: header
    
      code

    .. literalinclude:: /examples/list/list_1.c
      :language: c
 
```

### MicroPython
No examples yet.

## API 

```eval_rst

.. doxygenfile:: lv_list.h
  :project: lvgl
        
```


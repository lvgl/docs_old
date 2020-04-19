```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/hu/object-types/tabview.md
```
# Tabview (lv_tabview)

## Overview

The Tab view object can be used to organize content in tabs. 

### Adding tab
You can add a new tabs with `lv_tabview_add_tab(tabview, "Tab name")`. It will return with a pointer to a [Page](/object-types/page) object where you can add the tab's content.

### Change tab
To select a new tab you can:
- Click on it on the header part
- Slide horizontally 
- Use `lv_tabview_set_tab_act(tabview, id, LV_ANIM_ON/OFF)` function

The manual sliding can be disabled with `lv_tabview_set_sliding(tabview, false)`.

### Tab button's position

By default, the tab selector buttons are placed on the top of the Tabview. It can be changed with `lv_tabview_set_btns_pos(tabview, LV_TABVIEW_BTNS_POS_TOP/BOTTOM/LEFT/RIGHT)`

Note that, you can't change the tab position from top or bottom to left or right when tabs are already added.


### Hide the tabs

The tab buttons can be hidden by `lv_tabview_set_btns_hidden(tabview, true)`

### Animation time

The animation time is adjusted by `lv_tabview_set_anim_time(tabview, anim_time_ms)`. It is used when the new tab is loaded.

## Style usage

Use `lv_tabview_set_style(tabview, LV_TABVIEW_STYLE_...,  &style)` to set a new style for an element of the Tabview:

- **LV_TABVIEW_STYLE_BG** main background which uses all `style.body` properties (default: `lv_style_plain`)
- **LV_TABVIEW_STYLE_INDIC** a thin rectangle on indicating the current tab. Uses all `style.body` properties. Its height comes from `body.padding.inner` (default: `lv_style_plain_color`)
- **LV_TABVIEW_STYLE_BTN_BG** style of the tab buttons' background. Uses all `style.body` properties. The header height will be set automatically considering `body.padding.top/bottom` (default: `lv_style_transp`)
- **LV_TABVIEW_STYLE_BTN_REL** style of released tab buttons. Uses all `style.body` properties.  (default: `lv_style_tbn_rel`)
- **LV_TABVIEW_STYLE_BTN_PR** style of released tab buttons. Uses all `style.body` properties except `padding`.  (default: `lv_style_tbn_rel`)
- **LV_TABVIEW_STYLE_BTN_TGL_REL** style of selected released tab buttons. Uses all `style.body` properties except `padding`.  (default: `lv_style_tbn_rel`)
- **LV_TABVIEW_STYLE_BTN_TGL_PR** style of selected pressed tab buttons. Uses all `style.body` properties except `padding`.  (default: `lv_style_btn_tgl_pr`)

The height of the header is calculated like:
*font height and padding.top and padding.bottom from LV_TABVIEW_STYLE_BTN_REL + padding.top and padding bottom from LV_TABVIEW_STYLE_BTN_BG*

## Events
Besides the [Generic events](/overview/event.html#generic-events) the following [Special events](/overview/event.html#special-events) are sent by the Slider:
- **LV_EVENT_VALUE_CHANGED** Sent when a new tab is selected by sliding or clicking the tab button

Learn more about [Events](/overview/event).

## Keys

The following *Keys* are processed by the Tabview:
- **LV_KEY_RIGHT/LEFT** Select a tab
- **LV_KEY_ENTER** Change to the selected tab

Learn more about [Keys](/overview/indev).


## Example

```eval_rst

.. include:: /lv_examples/src/lv_ex_tabview/index.rst

```

## API 

```eval_rst

.. doxygenfile:: lv_tabview.h
  :project: lvgl
        
```

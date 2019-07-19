```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/hu/object-types/cb.md
```
# Check box (lv_cb)
## Overview

The Check Box objects are built from a [Button](/object-types/btn) background which contains an also Button *bullet* and a [Label](/object-types/label) to realize a classical check box. 

### Text
The text can be modified by the `lv_cb_set_text(cb, "New text")` function. It will dynamically allocate the text. 

To set a static text use `lv_cb_set_static_text(cb, txt)`. This way only a pointer of `txt` will be stored it shouldn't be deallocated while the checkbox exists. 

### Check/Uncheck
You can manually check / un-check the Check box  via `lv_cb_set_checked(cb, true/false)`.

### Inactive
To make the Check box inactive use `lv_cb_set_inactive(cb, true)`.

## Styles

The Check box styles can be modified with `lv_cb_set_style(cb, LV_CB_STYLE_..., &style)`.

- **LV_CB_STYLE_BG** Background style. Uses all `style.body` properties. The label's style comes from  `style.text`. Default: `lv_style_transp`
- **LV_CB_STYLE_BOX_REL** Style of the released box. Uses the `style.body` properties. Default: `lv_style_btn_rel`
- **LV_CB_STYLE_BOX_PR** Style of the pressed box. Uses the `style.body` properties. Default: `lv_style_btn_pr`
- **LV_CB_STYLE_BOX_TGL_REL** Style of the checked released box. Uses the `style.body` properties. Default: `lv_style_btn_tgl_rel`
- **LV_CB_STYLE_BOX_TGL_PR** Style of the checked released box. Uses the `style.body` properties. Default: `lv_style_btn_tgl_pr`
- **LV_CB_STYLE_BOX_INA** Style of the inactive box. Uses the `style.body` properties. Default: `lv_style_btn_ina`


## Events
Besides the [Generic events](/overview/event.html#generic-events) the following [Special events](/overview/event.html#special-events) are sent by the Check boxes:
 - **LV_EVENT_VALUE_CHANGED** sent when the Check box is toggled.

Note that the generic input device related events (like `LV_EVENT_PRESSED`) are sent in the inactive state too. You need to check the state with `lv_cb_is_inactive(cb)` to ignore the events from inactive Check boxes.
 
Learn more about [Events](/overview/event).


## Keys
The following *Keys* are processed by the Buttons:
- **LV_KEY_RIGHT/UP** Go to toggled state if toggling is enabled
- **LV_KEY_LEFT/DOWN** Go to non-toggled state if toggling is  enabled

Note that, as usual, the state of `LV_KEY_ENTER` is translated to `LV_EVENT_PRESSED/PRESSING/RELEASED` etc.

Learn more about [Keys](/overview/indev).


## Example

```eval_rst

.. include:: /lv_examples/src/lv_ex_cb/index.rst

```

## API 

```eval_rst

.. doxygenfile:: lv_cb.h
  :project: lvgl
        
```

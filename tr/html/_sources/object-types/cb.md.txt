```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/tr/object-types/cb.md
```
# Checkbox (lv_cb)
## Giriş

The Checkbox objects are built from a [Button](/object-types/btn) background which contains an also Button *bullet* and a [Label](/object-types/label) to realize a classical checkbox.

### Metin
The text can be modified by the `lv_cb_set_text(cb, "New text")` function. It will dynamically allocate the text.

To set a static text, use `lv_cb_set_static_text(cb, txt)`. This way, only a pointer of `txt` will be stored and it shouldn't be deallocated while the checkbox exists.

### Onay/Onayı Kaldır
You can manually check / un-check the Checkbox  via `lv_cb_set_checked(cb, true/false)`. Setting `true` will check the checkbox and `false` will un-check the checkbox.

### Pasif
To make the Checkbox inactive, use `lv_cb_set_inactive(cb, true)`.

## Biçim

The Checkbox styles can be modified with `lv_cb_set_style(cb, LV_CB_STYLE_..., &style)`.

- **LV_CB_STYLE_BG** - Background style. Uses all `style.body` properties. The label's style comes from  `style.text`. Default: `lv_style_transp`
- **LV_CB_STYLE_BOX_REL** - Style of the released box. Uses the `style.body` properties. Default: `lv_style_btn_rel`
- **LV_CB_STYLE_BOX_PR** - Style of the pressed box. Uses the `style.body` properties. Default: `lv_style_btn_pr`
- **LV_CB_STYLE_BOX_TGL_REL** - Style of the checked released box. Uses the `style.body` properties. Default: `lv_style_btn_tgl_rel`
- **LV_CB_STYLE_BOX_TGL_PR** - Style of the checked released box. Uses the `style.body` properties. Default: `lv_style_btn_tgl_pr`
- **LV_CB_STYLE_BOX_INA** - Style of the inactive box. Uses the `style.body` properties. Default: `lv_style_btn_ina`


## Aksiyonlar
Besides the [Generic events](/overview/event.html#generic-events) the following [Special events](/overview/event.html#special-events) are sent by the Checkboxes:
 - **LV_EVENT_VALUE_CHANGED** - sent when the checkbox is toggled.

Note that, the generic input device-related events (like `LV_EVENT_PRESSED`) are sent in the inactive state too. You need to check the state with `lv_cb_is_inactive(cb)` to ignore the events from inactive Checkboxes.

[Events](/overview/event) hakkında daha fazlasını öğrenin.


## Keys
The following *Keys* are processed by the 'Buttons':
- **LV_KEY_RIGHT/UP** - Go to toggled state if toggling is enabled
- **LV_KEY_LEFT/DOWN** - Go to non-toggled state if toggling is  enabled

Her zaman olduğu gibi `LV_KEY_ENTER`  `LV_EVENT_PRESSED/PRESSING/RELEASED` vs olarak çevrilir.

[Keys](/overview/indev) hakkında daha fazlasını öğrenin.


## Örnek

```eval_rst

.. include:: /lv_examples/src/lv_ex_cb/index.rst

```

## API

```eval_rst

.. doxygenfile:: lv_cb.h
  :project: lvgl

```

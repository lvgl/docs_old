```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/tr/object-types/cb.md
```
# Onay kutusu (lv_cb)
## Giriş

Onay kutusu nesneleri bir Button *imi* ve klasik bir onay kutusu gerçekleştirmek için bir [Label](/object-types/label) içeren bir [Button](/object-types/btn) arka planından oluşturulmuştur   . 

### Metin
`lv_cb_set_text(cb, "New text")` fonksiyonu tarafından değiştirilebilir. Bu fonksiyon dinamik olarak metin tahsis eder. 

Statik metin ayarlamak  için `lv_cb_set_static_text(cb, txt)` kullanın. Bu yolla sadece `txt` nin göstericisi saklanılacak, onay kutusu var iken yer tahsil edilmemelidir. 

### Onay/Onayı Kaldır
`lv_cb_set_checked(cb, true/false)` ile manuel olarak  onay kutusunu onaylayabilirsiniz/ onayı kaldırabilirsiniz.

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

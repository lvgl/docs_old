```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/tr/object-types/btn.md
```
# Buton (lv_btn)

## Giriş

Buttons are simple rectangle-like objects, but they change their style and state when they are pressed or released.

### Durumlar
Butonlar 5 olası durumdan birinde olabilir
- **LV_BTN_STATE_REL** - Released state
- **LV_BTN_STATE_PR** - Pressed state
- **LV_BTN_STATE_TGL_REL** - Toggled released state
- **LV_BTN_STATE_TGL_PR** - Toggled pressed state
- **LV_BTN_STATE_INA** - Inactive state

The state from `..._REL` to `..._PR` will be changed automatically when the button is pressed or released.

Butonun durumu el ile `lv_btn_set_state(btn, LV_BTN_STATE_TGL_REL)` fonksiyonu ile değiştirilebilir.

### Değiştir
You can configure the buttons as *toggle button* with `lv_btn_set_toggle(btn, true)`. In this case, on release, the button goes to *toggled released* state.

### Yerleşim planı ve Uyum
Similarly to [Containers](/object-types/cont), buttons also have layout and fit attributes.
- `lv_btn_set_layout(btn, LV_LAYOUT_...) `set a layout. The default is `LV_LAYOUT_CENTER`.
So, if you add a label, then it will be automatically aligned to the middle and can't be moved with `lv_obj_set_pos()`.
You can disable the layout with `lv_btn_set_layout(btn, LV_LAYOUT_OFF)`.
- `lv_btn_set_fit/fit2/fit4(btn, LV_FIT_..)` fonksiyonu butonun genişlik ve/veya yüksekliğini otomatik olarak bağlı bulunduğu üst birimi veya kendi alt birimleri için aktifleştirir ve şekil uyumunu sağlar.

### Mürekkep Etkisi
You can enable a special animation on buttons: when a button is pressed, the pressed state will be drawn in a growing circle starting from the point of pressing. It's similar in appearance and functionality to the Material Design ripple effect.

Another way to think about it is like an ink droplet dropped into water. When the button is released, the released state will be reverted by fading. It's like the ink is fully mixed with a lot of water and becomes invisible.

To control this animation, use the following functions:
- `lv_btn_set_ink_in_time(btn, time_ms)` - time of circle growing.
- `lv_btn_set_ink_wait_time(btn, time_ms)` - minim time to keep the fully covering (pressed) state.
- `lv_btn_set_ink_out_time(btn, time_ms)` - time fade back to releases state.

Bu özelliğin `LV_BTN_INK_EFFECT  1` in *lv_conf.h* ile aktifleştirilmesi gerekir.


## Biçimler

A button can have 5 independent styles for the 5 states. You can set them via: `lv_btn_set_style(btn, LV_BTN_STYLE_..., &style)`. The styles use the `style.body` properties.

- **LV_BTN_STYLE_REL** - style of the released state. Default: `lv_style_btn_rel`.
- **LV_BTN_STYLE_PR** - style of the pressed state. Default: `lv_style_btn_pr`.
- **LV_BTN_STYLE_TGL_REL** - style of the toggled released state. Default: `lv_style_btn_tgl_rel`.
- **LV_BTN_STYLE_TGL_PR** - style of the toggled pressed state. Default: `lv_style_btn_tgl_pr`.
- **LV_BTN_STYLE_INA** - style of the inactive state. Default: `lv_style_btn_ina`.

When you create a label on a button, it's a good practice to set the button's `style.text` properties too. Because labels have `style = NULL` by default, they inherit the parent's (button) style.
Hence you don't need to create a new style for the label.


## Aksiyonlar
Buton tarafından [Generic events](/overview/event.html#generic-events) yanında  [Special events](/overview/event.html#special-events) gönderilir:
 - **LV_EVENT_VALUE_CHANGED** - sent when the button is toggled.

Note that, the generic input device-related events (like `LV_EVENT_PRESSED`) are sent in the inactive state too. You need to check the state with `lv_btn_get_state(btn)` to ignore the events from inactive buttons.

[Events](/overview/event) hakkında daha fazlasını öğrenin.

## Anahtarlar
Aşağıdaki *Keys* butonlar tarafından işlenmiştir:
- **LV_KEY_RIGHT/UP** - Go to toggled state if toggling is enabled.
- **LV_KEY_LEFT/DOWN** - Go to non-toggled state if toggling is enabled.

Note that, by default, the state of `LV_KEY_ENTER` is translated to `LV_EVENT_PRESSED/PRESSING/RELEASED` etc.

[Keys](/overview/indev) hakkında daha fazlasını öğrenin.

## Örnek
```eval_rst

.. include:: /lv_examples/src/lv_ex_btn/index.rst

```

## API

```eval_rst

.. doxygenfile:: lv_btn.h
  :project: lvgl

```

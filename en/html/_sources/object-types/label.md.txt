```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/en/object-types/label.md
```
# Label (lv_label)

## Overview
A label is the basic object type that is used to display text. 

### Set text
You can set the text on a label at runtime with `lv_label_set_text(label, "New text")`. It will allocate a buffer dynamically, and the provided string will be copied into that buffer. Therefore, you don't need to keep the text you pass to `lv_label_set_text` in scope after that function returns.

With `lv_label_set_text_fmt(label, "Value: %d", 15)` **printf formatting** can used to set the text.

Labels are able to show text from a **static character buffer** which is NUL-terminated. To do so, use `lv_label_set_static_text(label, char_array)`. In this case, the text is not stored in the dynamic memory and the given buffer is used directly instead. This means that the array can't be a local variable which goes out of scope when the function exits. Constant strings are safe to use with `lv_label_set_static_text` (except when used with `LV_LABEL_LONG_DOT`, as it modifies the buffer in-place), as they are stored in RO memory, which is always accessible.

You can also use a **raw array** as label text. The array doesn't have to be `\0` terminated. In this case, the text will be saved to the dynamic memory like with `lv_label_set_text`. To set a raw character array, use the `lv_label_set_array_text(label, char_array, size)` function.


### Line break

Line breaks are handled automatically by the label object. You can use `\n` to make a line break. For example: `"line1\nline2\n\nline4"`

### Long modes
By default, the width of the label object automatically expands to the text size. Otherwise, the text can be manipulated according to several long mode policies:

* **LV_LABEL_LONG_EXPAND** - Expand the object size to the text size (Default)
* **LV_LABEL_LONG_BREAK** - Keep the object width, break (wrap) the too long lines and expand the object height
* **LV_LABEL_LONG_DOT** - Keep the object size, break the text and write dots in the last line (**not supported when using `lv_label_set_static_text`**)
* **LV_LABEL_LONG_SROLL** - Keep the size and scroll the label back and forth
* **LV_LABEL_LONG_SROLL_CIRC** - Keep the size and scroll the label circularly
* **LV_LABEL_LONG_CROP** - Keep the size and crop the text out of it

You can specify the long mode with `lv_label_set_long_mode(label, LV_LABEL_LONG_...)`

It's important to note that, when a label is created and its text is set, the label's size already expanded to the text size. 
In addition with the default `LV_LABEL_LONG_EXPAND`, *long mode* `lv_obj_set_width/height/size()` has no effect.
So you need to change the *long mode* first and then set the size with  `lv_obj_set_width/height/size()`.

Another important note is that **`LV_LABEL_LONG_DOT` manipulates the text buffer in-place** in order to add/remove the dots. When `lv_label_set_text` or `lv_label_set_array_text` are used, a separate buffer is allocated and this implementation detail is unnoticed. This is not the case with `lv_label_set_static_text`! **The buffer you pass to `lv_label_set_static_text` must be writable if you plan to use `LV_LABEL_LONG_DOT`.**

### Text align

The label's text can be aligned to the left, right or middle with `lv_label_set_align(label, LV_LABEL_ALIGN_LEFT/RIGHT/CENTER)`.

Vertical alignment is not supported by the label itself; you should place the label inside a larger container and align the whole label object instead.

### Draw background
You can enable to draw a background for the label with `lv_label_set_body_draw(label, draw)`

The background will be larger in every direction with `body.padding.top/bottom/left/right` values. 
However, the background is drawn only "virtually" and doesn't make the label's logical coordinates any larger. 
Therefore when the label is positioned, the label's coordinates will be taken into account and not background's.

### Text recolor
In the text, you can use commands to recolor parts of the text. For example: `"Write a #ff0000 red# word"`. 
This feature can be enabled individually for each label by `lv_label_set_recolor()` function. 

Note that, recoloring work only in a single line. Therefore, `\n` should not use in a recolored text or it should be wrapped by `LV_LABEL_LONG_BREAK` else, the text in the new line won't be recolored.

### Very long texts

LittlevGL can efficiently handle very long (> 40k characters) by saving some extra data (~12 bytes) to speed up drawing. To enable this feature, set `LV_LABEL_LONG_TXT_HINT   1` in *lv_conf.h*.

### Symbols
The labels can display symbols alongside letters (or on their own). Read the [Font](/overview/font) section to learn more about the symbols.

## Styles
The Label uses one style which can be set by `lv_label_set_style(label, LV_LABEL_STYLE_MAIN, &style)`. From the style the following properties are used:
* All properties from `style.text`
* For background drawing `style.body` properties. `padding` will increase the size only visually, the real object's size won't be changed.

The labels' default style is `NULL` so they inherit the parent's style. It's useful because it allows the parent to set an appropriate text style for any child labels.

## Events
Only the [Generic events](/overview/event.html#generic-events) are sent by the object type.

Learn more about [Events](/overview/event).

## Keys
No *Keys* are processed by the object type.

Learn more about [Keys](/overview/indev).

## Example

```eval_rst

.. include:: /lv_examples/src/lv_ex_label/index.rst

```

## API 

```eval_rst

.. doxygenfile:: lv_label.h
  :project: lvgl
        
```


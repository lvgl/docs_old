```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/fr/object-types/label.md
```
# Etiquette (lv_label)

## Vue d’ensemble
A label is the basic object type that is used to display text. 

### Définir le texte
You can set the text on a label at runtime with `lv_label_set_text(label, "New text")`. It will allocate a buffer dynamically, and the provided string will be copied into that buffer. Therefore, you don't need to keep the text you pass to `lv_label_set_text` in scope after that function returns.

With `lv_label_set_text_fmt(label, "Value: %d", 15)` **printf formatting** can used to set the text.

Labels are able to show text from a **static character buffer** which is NUL-terminated. To do so, use `lv_label_set_static_text(label, char_array)`. In this case, the text is not stored in the dynamic memory and the given buffer is used directly instead. This means that the array can't be a local variable which goes out of scope when the function exits. Constant strings are safe to use with `lv_label_set_static_text` (except when used with `LV_LABEL_LONG_DOTS`, as it modifies the buffer in-place), as they are stored in RO memory, which is always accessible.

You can also use a **raw array** as label text. The array doesn't have to be `\0` terminated. In this case, the text will be saved to the dynamic memory like with `lv_label_set_text`. To set a raw character array, use the `lv_label_set_array_text(label, char_array, size)` function.


### Saut de ligne

Line breaks are handled automatically by the label object. You can use `\n` to make a line break. For example: `"line1\nline2\n\nline4"`

### Modes d'adaptation au texte
By default, the width of the label object automatically expands to the text size. Otherwise, the text can be manipulated according to several long mode policies:

* **LV_LABEL_LONG_EXPAND** - Expand the object size to the text size (Default)
* **LV_LABEL_LONG_BREAK** - Keep the object width, break (wrap) the too long lines and expand the object height
* **LV_LABEL_LONG_DOTS** - Keep the object size, break the text and write dots in the last line (**not supported when using `lv_label_set_static_text`**)
* **LV_LABEL_LONG_SROLL** - Keep the size and scroll the label back and forth
* **LV_LABEL_LONG_SROLL_CIRC** - Keep the size and scroll the label circularly
* **LV_LABEL_LONG_CROP** - Keep the size and crop the text out of it

You can specify the long mode with `lv_label_set_long_mode(label, LV_LABEL_LONG_...)`

It's important to note that, when a label is created and its text is set, the label's size already expanded to the text size. 
In addition with the default `LV_LABEL_LONG_EXPAND`, *long mode* `lv_obj_set_width/height/size()` has no effect.
So you need to change the *long mode* first and then set the size with  `lv_obj_set_width/height/size()`.

Another important note is that **`LV_LABEL_LONG_DOTS` manipulates the text buffer in-place** in order to add/remove the dots. When `lv_label_set_text` or `lv_label_set_array_text` are used, a separate buffer is allocated and this implementation detail is unnoticed. This is not the case with `lv_label_set_static_text`! **The buffer you pass to `lv_label_set_static_text` must be writable if you plan to use `LV_LABEL_LONG_DOTS`.**

### Alignement du texte

The label's text can be aligned to the left, right or middle with `lv_label_set_align(label, LV_LABEL_ALIGN_LEFT/RIGHT/CENTER)`.

Vertical alignment is not supported by the label itself; you should place the label inside a larger container and align the whole label object instead.

### Dessin d'arrière-plan
Vous pouvez activer le dessin de l’arrière-plan de l’étiquette avec `lv_label_set_body_draw(label, draw)`

L’arrière-plan sera plus grand dans toutes les directions  de la valeur de `body.padding.top/bottom/left/right`.
However, the background is drawn only "virtually" and doesn't make the label's logical coordinates any larger. 
Therefore when the label is positioned, the label's coordinates will be taken into account and not background's.

### Coloration du texte
In the text, you can use commands to recolor parts of the text. For example: `"Write a #ff0000 red# word"`. 
Cette fonctionnalité peut être activée individuellement pour chaque étiquette à l’aide de la fonction `lv_label_set_recolor()`.

Note that, recoloring work only in a single line. Therefore, `\n` should not use in a recolored text or it should be wrapped by `LV_LABEL_LONG_BREAK` else, the text in the new line won't be recolored.

### Très long textes

LittlevGL can efficiently handle very long (> 40k characters) by saving some extra data (~12 bytes) to speed up drawing. To enable this feature, set `LV_LABEL_LONG_TXT_HINT   1` in *lv_conf.h*.

### Symboles
The labels can display symbols alongside letters (or on their own). Read the [Font](/overview/font) section to learn more about the symbols.

## Styles
The Label uses one style which can be set by `lv_label_set_style(label, LV_LABEL_STYLE_MAIN, &style)`. From the style the following properties are used:
* All properties from `style.text`
* For background drawing `style.body` properties. `padding` will increase the size only visually, the real object's size won't be changed.

The labels' default style is `NULL` so they inherit the parent's style. It's useful because it allows the parent to set an appropriate text style for any child labels.

## Evénements
Seuls les [événements génériques](/overview/event.html#generic-events) sont envoyés par ce type d'objet.

Apprenez-en plus sur les [événements](/overview/event).

## Touches
Aucune *touche* n'est traitée par ce type d'objet.

Apprenez-en plus sur les [touches](/overview/indev).

## Exemple

```eval_rst

.. include:: /lv_examples/src/lv_ex_label/index.rst

```

## API 

```eval_rst

.. doxygenfile:: lv_label.h
  :project: lvgl
        
```


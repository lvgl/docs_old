_Written for v5.1_

## Overview
The Labels are the basic objects to **display text**. There is no limitation in the text size because it's stored dynamically. You can modify the text in runtime at any time with lv_label_set_text().

You can use `\n` to make line break. For example: `"line1\nline2\n\nline4"`

The size of the label object can be automatically expanded to the text size or the text can be manipulated according to several **long mode policies**:

* LV_LABEL_LONG_EXPAND: Expand the object size to the text size (Default)
* LV_LABEL_LONG_BREAK: Keep the object width, break (wrap) the too long lines and expand the object height
* LV_LABEL_LONG_DOTS: Keep the object size, break the text and write dots in the last line
* LV_LABEL_LONG_SCROLL: Expand the object size and scroll the text on the parent (move the label object)
* LV_LABEL_LONG_ROLL: Keep the size and roll just the text (not the object)

You can specify the long mode with: `lv_label_set_long_mode(label, long_mode)`

It's important to note that if you change the `LONG_MODE` the size of the label obejct is already expanded to the text's size. 
So you need to set the label's size with `lv_obj_set_size()` or `lv_obj_set_width()` after changing long mode.

Labels are able to show text from a **static array**. Use: `lv_label_set_static_text(label, char_array)`. In this case, the text is not stored in the dynamic memory but the given array is used instead. Keep in my the array can't be a local variable which destroys when the function exits.

You can also use a **raw character array** as label text. The array doesn't have to be `\0` terminated. In this case, the text will be saved to the dynamic memory. To set a raw character array use the `lv_label_set_array_text(label, char_array)` function.

The label's **text can be aligned** to the left, right or middle with `lv_label_set_align(label, LV_LABEL_ALIGN_LEFT/RIGHT/CENTER)`

You can enable to **draw a background** for the label with `lv_label_set_body_draw(label, draw)`

In the text, you can use commands to **re-color parts of the text**. For example: `"Write a #ff0000 red# word"`. This feature can be enabled individually for each label by `lv_label_set_recolor()` function.

The labels can display symbols besides letters. Learn more about symbols [here](/Fonts).

The labels' **default style** is `NULL` so they inherit the parent's style.

## Style usage
* Use all properties from `style.text`
* For background drawing `style.body properties` are used

## Notes
The label's **click enable attribute is disabled** by default. You can enable clicking with `lv_obj_set_click(label, true)`

## Example
![Example of Label in LittlevGL Graphics Library ](http://docs.littlevgl.com/img/label-lv_label.png)

```c
/*Create label on the screen. By default it will inherit the style of the screen*/
lv_obj_t * title = lv_label_create(lv_scr_act(), NULL);
lv_label_set_text(title, "Title Label");
lv_obj_align(title, NULL, LV_ALIGN_IN_TOP_MID, 0, 20);  /*Align to the top*/

/*Create anew style*/
static lv_style_t style_txt;
lv_style_copy(&style_txt, &lv_style_plain);
style_txt.text.font = &lv_font_dejavu_40;
style_txt.text.letter_space = 2;
style_txt.text.line_space = 1;
style_txt.text.color = LV_COLOR_HEX(0x606060);

/*Create a new label*/
lv_obj_t * txt = lv_label_create(lv_scr_act(), NULL);
lv_obj_set_style(txt, &style_txt);                    /*Set the created style*/
lv_label_set_long_mode(txt, LV_LABEL_LONG_BREAK);     /*Break the long lines*/
lv_label_set_recolor(txt, true);                      /*Enable re-coloring by commands in the text*/
lv_label_set_align(txt, LV_LABEL_ALIGN_CENTER);       /*Center aligned lines*/
lv_label_set_text(txt, "Align lines to the middle\n\n"
                       "#000080 Re-color# #0000ff words of# #6666ff the text#\n\n"
                       "If a line become too long it can be automatically broken into multiple lines");
lv_obj_set_width(txt, 300);                           /*Set a width*/
lv_obj_align(txt, NULL, LV_ALIGN_CENTER, 0, 20);      /*Align to center*/
```

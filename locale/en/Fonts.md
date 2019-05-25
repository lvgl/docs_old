_Written for v5.1_

In LittlevGL fonts are bitmaps and other descriptors to store the images of the letters (glyph) and some additional information. A font is stored in a **lv_font_t** variable and can be set it in style's _text.font_ field. 

The fonts have a **bpp (Bit-Per-Pixel)** property. It shows how much bit is used to describe a pixel in the font. The value stored for a pixel determines the pixel's opacity. This way the image of the letters (especially on the edges) can be smooth and even. The possible bpp values are 1, 2, 4 and 8 (higher value means better quality). The bpp also affects the required memory size to store the font. E.g. bpp = 4 makes the font's memory size 4 times greater compared to bpp = 1.  

#### Built-in fonts

There are several built-in fonts which can be enabled in lv_conf.h by _USE_LV_FONT_..._ defines. There are built-in fonts in **different sizes**:

- 10 px
- 20 px
- 30 px
- 40 px

You can enable the fonts with 1, 2, 4 or 8 values to set its bpp (e.g. `#define USE_LV_FONT_DEJAVU_20 4` in `lv_conf.h`). 

The built-in fonts exist with **multiply character-sets** in each size:

- ASCII (Unicode 32..126)
- Latin supplement (Unicode 160..255)
- Cyrillic (Unicode 1024..1279)

The built-in fonts use the _Dejavu_ font.

The built-in fonts are **global variables** with names like: 

- `lv_font_dejavu_20` (20 px ASCII font)
- `lv_font_dejavu_20_latin_sup` (20 px Latin supplement font)
- `lv_font_dejavu_20_cyrillic` (20 px Cyrillic font)

#### Unicode support

The LittlevGL supports Unicode letter from **UTF-8** coded characters. You need to configure your editor to save your code/text as UTF-8 (usually this the default) and enable _LV_TXT_UTF8_ in lv_conf.h. Without enabled _LV_TXT_UTF8_ only ASCII fonts and symbols can be used (see the symbols below)

After it the texts will be decoded to determine the Unicode values. To display the letters your font needs to contain the image (glyph) of the characters. 

You can assign more fonts to create a **larger character-set**. To do this choose a base font (typically the ASCII font) and add the extensions to it: `lv_font_add(child, parent)`. Only fonts with the same height can be assigned.

The built-in fonts are already added to the same sized ASCII font. For example if _USE_LV_FONT_DEJAVU_20_ and _USE_LV_FONT_DEJAVU_20_LATIN_SUP_ are enabled in `lv_conf.h` then the _"abcÁÖÜ"_ text can be rendered when using _lv_font_dejavu_20_.

#### Symbol fonts

The symbol fonts are special fonts which contain symbols instead of letters. There are **built-in symbol fonts** as well and they are also assigned to the ASCII font with the same size. In a text, a symbol can be referenced like _SYMBOL_LEFT_, _SYMBOL_RIGHT_ etc. You can mix these symbol names with strings: 

```c
lv_label_set_text(label1,"Right "SYMBOL_RIGHT);
```

The symbols can be used without UTF-8 support as well. (_LV_TXT_UTF8 0_)

The list below shows the existing symbols:

![Basic symbols](https://littlevgl.com/docs/symbols.png)

#### Add new font

If you want to **add new fonts to the library** you can use the [Online Font Converter Tool](https://littlevgl.com/ttf-font-to-c-array). It can create a C array from a TTF file which can be copied copy to your project. You can specify the height, the range of characters and the bpp. Optionally you can enumerate the characters to include only them into the final font. To use the generated font declare it with _LV_FONT_DECLARE(my_font_name)_. After that, the font can be used as the built-in fonts.

#### Font example

![Fonts example](https://littlevgl.com/docs/example-fonts.png)

```c
/*Create a new style for the label*/
static lv_style_t style;
lv_style_copy(&style, &lv_style_plain);
style.text.color = LV_COLOR_BLUE;
style.text.font = &lv_font_dejavu_40;   /*Unicode and symbol fonts already assigned by the library*/

lv_obj_t *label;

/*Use ASCII and Unicode letters*/
label = lv_label_create(lv_scr_act(), NULL);
lv_obj_set_pos(label, 20, 20);
lv_label_set_style(label, &style);
lv_label_set_text(label, "aeuois\n"
                         "äéüöíß");

/*Mix text and symbols*/
label = lv_label_create(lv_scr_act(), NULL);
lv_obj_set_pos(label, 20, 100);
lv_label_set_style(label, &style);
lv_label_set_text(label, "Right "SYMBOL_RIGHT);
```

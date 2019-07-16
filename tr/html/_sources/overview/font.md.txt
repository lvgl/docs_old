```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/tr/overview/font.md
```
# Fonts

In LittlevGL fonts are collections of bitmaps and other information required to render the images of the letters (glyph). A font is stored in a **lv_font_t** variable and can be set it in style's *text.font* field. For example:
```c
my_style.text.font = &lv_font_roboto_28;  /*Set a larger font*/
```

The fonts have a **bpp (Bit-Per-Pixel)** property. It shows how many bits are used to describe a pixel in the font. The value stored for a pixel determines the pixel's opacity. 
This way with higher *bpp* the edges of the letter can be smoother. The possible *bpp* values are 1, 2, 4 and 8 (higher value means better quality). 

The *bpp* also affects the required memory size to store the font. E.g. *bpp = 4* makes the font ~4 times greater compared to *bpp = 1*.  

## Unicode support

LittlevGL supports **UTF-8** encoded Unicode characters. 
You need to configure your editor to save your code/text as UTF-8 (usually this the default) and be sure `LV_TXT_ENC` is set to `LV_TXT_ENC_UTF8` in *lv_conf.h*. (This is the default value)

To test it try
```c
lv_obj_t * label1 = lv_label_create(lv_scr_act(), NULL);
lv_label_set_text(label1, LV_SYMBOL_OK);
```

If all works well a ✓ character should be displayed. 

## Built-in fonts

There are several built-in fonts in different sizes which can be enabled in lv_conf.h by *LV_FONT_...* defines: 
- `LV_FONT_ROBOTO_12` 12 px
- `LV_FONT_ROBOTO_16` 16 px
- `LV_FONT_ROBOTO_22` 22 px
- `LV_FONT_ROBOTO_28` 28 px

The built-in fonts are **global variables** with names like `lv_font_roboto_16` for 16 px hight font. To use them in a style just add a pointer to a font variable like shown above.

The built-in fonts have *bpp = 4*, contains the ASCII characters and uses the [Roboto](https://fonts.google.com/specimen/Roboto) font.

In addition to the ASCII rangle, the following symbols are also added to the built-in fonts from the [FontAwesome](https://fontawesome.com/) font.

![](/misc/symbols.png "Built-in Symbols in LittlevGL")

The symbols can be used as:
```c
lv_label_set_text(my_label, LV_SYMBOL_OK);
```

Or with together with strings:
```c
lv_label_set_text(my_label, LV_SYMBOL_OK "Apply");
```

Or more symbols together:
```c
lv_label_set_text(my_label, LV_SYMBOL_OK LV_SYMBOL_WIFI LV_SYMBOL_PLAY);
```

## Add new font

There are several ways to add a new font to your project:
1. The most simple way is to use the [Online font converter](https://littlevgl.com/font_conv_new). Just set the parameters, click the *Convert* button, copy the font to your project and use it.
2. Use the [Offline font converter](https://github.com/littlevgl/lv_font_conv). (Requires Node.js to be installed)
3. If you want to create something like the built-in fonts (Roboto font and symbols) but in different size and/or ranges you can use the `built_in_font_gen.py` script in `lvgl/scripts/built_in_font` folder. 
(It requires Python and `lv_font_conv` to be installed) 

To declare the font in a file use `LV_FONT_DECLARE(my_font_name)`.

To make to font globally available add them to `LV_FONT_CUSTOM_DECLARE` in *lv_conf.h*.

## Add new symbols
The built-in symbols are created from [FontAwesome](https://fontawesome.com/) font. To add new symbols from the FontAwesome font do the following steps:
1. Search symbol on [https://fontawesome.com](https://fontawesome.com). For example the [USB symbol](https://fontawesome.com)
2. Open the [Online font converter](https://littlevgl.com/font_conv_new) add [FontAwesome.ttf](https://littlevgl.com/tools/FontAwesome.ttf) and add the Unicode ID of the symbol to the range field. E.g.` 0xf287` for the USB symbol.
More symbols can be enumerated with `,`.
3. Convert the font and copy it to your project.
4. Convert the Unicode value to UTF8. You can do it e.g.on [this site](http://www.ltg.ed.ac.uk/~richard/utf-8.cgi?input=f287&mode=hex). For `0xf287` the *Hex UTF-8 bytes* are `EF 8A 87`. 
5. Create a `define` from the UTF8 values: `#define MY_USB_SYMBOL "\xEF\x8A\x87"`
6. Use the symbol as the built-in symbols. `lv_label_set_text(label, MY_USB_SYMBOL)`

## Add a new font engine

LittlevGL's font interface is designed to be very flexible. 
You don't need to use LittlevGL's internal font engine but you can add your own. 
For example use [FreeType](https://www.freetype.org/) to real-time render glyphs from TTF fonts or use an external flash to store the font's bitmap and read them when the library need them.

To do this a custom `lv_font_t` variable needs to be created:
```c
/*Describe the properties of a font*/
lv_font_t my_font;
my_font.get_glyph_dsc = my_get_glyph_dsc_cb;        /*Set a callback to get info about gylphs*/
my_font.get_glyph_bitmap = my_get_glyph_bitmap_cb;  /*Set a callback to get bitmap of a glyp*/
my_font.line_height = height;                       /*The real line height where any text fits*/
my_font.base_line = base_line;                      /*Base line measured from the top of line_height*/
my_font.dsc = something_required;                   /*Store any implementation specific data here*/
my_font.user_data = user_data;                      /*Optionally some extra user data*/

...

/* Get info about glyph of `unicode_letter` in `font` font. 
 * Store the result in `dsc_out`.
 * The next letter (`unicode_letter_next`) might be used to calculate the width required by this glyph (kerning)
 */
bool my_get_glyph_dsc_cb(const lv_font_t * font, lv_font_glyph_dsc_t * dsc_out, uint32_t unicode_letter, uint32_t unicode_letter_next)
{
    /*Your code here*/
  
    /* Store the result.
     * For example ... 
     */
    dsc_out->adv_w = 12;        /*Horizontal space required by the glyph in [px]*/
    dsc_out->box_h = 8;         /*Height of the bitmap in [px]*/
    dsc_out->box_w = 6;         /*Width of the bitmap in [px]*/
    dsc_out->ofs_x = 0;         /*X offset of the bitmap in [pf]*/
    dsc_out->ofs_y = 3;         /*Y offset of the bitmap measured from the as line*/
    dsc_out->bpp   = 2;         /*Bit per pixel: 1/2/4/8*/
    
    return true;                /*true: glyph found; false: glyph was not found*/
}


/* Get the bitmap of `unicode_letter` from `font`. */
const uint8_t * my_get_glyph_bitmap_cb(const lv_font_t * font, uint32_t unicode_letter)
{
    /* Your code here */
    
    /* The bitmap should be a continuous bitstream where 
     * each pixel is represented by `bpp` bits */ 
    
    return bitmap;    /*Or NULL if not found*/
}
```
 



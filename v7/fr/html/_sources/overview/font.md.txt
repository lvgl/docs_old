```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/fr/overview/font.md
```
# Polices

In LittlevGL fonts are collections of bitmaps and other information required to render the images of the letters (glyph). A font is stored in a **lv_font_t** variable and can be set in style's *text.font* field. For example:
```c
my_style.text.font = &lv_font_roboto_28;  /* Définit une police plus grande */
```

The fonts have a **bpp (bits per pixel)** property. It shows how many bits are used to describe a pixel in the font. The value stored for a pixel determines the pixel's opacity.
This way, with higher *bpp*, the edges of the letter can be smoother. The possible *bpp* values are 1, 2, 4 and 8 (higher value means better quality).

The *bpp* also affects the required memory size to store the font. For example, *bpp = 4* makes the font nearly 4 times greater compared to *bpp = 1*.  

## Support Unicode

LittlevGL supports **UTF-8** encoded Unicode characters.
You need to configure your editor to save your code/text as UTF-8 (usually this the default) and be sure that, `LV_TXT_ENC` is set to `LV_TXT_ENC_UTF8` in *lv_conf.h*. (This is the default value)

Pour le vérifier, essayez
```c
lv_obj_t * label1 = lv_label_create(lv_scr_act(), NULL);
lv_label_set_text(label1, LV_SYMBOL_OK);
```

If all works well, a ✓ character should be displayed.

## Polices intégrées

There are several built-in fonts in different sizes, which can be enabled in lv_conf.h by *LV_FONT_...* defines:
- `LV_FONT_ROBOTO_12` 12 px
- `LV_FONT_ROBOTO_16` 16 px
- `LV_FONT_ROBOTO_22` 22 px
- `LV_FONT_ROBOTO_28` 28 px

The built-in fonts are **global variables** with names like `lv_font_roboto_16` for 16 px hight font. To use them in a style, just add a pointer to a font variable like shown above.

Les polices intégrées ont *bpp = 4*, contiennent les caractères ASCII et utilisent la police [Roboto](https://fonts.google.com/specimen/Roboto).

In addition to the ASCII range, the following symbols are also added to the built-in fonts from the [FontAwesome](https://fontawesome.com/) font.

![](/misc/symbols.png "Built-in Symbols in LittlevGL")

Les symboles peuvent être utilisés ainsi :
```c
lv_label_set_text(my_label, LV_SYMBOL_OK);
```

Ou avec des chaînes :
```c
lv_label_set_text(my_label, LV_SYMBOL_OK "Apply");
```

Ou plusieurs symboles ensemble :
```c
lv_label_set_text(my_label, LV_SYMBOL_OK LV_SYMBOL_WIFI LV_SYMBOL_PLAY);
```

## Special features

### Bidirectional support
Most of the languages use Left-to-Right (LTR for short) writing direction, however some languages (such as Hebrew) uses Right-to-Left (RTL for short) direction. 

LittlevGL not only supports RTL texts but supports mixed (a.k.a. bidirectional, BiDi) text rendering too. Some examples:

![](/misc/bidi.png "Bidirectional text examples")

The BiDi support can be enabled by `LV_USE_BIDI` in *lv_conf.h*

All texts have a base direction (LTR or RTL) which determines some rendering rules and the default alignment of the text (Left or Right).
However, in LittlevGL, base direction is not only for labels. It's a general property which can be set for every object. 
If unset then it will be inherited from the parent. 
So it's enough to set the base direction of the screen and every object will inherit it.

The default base direction of screen can be set by `LV_BIDI_BASE_DIR_DEF` in *lv_conf.h*.

To set an object's base direction use `lv_obj_set_base_dir(obj, base_dir)`.  The possible base direction are:
- `LV_BIDI_DIR_LTR`: Left to Right base direction
- `LV_BIDI_DIR_RTL`: Right to Left base direction
- `LV_BIDI_DIR_AUTO`: Auto detect base direction
- `LV_BIDI_DIR_INHERIT`: Inherit the base direction from the parent (default for non-screen objects)


This list summarizes the effect of RTL base direction on objects:
- Create objects by default on the right
- `lv_tabview`: displays tabs from right to left
- `lv_cb`: Show the box on the right
- `lv_btnm`: Show buttons from right to left
- `lv_list`: Show the icon on the right
- `lv_ddlist`: Align the options to the right
- The texts in `lv_table`, `lv_btnm`, `lv_kb`, `lv_tabview`, `lv_ddlist`, `lv_roller` are processed to display correctly with RTL parts too



### Subpixel rendering

Subpixel rendering means to increase the horizontal resolution by rendering on Red, Green and Blue channel instead of pixel level. It results in higher quality letter anti-alaising.

Subpixel rendering requires to generate the fonts with special settings: 
- In the online converter tick the `Subpixel` box
- In the command line tool use `--lcd` flag. Note that the generated font needs about 3 times more memory.

Subpixel rendering works only if the color channels of the pixels have a horizontal layout. That is the R, G, B channels are next eachother and not above eachother. 
The order of color channels also needs to match with the library settings. By default the LittlevGL assumes `RGB` order, however it can ba swapped by setting `LV_SUBPX_BGR  1` in *lv_conf.h*.

### Compress fonts
The bitmaps of the fonts can be compressed by 
- ticking the `Compressed` check box in the online converter
- not passing `--no-compress`flag to the offline converter (applies compression by default) 

The compression is more effective with larger fonts and higher bpp. However, it's about 30% slower to render the compressed fonts.
Therefore it's recommended to compress only the largest fonts of user interface, because
- they need the most memory 
- they can be compressed better
- and probably they are used less frequently then the medium sized fonts. (so performance cost is smaller)

## Ajouter une nouvelle police

Il y a plusieurs manières d'ajouter une nouvelle police à votre projet :
1. The simplest method is to use the [Online font converter](https://littlevgl.com/ttf-font-to-c-array). Just set the parameters, click the *Convert* button, copy the font to your project and use it. **Be sure to carefully read the steps provided on that site or you will get an error while converting.**
2. Utilisez le [Convertisseur de polices hors ligne] (https://github.com/littlevgl/lv_font_conv) (nécessite l'installation de Node.js).
3. If you want to create something like the built-in fonts (Roboto font and symbols) but in different size and/or ranges, you can use the `built_in_font_gen.py` script in `lvgl/scripts/built_in_font` folder.
(It requires Python and `lv_font_conv` to be installed)

To declare the font in a file, use `LV_FONT_DECLARE(my_font_name)`.

To make the fonts globally available (like the builtin fonts), add them to `LV_FONT_CUSTOM_DECLARE` in *lv_conf.h*.

## Ajouter de nouveaux symboles
The built-in symbols are created from [FontAwesome](https://fontawesome.com/) font. 

1. Search symbol on [https://fontawesome.com](https://fontawesome.com). For example the [USB symbol](https://fontawesome.com/icons/usb?style=brands). Copy it's Unicode ID which is `0xf287` in this case.
2. Open the [Online font converter](https://littlevgl.com/ttf-font-to-c-array). Add Add [FontAwesome.woff](https://littlevgl.com/tools/FontAwesome5-Solid+Brands+Regular.woff). . 
3. Set the parameters such as Name, Size, BPP. You'll use this name to declare and use the font in your code.
4. Add the Unicode ID of the symbol to the range field. E.g.` 0xf287` for the USB symbol. More symbols can be enumerated with `,`.
5. Convert the font and copy it to your project. Make sure to compile the .c file of your font.
6. Declare the font using `extern lv_font_t my_font_name;` or simply `LV_FONT_DECLARE(my_font_name);`.

**Using the symbol**
1. Convert the Unicode value to UTF8. You can do it e.g on [this site](http://www.ltg.ed.ac.uk/~richard/utf-8.cgi?input=f287&mode=hex). For `0xf287` the *Hex UTF-8 bytes* are `EF 8A 87`.
2. Create a `define` from the UTF8 values: `#define MY_USB_SYMBOL "\xEF\x8A\x87"`
3. Create a label and set the text. Eg. `lv_label_set_text(label, MY_USB_SYMBOL)`

Note - `lv_label_set_text(label, MY_USB_SYMBOL)` searches for this symbol in the font defined in `style.text.font` properties. To use the symbol you may need to change it. Eg ` style.text.font = my_font_name` 

## Ajouter un nouveau moteur de polices

LittlevGL's font interface is designed to be very flexible.
You don't need to use LittlevGL's internal font engine but, you can add your own.
For example, use [FreeType](https://www.freetype.org/) to real-time render glyphs from TTF fonts or use an external flash to store the font's bitmap and read them when the library needs them.

Pour ce faire, une variable `lv_font_t` personnalisée doit être créée :
```c
/* Décrit les propriétés d'une police */
lv_font_t my_font;
my_font.get_glyph_dsc = my_get_glyph_dsc_cb;        /* Définit une fonction de rappel pour obtenir des informations sur les glyphes */
my_font.get_glyph_bitmap = my_get_glyph_bitmap_cb;  /* Définit une fonction de rappel pour obtenir l'image matricielle d'un glyphe */
my_font.line_height = height;                       /* La hauteur réelle de la ligne où le texte s'inscrit */
my_font.base_line = base_line;                      /* La ligne de base mesurée à partir du haut de la ligne */
my_font.dsc = something_required;                   /*  Enregistre ici toutes les données spécifiques à l'implémentation */
my_font.user_data = user_data;                      /* Éventuellement des données utilisateur supplémentaires */

...

/* Get info about glyph of `unicode_letter` in `font` font.
 * Enregistre le résultat dans `dsc_out`.
 * La lettre suivante (`unicode_letter_next`) peut être utilisée pour calculer la largeur requise par ce glyphe (crénage)
 */
bool my_get_glyph_dsc_cb(const lv_font_t * font, lv_font_glyph_dsc_t * dsc_out, uint32_t unicode_letter, uint32_t unicode_letter_next)
{
    /* Votre code ici */

    /* Enregistre le résultat.
     * For example ...
     */
    dsc_out->adv_w = 12;        /* Espace horizontal requis par le glyphe en [px] */
    dsc_out->box_h = 8;         /* Hauteur de l'image en [px] */
    dsc_out->box_w = 6;         /* Largeur de l'image en [px] */
    dsc_out->ofs_x = 0;         /* Déplacement X de l'image en [px] */
    dsc_out->ofs_y = 3;         /* Déplacement Y de l'image mesuré depuis la ligne de base */
    dsc_out->bpp   = 2;         /*Bits per pixel: 1/2/4/8*/

    return true;                /* true : glyphe trouvé; false : glyphe non trouvé */
}


/* Obtient l'image matricielle de `unicode_letter` à partir de `font`.*/
const uint8_t * my_get_glyph_bitmap_cb(const lv_font_t * font, uint32_t unicode_letter)
{
    /* Votre code ici */

    /* The bitmap should be a continuous bitstream where
     * each pixel is represented by `bpp` bits */

    return bitmap;    /* Ou NULL si non trouvé */
}
```

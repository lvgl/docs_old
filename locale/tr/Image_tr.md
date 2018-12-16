_Written for v5.1_

## Overview

The Images are the basic object to **display images**. To provide maximum flexibility the **source of the image** can be:

- a variable in the code (a C array with the pixels)
- a file stored externally (like on an SD card)
- a text with [Symbols](/Fonts_tr)

To set the source of an image the `lv_img_set_src` function can be used. 

To generate a pixel array **from a PNG, JPG or BMP** image use the [Online image converter tool](https://littlevgl.com/image-to-c-array) and set the converted image with its pointer: 

```c
lv_img_set_src(img1, &converted_img_var);
```

To use **external files** you also need to convert the image files using the online converter tool but now you should select the binary Output format.  To see how to handle external image files from LittlevGL check the [Tutorial](https://github.com/littlevgl/lv_examples/tree/master/lv_tutorial/6_images).  

You can set a **symbol**  from lv_symbol_def.h too. In this case, the image will be rendered as text according to the **font** specified in the style.  It enables to use light weighted mono-color 
"letters" instead of real images. You can set symbol like this: 

```c
lv_img_set_src(img1, SYMBOL_OK);
```

The internal (variable) and external images support 2 **transparency handling** methods:

- **Chrome keying** `LV_COLOR_TRANSP` (lv_conf.h) will be transparent
- **Alpha byte** Add an alpha byte to every pixel

These options can be selected in the online font converter.

The images can be **re-colored in run-time** to any color according to the brightness of the pixels. It is very useful to show different states (selected, inactive, pressed etc) of an image without storing more versions of the same image. This feature can be enabled in the style by setting `img.intense` between `LV_OPA_TRANSP` (no recolor, value: 0) and `LV_OPA_COVER` (full recolor, value: 255). The default value is `LV_OPA_TRANSP` so this feature is disabled.

It is possible to **automatically set the size** of the image object to the image source's width and height if enabled by the `lv_img_set_auto_size(image, true)` function. If _auto size_ is enabled then when a new file is set the object size is automatically changed. Later you can modify the size manually. If the object size is 
greater then the image size in any directions then the image will be repeated like a mosaic.  The auto size is enabled by default if the image is not a screen.

The images' default style is NULL so they **inherit the parent's style**.

## Style usage

- For images **style.img**
- For symbols **style.text**

## Notes

- Symbols names (like SYMBOL_EDIT) are short strings, therefore, you can concatenate them to show more symbols.

## Example


![Example of Image in LittlevGL Graphics Library ](http://docs.littlevgl.com/img/image-lv_img.png)

```c
/*Declare a cogwheel image variable*/
LV_IMG_DECLARE(img_cw);

[...]

/***************************************
 * Create three images and re-color them
 ***************************************/

/*Create the first image without re-color*/
lv_obj_t * img1 = lv_img_create(lv_scr_act(), NULL);
lv_img_set_src(img1, &img_cw);
lv_obj_align(img1, NULL, LV_ALIGN_IN_TOP_LEFT, 20, 40);

/*Create style to re-color with light blue*/
static lv_style_t style_img2;
lv_style_copy( &style_img2, &lv_style_plain);
style_img2.image.color = LV_COLOR_HEX(0x003b75);
style_img2.image.intense = LV_OPA_50;

/*Create an image with the light blue style*/
lv_obj_t * img2 = lv_img_create(lv_scr_act(), img1);
lv_obj_set_style(img2, &style_img2);
lv_obj_align(img2, NULL, LV_ALIGN_IN_TOP_MID, 0, 40);

/*Create style to re-color with dark blue*/
static lv_style_t style_img3;
lv_style_copy(&style_img3, &lv_style_plain);
style_img3.image.color = LV_COLOR_HEX(0x003b75);
style_img3.image.intense = LV_OPA_90;

/*Create an image with the dark blue style*/
lv_obj_t * img3 = lv_img_create(lv_scr_act(), img2);
lv_obj_set_style(img3, &style_img3);
lv_obj_align(img3, NULL, LV_ALIGN_IN_TOP_RIGHT, -20, 40);


/**************************************
 * Create an image with symbols
 **************************************/

/*Create a string from symbols*/
char buf[32];
sprintf(buf, "%s%s%s%s%s%s%s",
             SYMBOL_DRIVE, SYMBOL_FILE, SYMBOL_DIRECTORY, SYMBOL_SETTINGS,
             SYMBOL_POWER, SYMBOL_GPS, SYMBOL_BLUETOOTH);

/*Create style with a symbol font*/
static lv_style_t style_sym;
lv_style_copy(&style_sym, &lv_style_plain);
// The built-in fonts are extended with symbols
style_sym.text.font = &lv_font_dejavu_60;
style_sym.text.letter_space = 10;

/*Create an image and use the string as source*/
lv_obj_t * img_sym = lv_img_create(lv_scr_act(), NULL);
lv_img_set_src(img_sym, buf);
lv_img_set_style(img_sym, &style_sym);
lv_obj_align(img_sym, NULL, LV_ALIGN_IN_BOTTOM_MID, 0, -30);


/*Create description labels*/
lv_obj_t * label = lv_label_create(lv_scr_act(), NULL);
lv_label_set_text(label, "Re-color the images in run time");
lv_obj_align(label, NULL, LV_ALIGN_IN_TOP_MID, 0, 15);

label = lv_label_create(lv_scr_act(), NULL);
lv_label_set_text(label, "Use symbols from fonts as images");
lv_obj_align(label, NULL, LV_ALIGN_IN_BOTTOM_MID, 0, -80);
```

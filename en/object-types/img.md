# Image (lv_img)

## Overview

The Images are the basic object to **display images**. To provide maximum flexibility the **source of the image** can be:

- a variable in the code (a C array with the pixels)
- a file stored externally (like on an SD card)
- a text with [Symbols](/overview/fonts)

To set the source of an image use `lv_img_set_src(img, src)`

To generate a pixel array **from a PNG, JPG or BMP** image use the [Online image converter tool](https://littlevgl.com/image-to-c-array) and set the converted image with its pointer: `lv_img_set_src(img1, &converted_img_var);`
To make the variable visible in the C file you need to declare it with `LV_IMG_DECLARE(converted_img_var)`

To use **external files** you also need to convert the image files using the online converter tool but now you should select the binary Output format. 
You also need to use LittlevGL's file system module and regsiter a driver with some functions for the basic file operation. Got to the [File system](/overview/file-system) to learn more.
To set an image source form a file use `lv_img_set_src(img, "S:folder1/my_img.bin")`


You can set a **symbol**  similarly to [Labels](/object-types/label). In this case, the image will be rendered as text according to the *font* specified in the style.  It enables to use light weighted mono-color 
"letters" instead of real images. You can set symbol like `lv_img_set_src(img1, LV_SYMBOL_OK)`

Images and labels are sometimes for the same thing. E.g.to describe what a button does. Therefore Images and Labels are somewhat interchangable. 
To handle this images can even display **texts** by using `LV_SYMBOL_DUMMY` as prefix of the text. For example `lv_img_set_src(img, LV_SYMBOL_DUMMY "Some text")`


The internal (variable) and external images support 2 **transparency handling** methods:

- **Chrome keying** pixels with `LV_COLOR_TRANSP` (lv_conf.h) color will be transparent
- **Alpha byte** An alpha byte is added to every pixel


Besides *True color* color format the following format are also supported:
- **Indexed** image has a palette
- **Alpha indexed** only alpha values are stored

These options can be selected in the font converter. To learn more about the color formats read the [Images](/overview/images) section.

The images can be **re-colored in run-time** to any color according to the brightness of the pixels. 
It is very useful to show different states (selected, inactive, pressed etc) of an image without storing more versions of the same image. 
This feature can be enabled in the style by setting `img.intense` between `LV_OPA_TRANSP` (no recolor, value: 0) and `LV_OPA_COVER` (full recolor, value: 255). 
The default value is `LV_OPA_TRANSP` so this feature is disabled.

It is possible to **automatically set the size** of the image object to the image source's width and height if enabled by the `lv_img_set_auto_size(image, true)` function. 
If *auto size* is enabled then when a new file is set the object size is automatically changed. Later you can modify the size manually. The *auto size* is enabled by default if the image is not a screen

If the object size is greater then the image size in any directions then the image will be repeated like a mosaic. 
It's a very useful a feature to create a large image from only a very narrow source. 
For example you can have a *300 x 1* image with a special gradient and set it as a wallpaper using the mosaic feature.

The images' default style is *NULL* so they **inherit the parent's style**.


## Styles
The images uses one style which can be set by `lv_img_set_style(lmeter, LV_IMG_STYLE_MAIN, &style)`. All the `style.image` propertis are used:
- **image.inense** intensity of recoloring (0..255 or *LV_OPA_...*)
- **image.color** color for recoloring or color of the alpha indexed images
- **image.opa** overall opacitiy of image

When the Image obejct idplays a text then `style.text` properties are used. See [Label](/object-types/label) for more information.

## Events
Only the [Genreric events](/overview/events.html#generic-events) are sent by the object type.

Learn more about [Events](/overview/events).

## Keys
No *Keys* are processed by the object type.

Learn more about [Keys](/overview/indev).

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

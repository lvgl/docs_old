# Image (lv_img)

## Overview

The Images are the basic object to display images. 

### Image source
To provide maximum flexibility the source of the image can be:

- a variable in the code (a C array with the pixels)
- a file stored externally (like on an SD card)
- a text with [Symbols](/overview/font)

To set the source of an image use `lv_img_set_src(img, src)`

To generate a **pixel array** from a PNG, JPG or BMP image use the [Online image converter tool](https://littlevgl.com/image-to-c-array) and set the converted image with its pointer: `lv_img_set_src(img1, &converted_img_var);`
To make the variable visible in the C file you need to declare it with `LV_IMG_DECLARE(converted_img_var)`

To use **external files** you also need to convert the image files using the online converter tool but now you should select the binary Output format. 
You also need to use LittlevGL's file system module and register a driver with some functions for the basic file operation. Got to the [File system](/overview/file-system) to learn more.
To set an image source form a file use `lv_img_set_src(img, "S:folder1/my_img.bin")`


You can set a **symbol**  similarly to [Labels](/object-types/label). In this case, the image will be rendered as text according to the *font* specified in the style.  It enables to use of light weighted mono-color 
"letters" instead of real images. You can set symbol like `lv_img_set_src(img1, LV_SYMBOL_OK)`

### Label as an image
Images and labels are sometimes for the same thing. E.g.to describe what a button does. Therefore Images and Labels are somewhat interchangeable. 
To handle these images can even display texts by using `LV_SYMBOL_DUMMY` as the prefix of the text. For example `lv_img_set_src(img, LV_SYMBOL_DUMMY "Some text")`


### Transparency
The internal (variable) and external images support 2 transparency handling methods:

- **Chrome keying** pixels with `LV_COLOR_TRANSP` (*lv_conf.h*) color will be transparent
- **Alpha byte** An alpha byte is added to every pixel

### Palette and Alpha index
Besides *True color* (RGB) color format the following formats are also supported:
- **Indexed** image has a palette
- **Alpha indexed** only alpha values are stored

These options can be selected in the font converter. To learn more about the color formats read the [Images](/overview/image) section.

### Recolor
The images can be re-colored in run-time to any color according to the brightness of the pixels. 
It is very useful to show different states (selected, inactive, pressed etc) of an image without storing more versions of the same image. 
This feature can be enabled in the style by setting `img.intense` between `LV_OPA_TRANSP` (no recolor, value: 0) and `LV_OPA_COVER` (full recolor, value: 255). 
The default value is `LV_OPA_TRANSP` so this feature is disabled.

### Auto-size
It is possible to automatically set the size of the image object to the image source's width and height if enabled by the `lv_img_set_auto_size(image, true)` function. 
If *auto size* is enabled then when a new file is set the object size is automatically changed. Later you can modify the size manually. The *auto size* is enabled by default if the image is not a screen

### Mosaic
If the object size is greater then the image size in any directions then the image will be repeated like a mosaic. 
It's a very useful feature to create a large image from only a very narrow source. 
For example, you can have a *300 x 1* image with a special gradient and set it as a wallpaper using the mosaic feature.

### Offset
With `lv_img_set_offset_x(img, x_ofs)` and `lv_img_set_offset_y(img, y_ofs)` you can add some offset to the displayed image. 
It is useful if the object size is smaller than the image source size. 
Using the offset parameter a [Texture atlas](https://en.wikipedia.org/wiki/Texture_atlas) or a "running image" effect can be created by [Animating](/overview/animation) the x or y offset. 


## Styles
The images uses one style which can be set by `lv_img_set_style(lmeter, LV_IMG_STYLE_MAIN, &style)`. All the `style.image` properties are used:
- **image.intense** intensity of recoloring (0..255 or *LV_OPA_...*)
- **image.color** color for recoloring or color of the alpha indexed images
- **image.opa** overall opacity of image

When the Image object displays a text then `style.text` properties are used. See [Label](/object-types/label) for more information.

The images' default style is *NULL* so they **inherit the parent's style**.

## Events
Only the [Generic events](/overview/event.html#generic-events) are sent by the object type.

Learn more about [Events](/overview/event).

## Keys
No *Keys* are processed by the object type.

Learn more about [Keys](/overview/indev).

## Example

```eval_rst

.. include:: /lv_examples/src/lv_ex_img/index.rst

```

## API 

```eval_rst

.. doxygenfile:: lv_img.h
  :project: lvgl
        
```

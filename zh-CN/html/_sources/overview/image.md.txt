```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/zh-CN/overview/image.md
```
# Images

An image can be a file or variable which stores the image itself and some metadata. 

## Store images
You can store images in two places
- as a variable in the internal memory (RAM or ROM)
- as a file 

### Variables
The images stored internally in a variable has `lv_img_dsc_t` type with the following fields:
- **header**
  - *cf* Color format. See [below](#color-format)
  - *w* width in pixels (<= 2048)
  - *h* height in pixels (<= 2048)
  - *always zero* 3 bits which need to be always zero
  - *reserved* reserved for future use
- **data** pointer to an array where the image itself is stored
- **data_size** length of `data` in bytes 

### Files
To deal with files you need to add a *Drive* to LittlevGL. In short, a Drive a collection of functions (*open*, *read*, *close*, etc) registered in LittlevGL to make file operation. 
You can add an interface to a standard file system (FAT32 on SD card) or you create your own simple file system to read data from an SPI Flash memory. 
In every cases, a Drive is just an abstraction to read and/or write data to a memory.
See the [File system](/overview/file-system) section to learn more. 


## Color formats
Various built-in color formats are supported:
- **LV_IMG_CF_TRUE_COLOR** Simply store the RGB colors
- **LV_IMG_CF_TRUE_COLOR_ALPHA** Store the RGB colors but add an Alpha byte too for every pixel
- **LV_IMG_CF_TRUE_COLOR_CHROMA_KEYED** Store the RGB color but if a pixel has `LV_COLOR_TRANSP` (set in *lv_conf.h*) color the pixel will be transparent
- **LV_IMG_CF_INDEXED_1/2/4/8BIT** Use palette with 2, 4, 16 or 256 colors and store each pixel on 1, 2, 4 or 8 bit
- **LV_IMG_CF_ALPHA_1/2/4/8BIT** Store only the Alpha value on 1, 2, 4 or 8 bits. Draw the pixels `style.image.color` and the set opacity. 

The bytes of the *True color* 32 bit images are stored in the following order
- Byte 0: Blue
- Byte 1: Green
- Byte 2: Red
- Byte 3: Alpha

For 16 bit color depth
- Byte 0: Green 3 lower bit, Blue 5 bit 
- Byte 1: Red 5 bit, Green 3 higher bit
- Byte 2: Alpha byte (only with LV_IMG_CF_TRUE_COLOR_ALPHA)

For 8 bit color depth
- Byte 0: Red 3 bit, Green 3 bit, Blue 2 bit
- Byte 2: Alpha byte (only with LV_IMG_CF_TRUE_COLOR_ALPHA)


You can store images in a *Raw* format to indicate that it's not a built-in color format and an [Image decoder](#image-decoder) needs to be used to decode the image.
- **LV_IMG_CF_RAW** A raw image e.g. a PNG or JPG image
- **LV_IMG_CF_RAW_ALPHA** Indicate that the image has alpha, and an Alpha byte is added for every pixel
- **LV_IMG_CF_RAW_CHROME_KEYED** Indicate that the image is chrome keyed as described in `LV_IMG_CF_TRUE_COLOR_CHROMA_KEYED` above.


## Add and use images

You can add images to LittlevGL in two ways:
- using the online converter 
- manually create images

### Online converter
The Online Image Converter is available here: https://littlevgl.com/image-to-c-array

You need to select a *BMP*, *PNG* or *JPG* image, give it a name, select the [Color format](#color-format), select the type (file or variable) and hit the *Convert* button and the result file be download.

In the converter C arrays (variables) the image for all the Color depths (1, 8, 16 or 32) are included and the used image will be selected in compile time based on `LV_COLOR_DEPTH` in *lv_conf.h*.

IN case of files you need to tell which color format you want
- RGB332 for 8 bit color depth
- RGB565 for 16 bit color depth
- RGB565 Swap for 16 bit color depth (two bytes are swapped)
- RGB888 for 32 bit color depth

### Manually create an image
If you calculate an image run-time you can craft an image variable to display it. For example:

```c
uint8_t my_img_data[] = {0x00, 0x01, 0x02, ...};

static lv_img_dsc_t my_img_dsc = {
    .header.always_zero = 0,
    .header.w = 80,
    .header.h = 60,
    .data_size = 80 * 60 * LV_COLOR_DEPTH / 8,
    .header.cf = LV_IMG_CF_TRUE_COLOR,          /*Set the color format*/
    .data = my_img_data,
};

```

If the color format is `LV_IMG_CF_TRUE_COLOR_ALPHA` you can set `data_size` like `80 * 60 * LV_IMG_PX_SIZE_ALPHA_BYTE`. 

An other option to create image run-time is to use the [Canvas](/object-types/canvas) object. 

### Use images

The most simple way to use an Image in LittlevGL is to display it with an [lv_img](/object-types/img) object:

```c
lv_obj_t * icon = lv_img_create(lv_scr_act(), NULL);

/*From variable*/
lv_img_set_src(icon, &my_icon_dsc);

/*From file*/
lv_img_set_src(icon, "S:my_icon.bin");
```

If the image was converted with the online converter you should use `LV_IMG_DECLARE(my_icon_dsc)` to declare the icon in the file where you want to use it.


## Image decoder
As you can see in the [Color formats](#color-formats) section LittlevGL supports several built image formats. However, it doesn't support for example PNG or JPG out of the box. 
To handle non-built-in image formats you need to use external libraries and attach them to LittlevGL via the *Image decoder* interface.

The image decoder consists of 4 images:
- **info** get some basic info about the image (width, height and color format)
- **open** open the image: either store the decoded image or set it to `NULL` to indicate the image can be read line-by-line
- **read** if *open* didn't fully open the image this function should give the some decoded data (max 1 line) from a given position.
- **close** close the opened image, free the allocated resources.

You can add any number of image decoders. When an image needs to be drawn the library will try all the registered image decoder until find one which is able to open the image, i.e. know that format.

The `LV_IMG_CF_TURE_COLOR_...`, `LV_IMG_INDEXED_...` and `LV_IMG_ALPHA_...` formats are known by the built-in decoder.

### Custom image formats

The easiest was to create a custom image is to use the Online image converter and set `Raw`, `Raw with alpha`, `Raw with chrome keyed` format. It will just take the every bytes of selected image and write them as image data. 
`heafer.cf` will be `LV_IMG_CF_RAW`, `LV_IMG_CF_RAW_ALPHA` or `LV_IMG_CF_RAW_CHROME_KEYED` accordingly. You should choose the correct format according to you needs: fully covering image, use alpha channel or use chroma keying.

After decoding, the *raw* formats are considered *True color*. In other words the image decoder should decode the *Raw* images to *True color* according to the format described in [#color-formats](Color formats) section.

If you want to create a really custom image you should use `LV_IMG_CF_USER_ENCODED_0..7` color formats. However, the library can draw the images only in *True color* format (or *Raw* but finally it's supposed to be in *True color* format). 
So the `LV_IMG_CF_USER_ENCODED_...` formats are not known by the library therefore they should be decoded to one of the known formats from [#color-formats](Color formats) section. 
It's possible to decoded the image to a non-true color format first, for example `LV_IMG_INDEXED_4BITS`, and then call the built-in decoder functions to convert it to *True color*. 

With *User encoded* formats the color format in the open function (`dsc->header.cf`) should be changed according to the new format.
 

### Register an image decoder

For example, if you want LittlevGL to "understand" PNG images you need to create a new image decoder and set some functions to open/close the PNG files. It should looks like this:

```c
/*Create a new decoder and register functions */
lv_img_decoder_t * dec = lv_img_decoder_create();
lv_img_decoder_set_info_cb(dec, decoder_info);
lv_img_decoder_set_open_cb(dec, decoder_open);
lv_img_decoder_set_close_cb(dec, decoder_close); 


/**
 * Get info about a PNG image
 * @param decoder pointer to the decoder where this function belongs
 * @param src can be file name or pointer to a C array
 * @param header store the info here
 * @return LV_RES_OK: no error; LV_RES_INV: can't get the info
 */
static lv_res_t decoder_info(lv_img_decoder_t * decoder, const void * src, lv_img_header_t * header)
{
  /*Check whether the type `src` is known by the decoder*/
  if(is_png(src) == false) return LV_RES_INV; 

  ...
  
  header->cf = LV_IMG_CF_RAW_ALPHA;
  header->w = width;
  header->h = height;
}

/**
 * Open a PNG image and return the decided image
 * @param decoder pointer to the decoder where this function belongs
 * @param dsc pointer to a descriptor which describes this decoding session
 * @return LV_RES_OK: no error; LV_RES_INV: can't get the info
 */
static lv_res_t decoder_open(lv_img_decoder_t * decoder, lv_img_decoder_dsc_t * dsc)
{

  /*Check whether the type `src` is known by the decoder*/
  if(is_png(src) == false) return LV_RES_INV; 
  
  /*Decode and store the image. If `dsc->img_data` the `read_line` function will be called to get the image data liny-by-line*/
  dsc->img_data = my_png_decoder(src);
  
  /*Change the color format if required. For PNG usually 'Raw' is fine*/
  dsc->header.cf = LV_IMG_CF_...
  
  /*Call a built in decoder function if required. It's not required if`my_png_decoder` opened the image in true color format.*/
  lv_res_t res = lv_img_decoder_built_in_open(decoder, dsc);
  
  return res;
}

/**
 * Decode `len` pixels starting from the given `x`, `y` coordinates and store them in `buf`.
 * Required only if the "open" function can't open the whole decoded pixel array. (dsc->img_data == NULL)
 * @param decoder pointer to the decoder the function associated with
 * @param dsc pointer to decoder descriptor
 * @param x start x coordinate
 * @param y start y coordinate
 * @param len number of pixels to decode
 * @param buf a buffer to store the decoded pixels
 * @return LV_RES_OK: ok; LV_RES_INV: failed
 */
lv_res_t decoder_built_in_read_line(lv_img_decoder_t * decoder, lv_img_decoder_dsc_t * dsc, lv_coord_t x,
                                                  lv_coord_t y, lv_coord_t len, uint8_t * buf)
{
   /*With PNG it's usually not required*/

   /*Copy `len` pixels from `x` and `y` coordinates in True color format to `buf` */
  
}

/**
 * Free the allocated resources
 * @param decoder pointer to the decoder where this function belongs
 * @param dsc pointer to a descriptor which describes this decoding session
 */
static void decoder_close(lv_img_decoder_t * decoder, lv_img_decoder_dsc_t * dsc)
{
  /*Free all allocated data*/
  
  /*Call the built-in close function if the built-in open/read_line was used*/
  lv_img_decoder_built_in_close(decoder, dsc);
  
}

```

So in summary:
- In `decoder_info` you should collect some basic information about the image and store it in `header`.
- In `decoder_open` you should try to open the image source pointed by `dsc->src`. It's type is already in `dsc->src_type == LV_IMG_SRC_FILE/VARIABLE`. 
If this format/type is not supported by the decoder return `LV_RES_INV`.
However, if you can open the image a pointer to the decoded *True color* image should be set in `dsc->img_data`. 
If the format is known but you don't want decode while image (e.g. no memory for it) set `dsc->img_data = NULL` to call `read_line` to get the pixels.
- In `decoder_close` you should free all the allocated resources.
- `decoder_read` is optional. Decoding the whole image requires extra memory and some computational overhead. 
However, if can decode one line of the image without decoding the whole image you can save memory and time. 
To indicate that the *line read* function should be used set `dsc->img_data = NULL` in the open function.


### Manually use an image decoder

LittlevGL will use th registered image decoder automatically but you can use them manually too. Create a `lv_img_decoder_dsc_t` variable to describe a the decoding session and call `lv_img_decoder_open()`, `lv_img_decoder_open()`. 

```c

lv_res_t res;
lv_img_decoder_dsc_t dsc;
res = lv_img_decoder_open(&dsc, &my_img_dsc, &lv_style_plain);

if(res == LV_RES_OK) {
  /*Do something with `dsc->img_data`*/
  lv_img_decoder_close(&dsc);
}

```


## Image caching
Sometimes it takes a lot of time to open an image. 
Continuously decoding a PNG image or loading images from a slow external memory would be effective. 
Therefore LittlevGL caches a given number of images. Caching means some images will be left open hence LittlevGl can quickly access them from `dsc->img_data` instead of decoding the again.

### Cache size
The number of cache entries can be defined in `LV_IMG_CACHE_DEF_SIZE` in *lv_conf.h*. The default value is 1 so only the lastly used image will be left open. 
The size of cache can be changed in tun-time with `lv_img_cache_set_size(entry_num)`

### Value of images
If you use more images then the cache size LittlevGL can't cache all of the images. Instead, if a new image needs to be opened but there is no place in the cache the library will close an image. 
To decide which image to close LittlevGL measured how much did it take to open the image. Images which more time consuming to open are considered more valuable and LittlevGL tries to cache them longer.
You can manually set the *time to open* value in the decoder open function in `dsc->time_to_open = time_ms` to give a higher or lower value to the image. (Leave it unchanged to let LittlevGL set it)

Every cache entry has a *"life"* value. Every time an image opening happens through the cache the *life* of all entries are decreased to make them older.
When a cached image is used its *life* is increased by the *time to open* value to make it more alive.

If there is no more space in the cache always the entry with the smallest life will be closed.

### Memory usage
Note that, the cached image might continuously consume memory. For example, if 3 PNG images are cached, they will consume memory while they are opened. 
Therefore it's the user responsibility to be sure there is enough RAM to cache even the largest images at the same time.

### Clean the cache
Let's say you have loaded a PNG image into a `lv_img_dsc_t my_png` variable and use it in an `lv_img` object. If the image is already cached and you change `my_png->data` you need to notify LittlevGL to cache the image again.
To do this use `lv_img_cache_invalidate_src(&my_png)`. If `NULL` is passed as parameter the whole cache will be cleaned.


## API

### Image decoder

```eval_rst

.. doxygenfile:: lv_img_decoder.h
  :project: lvgl
        
```


### Image cache

```eval_rst

.. doxygenfile:: lv_img_cache.h
  :project: lvgl
        
```

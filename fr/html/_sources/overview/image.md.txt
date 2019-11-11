```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/fr/overview/image.md
```
# Images

An image can be a file or variable which stores the bitmap itself and some metadata.

## Enregistrer des images
Vous pouvez enregistrer des images à deux endroits
- en tant que variable en mémoire interne (MEV ou MEM)
- as a file

### Variables
The images stored internally in a variable is composed mainly of an `lv_img_dsc_t` structure with the following fields:
- **header**
  - *cf* Format de couleur. Voir [ci-dessous](#formats-de-couleur)
  - *w* largeur en pixels (<= 2048)
  - *h* hauteur en pixels (<= 2048)
  - *always zero* 3 bits qui doivent toujours être à zéro
  - *reserved* réservé pour une utilisation future
- **data**pointeur sur un tableau où l'image elle-même est enregistrée
- **data_size** length of `data` in bytes

These are usually stored within a project as C files. They are linked into the resulting executable like any other constant data.

### Fichiers
To deal with files you need to add a *Drive* to LittlevGL. In short, a *Drive* is a collection of functions (*open*, *read*, *close*, etc.) registered in LittlevGL to make file operations.
You can add an interface to a standard file system (FAT32 on SD card) or you create your simple file system to read data from an SPI Flash memory.
In every case, a *Drive* is just an abstraction to read and/or write data to a memory.
See the [File system](/overview/file-system) section to learn more.

Images stored as files are not linked into the resulting executable, and must be read to RAM before being drawn. As a result, they are not as resource-friendly as variable images. However, they are easier to replace without needing to recompile the main program.

## Formats de couleur
Divers formats de couleur intégrés sont pris en charge:
- **LV_IMG_CF_TRUE_COLOR** Simply stores the RGB colors (in whatever color depth LittlevGL is configured for).
- **LV_IMG_CF_TRUE_COLOR_ALPHA** Like `LV_IMG_CF_TRUE_COLOR` but it also adds an alpha (transparency) byte for every pixel.
- **LV_IMG_CF_TRUE_COLOR_CHROMA_KEYED** Like `LV_IMG_CF_TRUE_COLOR` but if a pixel has `LV_COLOR_TRANSP` (set in *lv_conf.h*) color the pixel will be transparent.
- **LV_IMG_CF_INDEXED_1/2/4/8BIT** Uses a palette with 2, 4, 16 or 256 colors and stores each pixel in 1, 2, 4 or 8 bits.
- **LV_IMG_CF_ALPHA_1/2/4/8BIT** **Only stores the Alpha value on 1, 2, 4 or 8 bits.** The pixels take the color of `style.image.color` and the set opacity. The source image has to be an alpha channel. This is ideal for bitmaps similar to fonts (where the whole image is one color but you'd like to be able to change it).

The bytes of the `LV_IMG_CF_TRUE_COLOR` images are stored in the following order.

For 32-bit color depth:
- Byte 0: Bleu
- Byte 1: Vert
- Byte 2: Rouge
- Byte 3: Alpha

For 16-bit color depth:
- Byte 0: Green 3 lower bit, Blue 5 bit
- Byte 1: Rouge 5 bits, Vert 3 bits de poids fort
- Byte 2: octet Alpha (seulement avec LV_IMG_CF_TRUE_COLOR_ALPHA)

For 8-bit color depth:
- Byte 0: Rouge 3 bits, Vert 3 bits, Bleu 2 bits
- Byte 2: octet Alpha (seulement avec LV_IMG_CF_TRUE_COLOR_ALPHA)


You can store images in a *Raw* format to indicate that, it's not a built-in color format and an external [Image decoder](#image-decoder) needs to be used to decode the image.
- **LV_IMG_CF_RAW** Indicates a basic raw image (e.g. a PNG or JPG image).
- **LV_IMG_CF_RAW_ALPHA** Indicates that the image has alpha and an alpha byte is added for every pixel.
- **LV_IMG_CF_RAW_CHROME_KEYED** Indicates that the image is chrome keyed as described in `LV_IMG_CF_TRUE_COLOR_CHROMA_KEYED` above.


## Ajouter et utiliser des images

Vous pouvez ajouter des images à LittlevGL de deux manières :
- using the online converter
- créer manuellement des images

### Convertisseur en ligne
The online Image converter is available here: https://littlevgl.com/image-to-c-array

Adding an image to LittlevGL via online converter is easy.

1. You need to select a *BMP*, *PNG* or *JPG* image first.
2. Give the image a name that will be used within LittlevGL.
3. Select the [Color format](#color-formats).
4. Select the type of image you want. Choosing a binary will generate a `.bin` file that must be stored separately and read using the [file support](#files). Choosing a variable will generate a standard C file that can be linked into your project.
5. Hit the *Convert* button. Once the conversion is finished, your browser will automatically download the resulting file.

In the converter C arrays (variables), the bitmaps for all the color depths (1, 8, 16 or 32) are included in the C file, but only the color depth that matches `LV_COLOR_DEPTH` in *lv_conf.h* will actually be linked into the resulting executable.

In case of binary files, you need to specify the color format you want:
- RGB332 for 8-bit color depth
- RGB565 for 16-bit color depth
- RGB565 Swap for 16-bit color depth (two bytes are swapped)
- RGB888 for 32-bit color depth

### Créer une image manuellement
If you are generating an image at run-time, you can craft an image variable to display it using LittlevGL. For example:

```c
uint8_t my_img_data[] = {0x00, 0x01, 0x02, ...};

static lv_img_dsc_t my_img_dsc = {
    .header.always_zero = 0,
    .header.w = 80,
    .header.h = 60,
    .data_size = 80 * 60 * LV_COLOR_DEPTH / 8,
    .header.cf = LV_IMG_CF_TRUE_COLOR,          /* Définit le format de couleur */
    .data = my_img_data,
};

```

If the color format is `LV_IMG_CF_TRUE_COLOR_ALPHA` you can set `data_size` like `80 * 60 * LV_IMG_PX_SIZE_ALPHA_BYTE`.

Another (possibly simpler) option to create and display an image at run-time is to use the [Canvas](/object-types/canvas) object.

### Utiliser des images

The simplest way to use an image in LittlevGL is to display it with an [lv_img](/object-types/img) object:

```c
lv_obj_t * icon = lv_img_create(lv_scr_act(), NULL);

/* A partir d'une variable */
lv_img_set_src(icon, &my_icon_dsc);

/* A partir d'un fichier */
lv_img_set_src(icon, "S:my_icon.bin");
```

If the image was converted with the online converter, you should use `LV_IMG_DECLARE(my_icon_dsc)` to declare the image in the file where you want to use it.


## Décodeur d'images
As you can see in the [Color formats](#color-formats) section, LittlevGL supports several built-in image formats. In many cases, these will be all you need. LittlevGL doesn't directly support, however, generic image formats like PNG or JPG.

To handle non-built-in image formats, you need to use external libraries and attach them to LittlevGL via the *Image decoder* interface.

The image decoder consists of 4 callbacks:
- **info** get some basic info about the image (width, height and color format).
- **open** open the image: either store the decoded image or set it to `NULL` to indicate the image can be read line-by-line.
- **read** if *open* didn't fully open the image this function should give some decoded data (max 1 line) from a given position.
- **close** ferme l'image ouverte, libére les ressources allouées.

You can add any number of image decoders. When an image needs to be drawn, the library will try all the registered image decoder until finding one which can open the image, i.e. knowing that format.

The `LV_IMG_CF_TRUE_COLOR_...`, `LV_IMG_INDEXED_...` and `LV_IMG_ALPHA_...` formats (essentially, all non-`RAW` formats) are understood by the built-in decoder.

### Formats d'image personnalisés

The easiest way to create a custom image is to use the online image converter and set `Raw`, `Raw with alpha` or `Raw with chrome keyed` format. It will just take every byte of the binary file you uploaded and write it as the image "bitmap". You then need to attach an image decoder that will parse that bitmap and generate the real, renderable bitmap.

`header.cf` will be `LV_IMG_CF_RAW`, `LV_IMG_CF_RAW_ALPHA` or `LV_IMG_CF_RAW_CHROME_KEYED` accordingly. You should choose the correct format according to your needs: fully opaque image, use alpha channel or use chroma keying.

After decoding, the *raw* formats are considered *True color* by the library. In other words, the image decoder must decode the *Raw* images to *True color* according to the format described in [#color-formats](Color formats) section.

If you want to create a custom image, you should use `LV_IMG_CF_USER_ENCODED_0..7` color formats. However, the library can draw the images only in *True color* format (or *Raw* but finally it's supposed to be in *True color* format).
So the `LV_IMG_CF_USER_ENCODED_...` formats are not known by the library, therefore, they should be decoded to one of the known formats from [#color-formats](Color formats) section.
It's possible to decode the image to a non-true color format first, for example, `LV_IMG_INDEXED_4BITS`, and then call the built-in decoder functions to convert it to *True color*.

With *User encoded* formats, the color format in the open function (`dsc->header.cf`) should be changed according to the new format.


### Enregistrer un décodeur d'image

Here's an example of getting LittlevGL to work with PNG images.

First, you need to create a new image decoder and set some functions to open/close the PNG files. It should looks like this:

```c
/* Crée un nouveau décodeur et enregistre les fonctions */
lv_img_decoder_t * dec = lv_img_decoder_create();
lv_img_decoder_set_info_cb(dec, decoder_info);
lv_img_decoder_set_open_cb(dec, decoder_open);
lv_img_decoder_set_close_cb(dec, decoder_close);


/**
 * Obtient les informations sur une image PNG
 * @param decoder pointeur vers le décodeur auquel cette fonction appartient
 * @param src peut être un nom de fichier ou un pointeur sur un tableau C
 * @param header enregistre l'information ici
 * @returnLV_RES_OK : pas d'erreur ; LV_RES_INV : impossible d'obtenir l'information
 */
static lv_res_t decoder_info(lv_img_decoder_t * decoder, const void * src, lv_img_header_t * header)
{
  /* Vérifie si le type `src` est connu du décodeur */
  if(is_png(src) == false) return LV_RES_INV;

  /* Read the PNG header and find `width` and `height` */
  ...

  header->cf = LV_IMG_CF_RAW_ALPHA;
  header->w = width;
  header->h = height;
}

/**
 * Ouvre une image PNG et retourne l'image décodée
 * @param decoder pointeur vers le décodeur auquel cette fonction appartient
 * @param dsc pointeur sur le descripteur de cette session de décodage
 * @returnLV_RES_OK : pas d'erreur ; LV_RES_INV : impossible d'obtenir l'information
 */
static lv_res_t decoder_open(lv_img_decoder_t * decoder, lv_img_decoder_dsc_t * dsc)
{

  /* Vérifie si le type `src` est connu du décodeur */
  if(is_png(src) == false) return LV_RES_INV;

  /*Decode and store the image. If `dsc->img_data` is `NULL`, the `read_line` function will be called to get the image data line-by-line*/
  dsc->img_data = my_png_decoder(src);

  /* Change le format de couleur si nécessaire. Pour le PNG, généralement un format 'brut' convient */
  dsc->header.cf = LV_IMG_CF_...

  /* Appelle une fonction de décodeur intégré si nécessaire. Ce n'est pas nécessaire si `my_png_decoder` a décodé l'image au format couleurs vraies. */
  lv_res_t res = lv_img_decoder_built_in_open(decoder, dsc);

  return res;
}

/**
 * Décode `len` pixels à partir des coordonnées fournies `x`, `y` et enregistre-les dans `buf`.
* Requis uniquement si la fonction "open" ne peut pas décoder l'intégralité du tableau de pixels (dsc->img_data == NULL).
 * @param decoder pointeur vers le décodeur associé à la fonction 
 * @param dsc pointeur vers le descripteur de décodeur
 * @param x coordonnée x de début
 * @param y coordonnée y de début
 * @param len nombre de pixels à décoder
 * @param buf un tampon pour enregistrer les pixels décodés
 * @return LV_RES_OK : ok ; LV_RES_INV : échec
 */
lv_res_t decoder_built_in_read_line(lv_img_decoder_t * decoder, lv_img_decoder_dsc_t * dsc, lv_coord_t x,
                                                  lv_coord_t y, lv_coord_t len, uint8_t * buf)
{
   /* Avec PNG, ce n'est généralement pas nécessaire */

   /* Copie `len` pixels à partir des coordonnées `x` et `y` au format couleurs vraies dans `buf` */

}

/**
* Libère les ressources allouées
 * @param decoder pointeur vers le décodeur auquel cette fonction appartient
 * @param dsc pointeur sur le descripteur de cette session de décodage
 */
static void decoder_close(lv_img_decoder_t * decoder, lv_img_decoder_dsc_t * dsc)
{
 /* Libère toutes les données allouées */

  /* Appelle la fonction intégrée de fermeture si les fonctions intégrées open/read_line ont été utilisées */
  lv_img_decoder_built_in_close(decoder, dsc);

}

```

Donc en résumé :
- In `decoder_info`, you should collect some basic information about the image and store it in `header`.
- In `decoder_open`, you should try to open the image source pointed by `dsc->src`. Its type is already in `dsc->src_type == LV_IMG_SRC_FILE/VARIABLE`.
If this format/type is not supported by the decoder, return `LV_RES_INV`.
However, if you can open the image, a pointer to the decoded *True color* image should be set in `dsc->img_data`.
If the format is known but, you don't want to decode while image (e.g. no memory for it) set `dsc->img_data = NULL` to call `read_line` to get the pixels.
- Dans `decoder_close`, vous devez libérer toutes les ressources allouées.
- `decoder_read` is optional. Decoding the whole image requires extra memory and some computational overhead.
However, if can decode one line of the image without decoding the whole image, you can save memory and time.
To indicate that, the *line read* function should be used, set `dsc->img_data = NULL` in the open function.


### Utiliser manuellement un décodeur d'image

LittlevGL will use the registered image decoder automatically if you try and draw a raw image (i.e. using the `lv_img` object) but you can use them manually too. Create a `lv_img_decoder_dsc_t` variable to describe the decoding session and call `lv_img_decoder_open()`, `lv_img_decoder_open()`.

```c

lv_res_t res;
lv_img_decoder_dsc_t dsc;
res = lv_img_decoder_open(&dsc, &my_img_dsc, &lv_style_plain);

if(res == LV_RES_OK) {
  /* Faites quelque chose avec `dsc->img_data` */
  lv_img_decoder_close(&dsc);
}

```


## Mise en cache des images
Sometimes it takes a lot of time to open an image.
Continuously decoding a PNG image or loading images from a slow external memory would be inefficient and detrimental to the user experience.

Therefore, LittlevGL caches a given number of images. Caching means some images will be left open, hence LittlevGL can quickly access them from `dsc->img_data` instead of needing to decode them again.

Of course, caching images is resource-intensive as it uses more RAM (to store the decoded image). LittlevGL tries to optimize the process as much as possible (see below), but you will still need to evaluate if this would be beneficial for your platform or not. If you have a deeply embedded target which decodes small images from a relatively fast storage medium, image caching may not be worth it.

### Taille du cache
The number of cache entries can be defined in `LV_IMG_CACHE_DEF_SIZE` in *lv_conf.h*. The default value is 1 so only the most recently used image will be left open.

The size of the cache can be changed at run-time with `lv_img_cache_set_size(entry_num)`.

### Valeur des images
When you use more images than cache entries, LittlevGL can't cache all of the images. Instead, the library will close one of the cached images (to free space).

To decide which image to close, LittlevGL uses a measurement it previously made of how long it took to open the image. Cache entries that hold slower-to-open images are considered more valuable and are kept in the cache as long as possible.

If you want or need to override LittlevGL's measurement, you can manually set the *time to open* value in the decoder open function in `dsc->time_to_open = time_ms` to give a higher or lower value. (Leave it unchanged to let LittlevGL set it.)

Every cache entry has a *"life"* value. Every time an image opening happens through the cache, the *life* of all entries are decreased to make them older.
When a cached image is used, its *life* is increased by the *time to open* value to make it more alive.

If there is no more space in the cache, always the entry with the smallest life will be closed.

### Utilisation de la mémoire
Note that, the cached image might continuously consume memory. For example, if 3 PNG images are cached, they will consume memory while they are opened.

Therefore, it's the user's responsibility to be sure there is enough RAM to cache, even the largest images at the same time.

### Nettoyer le cache
Let's say you have loaded a PNG image into a `lv_img_dsc_t my_png` variable and use it in an `lv_img` object. If the image is already cached and you then change the underlying PNG file, you need to notify LittlevGL to cache the image again. Otherwise, there is no easy way of detecting that the underlying file changed and LittlevGL will still draw the old image.

To do this, use `lv_img_cache_invalidate_src(&my_png)`. If `NULL` is passed as a parameter, the whole cache will be cleaned.


## API

### Décodeur d'image

```eval_rst

.. doxygenfile:: lv_img_decoder.h
  :project: lvgl

```


### Cache d'images

```eval_rst

.. doxygenfile:: lv_img_cache.h
  :project: lvgl

```

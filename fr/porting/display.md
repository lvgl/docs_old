```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/fr/porting/display.md
```
# Interface d'affichage

To set up a display an `lv_disp_buf_t` and an `lv_disp_drv_t` variable has to be initialized.
- **lv_disp_buf_t** contains internal graphics buffer(s).
- **lv_disp_drv_t** contains callback functions to interact with the display and manipulate drawing related things.


## Display buffer

`lv_disp_buf_t` peut être initialisé comme ceci :
```c
/* Une variable statique ou globale pour mémoriser les tampons */
    static lv_disp_buf_t disp_buf;

   /* Tampon(s) statique(s) ou global(aux). Le second tampon est optionnel */
    static lv_color_t buf_1[MY_DISP_HOR_RES * 10];
    static lv_color_t buf_2[MY_DISP_HOR_RES * 10];

/* Initialise `disp_buf` avec le(s) tampon(s) */
    lv_disp_buf_init(&disp_buf, buf_1, buf_2, MY_DISP_HOR_RES*10);
```

There are 3 possible configurations regarding the buffer size:
1. **One buffer** LittlevGL draws the content of the screen into a buffer and sends it to the display.
The buffer can be smaller than the screen. In this case, the larger areas will be redrawn in multiple parts.
Si seules de petites zones changent (p.ex. appui sur un bouton), seules ces zones seront actualisées.
2. **Deux tampons de taille différente de l'écran** ayant deux tampons LittlevGL peut dessiner dans un tampon tandis que le contenu de l'autre tampon est envoyé à l’écran en arrière-plan.
Le DMA ou une autre méthode doit être utilisé pour transférer les données à l’écran afin de permettre au CPU de dessiner dans le même temps.
This way the rendering and refreshing of the display become parallel.
Similarly to the *One buffer*, LittlevGL will draw the display's content in chunks if the buffer is smaller than the area to refresh.
3. **Deux tampons de la taille d'un écran**.
In contrast to *Two non-screen-sized buffers* LittlevGL will always provide the whole screen's content not only chunks.
De cette façon, le pilote peut simplement changer l'adresse du tampon d'affichage par celle du tampon préparé par LittlevGL.
Par conséquent, cette méthode est la meilleure lorsque le microcontrôleur dispose d’une interface LCD/TFT et que le tampon d'affichage est un emplacement dans la MEV.


## Pilote d'affichage

Une fois l’initialisation des tampons effectuée, les pilotes d’affichage doivent être initialisés. Dans le cas le plus simple, seuls les deux champs suivants de `lv_disp_drv_t` doivent être définis :
- **buffer** pointeur sur une variable `lv_disp_buf_t` initialisée.
- **flush_cb** une fonction de rappel permettant de copier le contenu d'un tampon dans une zone spécifique de l'écran.

Il y a quelques champs de données optionnels :
- **hor_res** horizontal resolution of the display. (`LV_HOR_RES_MAX` by default from *lv_conf.h*).
- **ver_res** vertical resolution of the display. (`LV_VER_RES_MAX` by default from *lv_conf.h*).
- **color_chroma_key** a color which will be drawn as transparent on chrome keyed images. `LV_COLOR_TRANSP` by default from *lv_conf.h*).
- ** user_data ** donnée utilisateur personnalisée pour le pilote. Son type peut être modifié dans *lv_conf.h*.
- **anti-aliasing** use anti-aliasing (edge smoothing). `LV_ANTIALIAS` by default  from *lv_conf.h*.
- **rotated** si `1` permute `hor_res et `ver_res`. LittlevGL dessine dans le même sens dans les deux cas (lignes du haut vers le bas); le pilote doit donc également être reconfiguré pour modifier le sens de remplissage de l'écran.
- **screen_transp** if `1` the screen can have transparent or opaque style. `LV_COLOR_SCREEN_TRANSP` needs to enabled in *lv_conf.h*.

Pour utiliser un GPU, les fonctions de rappel suivantes peuvent être utilisées :
- **gpu_fill_cb** fill an area in memory with colors.
- **gpu_blend_cb** combine deux tampons en mémoire avec gestion de l'opacité.

Note that, these functions need to draw to the memory (RAM) and not your display directly.

Some other optional callbacks to make easier and more optimal to work with monochrome, grayscale or other non-standard RGB displays:
- **rounder_cb** round the coordinates of areas to redraw. E.g. a 2x2 px can be converted to 2x8.
Utile si la carte graphique ne peut actualiser que les zones ayant une hauteur ou une largeur spécifique (généralement une hauteur de 8 px avec des écrans monochromes).
- **set_px_cb** a custom function to write the *display buffer*.
It can be used to store the pixels more compactly if the display has a special color format. (e.g. 1-bit monochrome, 2-bit grayscale etc.)
De cette façon, les tampons utilisés dans `lv_disp_buf_t` peuvent être plus petits pour ne contenir que le nombre de bits requis pour la taille de zone donnée. `set_px_cb` ne fonctionne pas avec la configuration de tampons d'affichage `Deux tampons de la taille d'un écran`.
- **monitor_cb** a callback function tells how many pixels were refreshed in how much time.

Pour définir les champs de la variable *lv_disp_drv_t*, celle-ci doit être initialisée avec `lv_disp_drv_init(&disp_drv)`.
Et enfin, pour enregistrer un affichage pour LittlevGL, `lv_disp_drv_register(& disp_drv)` doit être appelée.

Dans l'ensemble, cela ressemble à ceci :
```c
    lv_disp_drv_t disp_drv;                 /* Une variable pour contenir les pilotes. Peut être une variable locale */
    lv_disp_drv_init(&disp_drv);            /* Initialisation de base */
    disp_drv.buffer = &disp_buf;            /* Affecte un tampon initialisé */
    disp_drv.flush_cb = my_flush_cb;        /* Définit une fonction de rappel pour dessiner à l'écran */
    lv_disp_t * disp;
    disp = lv_disp_drv_register(&disp_drv); /* Enregistre le pilote et sauvegarde les objets d'affichage créés */
```

Voici quelques exemples simples de fonctions de  rappel :
```c
void my_flush_cb(lv_disp_drv_t * disp_drv, const lv_area_t * area, lv_color_t * color_p)
{
    /* Le cas le plus simple (mais aussi le plus lent) pour mettre tous les pixels à l'écran un par un */
    int32_t x, y;
    for(y = area->y1; y <= area->y2; y++) {
        for(x = area->x1; x <= area->x2; x++) {
            put_px(x, y, *color_p)
            color_p++;
        }
    }

    /* IMPORTANT !!!
     * Informe la librairie graphique que vous êtes prêt pour le transfert */
    lv_disp_flush_ready(disp);
}

void my_gpu_fill_cb(lv_disp_drv_t * disp_drv, lv_color_t * dest_buf, const lv_area_t * dest_area, const lv_area_t * fill_area, lv_color_t color);
{
    /* Cet exemple de code devrait être effectué par un GPU */
    uint32_t x, y;
    dest_buf += dest_width * fill_area->y1; /* Aller à la première ligne */

    for(y = fill_area->y1; y < fill_area->y2; y++) {
        for(x = fill_area->x1; x < fill_area->x2; x++) {
            dest_buf[x] = color;
        }
        dest_buf+=dest_width;    /* Aller à la ligne suivante */
    }
}

void my_gpu_blend_cb(lv_disp_drv_t * disp_drv, lv_color_t * dest, const lv_color_t * src, uint32_t length, lv_opa_t opa)
{
    /* Cet exemple de code devrait être effectué par un GPU */
    uint32_t i;
    for(i = 0; i < length; i++) {
        dest[i] = lv_color_mix(dest[i], src[i], opa);
    }
}

void my_rounder_cb(lv_disp_drv_t * disp_drv, lv_area_t * area)
{
  /* Modifie les zones en fonction des besoins. Agrandir uniquement.
   * Par exemple, pour toujours avoir des lignes de 8 px de hauteur : */
   area->y1 = area->y1 & 0x07;
   area->y2 = (area->y2 & 0x07) + 8;
}

void my_set_px_cb(lv_disp_drv_t * disp_drv, uint8_t * buf, lv_coord_t buf_w, lv_coord_t x, lv_coord_t y, lv_color_t color, lv_opa_t opa)
{
    /* Write to the buffer as required for the display.
     * Write only 1-bit for monochrome displays mapped vertically:*/
 buf += buf_w * (y >> 3) + x;
 if(lv_color_brightness(color) > 128) (*buf) |= (1 << (y % 8));
 else (*buf) &= ~(1 << (y % 8));
}

void my_monitor_cb(lv_disp_drv_t * disp_drv, uint32_t time, uint32_t px)
{
  printf("%d px refreshed in %d ms\n", time, ms);
}
```

## API

```eval_rst

.. doxygenfile:: lv_hal_disp.h
  :project: lvgl

```

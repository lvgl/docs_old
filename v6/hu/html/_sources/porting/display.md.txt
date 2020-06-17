```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/hu/porting/display.md
```
# Kijelző interface

To set up a display an `lv_disp_buf_t` and an `lv_disp_drv_t` variable has to be initialized.
- **lv_disp_buf_t** contains internal graphics buffer(s).
- **lv_disp_drv_t** contains callback functions to interact with the display and manipulate drawing related things.


## Display buffer

`lv_disp_buf_t` így inicializálható:
```c
    /*Egy static vagy global változó a buffers tárolásához*/
    static lv_disp_buf_t disp_buf;

    /*Static vagy global buffer(ek). (A második buffer opcionális*/
    static lv_color_t buf_1[MY_DISP_HOR_RES * 10];
    static lv_color_t buf_2[MY_DISP_HOR_RES * 10];

    /*`disp_buf` inicializálása a buffer(ekkel) */
    lv_disp_buf_init(&disp_buf, buf_1, buf_2, MY_DISP_HOR_RES*10);
```

There are 3 possible configurations regarding the buffer size:
1. **One buffer** LittlevGL draws the content of the screen into a buffer and sends it to the display.
The buffer can be smaller than the screen. In this case, the larger areas will be redrawn in multiple parts.
Ha csak egy kis terület változik (pl. egy gomb megnyomásánál), akkor csak az a kis terület kerül firssítésre.
2. **Kettő nem képernyőméretű buffer** két bufferrel  LittlevGL képes az egyik bufferbe rajzolni, míg a másik buffer tartalmát el tudja küldeni a kijelzőnek a háttérben.
DMA vagy egyéb hardware használata ajánlott, hogy az adatokat háttérben küldd el a kijelzőnek és hagyd a CPU-t rajzolni a másik bufferbe időközben.
This way the rendering and refreshing of the display become parallel.
Similarly to the *One buffer*, LittlevGL will draw the display's content in chunks if the buffer is smaller than the area to refresh.
3. **Két képernyőméretű buffer**.
In contrast to *Two non-screen-sized buffers* LittlevGL will always provide the whole screen's content not only chunks.
Ennek köszönhetően a driver egyszerűen kicserélheti a frame buffer címét a kapott bufferre.
Ezért ez a mód olyan MCU-kkal működik a legjobban, amiknek van LCD/TFT perifériája és a frame buffer  csak egy terület a RAM-ban.


## Kijelző driver

Ha buffer inicializálása kész a kijlező dirver-t kell inicializálni. Legegyszerűbb esetben a következő mezőit kell inicializálni egy `lv_disp_drv_t` változónak:
- **buffer** pointer rgy inicializált `lv_disp_buf_t` változóra.
- **flush_cb** egy callback függvény, hogy a buffer tartalmát e kijelző egy megadott területére másolja

Van néhány opcionális adata mező is:
- **hor_res** horizontal resolution of the display. (`LV_HOR_RES_MAX` by default from *lv_conf.h*).
- **ver_res** vertical resolution of the display. (`LV_VER_RES_MAX` by default from *lv_conf.h*).
- **color_chroma_key** a color which will be drawn as transparent on chrome keyed images. `LV_COLOR_TRANSP` by default from *lv_conf.h*).
- **user_data** egyedi tetszőleges felhasználói adat. A típusa módosítható *lv_conf.h*-ban.
- **anti-aliasing** use anti-aliasing (edge smoothing). `LV_ANTIALIAS` by default  from *lv_conf.h*.
- **rotated** ha `1` megcseréli `hor_res` and `ver_res` értékét. LittlevGL mindkét esetben ugyanabba az iránya rajzol (fentről le soronként) ezért a kitöltés/scan-nelés irányát a driver-ben is át kell konfigurálni.
- **screen_transp** if `1` the screen can have transparent or opaque style. `LV_COLOR_SCREEN_TRANSP` needs to enabled in *lv_conf.h*.

A GPU használatához az alábbi callback-ek használhatók:
- **gpu_fill_cb** fill an area in memory with colors.
- **gpu_blend_cb** blend two memory buffers using opacity.

Note that, these functions need to draw to the memory (RAM) and not your display directly.

Some other optional callbacks to make easier and more optimal to work with monochrome, grayscale or other non-standard RGB displays:
- **rounder_cb** round the coordinates of areas to redraw. E.g. a 2x2 px can be converted to 2x8.
Ez akkor használható, ha kijelző vezérlő csak bizony magasságú vagy szélességű területeket tud frissíteni. (Általában 8px magasság monochrome kijelzőknél)
- **set_px_cb** a custom function to write the *display buffer*.
It can be used to store the pixels more compactly if the display has a special color format. (e.g. 1-bit monochrome, 2-bit grayscale etc.)
This way the buffers used in `lv_disp_buf_t` can be smaller to hold only the required number of bits for the given area size. `set_px_cb` is not working with `Two screen-sized buffers` display buffer configuration.
- **monitor_cb** a callback function tells how many pixels were refreshed in how much time.

Egy *lv_disp_drv_t* változó mezőinek beállítása előtt azt inicializálni kell a `lv_disp_drv_init(&disp_drv)` függvénnyel.
És végül a kijelző regisztrálásához a `lv_disp_drv_register(&disp_drv)` függvényt kell meghívni.

Minden együtt így néz ki:
```c
    lv_disp_drv_t disp_drv;                 /*Egy változó a driver-nek. Lehet lokális is.*/
    lv_disp_drv_init(&disp_drv);            /*Alap inicializálás*/
    disp_drv.buffer = &disp_buf;            /*Az incializált buffer használata*/
    disp_drv.flush_cb = my_flush_cb;        /*Egy flush callback beállítása a képernyőre rajzoláshoz*/
    lv_disp_t * disp;
    disp = lv_disp_drv_register(&disp_drv); /*A driver regisztrálása és létrehozott kijelző elmentése */
```

Alább egy-egy példa látható a fent leírt callback-ekre:
```c
void my_flush_cb(lv_disp_drv_t * disp_drv, const lv_area_t * area, lv_color_t * color_p)
{
    /*A legegyszerűbb (és egyben leglassabb) megoldás, hogy minden pixelt kiteszel a kijelzőre.*/
    int32_t x, y;
    for(y = area->y1; y <= area->y2; y++) {
        for(x = area->x1; x <= area->x2; x++) {
            put_px(x, y, *color_p)
            color_p++;
        }
    }

    /* FONTOS!!!
     * Szólj a library-nak, hogy kész vagy kijelző firssítéssel*/
    lv_disp_flush_ready(disp);
}

void my_gpu_fill_cb(lv_disp_drv_t * disp_drv, lv_color_t * dest_buf, const lv_area_t * dest_area, const lv_area_t * fill_area, lv_color_t color);
{
    /*Ez egy példa, amit a GPU-nak kellene csinálni*/
    uint32_t x, y;
    dest_buf += dest_width * fill_area->y1; /*Go to the first line*/

    for(y = fill_area->y1; y < fill_area->y2; y++) {
        for(x = fill_area->x1; x < fill_area->x2; x++) {
            dest_buf[x] = color;
        }
        dest_buf+=dest_width;    /*Go to the next line*/
    }
}

void my_gpu_blend_cb(lv_disp_drv_t * disp_drv, lv_color_t * dest, const lv_color_t * src, uint32_t length, lv_opa_t opa)
{
    /*Ez egy példa, amit a GPU-nak kellene csinálni*/
    uint32_t i;
    for(i = 0; i < length; i++) {
        dest[i] = lv_color_mix(dest[i], src[i], opa);
    }
}

void my_rounder_cb(lv_disp_drv_t * disp_drv, lv_area_t * area)
{
  /* Frissítsd az `area`-t ahogy szükséges. Csak nagyobb lehet. 
   * Például legyen mindig N x 8 px magas*/
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
  printf("%d px frissítve %d ms alatt\n", time, ms);
}
```

## API

```eval_rst

.. doxygenfile:: lv_hal_disp.h
  :project: lvgl

```

```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/hu/porting/display.md
```
# Kijelző interface

Ahhoz használhass egy kijelzőt egy `lv_disp_buf_t` és egy `lv_disp_drv_t` typusú változót kell inicializálnod.
- **lv_disp_buf_t** egy belső grafikus buffert tartalmaz 
- **lv_disp_drv_t** a kijelzőhöz kapcsolódó callback függvényeket és egyén beállításokat tartalmaz


## Kijelző buffer 

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

Három beállítási lehetőség van a bufferek méretének és számának megfelelően 
1. **Egy buffer** LittlevGL a bufferbe rajzolja a képernyő tartalmát és elküldi a  kijelzőre.
A buffer kisebb is lehet, mint kijelző. Ebben az esetben a nagyobb területek kisebb darabokban kerülnek kirajzolásra.
Ha csak egy kis terület változik (pl. egy gomb megnyomásánál), akkor csak az a kis terület kerül firssítésre.
2. **Kettő nem képernyőméretű buffer** két bufferrel  LittlevGL képes az egyik bufferbe rajzolni, míg a másik buffer tartalmát el tudja küldeni a kijelzőnek a háttérben.
DMA vagy egyéb hardware használata ajánlott, hogy az adatokat háttérben küldd el a kijelzőnek és hagyd a CPU-t rajzolni a másik bufferbe időközben.
Íly' módon a rajzolás és a kijelző frissítése párhozamosan történhet.
Az *Egy buffer* módhoz hasonlóan LittlevGL kisebb darabokban fogja rajzolni a buffernél nagyobb területeket.
3. **Két képernyőméretű buffer**.
Ellentétben a *Két nem képernyőméretű buffer* móddal LittlevGL mindig teljes képenyő képét szolgáltatja, nem csak egy kis darabot.
Ennek köszönhetően a driver egyszerűen kicserélheti a frame buffer címét a kapott bufferre.
Ezért ez a mód olyan MCU-kkal működik a legjobban, amiknek van LCD/TFT perifériája és a frame buffer  csak egy terület a RAM-ban.


## Kijelző driver

Once the buffer initialization is ready the display drivers need to be initialized. In the most simple case only the following two fields of `lv_disp_drv_t` needs to be set:
- **buffer** pointer to an initialized `lv_disp_buf_t` variable.
- **flush_cb** a callback function to copy a buffer's content to a specific area of the display.

There are some optional data fields:
- **hor_res** horizontal resolution of the display. (`LV_HOR_RES_MAX` by default from *lv_conf.h*)
- **ver_res** vertical resolution of the display. (`LV_VER_RES_MAX` by default from *lv_conf.h*)
- **color_chroma_key** a color which will be drawn as transparent on chrome keyed images. `LV_COLOR_TRANSP` by default from *lv_conf.h*)
- **user_data** custom user data for the driver. Its type can be modified in lv_conf.h.
- **anti-aliasing** use anti-aliasing (edge smoothing). `LV_ANTIALIAS` by default  from *lv_conf.h*
- **rotated** if `1` swap `hor_res` and `ver_res`. LittlevGL draws in the same direction in both cases (in lines from top to bottom) so the driver also needs to be reconfigured to change the display's fill direction.
- **screen_transp** if `1` the screen can have transparent or opaque style. `LV_COLOR_SCREEN_TRANSP` needs to enabled in *lv_conf.h*
To use a GPU the following callbacks can be used:
- **gpu_fill_cb** fill an area with colors. 
- **gpu_blend_cb** blend two buffers using opacity.
 
Some other optional callbacks to make easier and more optimal to work with monochrome, gray-scale or other non-standard RGB displays: 
- **rounder_cb** round the coordinates of areas to redraw. E.g. a 2x2 px can be converted to 2x8. 
It can be used if the display controller can refresh only areas with specific height or width (usually 8 px height with monochrome displays).
- **set_px_cb** a custom function to write the *display buffer*. 
It can be used to store the pixels in a more compact way if the display has a special color format. (e.g. 1 bit monochrome, 2  bit gray-scale etc.) 
This way the buffers used in `lv_disp_buf_t` can be smaller to hold only the required number of bits for the given area size.
- **monitor_cb** a callback function tell how many pixels were refreshed in how much time.

To set the fields of *lv_disp_drv_t* variable it needs to be initialized with `lv_disp_drv_init(&disp_drv)`.
And finally to register a display for LittlevGL `lv_disp_drv_register(&disp_drv)` needs to be called.

All together it looks like this:
```c
    lv_disp_drv_t disp_drv;                 /*A variable to hold the drivers. Can be local variable*/
    lv_disp_drv_init(&disp_drv);            /*Basic initialization*/
    disp_drv.buffer = &disp_buf;            /*Set an initialized buffer*/
    disp_drv.flush_cb = my_flush_cb;        /*Set a flush callback to draw to the display*/
    lv_disp_t * disp;
    disp = lv_disp_drv_register(&disp_drv); /*Register the driver and save the created display objects*/
```

Here some simple examples of the callbacks:
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
    uint32_t x,y;
    for(y = 0; i < length; i++) {
        dest[i] = color;
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
    /* Írd a buffert ahogy szükséges
     * 1 bit írása egy monochrome kijelzőre, ahol bitek függőlegesen vannak bájtokhoz mappolva:*/
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


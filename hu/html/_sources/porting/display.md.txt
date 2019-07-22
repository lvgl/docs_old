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

Ha buffer inicializálása kész a kijlező dirver-t kell inicializálni. Legegyszerűbb esetben a következő mezőit kell inicializálni egy `lv_disp_drv_t` változónak:
- **buffer** pointer rgy inicializált `lv_disp_buf_t` változóra.
- **flush_cb** egy callback függvény, hogy a buffer tartalmát e kijelző egy megadott területére másolja

Van néhány opcionális adata mező is:
- **hor_res** a kijelző vízszintes felbontása. (`LV_HOR_RES_MAX` alapértelmezetten az *lv_conf.h*-ból)
- **ver_res** a kijelző függőleges felbontása. (`LV_VER_RES_MAX`  alapértelmezetten az *lv_conf.h*-ból)
- **color_chroma_key** egy szín ami átlátszóként lesz megjelenítve chrome keyed képeken. `LV_COLOR_TRANSP`  alapértelmezetten az *lv_conf.h*-ból)
- **user_data** egyedi tetszőleges felhasználói adat. A típusa módosítható *lv_conf.h*-ban.
- **anti-aliasing** anti-aliasing (élsimítás) engedélyezése. `LV_ANTIALIAS`  alapértelmezetten az *lv_conf.h*-ból
- **rotated** ha `1` megcseréli `hor_res` and `ver_res` értékét. LittlevGL mindkét esetben ugyanabba az iránya rajzol (fentről le soronként) ezért a kitöltés/scan-nelés irányát a driver-ben is át kell konfigurálni.
- **screen_transp** ha`1` a képernyőknek lehetnek átlátszó vagy áttetsző pixeleik. `LV_COLOR_SCREEN_TRANSP` engedélyezve kell legyen az *lv_conf.h*-ben.
A GPU használatához az alábbi callback-ek használhatók:
- **gpu_fill_cb** tölts ki egy területet egy adott színnel. 
- **gpu_blend_cb** keverj össze két buffert valamilyen átlátszóság (opacity) szerint.
 
Néhány opcionális callback, melyek megkönnyítik és optimálisabbá teszik monochrome, szürkeárnyalatos vagy nem szabványos RGB kijelzők használatát.
- **rounder_cb** kerekíti az újrarajzolandó területek koordinátáit. Pl. egy 2x2 px terület 2x8re konvertálható.. 
Ez akkor használható, ha kijelző vezérlő csak bizony magasságú vagy szélességű területeket tud frissíteni. (Általában 8px magasság monochrome kijelzőknél)
- **set_px_cb** egyedi függvény  *kijelző buffer* írásához. 
Használatával a pixeleket egy tömörebb formában tárolhatók a kijelzőnek speciális színformátuma van (pl. 1 bit monochrome, 2  bit szürkeárnyalat etc.) 
Ennek köszönhetően a `lv_disp_buf_t`-ben használt buffer-ek kisebbek lehetnek, hogy szükséges mennyiségű bitet tartalmazzák.
- **monitor_cb** egy callback, mely megmutatja, hogy mennyi pixel került frissítésre adott idő alatt.

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


# Gyors áttekintés

Here you can learn the most important things about LittlevGL.
Ajánlott először ezt a fejezetet elolvasni, hogy egy átfogó képet kapj, majd a részletes [Portolás](/porting/index) és [Áttekintés](/overview/index) fejezetekkel folytatni.

## LittlevGL hozzáadása egy projekthez

The following steps show how to setup LittlevGL on an embedded system with a display and a touchpad.
You can use the [Simulators](/get-started/pc-simulator) to get 'ready to use' projects which can be run on your PC.

- [Töltsd le](https://littlevgl.com/download) vagy [Klónozd](https://github.com/littlevgl/lvgl) a könyvtárat!
- Másold az `lvgl` mappát a projektedbe!
- Copy `lvgl/lv_conf_templ.h` as `lv_conf.h` next to the `lvgl` folder and set at least `LV_HOR_RES_MAX`, `LV_VER_RES_MAX` and `LV_COLOR_DEPTH` macros.
- Include-old `lvgl/lvgl.h`-t, ahol LittlevGL függvénykeet akarsz használni!
- Hívd meg  `lv_tick_inc(x)`-t minden `x` milliszekundumban **egy Timer-ben vagy Task-ban** (`x` 1..10 között legyen)! Ez a LittlevGL belső időzítéseihez szükséges..
- Hívd meg az `lv_init()`-et!
- Hozz létre agy kijelző buffert!
```c
static lv_disp_buf_t disp_buf;
static lv_color_t buf[LV_HOR_RES_MAX * 10];                     /*Egy buffer 10 sor számára*/
lv_disp_buf_init(&disp_buf, buf, NULL, LV_HOR_RES_MAX * 10);    /*A kijelző buffer inicializálása*/
```
- Implementálj és regisztrálj egy függvényt, ami képes **pixeleket másolni** a kijelző egy adott területére:
```c
lv_disp_drv_t disp_drv;               /*A kijelző driver leírója*/
lv_disp_drv_init(&disp_drv);          /*Alap inicializálás*/
disp_drv.flush_cb = my_disp_flush;    /*A driver függvény hozzárendelése*/
disp_drv.buffer = &disp_buf;          /*A kijelző buffer hozzárendelése*/
lv_disp_drv_register(&disp_drv);      /*Végül a driver regisztrálása*/

void my_disp_flush(lv_disp_t * disp, const lv_area_t * area, lv_color_t * color_p)
{
    int32_t x, y;
    for(y = area->y1; y <= area->y2; y++) {
        for(x = area->x1; x <= area->x2; x++) {
            set_pixel(x, y, *color_p);  /* Egy pixel kirakása kijelzőre.*/
            color_p++;
        }
    }

    lv_disp_flush_ready(disp);         /*Jelezd, hogy kész vagy a a pixelek kiírásával*/
}

```
- Implementálj és regsiztrálj egy függvényt, ami képes  egy **bementi eszközt olvasni**. Például egy touchpad esetében:
```c
lv_indev_drv_init(&indev_drv);             /*Input device leíró*/
indev_drv.type = LV_INDEV_TYPE_POINTER;    /*A touch pad egy pointer szerű eszköz*/
indev_drv.read_cb = my_touchpad_read;      /*Egy driver függvény hozzárendelése*/
lv_indev_drv_register(&indev_drv);         /*Végül a driver regisztrálása*/

bool my_touchpad_read(lv_indev_t * indev, lv_indev_data_t * data)
{
    static lv_coord_t last_x = 0;
    static lv_coord_t last_y = 0;

    /*Az állapot és az utolsó megnyomott koordináta elmentése*/
    data->state = touchpad_is_pressed() ? LV_INDEV_STATE_PR : LV_INDEV_STATE_REL;
    if(data->state == LV_INDEV_STATE_PR) touchpad_get_xy(&last_x, &last_y);

    /*Koordináták beállítása (ha felengedett, az utolsó lenyomott koordináta használata)*/
    data->point.x = last_x;
    data->point.y = last_y;

    return false; /*Return `false` mivel nincs több kiolvasandó adat*/
}
```
- Call `lv_task_handler()` periodically every few milliseconds in the main `while(1)` loop, in Timer interrupt or in an Operation system task.
It will redraw the screen if required, handle input devices etc.


## Ismerkedj meg az alapokkal

### Objektumok (Widget-ek)

A grafikus elemek, mint gombok (Button), feliratok (Label), Csúszkák (Slider), grafikonok (Charts), stb gyűjtőnéven objektumok. Az [Objektum típusok](/object-types/index) oldalán látható az összes objektum típus.

Minden objektumnak vagy egy szülő objektuma. A gyerek objektum együtt mozog a szülőjével, ha a szülő törlésre kerül, a gyerekek is törlődnek. A gyerekek cask a szülőjükön láthatók.

The *screen* is the "root" parent. To get the current screen call `lv_scr_act()`.

You can create a new object with `lv_<type>_create(parent, obj_to_copy)`. It will return an `lv_obj_t *` variable which should be used as a reference to the object to set its parameters.
The first parameter is the desired *parent*, the second parameters can be an object to copy (`NULL` is unused).
Például:
```c
lv_obj_t * slider1 = lv_slider_create(lv_scr_act(), NULL);
```

Az alapvető paraméterek beállításához a`lv_obj_set_<paramtéter_név>(obj, <érték>)` függvény használható.  Például: 
```c
lv_obj_set_x(btn1, 30);
lv_obj_set_y(btn1, 10);
lv_obj_set_size(btn1, 200, 50);
```

Az objektumoknak vannak típus specifikus paramétereik is, amiket a `lv_<typus>_set_<paraméter_név>(obj, <value>)` függvényekkel lehet beállítani. Például:
```c
lv_slider_set_value(slider1, 70, LV_ANIM_ON);
```

A teljes API az egyes objektum típusok dokumentációjában vagy a header fájlukban olvasható. (pl. `lvgl/src/lv_objx/lv_slider.h`).

### Stílusok
Styles can be assigned to the objects to changed their appearance. A style describes the appearance of rectangle-like objects (like a button or slider), texts, images and lines at once.

Egy új stílus az alábbiak szerint hozható létre:
```c
static lv_style_t style1;                 /*Új stílus deklarálása. Ajánlott, hogy `static` legyen */
lv_style_copy(&style1, &lv_style_plain);  /*Egy beépített stílus másolása*/
style1.body.main_color = LV_COLOR_RED;          /*Fő szín*/
style1.body.grad_color = lv_color_hex(0xffd83c) /*Gradiens szín (narancssárga)*/
style1.body.radius = 3;
style1.text.color = lv_color_hex3(0x0F0)        /*Felirat szín color (zöld)*/
style1.text.font = &lv_font_dejavu_22;          /*Font megváltoztatása*/
...
```

Az objektumoknak új stílus a `lv_<típus>set_style(obj, LV_<TÍPUS>_STYLE_<NÉV>, &my_style)`  függvényekkel lehetséges. Például:
```c
lv_slider_set_style(slider1, LV_SLIDER_STYLE_BG, &slider_bg_style);
lv_slider_set_style(slider1, LV_SLIDER_STYLE_INDIC, &slider_indic_style);
lv_slider_set_style(slider1, LV_SLIDER_STYLE_KNOB, &slider_knob_style);
```

Ha egy objektum stílusa `NULL` akkor az a szülő stílusát örökli. Például a feliratok (label) stílusa alapértelmezetten `NULL`.  Így ha egy felirat egy gombon van, akkor az a gomb `style.text` tulajdonságait fogja használni.

Több információs [Stílus áttekintés](/overview/style) oldalon olvasható.

### Események
Events are used to inform the user if something has happened with an object. You can assign a callback to an object which will be called if the object is clicked, released, dragged, being deleted etc. It should look like this:

```c
lv_obj_set_event_cb(btn, btn_event_cb);                 /*Callback hozzárendelése egy gombhoz*/

...

void btn_event_cb(lv_obj_t * btn, lv_event_t event)
{
    if(event == LV_EVENT_CLICKED) {
        printf("Klikk\n");
    }
}
```

Learn more about the events in the [Event overview](/overview/event) section.


## Examples

### Gomb felirattal
```c
lv_obj_t * btn = lv_btn_create(lv_scr_act(), NULL);     /*Gomb létrehozása a jelenlegi képernyőre*/
lv_obj_set_pos(btn, 10, 10);                            /*Pozíció beállítása*/
lv_obj_set_size(btn, 100, 50);                          /*Méret beállítása*/
lv_obj_set_event_cb(btn, btn_event_cb);                 /*Callback hozzárendelése egy gombhoz*/

lv_obj_t * label = lv_label_create(btn, NULL);          /*Felirat létrehozása a gombon*/
lv_label_set_text(label, "Button");                     /*Felirat szövegének beállítása*/

...

void btn_event_cb(lv_obj_t * btn, lv_event_t event)
{
    if(event == LV_EVENT_CLICKED) {
        printf("Klikk\n");
    }
}
```
![](/misc/simple_button_example.*)

### Gomb stílusok
Stílusok hozzáadása az előző példában lévő gombhoz:
```c
static lv_style_t style_btn_rel;                        /*Egy változó a felengedett állapot stílusának*/
lv_style_copy(&style_btn_rel, &lv_style_plain);         /*Inicializálás egy beépített stílusból*/
style_btn_rel.body.border.color = lv_color_hex3(0x269);
style_btn_rel.body.border.width = 1;
style_btn_rel.body.main_color = lv_color_hex3(0xADF);
style_btn_rel.body.grad_color = lv_color_hex3(0x46B);
style_btn_rel.body.shadow.width = 4;
style_btn_rel.body.shadow.type = LV_SHADOW_BOTTOM;
style_btn_rel.body.radius = LV_RADIUS_CIRCLE;
style_btn_rel.text.color = lv_color_hex3(0xDEF);

static lv_style_t style_btn_pr;                         /*Egy változó a megnyomott állapot stílusának*/
lv_style_copy(&style_btn_pr, &style_btn_rel);           /*Inicializálás a felengedett stílusból*/
style_btn_pr.body.border.color = lv_color_hex3(0x46B);
style_btn_pr.body.main_color = lv_color_hex3(0x8BD);
style_btn_pr.body.grad_color = lv_color_hex3(0x24A);
style_btn_pr.body.shadow.width = 2;
style_btn_pr.text.color = lv_color_hex3(0xBCD);

lv_btn_set_style(btn, LV_BTN_STYLE_REL, &style_btn_rel);    /*A gomb felengedett stílusának beállítása*/
lv_btn_set_style(btn, LV_BTN_STYLE_PR, &style_btn_pr);      /*A gomb lenyomott stílusának beállítása*/
```

![](/misc/button_style_example.*)

### Csúszka és objektum igazítás
```c
lv_obj_t * label;

...

/* Csúszka létrehozása a képernyő közepére */
lv_obj_t * slider = lv_slider_create(lv_scr_act(), NULL);
lv_obj_set_width(slider, 200);                        /*Szélesség beállítása*/
lv_obj_align(slider, NULL, LV_ALIGN_CENTER, 0, 0);    /*A szülő (képernyő) közepére igazatás*/
lv_obj_set_event_cb(slider, slider_event_cb);         /*Event callback hozzárendelése*/

/* Felirat létrehozása a csúszka alá */
label = lv_label_create(lv_scr_act(), NULL);
lv_label_set_text(label, "0");
lv_obj_set_auto_realign(slider, true);
lv_obj_align(label, slider, LV_ALIGN_OUT_BOTTOM_MID, 0, 10);

...

void slider_event_cb(lv_obj_t * slider, lv_event_t event)
{
    if(event == LV_EVENT_VALUE_CHANGED) {
        static char buf[4];                                 /* max 3 bájt számoknak, +1 a záró nulla */
        snprintf(buf, 4, "%u", lv_slider_get_value(slider));
        lv_label_set_text(slider_label, buf);               /*Szöveg frissítése*/
    }
}
```

![](/misc/slider_example.*)

### Lista és témák
```c
/*A lista elemek feliratai*/
const char * txts[] = {"First", "Second", "Third", "Forth", "Fifth", "Sixth", NULL};

/* Egy téma inicializálása és beállítása. `LV_THEME_NIGHT` engedélyezve kell legyen az lv_conf.h-ben */
lv_theme_t * th = lv_theme_night_init(20, NULL);
lv_theme_set_current(th);

/*Egy lista létrehozása*/
lv_obj_t* list = lv_list_create(lv_scr_act(), NULL);
lv_obj_set_size(list, 120, 180);
lv_obj_set_pos(list, 10, 10);

/*Gombok hozzáadása*/
uint8_t i;
for(i = 0; txts[i]; i++) {
    lv_obj_t * btn = lv_list_add_btn(list, LV_SYMBOL_FILE, txts[i]);
    lv_obj_set_event_cb(btn, list_event);       /* Event függvény hozzárendelése*/
    lv_btn_set_toggle(btn, true);               /* Ki/be állalpotok engedélyezése*/
}

/* Egy másik téme inicializálása és aélkalmazása. `LV_THEME_MATERIAL` engedélyezve kell legyen lv_conf.h-ban.
 * Ha `LV_TEHE_LIVE_UPDATE  1` akkor az előző lista stílusa is frissülni fog.*/
th = lv_theme_material_init(210, NULL);
lv_theme_set_current(th);

/*Egy másik lista létrehozása*/
list = lv_list_create(lv_scr_act(), NULL);
lv_obj_set_size(list, 120, 180);
lv_obj_set_pos(list, 150, 10);

/*Gombok hozzáadása ugyanazzal a szöveggel*/
for(i = 0; txts[i]; i++) {
    lv_obj_t * btn = lv_list_add_btn(list, LV_SYMBOL_FILE, txts[i]);
    lv_obj_set_event_cb(btn, list_event);
    lv_btn_set_toggle(btn, true);
}

...

static void list_event(lv_obj_t * btn, lv_event_t e)
{
    if(e == LV_EVENT_CLICKED) {
        printf("%s\n", lv_list_get_btn_text(btn));
    }

}
```
![](/misc/list_theme_example.*)

###  LittlevGL használata Micropythonnal
Több információ a  [Micropython](/get-started/micropython) fejezetben olvasható.
```python
# Egy gomb és egy felirat létrehozása
scr = lv.obj()
btn = lv.btn(scr)
btn.align(lv.scr_act(), lv.ALIGN.CENTER, 0, 0)
label = lv.label(btn)
label.set_text("Button")

# Képernyő betöltése
lv.scr_load(scr)
```



## Közreműködés
LittlevGL uses the [Forum](https://forum.littlevgl.com) to ask and answer questions and [GitHub's Issue tracker](https://github.com/littlevgl/lvgl/issues) for development-related discussion (such as bug reports, feature suggestions etc.).

There are many opportunities to contribute to LittlevGL such as:
- **Segíts másoknak** a [Fórum](https://forum.littlevgl.com)-ban.
- **Inspirálj másokat** azzal, hogy hogy megosztod milyen projektben használtad a LittlevGL-t. Ezt a Fórun [My project](https://forum.littlevgl.com/c/my-projects) kategóriájában vagy a [References](https://blog.littlevgl.com/2018-12-26/references) blog posztban teheted meg.
- **Fejleszd és/vagy fordítsd le a dokumentációt.** A [Documentation](https://github.com/littlevgl/docs) repository-ban többet megtudhatsz erről.
- **Írj egy blog posztot** a tapasztalataidról. A [Blog](https://github.com/littlevgl/blog) repository-ban megtudhatod, hogyan.
- **Jelents és/vagy javíts hibákat** a [GitHub's issue tracker](https://github.com/littlevgl/lvgl/issues)-ében.
- **Segítsd a fejlesztést**. Nézd meg a  [Nyitott issue](https://github.com/littlevgl/lvgl/issues)-kat , különösön a [Help wanted](https://github.com/littlevgl/lvgl/issues?q=is%3Aissue+is%3Aopen+label%3A%22help+wanted%22) címkével ellátottakat, és mond el az véleményedet a témáról vagy implementáld az adott funkciót.

If you are interested in contributing to LittlevGL, then please read the guides below to get started.

```eval_rst
- `Contributing guide <https://blog.littlevgl.com/2018-12-06/contributing>`_
- `Coding style guide <https://github.com/littlevgl/lvgl/blob/master/docs/CODING_STYLE.md>`_

```

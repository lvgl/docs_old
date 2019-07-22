# Quick overview

Here you can learn the most important things about LittlevGL. 
You should read it first to get a general impression and read the detailed [Porting](/porting/index) and [Overview](/overview/index) sections after that.

## Add LittlevGL into your project

The steps below show how to setup LittlevGL on an embedded system with a display and a touchpad. 
You can use the [Simulators](/get-started/pc-simulator) to get ready to use projects which can be run on your PC. 

- [Download](https://littlevgl.com/download) or [Clone](https://github.com/littlevgl/lvgl) the library
- Copy the `lvgl` folder into your project
- Copy `lvgl/lv_conf_templ.h` as `lv_conf.h` next to the `lvgl` folder and set at least `LV_HOR_RES_MAX`, `LV_VER_RES_MAX` and `LV_COLOR_DEPTH`. 
- Include `lvgl/lvgl.h` where you need to use LittlevGL related functions.
- Call `lv_tick_inc(x)` every `x` milliseconds **in a Timer or Task** (`x` should be between 1 and 10). It is required for the internal timing of LittlevGL.
- Call `lv_init()`
- Create a display buffer for LittlevGL
```c
static lv_disp_buf_t disp_buf;
static lv_color_t buf[LV_HOR_RES_MAX * 10];                     /*Declare a buffer for 10 lines*/
lv_disp_buf_init(&disp_buf, buf, NULL, LV_HOR_RES_MAX * 10);    /*Initialize the display buffer*/
```
- Implement and register a function which can **copy a pixel array** to an area of your display:
```c
lv_disp_drv_t disp_drv;               /*Descriptor of a display driver*/
lv_disp_drv_init(&disp_drv);          /*Basic initialization*/
disp_drv.flush_cb = my_disp_flush;    /*Set your driver function*/
disp_drv.buffer = &disp_buf;          /*Assign the buffer to the display*/
lv_disp_drv_register(&disp_drv);      /*Finally register the driver*/
    
void my_disp_flush(lv_disp_t * disp, const lv_area_t * area, lv_color_t * color_p)
{
    int32_t x, y;
    for(y = area->y1; y <= area->y2; y++) {
        for(x = area->x1; x <= area->x2; x++) {
            set_pixel(x, y, *color_p);  /* Put a pixel to the display.*/
            color_p++;
        }
    }

    lv_disp_flush_ready(disp);         /* Indicate you are ready with the flushing*/
}
    
```
- Implement and register a function which can **read an input device**. E.g. for a touch pad:
```c
lv_indev_drv_init(&indev_drv);             /*Descriptor of a input device driver*/
indev_drv.type = LV_INDEV_TYPE_POINTER;    /*Touch pad is a pointer-like device*/
indev_drv.read_cb = my_touchpad_read;      /*Set your driver function*/
lv_indev_drv_register(&indev_drv);         /*Finally register the driver*/

bool my_touchpad_read(lv_indev_t * indev, lv_indev_data_t * data)
{
    static lv_coord_t last_x = 0;
    static lv_coord_t last_y = 0;

    /*Save the state and save the pressed coordinate*/
    data->state = touchpad_is_pressed() ? LV_INDEV_STATE_PR : LV_INDEV_STATE_REL; 
    if(data->state == LV_INDEV_STATE_PR) touchpad_get_xy(&last_x, &last_y);
   
    /*Set the coordinates (if released use the last pressed coordinates)*/
    data->point.x = last_x;
    data->point.y = last_y;

    return false; /*Return `false` because we are not buffering and no more data to read*/
}
```
- Call `lv_task_handler()` periodically every few milliseconds in the main `while(1)` loop, in Timer interrupt or in an Operation system task. 
It will redraw the screen if required, handle input devices etc. 


## Learn the basics

### Objects (Widgets)

The graphical elements like Buttons, Labels, Sliders, Charts etc are called objects in LittelvGL. Go to [Object types](/object-types/index) to see the full list of available types.

Every object has a parent object. The child object moves with the parent and if you delete the parent the children will be deleted too. Children can be visible only on their parent.

The *screen* are the "root" parents. To get the current screen call `lv_scr_act()`.

You can create a new object with `lv_<type>_create(parent, obj_to_copy)`. It will return an `lv_obj_t *` variable which should be used as a reference to the object to set its parameters. 
The first parameter is the desired *parent*, te second parameters can be an object to copy (`NULL` is unused). 
For example:
```c
lv_obj_t * slider1 = lv_slider_create(lv_scr_act(), NULL);
```

To set some basic attribute `lv_obj_set_<paramters_name>(obj, <value>)` function can be used. For example:
```c
lv_obj_set_x(btn1, 30);
lv_obj_set_y(btn1, 10);
lv_obj_set_size(btn1, 200, 50);
```

The objects has type specific parameters too which can be set by `lv_<type>_set_<paramters_name>(obj, <value>)` functions. For example:
```c
lv_slider_set_value(slider1, 70, LV_ANIM_ON);
```

To see the full API visit the documentation of the object types or the related header file (e.g. `lvgl/src/lv_objx/lv_slider.h`).

### Styles
Styles can be assigned to the objects to changed their appearance. A style describes the appearance of rectangle-like objects (like a button or slider), texts, images and lines at once. 

You can create a new style like this:
```c
static lv_style_t style1;                 /*Declare a new style. Should be `static`*/
lv_style_copy(&style1, &lv_style_plain);  /*Copy a buil-in style*/
style1.body.main_color = LV_COLOR_RED;          /*Main color*/
style1.body.grad_color = lv_color_hex(0xffd83c) /*Gradient color (orange)*/
style1.body.radius = 3;
style1.text.color = lv_color_hex3(0x0F0)        /*Label color (green)*/
style1.text.font = &lv_font_dejavu_22;          /*Change font*/
...
```

To set a new style for an object use the `lv_<type>set_style(obj, LV_<TYPE>_STYLE_<NAME>, &my_style)` functions. For example:
```c
lv_slider_set_style(slider1, LV_SLIDER_STYLE_BG, &slider_bg_style);
lv_slider_set_style(slider1, LV_SLIDER_STYLE_INDIC, &slider_indic_style);
lv_slider_set_style(slider1, LV_SLIDER_STYLE_KNOB, &slider_knob_style);
```

If an object's style is `NULL` then it will inherit its parent's style. For example, the labels' style are `NULL` by default. If you place them on a button then they will use the `style.text` properties from the button's style.

Learn more in [Style overview](/overview/style) section.

### Events
Events are used to inform the user if something has happened with an object. You can assign a callback to an object which will be called if the object is clicked, released, dragged, being deleted etc. It should look like this: 

```c
lv_obj_set_event_cb(btn, btn_event_cb);                 /*Assign a callback to the button*/

...

void btn_event_cb(lv_obj_t * btn, lv_event_t event)
{
    if(event == LV_EVENT_CLICKED) {
        printf("Clicked\n");
    }
}
```

Learn more about the events in the [Event overview](/overview/event) section. 


## Examples 

### Button with label
```c
lv_obj_t * btn = lv_btn_create(lv_scr_act(), NULL);     /*Add a button the current screen*/
lv_obj_set_pos(btn, 10, 10);                            /*Set its position*/
lv_obj_set_size(btn, 100, 50);                          /*Set its size*/
lv_obj_set_event_cb(btn, btn_event_cb);                 /*Assign a callback to the button*/

lv_obj_t * label = lv_label_create(btn, NULL);          /*Add a label to the button*/
lv_label_set_text(label, "Button");                     /*Set the labels text*/

...

void btn_event_cb(lv_obj_t * btn, lv_event_t event)
{
    if(event == LV_EVENT_CLICKED) {
        printf("Clicked\n");
    }
}
```
![](/misc/simple_button_example.*)

### Button with styles
Add styles to the previously button from the previous example
```c
static lv_style_t style_btn_rel;                        /*A variable to store the released style*/
lv_style_copy(&style_btn_rel, &lv_style_plain);         /*Initialize from a built-in style*/
style_btn_rel.body.border.color = lv_color_hex3(0x269);
style_btn_rel.body.border.width = 1;
style_btn_rel.body.main_color = lv_color_hex3(0xADF);
style_btn_rel.body.grad_color = lv_color_hex3(0x46B);
style_btn_rel.body.shadow.width = 4;
style_btn_rel.body.shadow.type = LV_SHADOW_BOTTOM;
style_btn_rel.body.radius = LV_RADIUS_CIRCLE;
style_btn_rel.text.color = lv_color_hex3(0xDEF);

static lv_style_t style_btn_pr;                         /*A variable to store the pressed style*/
lv_style_copy(&style_btn_pr, &style_btn_rel);           /*Initialize from the released style*/
style_btn_pr.body.border.color = lv_color_hex3(0x46B);
style_btn_pr.body.main_color = lv_color_hex3(0x8BD);
style_btn_pr.body.grad_color = lv_color_hex3(0x24A);
style_btn_pr.body.shadow.width = 2;
style_btn_pr.text.color = lv_color_hex3(0xBCD);

lv_btn_set_style(btn, LV_BTN_STYLE_REL, &style_btn_rel);    /*Set the button's released style*/
lv_btn_set_style(btn, LV_BTN_STYLE_PR, &style_btn_pr);      /*Set the button's pressed style*/
```

![](/misc/button_style_example.*)

### Slider and object alignment
```c
lv_obj_t * label;

...

/* Create a slider in the center of the display */
lv_obj_t * slider = lv_slider_create(lv_scr_act(), NULL);
lv_obj_set_width(slider, 200);                        /*Set the width*/
lv_obj_align(slider, NULL, LV_ALIGN_CENTER, 0, 0);    /*Align to the center of the parent (screen)*/
lv_obj_set_event_cb(slider, slider_event_cb);         /*Assign an event function*/

/* Create a label below the slider */
label = lv_label_create(lv_scr_act(), NULL);
lv_label_set_text(label, "0");
lv_obj_set_auto_realign(slider, true);
lv_obj_align(label, slider, LV_ALIGN_OUT_BOTTOM_MID, 0, 10);

...

void slider_event_cb(lv_obj_t * slider, lv_event_t event)
{
    if(event == LV_EVENT_VALUE_CHANGED) {
        static char buf[4];                                 /* max 3 bytes  for number plus 1 null terminating byte */
        snprintf(buf, 4, "%u", lv_slider_get_value(slider));
        lv_label_set_text(slider_label, buf);               /*Refresh the text*/
    }
}
```

![](/misc/slider_example.*)

### List and themes
```c
/*Texts of the list elements*/
const char * txts[] = {"First", "Second", "Third", "Forth", "Fifth", "Sixth", NULL};

/* Initialize and set a theme. `LV_THEME_NIGHT` needs to enabled in lv_conf.h. */
lv_theme_t * th = lv_theme_night_init(20, NULL);
lv_theme_set_current(th);

/*Create a list*/
lv_obj_t* list = lv_list_create(lv_scr_act(), NULL);
lv_obj_set_size(list, 120, 180);
lv_obj_set_pos(list, 10, 10);

/*Add buttons*/
uint8_t i;
for(i = 0; txts[i]; i++) {
    lv_obj_t * btn = lv_list_add_btn(list, LV_SYMBOL_FILE, txts[i]);
    lv_obj_set_event_cb(btn, list_event);       /*Assign event function*/
    lv_btn_set_toggle(btn, true);               /*Enable on/off states*/
}

/* Initialize and set an other theme. `LV_THEME_MATERIAL` needs to enabled in lv_conf.h.
 * If `LV_TEHE_LIVE_UPDATE  1` then the previous list's style will be updated too.*/
th = lv_theme_material_init(210, NULL);
lv_theme_set_current(th);

/*Create an other list*/
list = lv_list_create(lv_scr_act(), NULL);
lv_obj_set_size(list, 120, 180);
lv_obj_set_pos(list, 150, 10);

/*Add buttons with the same texts*/
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

### Use LittlevGL from Micropython
Learn more about [Micropython](/get-started/micropython).
```python
# Create a Button and a Label
scr = lv.obj()
btn = lv.btn(scr)
btn.align(lv.scr_act(), lv.ALIGN.CENTER, 0, 0)
label = lv.label(btn)
label.set_text("Button")

# Load the screen
lv.scr_load(scr)
```



## Contributing
To ask questions please use the [Forum](https://forum.littlevgl.com).
For development-related things (bug reports, feature suggestions) use [GitHub's Issue tracker](https://github.com/littlevgl/lvgl/issues). 

If you are interested in contributing to LittlevGL you can
- **Help others** in the [Forum](https://forum.littlevgl.com).
- **Inspire people** by speaking about your project in [My project](https://forum.littlevgl.com/c/my-projects) category in the Forum or add it to the [References](https://blog.littlevgl.com/2018-12-26/references) post
- **Improve and/or translate the documentation.** Go to the [Documentation](https://github.com/littlevgl/docs) repository to learn more
- **Write a blog post** about your experiences. See how to do it in the [Blog](https://github.com/littlevgl/blog) repository
- **Report and/or fix bugs** in [GitHub's issue tracker](https://github.com/littlevgl/lvgl/issues)
- **Help in the developement**. Check the [Open issues](https://github.com/littlevgl/lvgl/issues) especially the ones with [Help wanted](https://github.com/littlevgl/lvgl/issues?q=is%3Aissue+is%3Aopen+label%3A%22help+wanted%22) label and tell your ideas about a topic or implement a feature.

It should be useful to read the
- [Contributing guide](https://blog.littlevgl.com/2018-12-06/contributing)
- [Coding style guide](https://github.com/littlevgl/lvgl/blob/master/docs/CODING_STYLE.md)


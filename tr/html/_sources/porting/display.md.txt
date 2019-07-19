```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/tr/porting/display.md
```
# Display interface

To set up a display an `lv_disp_buf_t` and an `lv_disp_drv_t` variable has to be initialized. 
- **lv_disp_buf_t** contains internal graphics buffer(s). 
- **lv_disp_drv_t** contains callback functions to interact with the display and manipulate drawing related things. 


## Display buffer 

`lv_disp_buf_t` can be initialized like this:
```c
    /*A static or global variable to store the buffers*/
    static lv_disp_buf_t disp_buf;
    
    /*Static or global buffer(s). The second buffer is optional*/
    static lv_color_t buf_1[MY_DISP_HOR_RES * 10];
    static lv_color_t buf_2[MY_DISP_HOR_RES * 10];
    
    /*Initialize `disp_buf` with the buffer(s) */
    lv_disp_buf_init(&disp_buf, buf_1, buf_2, MY_DISP_HOR_RES*10);
```

There are there possible configurations regarding the buffer size:
1. **One buffer** LittlevGL draws the content of the screen into a buffer and sends it to the display. 
The buffer can be smaller than the screen. In this case, the larger areas will be redrawn in multiple parts. 
If only small areas changes (e.g. button press) then only those areas will be refreshed.
2. **Two non-screen-sized buffers** having two buffers LittlevGL can draw into one buffer while the content of the other buffer is sent to display in the background.
DMA or other hardware should be used to transfer the data to the display to let the CPU draw meanwhile.
This way the rendering and refreshing of the display become parallel. 
Similarly to the *One buffer* LittlevGL will draw the display's content in chunks if the buffer is smaller than the area to refresh.
3. **Two screen-sized buffers**.
In contrast to *Two non-screen-sized buffers* LittlevGL will always provide the whole screen's content not only chunks. 
This way the driver can simply change the address of the frame buffer to the buffer received from LittlevGL.
Therefore this method works the best when the MCU has an LCD/TFT interface and the frame buffer is just a location in the RAM.


## Display driver

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
    /*The most simple case (but also the slowest) to put all pixels to the screen one-by-one*/
    int32_t x, y;
    for(y = area->y1; y <= area->y2; y++) {
        for(x = area->x1; x <= area->x2; x++) {
            put_px(x, y, *color_p)
            color_p++;
        }
    }

    /* IMPORTANT!!!
     * Inform the graphics library that you are ready with the flushing*/
    lv_disp_flush_ready(disp);
}

void my_gpu_fill_cb(lv_disp_drv_t * disp_drv, lv_color_t * dest_buf, const lv_area_t * dest_area, const lv_area_t * fill_area, lv_color_t color);
{
    /*It's an example code which should be done by your GPU*/
    uint32_t x,y;
    for(y = 0; i < length; i++) {
        dest[i] = color;
    }
}

void my_gpu_blend_cb(lv_disp_drv_t * disp_drv, lv_color_t * dest, const lv_color_t * src, uint32_t length, lv_opa_t opa)
{
    /*It's an example code which should be done by your GPU*/
    uint32_t i;
    for(i = 0; i < length; i++) {
        dest[i] = lv_color_mix(dest[i], src[i], opa);
    }
}

void my_rounder_cb(lv_disp_drv_t * disp_drv, lv_area_t * area)
{
  /* Update the areas as needed. Can be only larger.
   * For example to always have lines 8 px height:*/
   area->y1 = area->y1 & 0x07;
   area->y2 = (area->y2 & 0x07) + 8; 
}

void my_set_px_cb(lv_disp_drv_t * disp_drv, uint8_t * buf, lv_coord_t buf_w, lv_coord_t x, lv_coord_t y, lv_color_t color, lv_opa_t opa)
{
    /* Write to the buffer as required for the display. 
     * Write only 1 bit for monochrome displays mapped vertically:*/
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


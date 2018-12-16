_Written for v5.2_

## System architecture

![System architecture of Littlev Graphics Library](http://docs.littlevgl.com/img/sys.png)  

**Application**  

Your application which creates the GUI and handles the specific tasks.

**LittlevGL**  

The graphics library itself. Your application can communicate with the library to create a GUI. It contains a HAL (Hardware Abstraction Layer) interface to register your display and input device drivers. 

**Driver**  

Besides your specific drivers, it contains functions to drive your display, optionally to a GPU and to read the touchpad or buttons. 

* * *

There are **two typical hardware set-ups** depending on the MCU has an LCD/TFT driver periphery or not. In both cases, a frame buffer will be required to store the current image of the screen. 

**MCU with TFT/LCD driver**  

If your MCU has a TFT/LCD driver periphery then you can connect a display directly via RGB interface. In this case, the frame buffer can be in the internal RAM (if the MCU has enough RAM) or in the external RAM (if the MCU has a memory interface).  

**External display controller**  

If the MCU doesn't have TFT/LCD driver then an external display controller (E.g. SSD1963, SSD1306, ILI9341) has to be used. In this case, the MCU can communicate with the display controller via Parallel port, SPI or sometimes I2C. The frame buffer is usually located in the display controller which saves a lot of RAM for the MCU. 

* * *

## Requirements

- **16, 32 or 64 bit** microcontroller or processor
- **16 MHz** clock speed
- **8 kB RAM** for static data and **&gt;2 KB RAM** for dynamic data (graphical objects)
- **64 kB program memory** (flash)
- **Optionally ~1/10 screen sized memory** for internal buffering (at 240 × 320, 16 bit colors it means 15 kB)

The LittlevGL is designed to be highly portable and to not use any **external resources**:

- No external RAM required (but supported)
- No float numbers are used
- No GPU needed (but supported)
- Only a single frame buffer is required located in:
    - Internal RAM or
    - External RAM or
    - External display controller's memory

If you would like to **reduce** the required **hardware resources** you can:

- Disable the unused object types to save RAM and ROM
- Change the size of the graphical buffer to save RAM
- Use simpler styles to reduce the rendering time

* * *

## Project set-up

### Get the library

The Littlev Graphics Library is available on GitHub: [https://github.com/littlevgl/lvgl](https://github.com/littlevgl/lvgl). You can clone or download the latest version of the library from here or you can use the [Download](https://littlevgl.com/download) page as well. 

The graphics library is the **lvgl** directory which should be copied into your project.

### Config file

There is a configuration header file for LittlevGL: **lv_conf.h**. It sets the library's basic behavior in compile time,  disable unused modules and features and adjust the size of memory buffers etc.

Copy _lvgl/lv_conf_templ.h_ next to the _lvgl_ directory and rename it to _lv_conf.h_. Open the file and delete the first _#if_ and the last _#endif_ to enable the content. In the config file comments explain the meaning of the options. Check at least these three config options and modify them according to your hardware:

1. **LV_HOR_RES** Your display's horizontal resolution
2. **LV_VER_RES** Your display's vertical resolution
3. **LV_COLOR_PETH** 8 for (RG332), 16 for (RGB565) or 32 for (RGB888 and ARGB8888). 

### Initialization

In order to use the graphics library you have to initialize it and the other components too. To order of the initialization is:

1. Call _lv_init()_
2. Initialize your drivers
3. Register the display and input devices drivers in LittlevGL. (see below) 

* * *

## Porting the library

To adopt LittlevGL into your project firstly you have to provide some functions and register them in the graphics library. 

### Display interface

To set up a display an **lv_disp_drv_t** variable has to be initialized:

```c
lv_disp_drv_t disp_drv;
lv_disp_drv_init(&disp_drv); /*Basic initialization*/
disp_drv. ...=...; /*Initialize the fields here. See below.*/
disp_drv_register(&disp_drv); /*Register the driver in LittlevGL*/
```

You can configure the driver for different operation modes. To learn more about the drawing modes visit [Drawing and rendering](/Drawing).

#### Internal buffering (VDB)

The graphics library works with an internal buffering mechanism to create advances graphics features with only one frame buffer. The internal buffer is called VDB (Virtual Display Buffer) and its size can be adjusted in lv_conf.h with _LV_VDB_SIZE_. When _LV_VDB_SIZE_ &gt; 0 then the internal buffering is used and you have to provide a function which flushes the buffer's content to your display:

```c
disp_drv.disp_flush = my_disp_flush;
...
void my_disp_flush(int32_t x1, int32_t y1, int32_t x2, int32_t y2, const lv_color_t* color_p)
{
    /*TODO Copy 'color_p' to the specified area*/
    /*Call 'lv_fluh_ready()' when ready*/lv_flush_ready();
}
```

In the flush function, you can use DMA or any hardware to do the flushing in the background, but when the flushing is ready you have to 
call 
```c
lv_flush_ready();
```
##### Hardware acceleration (GPU)

First of all using GPU is totally optional. But if your MCU supports graphical acceleration then you can use it. The _mem_blend_ and _mem_fill_ fields of the display driver is used to interface with a GPU. 
The GPU related functions can be used only if internal buffering (VDB) is enabled.

```c
disp_drv.mem_blend = my_mem_blend;     /*Blends two color arrays using opacity*/
disp_drv.mem_fill = my_mem_fill;       /*Fills an array with a color*/
...
void my_mem_blend(lv_color_t* dest, constlv_color_t* src, uint32_t length, lv_opa_t opa)
{
  /*TODO Copy 'src' to 'dest' but blend it with 'opa' alpha */
}

void my_mem_fill(lv_color_t* dest, uint32_t length, lv_color_t color)
{
  /*TODO Fill 'length' pixels in 'dest' with 'color'*/
}
```

##### Unbuffered drawing

It is possible to draw directly to a frame buffer when the internal buffering is disabled (LV_VDB_SIZE = 0).

```c
disp_drv.disp_fill = my_disp_fill;/*Fill an area in the frame buffer*/
disp_drv.disp_map = my_disp_map;/*Copy a color_map (e.g. image) into the frame buffer*/
...
void my_disp_map(int32_t x1,int32_t y1,int32_t x2,int32_t y2,constlv_color_t* color_p)
{
  /*TODO Copy 'color_p' to the specified area*/
}

voidmy_disp_fill(int32_t x1,int32_t y1,int32_t x2,int32_t y2,lv_color_t color)
{
  /*TODO Fill the specified area with 'color'*/
}
```

Keep in mind this way during refresh some artifacts can be visible because the layers are drawn after each other. And some high-level graphics features like anti-aliasing, opacity or shadows aren't available in this configuration. 

If you use an external display controller which supports accelerated filling (e.g. RA8876) then you can use this feature in _disp_fill()_

### Input device interface

To set up an input device an **lv_indev_drv_t** variable has to be initialized:

```c
lv_indev_drv_t indev_drv;lv_indev_drv_init(&indev_drv);  /*Basic initialization*/
indev_drv.type =.../*See below.*/
indev_drv.read =.../*See below.*/
lv_indev_drv_register(&indev_drv);  /*Register the driver in LittlevGL*/
```

**type** can be 
- LV_INDEV_TYPE_POINTER: touchpad or mouse
- LV_INDEV_TYPE_KEYPAD: keyboard
- LV_INDEV_TYPE_ENCODER: left, right, push
- LV_INDEV_TYPE_BUTTON: external buttons pressing the screen
  
**read** is a function pointer which will be called periodically to report the current state of an input device. It can also buffer data and return _false_ when no more data to be read or _true_ when the buffer is not empty.

To learn more about input devices visit [Input devices](Input-devices).

####  Touchpad, mouse or any pointer

```c
indev_drv.type = LV_INDEV_TYPE_POINTER;
indev_drv.read = my_input_read;
```

The read function should look like this:

```c
bool my_input_read(lv_indev_data_t*data)
{
    data->point.x = touchpad_x;   
    data->point.y = touchpad_y;
    data->state = LV_INDEV_STATE_PR or LV_INDEV_STATE_REL;
    return false; /*No buffering so no more data read*/
}
```

> **IMPORTANT NOTE:** Touchpad drivers must return the last X/Y coordinates even when the state is `LV_INDEV_STATE_REL`.

#### Keypad or keyboard 
```c
indev_drv.type = LV_INDEV_TYPE_KEYPAD;
indev_drv.read = my_input_read;
```
The read function should look like this:
```c
bool keyboard_read(lv_indev_data_t*data){
  data->key = last_key();            /*Set the last pressed or released key*/
  if(key_pressed()){
    data->state = LV_INDEV_STATE_PR;
  }
  else{
    data->state = LV_INDEV_STATE_REL;
  }
  return false; /*No buffering so no more data read*/
}
```
To use a keyboard:
-  Register a _read_ function (like above) with _LV_INDEV_TYPE_KEYPAD_ type.
- _USE_LV_GROUP_ has to be enabled in _lv_conf.h_
-  An object group has to be created: _lv_group_create()_ and objects have to be added: _lv_group_add_obj()_
-  The created group has to be assigned to an input device: _lv_indev_set_group(my_indev, group1);_
-  Use _LV_GROUP_KEY_..._ to navigate among the objects in the group

Visit [Touchpad-less navigation](Input-devices) to learn more.

#### Encoder 
With an encoder you can do 4 things:
1. press its button
2. long press its button
3. turn left
4. turn right

By turning the encoder you can focus on the next/previous object. When you press the encoder on a simple object (like a button), it will be clicked. If you press the encoder on a complex object (like a list, message box etc.) the object will go to edit mode where by turning the encoder you can navigate inside the object. To leave edit mode press long the button.

```c
indev_drv.type = LV_INDEV_TYPE_ENCODER;
indev_drv.read = my_input_read;
```
The read function should look like this:
```c
bool encoder_read(lv_indev_data_t*data){
  data->enc_diff = enc_get_new_moves();
  if(enc_pressed()){
    data->state = LV_INDEV_STATE_PR;
  }
  else{
    data->state = LV_INDEV_STATE_REL;
  }

  return false; /*No buffering so no more data read*/
}
```

- To use an `ENCODER`, similarly to the `KEYPAD`, the objects should be added to groups

#### Button 
```c
indev_drv.type = LV_INDEV_TYPE_BUTTON;
indev_drv.read = my_input_read;
```
The read function should look like this:
```c
bool button_read(lv_indev_data_t*data){
    static uint32_t last_btn = 0;   /*Store the last pressed button*/ 
    int btn_pr = my_btn_read();     /*Get the ID (0,1,2...) of the pressed button*/
    if(btn_pr >= 0) {               /*Is there a button press?*/  
       last_btn = btn_pr;           /*Save the ID of the pressed button*/
       data->state = LV_INDEV_STATE_PR;  /*Set the pressed state*/
    } else {
       data->state = LV_INDEV_STATE_REL; /*Set the released state*/
    }
  
    data->btn = last_btn;            /*Set the last button*/         
   
    return false;                    /*No buffering so no more data read*/
}
```

- The buttons need to be assigned to pixels on the screen using `lv_indev_set_button_points(indev, points_array)`. Where _points_array_ look like `const lv_point_t points_array[] =  { {12,30},{60,90}, ...}`   

### Tick interface

The LittlevGL uses a system tick. Call the `lv_tick_inc(tick_period)` function periodically and tell the call period in milliseconds. For example if called in every milliseconds: `lv_tick_inc(1)`.

### Task handling

To handle the tasks of LittlevGL you need to call `lv_task_handler()` periodically in one of the following:

- _while(1)_ of _main()_ function 
- timer interrupt periodically
- an OS task periodically

The timing is not critical but it should be about 5 milliseconds to keep the system responsive.

Example:
```c
while(1) {
  lv_task_handler();
  my_delay_ms(5);
}
```

The MCU can go to **sleep** when no user input happens. In this case the main `while(1)` should look like this:
```c
while(1) {
  /*Normal operation in 1 sec*/ 
  if(lv_indev_get_inactive_time(NULL) < 1000) {    
	lv_task_handler();
  } 
  /*Sleep after 1 sec inactivity*/
  else {                                         
	timer_stop();               /*Stop the timer where lv_tick_inc() is called*/
	sleep();		    /*Sleep the MCU*/
  }
  my_delay_ms(5);
}
```

You should also add these lines to your input device read function if a press happens:
```c
/*Force task execution on wake-up*/
lv_tick_inc(LV_REFR_PERIOD);
timer_start();               /*Restart the timer where lv_tick_inc() is called*/
lv_task_handler();
``` 

In addition to `lv_indev_get_inactive_time()` you can check `lv_anim_count_running()` to see if every animations are finished.

### Using with an operating system
LittlevGL is **not thread-safe**. Despite it, it's quite simple to use LittlevGL inside an operating system. 

The **simple scenario** is to don't use the operating system's tasks but use `lv_task`s. An _lv_task_ is a function called periodically in `lv_task_handler`. In the _lv_task_ you can get the state of the sensors, buffers etc and call LittlevGL functions to refresh the GUI. To create an _lv_task_ use: `lv_task_create(my_func, period_ms, LV_TASK_PRIO_LOWEST/LOW/MID/HIGH/HIGHEST, custom_ptr)`

If you need to **use other task or threads** you need one mutex which should be taken before calling `lv_task_handler` and released after it. In addition, you have to use to that mutex in other tasks and threads around every LittlevGL (`lv_...`) related code. This way you can use LittlevGL in a real multitasking environment. Just use a mutex to avoid concurrent calling of LittlevGL functions.

### Porting example

Here you will find an example porting code: [Porting tutorial](https://github.com/littlevgl/lv_examples/blob/beta/lv_tutorial/0_porting/lv_tutorial_porting.c).

```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/en/index.md
```

```eval_rst
.. include:: /lang.rst

PDF version: :download:`LittlevGL.pdf <LittlevGL.pdf>`
```

# Welcome to LittlevGL's documentation!

![](/misc/lv_theme_intro.png "LittlevGL cover")

LittlevGL is a free and open-source graphics library providing everything you need to create embedded GUI with easy-to-use graphical elements, beautiful visual effects and low memory footprint.

**[Website](https://littlevgl.com) &nbsp; · &nbsp;** 
**[GitHub](https://github.com/littlevgl/lvgl) &nbsp; · &nbsp;** 
**[Forum](https://forum.littlevgl.com) &nbsp; · &nbsp;** 
**[Live demo](https://littlevgl.com/live-demo) &nbsp; · &nbsp;** 
**[Simulator](/get-started/pc-simulator) &nbsp; · &nbsp;** 
**[Blog](https://blog.littlevgl.com/)**

## Key features
- Powerful building blocks buttons, charts, lists, sliders, images etc
- Advanced graphics with animations, anti-aliasing, opacity, smooth scrolling
- Various input devices touchpad, mouse, keyboard, encoder etc
- Multi-language support with UTF-8 encoding
- Multi-display support, i.e. use more TFT, monochrome displays simultaneously
- Fully customizable graphical elements
- Hardware independent to use with any microcontroller or display
- Scalable to operate with little memory (64 kB Flash, 16 kB RAM)
- OS, External memory and GPU supported but not required
- Single frame buffer operation even with advanced graphical effects
- Written in C for maximal compatibility (C++ compatible)
- Simulator to start embedded GUI design on PC without embedded hardware
- Tutorials, examples, themes for rapid GUI design
- Documentation online and offline
- Free and open-source under MIT license

## Requirements
- 16, 32 or 64 bit microcontroller or processor
- &gt; 16 MHz clock speed is recommended
- Flash/ROM: &gt; 64 kB for the very essential components (&gt; 180 kB is recommended)
- RAM: 
  - Static RAM usage: ~8..16 kB depending on the used features and objects types
  - Stack: &gt; 2kB (&gt; 4 kB is recommended)
  - Dynamic data (heap): &gt; 4 KB (&gt; 16 kB is recommended if using several objects).
    Set by `LV_MEM_SIZE` in *lv_conf.h*. 
  - Display buffer:  &gt; *"Horizontal resolution"* pixels (&gt; 10 &times; *"Horizontal resolution"* is recommended) 
-  C99 or newer compiler
- Basic C (or C++) knowledge: [pointers](https://www.tutorialspoint.com/cprogramming/c_pointers.htm), [structs](https://www.tutorialspoint.com/cprogramming/c_structures.htm), [callbacks](https://www.geeksforgeeks.org/callbacks-in-c/).

*Note that the memory usage might vary depending on the architecture, compiler and build options.*


## FAQ

### Where to get started?
- For a general overview of LittlevGL visit [littlevgl.com](https://littlevgl.com)
- Go to the [Get started](/get-started/index) section to try Live demos in you browser, learn about the Simulator(s) and learn the basics of LittlevGL.
- A detailed porting guide can be found in the [Porting](/porting/index) section.
- To learn how LittlevGL works go to the [Overview](/overview/index).
- To read tutorials or share your own experiences go to the [Blog](https://blog.littlevgl.com)
- To see the source code of the library check it on GitHub: [https://github.com/littlevgl/lvgl/](https://github.com/littlevgl/lvgl/).


### Where can I ask questions?
To ask questions in the Forum: [https://forum.littlevgl.com/](https://forum.littlevgl.com/).

We use [GitHub issues](https://github.com/littlevgl/lvgl/issues) for development related discussion. So you should use them only if your question or issue is tightly related to the development of the library. 


### Is my MCU/hardware supported?
Every MCU which is capable of driving a display via Parallel port, SPI, RGB interface or anything else and fulfills the [Requirements](#Requirements) is supported by LittlevGL. 
It includes 
- "Common" MCUs like STM32F, STM32H, NXP Kinetis, LPC, iMX, dsPIC33, PIC32 etc. 
- Bluetooth, GSM, WiFi modules like Nordic NRF and Espressif ESP32
- Linux frame buffer like /dev/fb0 which includes Single board computers too like Raspberry
- and anything else with a strong enough MCU and a periphery to drive a display

### Is my display supported?
LittlevGL needs just one simple driver to copy an array of pixels to a given area of the display. If you can do this with your display then you can use that display with LittlevGL. 
It includes
- TFTs with 16 or 24 bit color depth 
- Monitors with HDMI port
- Small monochrome displays
- Gray-scale displays
- LED matrices
- or any other display where you can control the color/state of the pixels

See the [Porting](/porting/display) section to learn more.

### Is LittlevGL free? How can I use it in a commercial product?
LittlevGL comes with MIT license which means you can download and use it for any purpose you want without any obligations.

### Nothing happens, my display driver is not called. What have I missed?
Be sure you are calling `lv_tick_inc(x)` in an interrupt and `lv_task_handler()` in your main `while(1)`.

Learn more in the [Tick](/porting/tick) and [Task handler](/porting/task-handler) section.

### Why the display driver is called only one? Only the upper part of the display is refreshed. 
Be sure you are calling `lv_disp_flush_ready(drv)` at the end of you *display flush callback*. 

### Why I see only garbage on the screen?
Probably there a bug in your display driver. Try the following code without using LittlevGL:

```c
#define BUF_W 20
#define BUF_H 10
lv_color_t buf[BUF_W * BUF_H];
lv_color_t * buf_p = buf;
uint16_t x, y;
for(y = 0; y < BUF_H; y++) {
    lv_color_t c = lv_color_mix(LV_COLOR_BLUE, LV_COLOR_RED, (y * 255) / BUF_H);
    for(x = 0; x < BUF_W; x++){
        (*buf_p) =  c;
        buf_p++;
    }
}

lv_area_t a;
a.x1 = 10;
a.y1 = 40;
a.x2 = a.x1 + BUF_W - 1;
a.y2 = a.y1 + BUF_H - 1;
my_flush_cb(NULL, &a, buf);
```

### Why I see non-sense colors on the screen? 
Probably LittlevGL's the color format is not compatible with your displays color format. Check `LV_COLOR_DEPTH` in *lv_conf.h*.

If you are using 16 bit colors with SPI (or other byte-oriented) interface probably you need to set `LV_COLOR_16_SWAP  1` in *lv_conf.h*. It swaps the upper and lower bytes of the pixels.

### How to speed up my UI?
- Turn on compiler optimization
- Increase the size of the display buffer
- Use 2 display buffers and flush the buffer with DMA (or similar periphery) in the background 
- Increase the clock speed of the SPI or Parallel port if you use them to drive the display
- If you display has SPI port consider changing to a model with parallel because it has much higher throughput
- Keep the display buffer in the internal RAM (not external SRAM) because LittlevGL uses it a lot and it should have a small access time
 
### How to reduce flash/ROM usage?
You can disable all the unused feature (like animations, file system, GPU etc) and object types in *lv_conf.h*.

IF you are using GCC you can add 
- `-fdata-sections -ffunction-sections` compiler flags 
- `--gc-sections` linker flag

to remove unused functions and variables.
`
### How to reduce the RAM usage
- Lower the size of the *Display buffer* 
- Reduce `LV_MEM_SIZE` in *lv_conf.h*. This memory used when you create objects like buttons, labels, etc
- To work with lower `LV_MEM_SIZE` you can create the objects only when required and deleted them when they are not required anymore.
 
### How to work with an operating system?

To work with an operating system where tasks can interrupt each other you should protect LittlevGL related function calls with a mutex. See the [Operation system](/porting/os) section to learn more.

### How to contribute to LittlevGL?
There are several ways to contribute to LittlevGL:
- write a few lines about your project to inspire others
- answer other’s questions
- report and/or fix bugs
- suggest and/or implement new features
- improve and/or translate the documentation
- write a blog post about your experiences

To learn more see [Contributing guide](https://blog.littlevgl.com/2018-12-06/contributing)


### Where can I find the documentation of the previous version (v5.3)?

You can download it here and open offline:
```eval_rst
:download:`Docs-v5-3.zip <docs_v5_3.zip>`
```

```eval_rst
.. toctree::
   :maxdepth: 2
   
   get-started/index
   porting/index
   overview/index
   object-types/index

```

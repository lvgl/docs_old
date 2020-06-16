```eval_rst
:github_url: https://github.com/lvgl/docs/blob/master/v7/en/intro/index.md
```

# Introduction

LVGL (Light and Versatile Graphic Library) is a free and open-source graphics library providing everything you need to create embedded GUI with easy-to-use graphical elements, beautiful visual effects and low memory footprint.


## Key features
- Powerful building blocks such as buttons, charts, lists, sliders, images etc.
- Advanced graphics with animations, anti-aliasing, opacity, smooth scrolling
- Various input devices such as touchpad, mouse, keyboard, encoder etc.
- Multi-language support with UTF-8 encoding
- Multi-display support, i.e. use more TFT, monochrome displays simultaneously
- Fully customizable graphic elements
- Hardware independent to use with any microcontroller or display
- Scalable to operate with little memory (64 kB Flash, 16 kB RAM)
- OS, External memory and GPU supported but not required
- Single frame buffer operation even with advanced graphical effects
- Written in C for maximal compatibility (C++ compatible)
- Simulator to start embedded GUI design on a PC without embedded hardware
- Binding to MicroPython
- Tutorials, examples, themes for rapid GUI design
- Documentation is available as online and offline
- Free and open-source under MIT license

## Requirements
Basically, every modern controller  (which is able to drive a display( is suitable to run LVGL. The minimal requirements are:
- 16, 32 or 64 bit microcontroller or processor
- &gt; 16 MHz clock speed is recommended
- Flash/ROM: &gt; 64 kB for the very essential components (&gt; 180 kB is recommended)
- RAM: 
  - Static RAM usage: ~2 kB depending on the used features and objects types
  - Stack: &gt; 2kB (&gt; 8 kB is recommended)
  - Dynamic data (heap): &gt; 2 KB (&gt; 16 kB is recommended if using several objects).
    Set by `LV_MEM_SIZE` in *lv_conf.h*. 
  - Display buffer:  &gt; *"Horizontal resolution"* pixels (&gt; 10 &times; *"Horizontal resolution"* is recommended) 
- One frame buffer in the MCU or in external display controller
- C99 or newer compiler
- Basic C (or C++) knowledge: [pointers](https://www.tutorialspoint.com/cprogramming/c_pointers.htm), [structs](https://www.tutorialspoint.com/cprogramming/c_structures.htm), [callbacks](https://www.geeksforgeeks.org/callbacks-in-c/)

*Note that the memory usage might vary depending on the architecture, compiler and build options.*

## FAQ

### Where to get started?
- For a general overview of LVGL visit [lvgl.io](https://lvgl.io)
- Go to the [Get started](/get-started/index) section to learn the basics of LVGL
- A detailed porting guide can be found in the [Porting](/porting/index) section
- To learn how LVGL works go to the [Overview](/overview/index)
- To see the source code of the library check it on GitHub: [https://github.com/lvgl/lvgl/](https://github.com/lvgl/lvgl/)
- To read tutorials or share your own experiences go to the [Blog](https://blog.lvgl.io)


### Where can I ask questions?
You ask questions in the Forum: [https://forum.lvgl.io/](https://forum.lvgl.io/).

We use [GitHub issues](https://github.com/lvgl/lvgl/issues) for development related discussion. 
So you should use them only if your question or issue is tightly related to the development of the library. 

### Is my MCU/hardware supported?
Every MCU which is capable of driving a display via Parallel port, SPI, RGB interface or anything else and fulfills the [Requirements](#Requirements) is supported by LLVGL.

It includes:
- "Common" MCUs like STM32F, STM32H, NXP Kinetis, LPC, iMX, dsPIC33, PIC32 etc. 
- Bluetooth, GSM, WiFi modules like Nordic NRF and Espressif ESP32
- Linux frame buffer like /dev/fb0 which includes Single board computers too like Raspberry Pi
- And anything else with a strong enough MCU and a periphery to drive a display

### Is my display supported?
LVGL needs just one simple driver function to copy an array of pixels into a given area of the display. 
If you can do this with your display then you can use that display with LVGL.

Some examples of the supported display types:
- TFTs with 16 or 24 bit color depth 
- Monitors with HDMI port
- Small monochrome displays
- Gray-scale displays
- even LED matrices
- or any other display where you can control the color/state of the pixels

See the [Porting](/porting/display) section to learn more.

### Is LVGL free? How can I use it in a commercial product?
LVGL comes with [MIT license](https://github.com/lvgl/lvgl/blob/master/LICENCE.txt) which means you can download and use it for any purpose you want.

The only thing you need to do is to add a notice about you are using LVGL in you product. 
This notice can be placed in the user guide, on you website, on an about screen, or anywhere else where users might see it.

### Nothing happens, my display driver is not called. What have I missed?
Be sure you are calling `lv_tick_inc(x)` in an interrupt and `lv_task_handler()` in your main `while(1)`.

Learn more in the [Tick](/porting/tick) and [Task handler](/porting/task-handler) section.

### Why the display driver is called only once? Only the upper part of the display is refreshed. 
Be sure you are calling `lv_disp_flush_ready(drv)` at the end of your "*display flush callback*". 

### Why I see only garbage on the screen?
Probably there a bug in your display driver. Try the following code without using LVGL. You should see a square with red-blue gradient

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
Probably LVGL's color format is not compatible with your displays color format. Check `LV_COLOR_DEPTH` in *lv_conf.h*.

If you are using 16 bit colors with SPI (or other byte-oriented interface) probably you need to set `LV_COLOR_16_SWAP  1` in *lv_conf.h*. 
It swaps the upper and lower bytes of the pixels.

### How to speed up my UI?
- Turn on compiler optimization and enable cache if your MCU has
- Increase the size of the display buffer
- Use 2 display buffers and flush the buffer with DMA (or similar periphery) in the background 
- Increase the clock speed of the SPI or Parallel port if you use them to drive the display
- If your display has SPI port consider changing to a model with parallel because it has much higher throughput
- Keep the display buffer in the internal RAM (not in external SRAM) because LVGL uses it a lot and it should have a small access time
 
### How to reduce flash/ROM usage?
You can disable all the unused feature (such as animations, file system, GPU etc.) and object types in *lv_conf.h*.

If you are using GCC you can add 
- `-fdata-sections -ffunction-sections` compiler flags 
- `--gc-sections` linker flag

to remove unused functions and variables from the final binary

### How to reduce the RAM usage
- Lower the size of the *Display buffer* 
- Reduce `LV_MEM_SIZE` in *lv_conf.h*. This memory used when you create objects like buttons, labels, etc.
- To work with lower `LV_MEM_SIZE` you can create the objects only when required and deleted them when they are not required anymore
 
### How to work with an operating system?

To work with an operating system where tasks can interrupt each other you should protect LVGL related function calls with a mutex. S
ee the [Operating system and interrupts](/porting/os) section to learn more.

### How to contribute to LVGL?
There are several ways to contribute to LVGL:
- Write a few lines about your project to inspire others in the [Forum](https://forum.lvgl.io.com/c/my-projects)
- Help others questions in the [Froum]
- Report and/or fix bugs
- Suggest and/or implement new features
- Improve and/or translate the documentation
- Write a blog post about your experiences

To learn more see [Contributing guide](https://github.com/lvgl/lvgl/blob/master/docs/CONTRIBUTING.md)

### How is LVGL versioned?
LVGL follows the rules of [Semantic versioning](https://semver.org/):
- Major versions for incompatible API changes. E.g. v5.0.0, v6.0.0
- Minor version for new but backward-compatible functionalities. E.g. v6.1.0, v6.2.0
- Patch version for backward-compatible bug fixes. E.g. v6.1.1, v6.1.2

Branches:
- `master` most recent version, patches are merged directly here. 
- `dev` merge new features here until they are merged into `master`.
- `release/vX` there is a branch for every major version to allow adding specific, not forward compatible fixes.

LVGL has a monthly periodic release cycle.
- **1st Tuesday of the month** 
  - Make a major, minor, or patch release from `master` depending on the new features.
  - After that merge only patches into `master` and add new features into the `dev`.
- **3rd Tuesday of the month** 
  - Make a patch release from `master`.
  - After that merge the new features from the `dev` to `master` branch. 
  - In the rest of the month merge only patches into `master` and new features into `dev` branch.


```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/tr/porting/project.md
```

# Set-up a project

## Get the library

LittlevGL Graphics Library is available on GitHub: [https://github.com/littlevgl/lvgl](https://github.com/littlevgl/lvgl). 

You can clone it or download the latest version of the library from GitHub or you can use the [Download](https://littlevgl.com/download) page as well. 

The graphics library is the **lvgl** directory which should be copied into your project.

## Config file

There is a configuration header file for LittlevGL called **lv_conf.h**. It sets the library's basic behavior, disables unused modules and features, adjusts the size of memory buffers in compile time, etc.
 
Copy **lvgl/lv_conf_template.h** next to the *lvgl* directory and rename it to *lv_conf.h*. Open the file and change the `#if 0` at the beginning to `#if 1` to enable its content. 

*lv_conf.h* can be copied other places as well but then you should add `LV_CONF_INCLUDE_SIMPLE` define to your compiler options (e.g. `-DLV_CONF_INCLUDE_SIMPLE` for gcc) and set the include path manually.

In the config file comments explain the meaning of the options. Check at least these three configuration options and modify them according to your hardware:
1. **LV_HOR_RES_MAX** Your display's horizontal resolution
2. **LV_VER_RES_MAX** Your display's vertical resolution
3. **LV_COLOR_DEPTH** 8 for (RG332), 16 for (RGB565) or 32 for (RGB888 and ARGB8888). 

## Initialization

In order to use the graphics library you have to initialize it and the other components too. To order of the initialization is:

1. Call *lv_init()*
2. Initialize your drivers
3. Register the display and input devices drivers in LittlevGL.  More about [Display](/porting/display) and [Input device](/porting/indev) registration.
4. Call `lv_tick_inc(x)` in every `x` milliseconds in an interrupt to tell the elapsed time. [Learn more](/porting/tick).
5. Call `lv_task_handler()` periodically in every few milliseconds to handle LittlevGL related tasks. [Learn more](/porting/task-handler).

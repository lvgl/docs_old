```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/zh-CN/index.md
```

```eval_rst
.. include:: /lang.rst

PDF版本: :download:`LittlevGL.pdf <LittlevGL.pdf>`
```

# 欢迎来到LittlevGL的文档

![](/misc/lv_theme_intro.png "LittlevGL cover")

LittlevGL是一个免费的开源图形库，提供了创建嵌入式GUI所需的一切，具有易于使用的组件，美观的视觉效果和低内存占用等特点。

**[官网](https://littlevgl.com) &nbsp; · &nbsp;** 
**[GitHub](https://github.com/littlevgl/lvgl) &nbsp; · &nbsp;** 
**[论坛](https://forum.littlevgl.com) &nbsp; · &nbsp;** 
**[在线演示](https://littlevgl.com/live-demo) &nbsp; · &nbsp;** 
**[模拟器](/get-started/pc-simulator) &nbsp; · &nbsp;** 
**[博客](https://blog.littlevgl.com/)**

## 主要特点
- Powerful building blocks such as buttons, charts, lists, sliders, images etc.
- 高级图形效果：动画，反锯齿，透明度，平滑滚动
- Various input devices such as touchpad, mouse, keyboard, encoder etc.
- 支持多语言的UTF-8编码
- 支持多个显示设备，例如同步显示在多个TFT, monochrome设备
- Fully customizable graphic elements
- 硬件独立于任何微控制器或显示器
- 可以缩小到最小内存 (64 kB Flash, 16 kB RAM)
- 支持操作系统、外部储存和GPU（非必须）
- 仅仅单个帧缓冲设备就可以呈现高级视觉特效
- 使用C编写以获得最大兼容性(兼容C++)
- Simulator to start embedded GUI design on a PC without embedded hardware
- 为加速GUI设计，提供教程,、案例和主题
- Documentation is available as online and offline
- 基于自由和开源的MIT协议

## 要求
- 16、32或64位的单片机（微控制器）或处理器
- Greater than 16 MHz clock speed is recommended
- Flash/ROM: Greater than 64 kB size for the very essential components (greater than 180 kB is recommended)
- RAM:
  - Static RAM usage: approximately 8 to 16 kB depending on the used features and objects types
  - Stack: greater than 2kB (greater than 4 kB is recommended)
  - Dynamic data (heap): greater than 4 KB (greater than 16 kB is recommended if using several objects).
    Set by `LV_MEM_SIZE` in *lv_conf.h* 
  - Display buffer: greater than *"Horizontal resolution"* pixels (greater than 10 &times; *"Horizontal resolution"* is recommended) 
-  C99或更新的编译器
- Basic C (or C++) knowledge: [pointers](https://www.tutorialspoint.com/cprogramming/c_pointers.htm), [structs](https://www.tutorialspoint.com/cprogramming/c_structures.htm), [callbacks](https://www.geeksforgeeks.org/callbacks-in-c/)

*请注意内存占用可能非常依赖于构架、编译器和编译选项。*


## 常见问题

### 从哪来开始？
- 总体概览LittlevGL请访问[littlevgl.com](https://littlevgl.com)
- Go to the [Get started](/get-started/index) section to try Live demos in you browser, learn about the Simulator(s) and learn the basics of LittlevGL
- A detailed porting guide can be found in the [Porting](/porting/index) section
- To learn how LittlevGL works go to the [Overview](/overview/index)
- 阅读教程或者分享你的见解请前往 [博客](https://blog.littlevgl.com)
- To see the source code of the library check it on GitHub: [https://github.com/littlevgl/lvgl/](https://github.com/littlevgl/lvgl/)


### 在哪里我可以问问题?
可以在论坛上问问题: [https://forum.littlevgl.com/](https://forum.littlevgl.com/).

我们使用 [GitHub 问题](https://github.com/littlevgl/lvgl/issues)和库开发相关的问题，因此你应该仅仅在上面问与库开发紧密相关的的问题。 （即普通问题，如使用问题应该在论坛上问，库的设计问题或者bug可以在Github上提）


### 是否支持我的单片机或硬件?
Every MCU which is capable of driving a display via Parallel port, SPI, RGB interface or anything else and fulfills the [Requirements](#Requirements) is supported by LittlevGL.

It includes:
- "一般的"单片机如 STM32F, STM32H, NXP Kinetis, LPC, iMX, dsPIC33, PIC32 等等. 
- 蓝牙, GSM, WiFi 模块如 Nordic NRF 和 Espressif ESP32
- Linux frame buffer like /dev/fb0 which includes Single board computers too like Raspberry Pi
- And anything else with a strong enough MCU and a periphery to drive a display

### 是否支持我的屏幕?
LittlevGL needs just one simple driver to copy an array of pixels into a given area of the display. If you can do this with your display then you can use the same display with LittlevGL.

It includes:
- 16或24位色彩深度的TFT屏幕
- 带有HDMI端口的监视器
- 小的单色显示屏
- 灰阶显示设备
- LED矩阵
- 或其他任何你可以控制像素颜色或状态的显示设备

在 [移植](/porting/display) 章节查看更多内容

### LittlevGL是免费的吗？我该如何在商业产品中使用它呢？
LittlevGL comes with [MIT license](https://github.com/littlevgl/lvgl/blob/master/LICENCE.txt) which means you can download and use it for any purpose you want without any obligations.

### 什么都没有显示，我的显示驱动没有被调用，我漏掉了什么？
确保你在中断上调用了 `lv_tick_inc(x)` 并且 在 main方法的`while(1)` 中调用了`lv_task_handler()`。

更多请查看 [Tick](/porting/tick) 和[任务处理](/porting/task-handler) 章节。

### 为什么显示驱动只被调用了一次？只刷新了显示屏的上半部分。
Be sure you are calling `lv_disp_flush_ready(drv)` at the end of your "*display flush callback*". 

### 为什么我只在我的屏幕上看到垃圾（雪花）?
可以在你的显示驱动上有一个bug，先尝试下面不使用 LittlevGL 的代码:

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

### 为什么我的屏幕的颜色有点不对劲？
Probably LittlevGL's color format is not compatible with your displays color format. Check `LV_COLOR_DEPTH` in *lv_conf.h*.

如果你使用的是16位颜色的SPI (或者其他面向字节的) 接口，可能你需要在 *lv_conf.h* 设置 `LV_COLOR_16_SWAP  1`，它的作用是将高位和低位的字节互换。

### 如何提高我的UI速度?
- 启用编译优化(gcc -O)
- 增加显示缓冲的大小
- 使用双显示缓冲和在后台使用DMA（或类似的外围设备）刷新缓冲
- 如果你使用SPI或并口驱动显示，增加他们的时钟速度
- 如果你的显示设备有SPI端口，请考虑使用并行模式，因为这样可以提高吞吐量
- Keep the display buffer in the internal RAM (not in external SRAM) because LittlevGL uses it a lot and it should have a small access time
 
### 如何减少 flash/ROM 使用量?
You can disable all the unused feature (such as animations, file system, GPU etc.) and object types in *lv_conf.h*.

If you are using GCC you can add 
- `-fdata-sections -ffunction-sections` 编译标志
- `--gc-sections` 链接标志

来去除无用的函数和变量

### 怎么减少 RAM  使用量
- 降低*显示缓冲* 的大小
- Reduce `LV_MEM_SIZE` in *lv_conf.h*. This memory used when you create objects like buttons, labels, etc.
- To work with lower `LV_MEM_SIZE` you can create the objects only when required and deleted them when they are not required anymore
 
### 怎么在我的操作系统上使用?

为了在拥有中断的操作系统上使用，为了保护LittlevGL，你可以与互斥锁一同调用相关函数，请查看 [操作系统](/porting/os) 章节获取更多内容

### 如何为LittlevGL做出贡献?
这里有多种方法为LittlevGL做出贡献:
- Write a few lines about your project to inspire others
- Answer other’s questions
- Report and/or fix bugs
- Suggest and/or implement new features
- Improve and/or translate the documentation
- Write a blog post about your experiences

要了解更多请查看 [贡献指南](https://blog.littlevgl.com/2018-12-06/contributing)

### How is LittlevGL versioned?

LittlevGL follows the rules of [Semantic versioning](https://semver.org/):
- *Major* versions for incompatible API changes. E.g. v5.0.0, v6.0.0
- *Minor* version for new but backwards-compatible functionalities. E.g. v6.1.0, v6.2.0
- *Patch* version for backwards-compatible bug fixes. E.g. v6.1.1, v6.1.2

The new versions are developed in `dev-X.Y` branchs on GitHub. It can be cloned to test the newset features, however, still anything can be changed there.

The bugfixes are added directly to the `master` branch on GitHub and a bugfix release is created every month.

### 我可以在哪里查看之前版本的文档 (v5.3)?

你可以在这里下载然后离线打开:
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

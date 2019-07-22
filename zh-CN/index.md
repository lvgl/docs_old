```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/zh-CN/index.md
```

```eval_rst
.. include:: /lang.rst

PDF版本: :download:`LittlevGL.pdf <LittlevGL.pdf>`
```

# 欢迎来到LittlevGL的文档

![](/misc/lv_theme_intro.png "LittlevGL cover")

LittlevGL is a free and open-source graphics library providing everything you need to create embedded GUI with easy-to-use graphical elements, beautiful visual effects and low memory footprint.

**[官网](https://littlevgl.com) &nbsp; · &nbsp;** 
**[GitHub](https://github.com/littlevgl/lvgl) &nbsp; · &nbsp;** 
**[论坛](https://forum.littlevgl.com) &nbsp; · &nbsp;** 
**[在线演示](https://littlevgl.com/live-demo) &nbsp; · &nbsp;** 
**[模拟器](/get-started/pc-simulator) &nbsp; · &nbsp;** 
**[博客](https://blog.littlevgl.com/)**

## 主要特点
- 强大的块构建能力：按钮，图表，列表，滑动条，图片等
- 高级图形效果：动画，反锯齿，透明度，平滑滚动
- 多种输入设备支持： 触摸板，鼠标，键盘，编码器等
- 支持多语言的UTF-8编码
- Multi-display support, i.e. use more TFT, monochrome displays simultaneously
- 完全的自定义图形组件功能
- Hardware independent to use with any microcontroller or display
- Scalable to operate with little memory (64 kB Flash, 16 kB RAM)
- OS, External memory and GPU supported but not required
- 仅仅单个帧缓冲设备就可以呈现高级视觉特效
- 使用C编写以获得最大兼容性(兼容C++)
- 无需拥有嵌入式硬件设备，在PC上的模拟器开始设计嵌入式GUI
- 为加速GUI设计，提供教程,、案例和主题
- 在线和离线文档
- 基于自由和开源的MIT协议

## 要求
- 16、32或64位的单片机（微控制器）或处理器
- 推荐使用&gt; 16 MHz时钟速度
- Flash/ROM: 为了运行让最基本的组件运行起来，需要&gt; 64 kB (推荐&gt; 180 kB)
- RAM: 
  - 静态RAM 使用: ~8..16 kB ，取决于使用的功能对象类型
  - 栈内存: &gt; 2kB (推荐&gt; 4 kB)
  - 动态数据 (推内存): &gt; 4 KB (当使用多种不同的对象，推荐&gt; 16 kB).
 在*lv_conf.h*设置 `LV_MEM_SIZE` 。
  - 显示缓冲:  &gt; *"水平分辨率"* 像素 (推荐&gt; 10 &times; *"水平分辨率"* ) 
-  C99或更新的编译器
- 基础C (or C++) 知识: [指针](https://www.tutorialspoint.com/cprogramming/c_pointers.htm), [结构体](https://www.tutorialspoint.com/cprogramming/c_structures.htm), [回调](https://www.geeksforgeeks.org/callbacks-in-c/).

*请注意内存占用可能非常依赖于构架、编译器和编译选项。*


## 常见问题

### 从哪来开始？
- 总体概览LittlevGL请访问[littlevgl.com](https://littlevgl.com)
- Go to the [Get started](/get-started/index) section to try Live demos in you browser, learn about the Simulator(s) and learn the basics of LittlevGL.
- A detailed porting guide can be found in the [Porting](/porting/index) section.
- To learn how LittlevGL works go to the [Overview](/overview/index).
- 阅读教程或者分享你的见解请前往 [博客](https://blog.littlevgl.com)
- To see the source code of the library check it on GitHub: [https://github.com/littlevgl/lvgl/](https://github.com/littlevgl/lvgl/).


### 在哪里我可以问问题?
可以在论坛上问问题: [https://forum.littlevgl.com/](https://forum.littlevgl.com/).

我们使用 [GitHub 问题](https://github.com/littlevgl/lvgl/issues)和库开发相关的问题，因此你应该仅仅在上面问与库开发紧密相关的的问题。 （即普通问题，如使用问题应该在论坛上问，库的设计问题或者bug可以在Github上提）


### 是否支持我的单片机或硬件?
每个可以通过并口、SPI、RGB接口或者其他设备驱动一个屏幕并且能够满足 [需求](#Requirements)的单片机都支持LittlevGL。
它包含
- "普通"单片机如 STM32F, STM32H, NXP Kinetis, LPC, iMX, dsPIC33, PIC32 等等. 
- 蓝牙, GSM, WiFi 模块如 Nordic NRF 和 Espressif ESP32
- 包含在一些单片机的Linux帧缓冲设备，如树莓派上的的/dev/fb0
- and anything else with a strong enough MCU and a periphery to drive a display

### 是否支持我的屏幕?
LittlevGL needs just one simple driver to copy an array of pixels to a given area of the display. If you can do this with your display then you can use that display with LittlevGL. 
它包含
- 16或24位色彩深度的TFT屏幕
- 带有HDMI端口的监视器
- 小的单色显示屏
- 灰阶显示设备
- LED矩阵
- 或其他任何你可以控制像素颜色或状态的显示设备

在 [移植](/porting/display) 章节查看更多内容

### LittlevGL是免费的吗？我该如何在商业产品中使用它呢？
LittlevGL伴随着MIT协议，这意味着你可以以任何目的去下载和使用它而无需做出任何义务。

### 什么都没有显示，我的显示驱动没有被调用，我漏掉了什么？
确保你在中断上调用了 `lv_tick_inc(x)` 并且 在 main方法的`while(1)` 中调用了`lv_task_handler()`。

更多请查看 [Tick](/porting/tick) 和[任务处理](/porting/task-handler) 章节。

### 为什么显示驱动只被调用了一次？只刷新了显示屏的上半部分。
Be sure you are calling `lv_disp_flush_ready(drv)` at the end of you *display flush callback*. 

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
可能LittlevGL的色彩格式不和你的显示设备兼容，检查*lv_conf.h* 的 `LV_COLOR_DEPTH`。

如果你使用的是16位颜色的SPI (或者其他面向字节的) 接口，可能你需要在 *lv_conf.h* 设置 `LV_COLOR_16_SWAP  1`，它的作用是将高位和低位的字节互换。

### 如何提高我的UI速度?
- 启用编译优化(gcc -O)
- 增加显示缓冲的大小
- 使用双显示缓冲和在后台使用DMA（或类似的外围设备）刷新缓冲
- Increase the clock speed of the SPI or Parallel port if you use them to drive the display
- 如果你的显示设备有SPI端口，请考虑使用并行模式，因为这样可以提高吞吐量
- 保持显示缓冲在内部RAM (不是外部SRAM) 因为 LittlevGL 会频繁使用它所以它应该拥有较小的访问时间
 
### 如何减少 flash/ROM 使用量?
你可以在*lv_conf.h*关闭不必要的功能（如动画、文件系统和GPU等等）和对象类型

如果你使用GCC你可以加上
- `-fdata-sections -ffunction-sections` 编译标志
- `--gc-sections` 链接标志

来去除无用的函数和变量
`
### 怎么减少 RAM  使用量
- 降低*显示缓冲* 的大小
- 减少*lv_conf.h*中的`LV_MEM_SIZE`，这个是你创建按钮、标签和其他对象时使用的内存大小
- To work with lower `LV_MEM_SIZE` you can create the objects only when required and deleted them when they are not required anymore.
 
### 怎么在我的操作系统上使用?

为了在拥有中断的操作系统上使用，为了保护LittlevGL，你可以与互斥锁一同调用相关函数，请查看 [操作系统](/porting/os) 章节获取更多内容

### 如何为LittlevGL做出贡献?
这里有多种方法为LittlevGL做出贡献:
- 通过实际项目代码来激励别人
- 回答别人的问题
- 返回或修复bug
- 提出或实现新功能
- 提高或翻译文档
- 写一篇博客文章发表你的体验

要了解更多请查看 [贡献指南](https://blog.littlevgl.com/2018-12-06/contributing)


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


# Welcome to LittlevGL's documentation!


![](_static/img/lv_theme_intro.png "LittlevGL cover")

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
- Various input devices touch pad, mouse, keyboard, encoder etc
- Multi language support with UTF-8 encoding
- Multi-display support, i.e. use more TFT, monochrome displays simultaneously
- Fully customizable graphical elements
- Hardware independent to use with any microcontroller or display
- Scalable to operate with little memory (80 kB Flash, 12 kB RAM)
- OS, External memory and GPU supported but not required
- Single frame buffer operation even with advanced graphical effects
- Written in C for maximal compatibility (C++ compatible)
- Simulator to start embedded GUI design on PC without embedded hardware
- Tutorials, examples, themes for rapid GUI design
- Documentation online and offline
- Free and open-source under MIT licence

## Requirements
- 16, 32 or 64 bit microcontroller or processor
- &gt; 16 MHz clock speed is recommended
- 8 kB RAM for static data and 2 KB RAM for dynamic data for graphical objects (widgets), 2 kB Stack
- 64 kB program memory (flash)
- Optionally ~1/10 screen sized memory for internal buffering (at 240 × 320, 16 bit colors it means 15 kB)
- C99 or newer compiler
- Basic C (or C++) knowledge: [pointers](https://www.tutorialspoint.com/cprogramming/c_pointers.htm), [structs](https://www.tutorialspoint.com/cprogramming/c_structures.htm), [callbacks](https://www.geeksforgeeks.org/callbacks-in-c/)

## See the source on GitHub
The source code of LittlevGL is available on GitHub:

[https://github.com/littlevgl/lvgl/](https://github.com/littlevgl/lvgl/)

## Ask questions in the Forum
We use [GitHub issues](https://github.com/littlevgl/lvgl/issues) for delopment releated discussion.
To ask questions, please use the forum:
[https://forum.littlevgl.com/](https://forum.littlevgl.com/)

## Documentation in PDF
You can download the documentation in PDF here:
[LittlevGL.pdf](file:///home/kisvegabor/projects/littlevgl/docs/en/latex/LittlevGL.pdf)


## Get started
For a general overview of LittlvGL visit [littlevgl.com](https://littlevgl.com)

To make some experiments with LittlevGL in a simulator on you PC or in even in your browser see the [Get started](/get-started/index) guide.

To see how you can port LittlevGL to your device go to the [Porting](/porting/index) section.

To learn how LittlevGL works start to read the [Overview](/overview/index).

To read tutorial or shar your own experiences go to the [Blog](https://blog.littlevgl.com)


---

```eval_rst

.. toctree::
   :maxdepth: 2
   
   get-started/index
   porting/index
   overview/index
   object-types/index
```

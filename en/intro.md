# Introduction

LittlevGL is a free and open-source graphics library providing everything you need to create embedded GUI with easy-to-use graphical elements, beautiful visual effects and low memory footprint.


## Key features
- Powerful building blocks buttons, charts, lists, sliders, images etc
- Advanced graphics with animations, anti-aliasing, opacity, smooth scrolling
- Various input devices touch pad, mouse, keyboard, encoder etc
- Multi language support with UTF-8 encoding
- Fully customizable graphical elements

- Hardware independent to use with any microcontroller or display
- Scalable to operate with little memory (80 kB Flash, 10 kB RAM)
- OS, External memory and GPU supported but not required
- Single frame buffer operation even with advanced graphical effects

- Written in C for maximal compatibility (C++ compatible)
- Simulator to start embedded GUI design on PC without embedded hardware
- Tutorials, examples, themes for rapid GUI design
- Documentation online and offline
- Free and open-source under MIT licence


## Requirements

- 16, 32 or 64 bit microcontroller or processor
- 16 MHz clock speed
- 8 kB RAM for static data and &gt;2 KB RAM for dynamic data (graphical objects)
- 64 kB program memory (flash)
- Optionally ~1/10 screen sized memory for internal buffering (at 240 × 320, 16 bit colors it means 15 kB)
- C99 or newer compiler

* * *

The LittlevGL is designed to be highly portable and to not use any external resources:
- No external RAM required (but supported)
- No float numbers are used
- No GPU needed (but supported)
- Only a single frame buffer is required located in:
    - Internal RAM or
    - External RAM or
    - External display controller's memory

* * *

If you would like to reduce the required hardware resources you can:
- Disable the unused object types to save RAM and ROM
- Change the size of the graphical buffer to save RAM (see later)
- Use more simple styles to reduce the rendering time


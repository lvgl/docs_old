# Micropython

## What is Micropython?

[Micropython](http://micropython.org/) is Python for microcontrollers.  
With Micropython you can write Python3 code and run it on bare metal architectures with limited resources.

### Micropython highlights

- **Compact** - fit and run within just 256k of code space and 16k of RAM. No OS is needed, although you can also run it with OS, if you want.
- **Compatible** - strives to be as compatible as possible with normal Python (known as CPython)
- **Verstile** - Supports many architectures (x86, x86-64, ARM, ARM Thumb, Xtensa)
- **Interactive** - No need for the compile-flash-boot cycle. With the REPL (interactive prompt) you can type commands and execute them immediately, run scripts etc.
- **Popular** - Many platforms are supported. User base is growing bigger.  
Notable forks: [MicroPython](https://github.com/micropython/micropython), [CircuitPython](https://github.com/adafruit/circuitpython), [MicroPython_ESP32_psRAM_LoBo](https://github.com/loboris/MicroPython_ESP32_psRAM_LoBo)
- **Embedded Oriented** - Comes with modules specifically for embedded systems, such as the [machine module](https://docs.micropython.org/en/latest/library/machine.html#classes) for accessing low-level hardware (I/O pins, ADC, UART, SPI, I2C, RTC, Timers etc.)

---

## Why Micropython + LittlevGL?

Micropython today [does not have a good high-level GUI library](https://forum.micropython.org/viewtopic.php?f=18&t=5543).  
LittlevGL is a good high-level GUI library, it's implemented in C and its API is in C.  
LittlevGL is an [Object Oriented Component Based](https://blog.littlevgl.com/2018-12-13/extend-lvgl-objects) library, which seems a natural candidate to map into a higher level language, such as Python.

### Here are some advantages of using LittlevGL in Micropython:

- Develop GUI in Python, a very popular high level language. Use paradigms such as Object Oriented Programming.
- GUI development requires multiple iterations to get things right.  
With C, each iteration consists of **`Change code` > `Build` > `Flash` > `Run`**.  
In Micropython it's just **`Change code` > `Run`**. You can even run commands interactively using the [REPL](https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop) (the interactive prompt)

### Micropython + LittlevGL could be used for:

- Fast prototyping GUI.  
- Shorten the cycle of changing and fine-tuning the GUI.
- Model the GUI in a more abstract way by defining reusable composite objects, taking advantage of Python's language features such as Inheritance, Closures, List Comprehension, Generators, Exception Handling, Arbitrary Precision Integers and others.
- Make LittlevGL accessible to a larger audience. No need to know C in order to create a nice GUI on an embedded system.  
This goes well with [CircuitPython vision](https://learn.adafruit.com/welcome-to-circuitpython/what-is-circuitpython). CircuitPython was designed with education in mind, to make it easier for new or unexperienced users to get started with embedded development.

---

## So how does it look like?

> TL;DR:
> It's very much like the C API, but Object Oriented for LittlevGL components.

Let's dive right into an example!  

### A simple example

```python
import lvgl as lv
lv.init()
scr = lv.obj()
btn = lv.btn(scr)
btn.align(lv.scr_act(), lv.ALIGN.CENTER, 0, 0)
label = lv.label(btn)
label.set_text("Button")
lv.scr_load(scr)
```

## How can I use it?

### Online Simulator

If you want to experiment with LittlevGL + Micropython without downloading anything - you can use our online simulator!  
It's a fully functional LittlevGL + Micropython that runs entirely in the browser and allows you to edit a python script and run it.

[Link to the online simulator](https://cdn.statically.io/gh/littlevgl/lv_micropython/ef943a1ab40b32a8a77059d6e833a440446c51e8/ports/javascript/lvgl_editor.html?env=dev&script=https://raw.githubusercontent.com/littlevgl/lv_binding_micropython/dev-6.0/examples/chart_anim_example.py)

### PC Simulator

Micropython is ported to many platform, one of the is the "unix port", which allows you to build and run Micropython (+LittlevGL) on a Linux machine. (On a windows machine you might need Virtual Box or WSL or MinGW or Cygwin etc.)  

[More information about building and running the unix port](https://github.com/littlevgl/lv_micropython)

### The real thing

At the end, the goal is to run it all on an embedded platform.  
Both Micropython and LittlevGL can be used on many embedded architectures, such as stm32, ESP32 etc.  
You would also need display and input drivers. We have some example drivers (ESP32+ILI9341, as well as some other examples), but most chances are you would want to create your own input/display drivers for your specific purposes.  
Drivers can be implemented either in C as Micropython module, or in pure Micropython!

## Where can I find more information?

- On the [Blog Post](https://blog.littlevgl.com/2019-02-20/micropython-bindings)
- On `lv_micropython` [README](https://github.com/littlevgl/lv_micropython)
- On `lv_binding_micropython` [README](https://github.com/littlevgl/lv_binding_micropython)
- On LittlevGL forum (Feel free to ask anything!)
- On Micropython [docs](http://docs.micropython.org/en/latest/) and [forum](https://forum.micropython.org/)

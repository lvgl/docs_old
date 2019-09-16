```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/fr/get-started/micropython.md
```
# Micropython

## Qu'est-ce que Micropython ?

[Micropython](http://micropython.org/) est une version de Python destinées aux microcontrôleurs.  
Using Micropython, you can write Python3 code and run it even on a bare metal architecture with limited resources.

### Highlights of Micropython

- **Compact** - Fits and runs within just 256k of code space and 16k of RAM. No OS is needed, although you can also run it with an OS, if you want.
- **Compatible** - Strives to be as compatible as possible with normal Python (known as CPython).
- **Versatile** - Supports many architectures (x86, x86-64, ARM, ARM Thumb, Xtensa).
- **Interactif** - le cycle compilation-programmation-démarrage n'est pas nécessaire. Avec REPL (l'invite interactive) vous pouvez entrer des commandes et les exécuter immédiatement, lancer des scripts etc.
- **Popular** - Many platforms are supported. The user base is growing bigger. Notable forks: [MicroPython](https://github.com/micropython/micropython), [CircuitPython](https://github.com/adafruit/circuitpython), [MicroPython_ESP32_psRAM_LoBo](https://github.com/loboris/MicroPython_ESP32_psRAM_LoBo)
- **Orienté embarqué** - fourni avec des modules spécifiques aux systèmes embarqués, comme le module [machine](https://docs.micropython.org/en/latest/library/machine.html#classes) pour accéder au matériel bas-niveau (broches d'E/S, CAN, UART, SPI, I2C, RTC, horloges etc.)

---

## Pourquoi Micropython + LittlevGL ?

Currently, Micropython [does not have a good high-level GUI library](https://forum.micropython.org/viewtopic.php?f=18&t=5543) by default. LittlevGL is an [Object Oriented Component Based](https://blog.littlevgl.com/2018-12-13/extend-lvgl-objects) high-level GUI library, which seems to be a natural candidate to map into a higher level language, such as Python. LittlevGL is implemented in C and its APIs are in C.

### Voici quelques avantages à utiliser LittlevGL avec Micropython :

- Développez des interfaces graphiques en Python, language de haut-niveau très populaire. Utilisez des paradigmes tels que la programmation orientée objet.
- Usually, GUI development requires multiple iterations to get things right. With C, each iteration consists of **`Change code` > `Build` > `Flash` > `Run`**.  
In Micropython it's just **`Change code` > `Run`** ! You can even run commands interactively using the [REPL](https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop) (the interactive prompt)

### Micropython + LittlevGL peuvent être utilisés pour :

- Le prototypage rapide d'interface graphique.  
- Réduire le cycle de modification et d'optimisation de l'interface graphique.
- Modéliser l'interface graphique d'une manière plus abstraite en définissant des objets composites réutilisables, en tirant avantage des fonctionnalités du langage Python telles que l'héritage, les clôtures, les 
listes en compréhension, les générateurs, la gestion d'exception, les entiers multiprécision et autres.
- Rendre LittlevGL accessible à une plus large audience.  Aucun besoin de connaître le C dans le but de créer une interface graphique fonctionnelle sur un système embarqué.  
C'est également vrai pour [CircuitPython vision](https://learn.adafruit.com/welcome-to-circuitpython/what-is-circuitpython). CircuitPython a été conçu avec l'éducation à l'esprit, pour rendre plus facile à des utilisateurs, nouveaux ou inexpérimentés, de débuter avec le développement embarqué.
- Creating tools to work with LittlevGL at a higher level (e.g. drag-and-drop designer).

---

## So what does it look like?

> TL;DR :
> C'est très similaire à l'API C, mais orienté objet pour les composants de LittlevGL.

Plongeons droit dans un exemple !

### Un exemple simple

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

## Comment l'utiliser?

### Simulateur en ligne

Si vous souhaitez expérimenter LittlevGL + Micropython sans télécharger quoi que ce soit - vous pouvez utiliser notre simulateur en ligne !  
C'est un ensemble LittlevGL + Micropython entièrement fonctionnel qui s'exécute dans le navigateur et permet d'éditer et d'exécuter un script Python.

[Click here to experiment on the online simulator](https://cdn.statically.io/gh/littlevgl/lv_micropython/ef943a1ab40b32a8a77059d6e833a440446c51e8/ports/javascript/lvgl_editor.html?env=dev&script=https://raw.githubusercontent.com/littlevgl/lv_binding_micropython/dev-6.0/examples/chart_anim_example.py)

### Simulateur PC

Micropython is ported to many platforms. One notable port is "unix", which allows you to build and run Micropython (+LittlevGL) on a Linux machine. (On a Windows machine you might need Virtual Box or WSL or MinGW or Cygwin etc.)  

[Click here to know more information about building and running the unix port](https://github.com/littlevgl/lv_micropython)

### Embedded platform

Au final, le but est d'exécuter sur une plateforme embarquée.
Micropython et LittlevGL peuvent être utilisés sur de nombreuses architectures embarquées, telles que STM32, ESP32 etc.  
You would also need display and input drivers. We have some sample drivers (ESP32+ILI9341, as well as some other examples), but most chances are you would want to create your own input/display drivers for your specific purposes.  
Les pilotes peuvent être implémentés soit en C en tant que module Micropython, soit en Micropython pur !

## Où trouver plus d'informations ?

- Dans le sujet du [Blog](https://blog.littlevgl.com/2019-02-20/micropython-bindings)
- Dans le [README](https://github.com/littlevgl/lv_micropython) `lv_micropython`
- Dans le [README](https://github.com/littlevgl/lv_binding_micropython) `lv_binding_micropython`
- Sur le forum LittlevGL (n'hésitez pas à demander quoi que ce soit !)
- Dans la [documentation](http://docs.micropython.org/en/latest/) et sur le [forum](https://forum.micropython.org/) Micropython

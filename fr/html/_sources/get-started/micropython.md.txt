```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/fr/get-started/micropython.md
```
# Micropython

## Qu'est-ce que Micropython ?

[Micropython](http://micropython.org/) est une version de Python destinées aux microcontrôleurs.  
En utilisant Micropython vous pouvez écrire du code Python 3 et l'exécuter directement sur des architectures aux ressources limitées.

### Points forts de Micropython

- **Compact** - s'exécute dans seulement 256 ko d'espace de code et 16 ko de MEV. Aucun SE n'est nécessaire, bien qu'il soit possible de l'exécuter sur un SE, si vous le souhaitez.
- **Compatible** - s'efforce d'être aussi compatible que possible avec le Python de référence (CPython).
- **Adaptable** - supporte de multiples architectures (x86, x86-64, ARM, ARM Thumb, Xtensa).
- **Interactif** - le cycle compilation-programmation-démarrage n'est pas nécessaire. Avec REPL (l'invite interactive) vous pouvez entrer des commandes et les exécuter immédiatement, lancer des scripts etc.
- **Populaire** - de nombreuses plateformes sont supportées. Le nombre d'utilisateurs est en constante augmentation. Variantes notables : [MicroPython](https://github.com/micropython/micropython), [CircuitPython](https://github.com/adafruit/circuitpython), [MicroPython_ESP32_psRAM_LoBo](https://github.com/loboris/MicroPython_ESP32_psRAM_LoBo)
- **Orienté embarqué** - fourni avec des modules spécifiques aux systèmes embarqués, comme le module [machine](https://docs.micropython.org/en/latest/library/machine.html#classes) pour accéder au matériel bas-niveau (broches d'E/S, CAN, UART, SPI, I2C, RTC, horloges etc.)

---

## Pourquoi Micropython + LittlevGL ?

Actuellement, par défaut, Micropython [ne dispose pas d'une bonne librairie de haut-niveau pour réaliser des interfaces graphiques](https://forum.micropython.org/viewtopic.php?f=18&t=5543).  LittlevGL est une librairie basée sur l'utilisation de [composants orientés objet](https://blog.littlevgl.com/2018-12-13/extend-lvgl-objects), ce qui en fait une candidate idéale pour s'interfacer à un langage de plus haut-niveau tel que Python. LittlevGL est implémentée en C est ses APIs sont en C.  

### Voici quelques avantages à utiliser LittlevGL avec Micropython :

- Développez des interfaces graphiques en Python, language de haut-niveau très populaire. Utilisez des paradigmes tels que la programmation orientée objet.
- Actuellement, le développement d'interface graphique nécessite de nombreuses itérations pour obtenir un résultat correct. Avec C, chaque itération nécessite de **`modifier le code` > `compiler` > `programmer` > `exécuter`**.  
En Micropython il faut seulement **`modifier le code` > `exécuter`**. Vous pouvez même exécuter des commandes de manière interactive en utilisant [REPL](https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop) (l'invite interactive)

### Micropython + LittlevGL peuvent être utilisés pour :

- Le prototypage rapide d'interface graphique.  
- Réduire le cycle de modification et d'optimisation de l'interface graphique.
- Modéliser l'interface graphique d'une manière plus abstraite en définissant des objets composites réutilisables, en tirant avantage des fonctionnalités du langage Python telles que l'héritage, les clôtures, les 
listes en compréhension, les générateurs, la gestion d'exception, les entiers multiprécision et autres.
- Rendre LittlevGL accessible à une plus large audience.  Aucun besoin de connaître le C dans le but de créer une interface graphique fonctionnelle sur un système embarqué.  
C'est également vrai pour [CircuitPython vision](https://learn.adafruit.com/welcome-to-circuitpython/what-is-circuitpython). CircuitPython a été conçu avec l'éducation à l'esprit, pour rendre plus facile à des utilisateurs, nouveaux ou inexpérimentés, de débuter avec le développement embarqué.
- Création d'outils pour utiliser LittlevGL à un niveau supérieur (concepteur graphique par glisser-déposer, par exemple).

---

## Alors, à quoi ça ressemble ?

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

[Click here to experiment on the online simulator](https://sim.littlevgl.com/v6/micropython/ports/javascript/lvgl_editor.html)

[Hello World](https://sim.littlevgl.com/v6/micropython/ports/javascript/lvgl_editor.html?script=https://gist.githubusercontent.com/amirgon/51299ce9b6448328a855826149482ae6/raw/0f235c6d40462fd2f0e55364b874f14fe3fd613c/lvgl_hello_world.py&script_startup=https://gist.githubusercontent.com/amirgon/7bf15a66ba6d959bbf90d10f3da571be/raw/8684b5fa55318c184b1310663b187aaab5c65be6/init_lv_mp_js.py)

### Simulateur PC

Micropython est porté sur de nombresues plateformes, dont Unix, ce qui permet de compiler et exécuter Micropython (+ LittlevGL) sur une machine Linux (sur une machine Windows, d'autres outils peuvent être nécessaires : VirtualBox ou WSL ou MinGW ou Cygwin etc.).

[Cliquez ici pour en savoir plus sur la compilation et l'utilisation du port Unix](https://github.com/littlevgl/lv_micropython)

### Plateforme embarquée

Au final, le but est d'exécuter sur une plateforme embarquée.
Micropython et LittlevGL peuvent être utilisés sur de nombreuses architectures embarquées, telles que STM32, ESP32 etc.  
Vous aurez également besoin de pilotes d’affichage et d’entrée. Nous avons quelques exemples de pilotes (ESP32 + ILI9341, ainsi que d’autres exemples), mais il est fort probable que vous souhaitiez créer vos propres pilotes d’affichage et d’entrée pour vos besoins spécifiques.
Les pilotes peuvent être implémentés soit en C en tant que module Micropython, soit en Micropython pur !

## Où trouver plus d'informations ?

- Dans le sujet du [Blog](https://blog.littlevgl.com/2019-02-20/micropython-bindings)
- Dans le [README](https://github.com/littlevgl/lv_micropython) `lv_micropython`
- Dans le [README](https://github.com/littlevgl/lv_binding_micropython) `lv_binding_micropython`
- Sur le forum LittlevGL (n'hésitez pas à demander quoi que ce soit !)
- Dans la [documentation](http://docs.micropython.org/en/latest/) et sur le [forum](https://forum.micropython.org/) Micropython

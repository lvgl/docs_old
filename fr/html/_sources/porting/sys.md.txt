```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/fr/porting/sys.md
```
# Aperçu système

![](/misc/sys.png "System architecture with Littlev Graphics Library (LittlevGL)")

**Application**
Votre application qui crée l'interface graphique et gère les tâches spécifiques.

**LittlevGL**
The graphics library itself. Your application can communicate with the library to create a GUI. It contains a HAL (Hardware Abstraction Layer) interface to register your display and input device drivers.

**Pilote**
Besides your specific drivers, it contains functions to drive your display, optionally to a GPU and to read the touchpad or buttons.

* * *

Depending on the MCU, there are two typical hardware set-ups. One with built-in LCD/TFT driver periphery and another without it. In both cases, a frame buffer will be required to store the current image of the screen.

1. **Microcontrôleur avec contrôleur TFT/LCD**
Si votre microcontrôleur dispose d'un contrôleur  TFT/LCD, vous pouvez connecter un écran directement via une interface RVB.
Dans ce cas, le tampon d'affichage peut résider dans la MEV interne (si le microcontrôleur dispose de suffisamment de MEV) ou dans la MEV externe (si la microcontrôleur a une interface mémoire).

2. **Contrôleur d'affichage externe**
If the MCU doesn't have TFT/LCD driver interface then an external display controller (E.g. SSD1963, SSD1306, ILI9341) has to be used.
In this case, the MCU can communicate with the display controller via Parallel port, SPI or sometimes I2C.
The frame buffer is usually located in the display controller which saves a lot of RAM for the MCU.

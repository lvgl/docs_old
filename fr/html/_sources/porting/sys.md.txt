```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/fr/porting/sys.md
```
# Aperçu système

![](/misc/sys.png "System architecture with Littlev Graphics Library (LittlevGL)")

**Application**
Votre application qui crée l'interface graphique et gère les tâches spécifiques.

**LittlevGL**
La bibliothèque graphique elle-même. Votre application peut communiquer avec la bibliothèque pour créer une interface graphique. Elle contient une interface HAL (Hardware Abstraction Layer, couche d'abstraction matérielle) permettant d’enregistrer vos pilotes de périphérique d’affichage et d'entrée.

**Pilote**
Outre vos pilotes spécifiques, il contient des fonctions pour gérer l'écran, éventuellement un GPU (processeur graphique), et lire un pavé tactile ou des boutons.

* * * 

Il existe ** deux configurations matérielles typiques **, selon que le microcontrôleur dispose ou non d'un contrôleur LCD/TFT. Dans les deux cas, un tampon d'affichage sera nécessaire pour mémoriser l'image actuelle de l'écran.

1. **Microcontrôleur avec contrôleur TFT/LCD**
Si votre microcontrôleur dispose d'un contrôleur  TFT/LCD, vous pouvez connecter un écran directement via une interface RVB.
Dans ce cas, le tampon d'affichage peut résider dans la MEV interne (si le microcontrôleur dispose de suffisamment de MEV) ou dans la MEV externe (si la microcontrôleur a une interface mémoire).

2. **Contrôleur d'affichage externe**
Si votre microcontrôleur ne dispose pas d'un contrôleur  TFT/LCD alors un contrôleur d'affichage externe (ex. SSD1963, SSD1306, ILI9341) doit être utilisé.
Dans ce cas, le microcontrôleur peut communiquer avec le contrôleur d'affichage via un port parallèle, SPI ou parfois I2C.
Le tampon d'affichage est généralement situé dans le contrôleur d'affichage, ce qui économise beaucoup de MEV pour le microcontrôleur.

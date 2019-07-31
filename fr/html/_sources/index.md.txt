```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/fr/index.md
```

```eval_rst
.. include:: /lang.rst

Version PDF: :download:`LittlevGL.pdf <LittlevGL.pdf>`
```

# Bienvenue dans la documentation de LittlevGL !

![](/misc/lv_theme_intro.png "LittlevGL cover")

LittlevGL est une bibliothèque graphique gratuite et à code source ouvert offrant tout ce dont vous avez besoin pour créer une interface graphique embarquée avec des éléments graphiques faciles à utiliser, de superbes effets visuels et une faible empreinte mémoire.

**[Site Internet](https://littlevgl.com) &nbsp; · &nbsp;** 
**[GitHub](https://github.com/littlevgl/lvgl) &nbsp; · &nbsp;** 
**[Forum](https://forum.littlevgl.com) &nbsp; · &nbsp;** 
**[Démonstration en ligne](https://littlevgl.com/live-demo) &nbsp; · &nbsp;** 
**[Simulateur](/get-started/pc-simulator) &nbsp; · &nbsp;** 
**[Blog](https://blog.littlevgl.com/)**

## Points forts
- Eléments de base évolués : boutons, graphiques, listes, curseurs, images, etc.
- Graphiques avancés avec animations, anti-crénelage, opacité, défilement doux
- Périphériques d'entrée variés : pavé tactile, souris, clavier, encodeur, etc.
- Prise en charge multilingue avec encodage UTF-8
- Prise en charge de plusieurs écrans, c-à-d utilisation simultanée d'un écran TFT et d'un écran monochrome
- Eléments graphiques entièrement personnalisables
- Indépendant du matériel : utilisable avec n’importe quel microcontrôleur ou écran
- Adaptable pour fonctionner avec peu de mémoire (64 ko de mémoire Flash, 16 ko de MEV)
- SE, mémoire externe et GPU pris en charge mais non requis
- Fonctionne avec un seul tampon d'affichage même avec des effets graphiques avancés
- Ecrit en C pour une compatibilité maximale (compatible C++)
- Simulateur pour débuter la conception d'interface graphique embarquée sans le matériel embarqué
- Tutoriels, exemples, thèmes pour une conception rapide
- Documentation en ligne et hors ligne
- Gratuit et à code source ouvert, sous licence MIT

## Eléments requis
- Microcontrôleur ou processeur 16, 32 ou 64 bits
- Une vitesse d'horloge &gt; à 16 MHz est recommandée
- Taille de la mémoire Flash/MEM : &gt; à 64 ko pour les composants essentiels (une taille &gt; à 180 ko est recommandée)
- MEV : 
  - Utilisation de MEV statique : ~8..16 ko en fonction des types d'objets et des fonctionnalités utilisés
  - Pile : &gt; à 2 ko (une taille &gt; à 4 ko est recommandée)
  - Données dynamiques (tas) : &gt; à 4 ko (une taille &gt; à 16 ko est recommandée si plusieurs objets sont utilisés).
    Défini par `LV_MEM_SIZE` dans *lv_conf.h*. 
  - Tampon d'affichage :  &gt; à *"résolution horizontale"* pixels (une taille &gt; à 10 &times; *"résolution horizontale"* est recommandée) 
-  Compilateur conforme à C99 ou plus récent
- Connaissances de bases en C (ou C++)  : [pointeurs](https://www.tutorialspoint.com/cprogramming/c_pointers.htm), [structures](https://www.tutorialspoint.com/cprogramming/c_structures.htm), [fonctions de rappel](https://www.geeksforgeeks.org/callbacks-in-c/).

*Notez que l'utilisation de la mémoire peut varier en fonction de l'architecture, du compilateur et des options de compilation.*


## FAQ

### Où commencer ?
- Pour un aperçu général de LittlevGL, visitez [littlevgl.com](https://littlevgl.com)
- Accédez à la section [Démarrer](/get-started/index) pour essayer des démonstrations en ligne dans votre navigateur, en savoir plus sur le simulateur et les bases de LittlevGL.
- Vous trouverez un guide de portage détaillé dans la section [Portage](/porting/index).
- Pour savoir comment LittlevGL fonctionne, accédez à 
 [Vue d'ensemble](/overview/index).
- Pour lire des tutoriels ou partager vos propres expériences, accédez au [Blog](https://blog.littlevgl.com)
- Pour découvrir le code source de la bibliothèque, consultez-le sur GitHub : [https://github.com/littlevgl/lvgl/](https://github.com/littlevgl/lvgl/).


### Où puis-je poser des questions ?
Pour poser des questions sur le forum : [https://forum.littlevgl.com/](https://forum.littlevgl.com/).

Nous utilisons le suivi des problèmes de [GitHub](https://github.com/littlevgl/lvgl/issues) pour les discussions relatives au développement. Vous ne devez donc l'utiliser que si votre question ou votre problème est étroitement lié au développement de la bibliothèque.


### Est-ce que mon microcontrôleur/matériel est supporté ?
Chaque microcontrôleur capable de piloter un affichage via un port parallèle, SPI, une interface RVB ou autre, et conforme aux [éléments requis](#elements-requis), est pris en charge par LittlevGL.
Cela inclut
- Les microcontrôleurs "courants" tels que les STM32F, STM32H, NXP Kinetis, LPC, iMX, dsPIC33, PIC32, etc.
- Les modules Bluetooth, GSM, WiFi tels que les Nordic NRF et Espressif ESP32
- Le tampon de trame de Linux comme /dev/fb0 ce qui inclut également les ordinateurs monocartes comme le Raspberry Pi
- Et tout ce qui possède un microcontrôleur suffisamment puissant et le nécessaire pour piloter un écran

### Mon écran est-il supporté?
LittlevGL nécessite uniquement un simple pilote pour copier un tableau de pixels vers une zone donnée de l'affichage. Si vous pouvez le faire avec votre écran, vous pouvez utiliser cet écran avec LittlevGL.
Cela inclut
- Les TFT avec une profondeur de couleur de 16 ou 24 bits
- Les moniteurs avec port HDMI
- Les petits écrans monochromes
- Les écrans à affichages en niveaux de gris
- Les matrices LED
- Ou tout autre affichage où vous pouvez contrôler la couleur/l'état des pixels

Consultez la section [Portage](/porting/display) pour en savoir plus.

### LittlevGL est-il libre ? Comment puis-je l'utiliser dans un produit commercial ?
LittlevGL est fourni avec une licence MIT, ce qui signifie que vous pouvez le télécharger et l’utiliser à vos fins sans obligation.

### Rien ne se passe, mon pilote d'affichage n'est pas appelé. Qu'est-ce que j'ai raté ?
Assurez-vous que vous appelez `lv_tick_inc(x)` dans une interruption et `lv_task_handler ()` dans votre boucle principale `while (1)`.

Apprenez-en plus dans les sections [Tic](/porting/tick) et [Gestionnaire de tâche](/porting/task-handler).

### Pourquoi le pilote d'affichage n'est appelé qu'une seule fois ? Seule la partie supérieure de l'écran est actualisée.
Assurez-vous que vous appelez `lv_disp_flush_ready(drv)` à la fin de votre *fonction de rappel du pilote d'affichage*.

### Pourquoi je ne vois que des parasites à l'écran?
Il y a probablement un bogue dans votre pilote d'affichage. Essayez le code suivant sans utiliser LittlevGL :

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

### Pourquoi vois-je des couleurs incorrectes à l'écran ?
Le format de couleur de LittlevGL n'est probablement pas compatible avec le format de couleur de votre écran. Vérifiez `LV_COLOR_DEPTH` dans *lv_conf.h*.

Si vous utilisez des couleurs 16 bits avec SPI (ou toute autre interface orientée octets), vous devez probablement définir `LV_COLOR_16_SWAP 1` dans *lv_conf.h*. Les octets supérieurs et inférieurs des pixels seront échangés.

### Comment accélérer mon interface utilisateur ?
- Activez les optimisations du compilateur
- Augmentez la taille du tampon d'affichage
- Utilisez 2 tampons d'affichage et transférez le tampon en DMA (ou une technique similaire) en arrière-plan
- Augmentez la vitesse de fonctionnement des ports SPI ou parallèle si vous les utilisez pour piloter l'affichage
- Si votre écran dispose d'un port SPI, envisagez de passer à un modèle avec port parallèle, car son débit est beaucoup plus élevé.
- Conservez le tampon d'affichage dans la MEV interne (pas la SRAM externe) car LittlevGL l'utilise intensivement ce qui implique un temps d'accès minimal.
 
### Comment réduire l'utilisation de mémoire flash/MEM ?
Vous pouvez désactiver toutes les fonctionnalités (animations, système de fichiers, GPU, etc.) et les types d'objet non utilisés dans *lv_conf.h*.

Si vous utilisez GCC, vous pouvez ajouter
- `-fdata-sections -ffunction-sections` aux options du compilateur
- `--gc-sections` aux options de l'éditeur de liens

pour supprimer les fonctions et variables inutilisées.

### Comment réduire l'utilisation de la MEV
- Réduisez la taille du *tampon d'affichage*
- Réduisez `LV_MEM_SIZE` dans *lv_conf.h*. Cette mémoire est utilisée lorsque vous créez des objets tels que des boutons, des étiquettes, etc.
- Pour travailler avec un `LV_MEM_SIZE` réduit, vous pouvez créer les objets uniquement à l'utilisation et les supprimer lorsqu'ils ne sont plus nécessaires.
 
### Comment travailler avec un système d'exploitation ?

Pour travailler avec un système d'exploitation où les tâches peuvent s'interrompre, vous devez protéger les appels de fonctions liés à LittlevGL avec un mutex. Consultez la section [Système d'exploitation](/porting/os) pour en savoir plus.

### Comment contribuer à LittlevGL ?
Il y a plusieurs façons de contribuer à LittlevGL :
- Ecrivez quelques lignes sur votre projet pour inspirer les autres
- Répondez aux questions des autres
- Signalez et/ou corrigez des bogues
- Suggérez et/ou implémentez de nouvelles fonctionnalités
- Améliorez et/ou traduisez la documentation
- Ecrivez un article de blog sur vos expériences

Pour en savoir plus, consultez le [Guide de contribution](https://blog.littlevgl.com/2018-12-06/contributing)


### Où puis-je trouver la documentation de la version précédente (5.3) ?

Vous pouvez la télécharger ici et l'ouvrir hors ligne :
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

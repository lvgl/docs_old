```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/fr/overview/display.md
```
# Affichage

``` important:: Le concept de base d'*affichage* dans LittlevGL est expliqué dans la section [Portage](/porting/display). Donc, avant de continuer à lire, veuillez lire cette section en premier.
```
Dans LittlevGL, vous pouvez avoir plusieurs affichages, chacun avec ses propres pilotes et objets.

Il est facile de créer plus d'affichages : il suffit d’initialiser les tampons d’affichage et d’enregistrer les pilotes pour chaque affichage.
Lorsque vous créez l'interface utilisateur, utilisez `lv_disp_set_default(disp)` pour indiquer à la librairie dans quel affichage afficher l'objet.


Mais dans quels cas pouvez-vous utiliser le support multi-affichages ? Voici quelques exemples :
- Avoir un écran TFT "normal" avec une interface utilisateur locale et créer des écrans "virtuels" sur VNC à la demande (vous devez ajouter votre propre pilote VNC).
- Avoir un grand écran TFT et un petit écran monochrome.
- Avoir des écrans plus petits et simples dans un grand appareil
- Avoir deux grands écrans TFT : un pour le client et un pour le vendeur

### Utiliser un seul affichage
L'utilisation de plusieurs affichages peut être utile, mais dans la plupart des cas, cela n'est pas nécessaire. Par conséquent, le concept de multi-affichages est complètement masqué si vous ne déclarez qu'un seul affichage.
Par défaut, l’affichage créé en dernier (le seul) est utilisé par défaut.

`lv_scr_act()`, `lv_scr_load(scr)`, `lv_layer_top()`, `lv_layer_sys()`, `LV_HOR_RES` et` LV_VER_RES` sont toujours appliqués sur l’affichage créé en dernier (par défaut).
Si vous passez `NULL` en tant que paramètre `disp` de fonctions associées à l'affichage, l'affichage par défaut sera utilisé.
P.ex. `lv_disp_trig_activity(NULL)` déclenchera une activité utilisateur sur l'affichage par défaut (voir ci-dessous dans [Inactivité](#inactivite)).

### Affichage miroir

Pour refléter l'image de l'affichage sur un autre affichage, vous n'avez pas besoin d'utiliser le support multi-affichages. Transférez simplement le tampon reçu dans `drv.flush_cb` vers un autre affichage.

### Division d'image
Vous pouvez créer un affichage plus grand à partir de plus petits. Voici comment faire :
1. Définissez la résolution des affichages à celle désirée
2. Dans `drv.flush_cb`, tronquez et modifiez le paramètre `area` pour chaque affichage
3. Envoyez le contenu du tampon à chaque affichage pour la zone tronquée

## Ecrans

Chaque affichage possède son propre ensemble d' [Ecrans](/overview/object#ecran-le-parent-le-plus-elementaire) et d'objets à l'écran.

Les écrans peuvent être considérés comme les conteneurs de plus haut niveau sans parent.
La taille de l'écran est toujours égale à celle de son affichage et sa position est (0, 0). Par conséquent, les coordonnées des écrans ne peuvent pas être modifiées, c-à-d `lv_obj_set_pos()`, `lv_obj_set_size()` ou les fonctions similaires ne peuvent pas être utilisées sur les écrans.

Un écran peut être créé à partir de n'importe quel type d'objet, mais les deux types les plus courants sont [Objet de base](/object-types/obj) et [Image](/object-types/img) (pour créer un fond d'écran).

Pour créer un écran, utilisez `lv_obj_t * scr = lv_<type>_create(NULL, copy)`. `copy` peut être un autre écran à copier.

Pour charger un écran, utilisez `lv_scr_load(scr)`. Pour obtenir l'écran actif utilisez `lv_scr_act()`. Ces fonctions agissent sur l’affichage par défaut. Pour spécifier l’affichage, utilisez `lv_disp_get_scr_act(disp)` et `lv_disp_load_scr(disp, scr)`.
 
Les écrans peuvent être supprimés avec `lv_obj_del(scr)` mais assurez-vous de ne pas supprimer l'écran actuellement chargé.


### Ecran opaque
Habituellement, l’opacité de l’écran est `LV_OPA_COVER` afin de fournir un fond solide et totalement couvrant pour les enfants.
Cependant, dans certains cas particuliers, vous voudrez peut-être un écran transparent. Par exemple, si vous avez un lecteur vidéo qui restitue les images vidéo sur un calque mais sur un autre calque, vous souhaitez créer un menu OSD (au-dessus de la vidéo) à l'aide de LittlevGL.
Dans ce cas, le style de l'écran doit avoir `body.opa = LV_OPA_TRANSP` ou `image.opa = LV_OPA_TRANSP` (ou d'autres valeurs `LV_OPA _...`) pour rendre l'écran transparent.
Pour gérer correctement l'opacité des écrans, `LV_COLOR_SCREEN_TRANSP` doit être activé. Notez que cela ne fonctionne qu'avec `LV_COLOR_DEPTH = 32`.
Le canal alpha des couleurs 32 bits sera 0 lorsqu'il n'y a pas d'objets et 255 en cas d'objets solides.


## Fonctionnalités des affichages

### Inactivité

L'inactivité de l'utilisateur est surveillée pour chaque affichage. Chaque utilisation d'un [Périphérique d'entrée](/overview/indev) (s'il est [associé à l'affichage](/porting/indev#autres-fonctionnalites)) compte comme une activité.
Pour obtenir le temps écoulé depuis la dernière activité, utilisez `lv_disp_get_inactive_time(disp)`. Si `NULL` est passé comme paramètre, le temps d'inactivité le plus petit de tous les affichages sera retourné.

Vous pouvez simuler une activité en utilisant `lv_disp_trig_activity(disp)`. Si `disp` est` NULL`, l'affichage par défaut sera utilisé.


## Couleurs

Le module couleur gère toutes les fonctions liées aux couleurs telles que la modification de la profondeur de couleur, la création de couleurs à partir de code hexadécimal, la conversion entre les profondeurs de couleur, le mélange de couleurs, etc.

Les types de variable suivants sont définis par le module couleur :

- **lv_color1_t** Enregistre une couleur monochrome. Pour la compatibilité, il possède également des champs R, G, B mais ils sont tous identiques (1 octet)
- **lv_color8_t** Une structure pour enregistrer R (3 bits), G (3 bits), B (2 bits) composantes d'une couleur 8 bits (1 octet)
- **lv_color16_t** Une structure pour enregistrer R (5 bits), G (6 bits), B (5 bits) composantes d'une couleur 16 bits (2 octets)
- **lv_color32_t** Une structure pour enregistrer R (8 bits), G (8 bits), B (8 bits) composantes d'une couleur 24 bits (4 octets)
- **lv_color_t** Equivaut à `lv_color1/8/16/24_t` selon le paramètre de profondeur de couleur
- **lv_color_int_t** `uint8_t`, `uint16_t` ou `uint32_t` selon le paramètre de profondeur de couleur. Utilisé pour construire des tableaux de couleurs à partir de valeurs numériques.
- **lv_opa_t** Un simple type `uint8_t` pour définir l'opacité.

Les types `lv_color_t`,` lv_color1_t`, `lv_color8_t`, `lv_color16_t` et `lv_color32_t` ont quatre champs :

- **ch.red** canal rouge
- **ch.green** canal vert
- **ch.blue** canal bleu
- **full** rouge + vert + bleu en une seule valeur

Vous pouvez définir la profondeur de couleur actuelle dans *lv_conf.h* en définissant la valeur `LV_COLOR_DEPTH` sur 1 (monochrome), 8, 16 ou 32.

### Conversion de couleur
Vous pouvez convertir une couleur de la profondeur de couleur actuelle en une autre. Les fonctions de conversion retourne un nombre, vous devez donc utiliser le champ `full` :

```c
lv_color_t c;
c.red   = 0x38;
c.green = 0x70;
c.blue  = 0xCC;

lv_color1_t c1;
c1.full = lv_color_to1(c);	/* Retourne 1 pour les couleurs claires, 0 pour les couleurs sombres */

lv_color8_t c8;
c8.full = lv_color_to8(c);	/* Donne un nombre de 8 bits avec la couleur convertie */ 

lv_color16_t c16;
c16.full = lv_color_to16(c); /* Donne un nombre de 16 bits avec la couleur convertie */

lv_color32_t c32;
c32.full = lv_color_to32(c);	/* Donne un nombre de 32 bits avec la couleur convertie */
```

### Permutation 16 bits
Vous pouvez définir `LV_COLOR_16_SWAP` dans *lv_conf.h* pour permuter les octets de *couleurs RGB565*. C'est utile si vous transférez les couleurs 16 bits via une interface orientée octet comme SPI.
Comme les nombres de 16 bits sont stockés au format Little Endian (octet le moins significatif à l'adresse la plus basse), l'interface envoie d'abord l'octet le moins significatif. Cependant, les écrans ont généralement besoin de l'octet le plus significatif en premier. Une non-concordance dans l'ordre des octets entraînera une altération des couleurs.


### Créer et mélanger les couleurs
Vous pouvez créer des couleurs avec la profondeur de couleur actuelle à l'aide de la macro LV_COLOR_MAKE. Il faut 3 arguments (rouge, vert, bleu) sous forme de nombres de 8 bits.
Par exemple, pour créer une couleur rouge clair : `my_color = COLOR_MAKE(0xFF, 0x80,0x80)`.

Les couleurs peuvent aussi être créées à partir de codes hexadécimaux : `my_color = lv_color_hex(0x288ACF)` ou `my_color = lv_color_hex(0x28C)`.

Le mélange de deux couleurs est possible avec `mixed_color = lv_color_mix(color1, color2, ratio)`. Le ratio peut être 0..255. 0 donne entièrement color2, 255 donne entièrement color1.

Les couleurs peuvent aussi être créées avec l’espace HSV en utilisant `lv_color_hsv_to_rgb(hue, saturation, value)`. `hue` devrait être dans la plage 0..360, `saturation` et `value` dans la plage 0..100.

### Opacité
Pour décrire l'opacité, le type `lv_opa_t` est créé comme équivalent d'un `uint8_t`. Quelques définitions sont également introduites :

- **LV_OPA_TRANSP** Valeur : 0, l'opacité rend la couleur totalement transparente.
- **LV_OPA_10** Valeur : 25, signifie que la couleur est un peu couvrante
- **LV_OPA_20 ... OPA_80** viennent logiquement
- **LV_OPA_90** Valeur : 229 signifie que la couleur est presque entièrement couvrante
- **LV_OPA_COVER** Valeur : 255, signifie que la couleur couvre entièrement

Vous pouvez également utiliser les définitions `LV_OPA_*` dans `lv_color_mix()` en tant que *ratio*.

### Couleurs intégrées

Le module couleur définit les couleurs les plus basiques :

- ![#000000](https://placehold.it/15/000000/000000?text=+) `LV_COLOR_BLACK`
- ![#808080](https://placehold.it/15/808080/000000?text=+) `LV_COLOR_GRAY`
- ![#c0c0c0](https://placehold.it/15/c0c0c0/000000?text=+) `LV_COLOR_SILVER`
- ![#ff0000](https://placehold.it/15/ff0000/000000?text=+) `LV_COLOR_RED`
- ![#800000](https://placehold.it/15/800000/000000?text=+) `LV_COLOR_MARRON`
- ![#00ff00](https://placehold.it/15/00ff00/000000?text=+) `LV_COLOR_LIME`
- ![#008000](https://placehold.it/15/008000/000000?text=+) `LV_COLOR_GREEN`
- ![#808000](https://placehold.it/15/808000/000000?text=+) `LV_COLOR_OLIVE`
- ![#0000ff](https://placehold.it/15/0000ff/000000?text=+) `LV_COLOR_BLUE`
- ![#000080](https://placehold.it/15/000080/000000?text=+) `LV_COLOR_NAVY`
- ![#008080](https://placehold.it/15/008080/000000?text=+) `LV_COLOR_TAIL`
- ![#00ffff](https://placehold.it/15/00ffff/000000?text=+) `LV_COLOR_CYAN`
- ![#00ffff](https://placehold.it/15/00ffff/000000?text=+) `LV_COLOR_AQUA`
- ![#800080](https://placehold.it/15/800080/000000?text=+) `LV_COLOR_PURPLE`
- ![#ff00ff](https://placehold.it/15/ff00ff/000000?text=+) `LV_COLOR_MAGENTA`
- ![#ffa500](https://placehold.it/15/ffa500/000000?text=+) `LV_COLOR_ORANGE`
- ![#ffff00](https://placehold.it/15/ffff00/000000?text=+) `LV_COLOR_YELLOW`

ainsi que `LV_COLOR_WHITE`.



## API


### Affichage

```eval_rst

.. doxygenfile:: lv_disp.h
  :project: lvgl
        
```

### Couleurs

```eval_rst

.. doxygenfile:: lv_color.h
  :project: lvgl
        
```

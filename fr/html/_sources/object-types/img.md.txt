```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/fr/object-types/img.md
```
# Image (lv_img)

## Vue d’ensemble

Les images sont les objets de base pour afficher des images.

### Image source
Pour offrir un maximum de flexibilité, la source de l'image peut être :

- une variable dans le code (un tableau C avec les pixels),
- un fichier enregistré sur support externe (comme une carte SD),
- un texte avec [symboles](/overview/font).

Pour définir la source d'une image, utilisez `lv_img_set_src(img, src)`

Pour générer un **tableau de pixels** à partir d’une image PNG, JPG ou BMP, utilisez le [convertisseur d’images en ligne](https://littlevgl.com/image-to-c-array) et définissez l'image convertie avec son pointeur : `lv_img_set_src(img1, &converted_img_var)`.
Pour rendre la variable visible dans le fichier C, vous devez la déclarer avec `LV_IMG_DECLARE(converted_img_var)`.

Pour utiliser des **fichiers externes**, vous devez également convertir les fichiers image à l'aide de l'outil de conversion en ligne, mais vous devez dans ce cas sélectionner le format de sortie binaire.
Vous devez également utiliser le module de système de fichiers de LittlevGL et enregistrer un pilote avec certaines fonctions pour le fonctionnement de base des fichiers. Allez dans [Système de fichiers](/overview/file-system) pour en savoir plus.
Pour définir une source d'image à partir d'un fichier, utilisez `lv_img_set_src(img, "S:folder1/my_img.bin")`.


Vous pouvez définir un **symbole** de la même manière que pour les [étiquettes](/object-types/label). Dans ce cas, l'image sera rendue sous forme de texte conformément à la *police* spécifiée dans le style.
Cela permet d’utiliser des "lettres" monochromes lègères au lieu d’images réelles. Pour définir une source d'image à partir d'un symbole, utilisez `lv_img_set_src(img1, LV_SYMBOL_OK)`.

### Etiquette comme image
Les images et les étiquettes ont parfois la même utilisation. P.ex., décrire ce que fait un bouton. Par conséquent, les images et les étiquettes sont quelque peu interchangeables.
Pour gérer cela, les images peuvent même afficher des textes en utilisant `LV_SYMBOL_DUMMY` comme préfixe du texte. Par exemple `lv_img_set_src(img, LV_SYMBOL_DUMMY "Some text")`.


### Transparence
Les images internes (variables) et externes prennent en charge 2 méthodes de traitement de la transparence :

- **couleur transparente** les pixels avec la couleur `LV_COLOR_TRANSP` (*lv_conf.h*) seront transparents,
- **canal alpha** un canal alpha est ajouté à chaque pixel.

### Palette et index alpha
Outre le format de couleur *couleurs vraies* (RVB), les formats suivants sont également pris en charge :
- **indexé** l'image a une palette,
- **alpha indexé ** seules les valeurs alpha sont enregistrées.

Ces options peuvent être sélectionnées dans le convertisseur d'images. Pour en savoir plus sur les formats de couleur, lisez la section [Images](/overview/image).

### Coloration
Les images peuvent être re-colorées au moment de l'exécution en n'importe quelle couleur en fonction de la luminosité des pixels. 
C'est très utile pour montrer différents états (sélectionné, désactivé, pressé, etc.) d’une image sans enregistrer plusieurs de versions de la même image.
Cette fonctionnalité peut être activée dans le style en définissant `img.intense` de `LV_OPA_TRANSP` (pas de coloration, valeur : 0) à `LV_OPA_COVER` (coloration totale, valeur : 255).
La valeur par défaut est `LV_OPA_TRANSP`, cette fonctionnalité est donc désactivée.

### Taille automatique
Il est possible de définir automatiquement la taille de l'objet image à la largeur et la hauteur de la source de l'image si ceci est activée par la fonction `lv_img_set_auto_size(image, true)`.
Si la *taille automatique* est activée, lorsqu'un nouveau fichier est défini, la taille de l'objet est automatiquement modifiée. Plus tard, vous pouvez modifier la taille manuellement. La *taille automatique* est activée par défaut si l'image n'est pas un écran

### Mosaïque
Si la taille de l'objet est supérieure à la taille de l'image dans n'importe quelle direction, l'image sera répétée comme une mosaïque.
C'est une fonctionnalité très utile pour créer une grande image à partir d'une source plus petite.
Par exemple, vous pouvez avoir une image *300 x 1* avec un dégradé spécial et la définir comme fond d’écran à l’aide de la fonction mosaïque.

### Décalage
Avec `lv_img_set_offset_x(img, x_ofs)` et`lv_img_set_offset_y(img, y_ofs)`vous pouvez ajouter un décalage à l'image affichée.
Cela est utile si la taille de l'objet est inférieure à la taille de la source de l'image.
En utilisant le paramètre décalage un [atlas de texture](https://en.wikipedia.org/wiki/Texture_atlas) ou un effet d'"image mouvante" peut être créer en [animant](/overview/animation) le décalage x ou y. 


## Styles
Les images utilisent un style qui peut être défini par `lv_img_set_style(lmeter, LV_IMG_STYLE_MAIN, &style)`. Toutes les propriétés `style.image` sont utilisées :
- **image.intense** intensité de coloration (0..255 ou *LV_OPA_...*),
- **image.color** couleur pour colorer ou couleur des images indexées alpha,
- **image.opa** opacité globale de l'image.

Lorsque l'objet Image affiche un texte, les propriétés `style.text` sont utilisées. Voir [étiquette](/object-types/label) pour plus d'informations.

Le style par défaut des images est *NULL* donc elles **héritent du style du parent**.

## Evénements
Seuls les [événements génériques](/overview/event.html#generic-events) sont envoyés par ce type d'objet.

Apprenez-en plus sur les [événements](/overview/event).

## Touches
Aucune *touche* n'est traitée par ce type d'objet.

Apprenez-en plus sur les [touches](/overview/indev).

## Exemple

```eval_rst

.. include:: /lv_examples/src/lv_ex_img/index.rst

```

## API 

```eval_rst

.. doxygenfile:: lv_img.h
  :project: lvgl
        
```

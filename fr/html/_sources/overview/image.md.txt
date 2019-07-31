```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/fr/overview/image.md
```
# Images

Une image peut être un fichier ou une variable qui enregistre l'image elle-même et des métadonnées.

## Enregistrer des images
Vous pouvez enregistrer des images à deux endroits
- en tant que variable en mémoire interne (MEV ou MEM)
- en tant que fichier

### Variables
Les images enregistrées dans une variable ont le type `lv_img_dsc_t` avec les champs suivants :
- **header**
  - *cf* Format de couleur. Voir [ci-dessous](#formats-de-couleur)
  - *w* largeur en pixels (<= 2048)
  - *h* hauteur en pixels (<= 2048)
  - *always zero* 3 bits qui doivent toujours être à zéro
  - *reserved* réservé pour une utilisation future
- **data**pointeur sur un tableau où l'image elle-même est enregistrée
- **data_size** longueur de `data` en octets

### Fichiers
Pour traiter les fichiers, vous devez ajouter un *lecteur* à LittlevGL. En bref, un lecteur est une collection de fonctions (*open*, *read*, *close*, etc.) enregistrées dans LittlevGL pour effectuer des opérations sur les fichiers.
Vous pouvez ajouter une interface à un système de fichiers standard (FAT32 sur une carte SD) ou créer votre propre système de fichiers pour lire des données à partir d'une mémoire Flash SPI.
Dans tous les cas, un lecteur n'est qu'une abstraction pour lire et/ou écrire des données dans une mémoire.
Voir la section [Système de fichiers](/overview/file-system) pour en apprendre plus.


## Formats de couleur
Divers formats de couleur intégrés sont pris en charge:
- **LV_IMG_CF_TRUE_COLOR** Enregistre simplement les couleurs RVB
- **LV_IMG_CF_TRUE_COLOR_ALPHA** Enregistre les couleurs RVB mais ajoute également un octet Alpha pour chaque pixel
- **LV_IMG_CF_TRUE_COLOR_CHROMA_KEYED** Enregistre les couleurs RVB, mais si un pixel prend la valeur `LV_COLOR_TRANSP` (défini dans *lv_conf.h*), le pixel sera transparent
- **LV_IMG_CF_INDEXED_1/2/4/8BIT** Utilise une palette avec 2, 4, 16 ou 256 couleurs et enregistre chaque pixel sur 1, 2, 4 ou 8 bits
- **LV_IMG_CF_ALPHA_1/2/4/8BIT** Enregistre uniquement la valeur Alpha sur 1, 2, 4 ou 8 bits. Dessine les pixels avec la couleur `style.image.color` et l'opacité définie.

Les octets des images *Couleurs vraies* 32 bits sont enregistrés dans l'ordre suivant
- Byte 0: Bleu
- Byte 1: Vert
- Byte 2: Rouge
- Byte 3: Alpha

Pour une profondeur de couleur de 16 bits
- Byte 0: Vert 3 bits de poids faible, Bleu 5 bits 
- Byte 1: Rouge 5 bits, Vert 3 bits de poids fort
- Byte 2: octet Alpha (seulement avec LV_IMG_CF_TRUE_COLOR_ALPHA)

Pour une profondeur de couleur de 8 bits
- Byte 0: Rouge 3 bits, Vert 3 bits, Bleu 2 bits
- Byte 2: octet Alpha (seulement avec LV_IMG_CF_TRUE_COLOR_ALPHA)


Vous pouvez enregistrer des images au format *brut* pour indiquer qu'il ne s'agit pas d'un format de couleur intégré et qu'un [Décodeur d'images](#decodeur-d-images) doit être utilisé pour décoder l'image.
- **LV_IMG_CF_RAW** Une image brute, p.ex. une image PNG ou JPG
- **LV_IMG_CF_RAW_ALPHA** Indique que l'image a un canal alpha et qu'un octet Alpha est ajouté pour chaque pixel
- **LV_IMG_CF_RAW_CHROME_KEYED** Indique que l'image a une couleur transparente comme indiqué par `LV_IMG_CF_TRUE_COLOR_CHROMA_KEYED` ci-dessus.


## Ajouter et utiliser des images

Vous pouvez ajouter des images à LittlevGL de deux manières :
- utiliser le convertisseur en ligne
- créer manuellement des images

### Convertisseur en ligne
Le convertisseur d’image en ligne est disponible [ici]( https://littlevgl.com/image-to-c-array).

Vous devez sélectionner une image *BMP*, *PNG* ou *JPG*, lui donner un nom, sélectionner le [Format de couleur](#formats-de-couleur), sélectionner le type (fichier ou variable) et cliquer sur le bouton *Convert*. Le fichier de résultat est téléchargé.

Dans le cas de tableaux C (variables), les données de l'image sont incluses pour toutes les profondeurs de couleurs (1, 8, 16 ou 32) et les données à utiliser seront sélectionnées lors de la compilation en fonction de `LV_COLOR_DEPTH` dans *lv_conf.h*.

Dans le cas de fichiers, vous devez indiquer le format de couleur souhaité
- Binary RGB332 pour une profondeur de couleur de 8 bits
- Binary RGB565 pour une profondeur de couleur de 16 bits
- Binary RGB565 pour une profondeur de couleur de 16 bits (les deux octets sont permutés)
- Binary RGB888 pour une profondeur de couleur de 32 bits

### Créer une image manuellement
Si vous réalisez une image au moment de l'exécution, vous pouvez créer une variable d'image pour l'afficher. Par exemple :

```c
uint8_t my_img_data[] = {0x00, 0x01, 0x02, ...};

static lv_img_dsc_t my_img_dsc = {
    .header.always_zero = 0,
    .header.w = 80,
    .header.h = 60,
    .data_size = 80 * 60 * LV_COLOR_DEPTH / 8,
    .header.cf = LV_IMG_CF_TRUE_COLOR,          /* Définit le format de couleur */
    .data = my_img_data,
};

```

Si le format de couleur est `LV_IMG_CF_TRUE_COLOR_ALPHA`, vous pouvez définir `data_size` comme `80 * 60 * LV_IMG_PX_SIZE_ALPHA_BYTE`.

Une autre option pour créer une image au moment de l'exécution consiste à utiliser l'objet [Canvas](/object-types/canvas).

### Utiliser des images

Le moyen le plus simple d'utiliser une image dans LittlevGL consiste à l'afficher avec un objet [Image](/object-types/img):

```c
lv_obj_t * icon = lv_img_create(lv_scr_act(), NULL);

/* A partir d'une variable */
lv_img_set_src(icon, &my_icon_dsc);

/* A partir d'un fichier */
lv_img_set_src(icon, "S:my_icon.bin");
```

Si l'image a été convertie avec le convertisseur en ligne, vous devez utiliser `LV_IMG_DECLARE(my_icon_dsc)` pour déclarer l'icône dans le fichier où vous souhaitez l'utiliser.


## Décodeur d'images
Comme vous pouvez le voir dans la section [Formats de couleur] (#formats-de-couleur), LittlevGL prend en charge plusieurs formats d'image intégrés. Cependant, il ne supporte pas par exemple les formats PNG ou JPG.
Pour gérer les formats d'image non intégrés, vous devez utiliser des librairie externes et les attacher à LittlevGL via l'interface *décodeur d'images*.

Le décodeur d'image comprend 4 fonctions :
- **info** obtient des informations de base sur l'image (largeur, hauteur et format de couleur)
- **open** ouvre l'image : enregistre l'image décodée. 
 `NULL` indique que l'image peut être lue ligne par ligne
- **read** si *open* ne traite pas complètement l'image, cette fonction devrait retourner les données décodées (maximum 1 ligne) à partir d'une position donnée.
- **close** ferme l'image ouverte, libére les ressources allouées.

Vous pouvez ajouter n'importe quel nombre de décodeurs d'image. Quand une image doit être dessinée, la librairie essaiera tout les décodeurs d’images enregistrés jusqu’à en trouver un capable d’ouvrir l’image, c-à-d de manipuler le format.

Les formats `LV_IMG_CF_TRUE_COLOR_...`, `LV_IMG_INDEXED_...` and `LV_IMG_ALPHA_...` sont connus par le décodeur intégré.

### Formats d'image personnalisés

Le moyen le plus simple de créer une image personnalisée consiste à utiliser le convertisseur d’image en ligne et à définir le format `Raw`, `Raw with alpha` ou  `Raw with chrome keyed`. Le convertisseur prendra tous les octets de l'image sélectionnée et les écrira en tant que données d'image.
`header.cf` sera respectivement `LV_IMG_CF_RAW`, `LV_IMG_CF_RAW_ALPHA` ou `LV_IMG_CF_RAW_CHROME_KEYED`.Vous devez choisir le bon format en fonction de vos besoins : image normale, utilisation de canal alpha ou de couleur transparente.

Après décodage, les formats *bruts* sont considérés comme des *couleurs vraies*. En d’autres termes, le décodeur d’image doit décoder les images *brutes* en *vraies couleurs* conformément au format décrit dans la section [Formats de couleur](#formats-de-couleur).

Si vous voulez créer une image vraiment personnalisée, vous devez utiliser les formats de couleur `LV_IMG_CF_USER_ENCODED_0..7`. Cependant, la librairie peut dessiner les images uniquement au format *couleurs vraies* (ou *brut*, mais finalement, elles sont supposées être au format *couleurs vraies*).
Donc, les formats `LV_IMG_CF_USER_ENCODED_...` ne sont pas connus de la librairie . Ils doivent donc être décodés dans l'un des formats connus de la section [Formats de couleur](#formats-de-couleur).
Il est possible de décoder d'abord l'image dans un format de couleur non vraie, par exemple `LV_IMG_INDEXED_4BITS`, puis d'appeler les fonctions du décodeur intégré pour la convertir en *couleurs vraies*.

Pour les formats *encodés par l'utilisateur*, le format de couleur (`dsc-> header.cf`) doit être modifié en conséquence, dans la fonction open.
 

### Enregistrer un décodeur d'image

Par exemple, si vous voulez que LittlevGL "comprenne" les images PNG, vous devez créer un nouveau décodeur d'images et définir certaines fonctions pour ouvrir/fermer les fichiers PNG. Voici à quoi cela devrait ressembler :

```c
/* Crée un nouveau décodeur et enregistre les fonctions */
lv_img_decoder_t * dec = lv_img_decoder_create();
lv_img_decoder_set_info_cb(dec, decoder_info);
lv_img_decoder_set_open_cb(dec, decoder_open);
lv_img_decoder_set_close_cb(dec, decoder_close); 


/**
 * Obtient les informations sur une image PNG
 * @param decoder pointeur vers le décodeur auquel cette fonction appartient
 * @param src peut être un nom de fichier ou un pointeur sur un tableau C
 * @param header enregistre l'information ici
 * @returnLV_RES_OK : pas d'erreur ; LV_RES_INV : impossible d'obtenir l'information
 */
static lv_res_t decoder_info(lv_img_decoder_t * decoder, const void * src, lv_img_header_t * header)
{
  /* Vérifie si le type `src` est connu du décodeur */
  if(is_png(src) == false) return LV_RES_INV; 

  ...
  
  header->cf = LV_IMG_CF_RAW_ALPHA;
  header->w = width;
  header->h = height;
}

/**
 * Ouvre une image PNG et retourne l'image décodée
 * @param decoder pointeur vers le décodeur auquel cette fonction appartient
 * @param dsc pointeur sur le descripteur de cette session de décodage
 * @returnLV_RES_OK : pas d'erreur ; LV_RES_INV : impossible d'obtenir l'information
 */
static lv_res_t decoder_open(lv_img_decoder_t * decoder, lv_img_decoder_dsc_t * dsc)
{

  /* Vérifie si le type `src` est connu du décodeur */
  if(is_png(src) == false) return LV_RES_INV; 
  
  /* Décode et enregistre l'image. Si `dsc->img_data` est `NULL`, la fonction `read_line` sera appelée pour obtenir les données de l'image ligne par ligne */
  dsc->img_data = my_png_decoder(src);
  
  /* Change le format de couleur si nécessaire. Pour le PNG, généralement un format 'brut' convient */
  dsc->header.cf = LV_IMG_CF_...
  
  /* Appelle une fonction de décodeur intégré si nécessaire. Ce n'est pas nécessaire si `my_png_decoder` a décodé l'image au format couleurs vraies. */
  lv_res_t res = lv_img_decoder_built_in_open(decoder, dsc);
  
  return res;
}

/**
 * Décode `len` pixels à partir des coordonnées fournies `x`, `y` et enregistre-les dans `buf`.
* Requis uniquement si la fonction "open" ne peut pas décoder l'intégralité du tableau de pixels (dsc->img_data == NULL).
 * @param decoder pointeur vers le décodeur associé à la fonction 
 * @param dsc pointeur vers le descripteur de décodeur
 * @param x coordonnée x de début
 * @param y coordonnée y de début
 * @param len nombre de pixels à décoder
 * @param buf un tampon pour enregistrer les pixels décodés
 * @return LV_RES_OK : ok ; LV_RES_INV : échec
 */
lv_res_t decoder_built_in_read_line(lv_img_decoder_t * decoder, lv_img_decoder_dsc_t * dsc, lv_coord_t x,
                                                  lv_coord_t y, lv_coord_t len, uint8_t * buf)
{
   /* Avec PNG, ce n'est généralement pas nécessaire */

   /* Copie `len` pixels à partir des coordonnées `x` et `y` au format couleurs vraies dans `buf` */
  
}

/**
* Libère les ressources allouées
 * @param decoder pointeur vers le décodeur auquel cette fonction appartient
 * @param dsc pointeur sur le descripteur de cette session de décodage
 */
static void decoder_close(lv_img_decoder_t * decoder, lv_img_decoder_dsc_t * dsc)
{
 /* Libère toutes les données allouées */
  
  /* Appelle la fonction intégrée de fermeture si les fonctions intégrées open/read_line ont été utilisées */
  lv_img_decoder_built_in_close(decoder, dsc);
  
}

```

Donc en résumé :
- Dans `decoder_info`, vous devez collecter les informations de base sur l'image et les mémoriser dans `header`.
- Dans `decoder_open`, vous devez essayer d'ouvrir la source de l'image indiquée par `dsc-> src`. Son type est déjà dans `dsc->src_type == LV_IMG_SRC_FILE/VARIABLE`.
Si le format/type n'est pas pris en charge par le décodeur, retournez `LV_RES_INV`.
Autrement, si vous pouvez ouvrir l'image, un pointeur sur l'image *couleurs vraies* décodée doit être défini dans `dsc-> img_data`.
Si le format est géré mais que vous ne voulez pas décoder l’ensemble de l’image (p.ex. pas de mémoire), définissez `dsc->img_data = NULL` pour appeler `read_line` afin d’obtenir les pixels.
- Dans `decoder_close`, vous devez libérer toutes les ressources allouées.
- `decoder_read` est optionnel. Le décodage de l’ensemble de l’image nécessite de la mémoire et des calculs supplémentaires.
Cependant, si vous pouvez décoder une ligne de l'image sans décoder toute l'image, vous pouvez économiser de la mémoire et du temps.
Pour indiquer que la fonction *line read* doit être utilisée, définissez `dsc->img_data = NULL` dans la fonction `open`.


### Utiliser manuellement un décodeur d'image

LittlevGL utilisera automatiquement les décodeurs d'images enregistrés, mais vous pouvez également les utiliser manuellement. Créez une variable `lv_img_decoder_dsc_t` pour décrire la session de décodage et appelez `lv_img_decoder_open()` et `lv_img_decoder_close() `.

```c

lv_res_t res;
lv_img_decoder_dsc_t dsc;
res = lv_img_decoder_open(&dsc, &my_img_dsc, &lv_style_plain);

if(res == LV_RES_OK) {
  /* Faites quelque chose avec `dsc->img_data` */
  lv_img_decoder_close(&dsc);
}

```


## Mise en cache des images
Parfois, il faut beaucoup de temps pour ouvrir une image.
Continuellement décoder une image PNG ou charger des images à partir d'une mémoire externe lente serait inefficace.
LittlevGL place donc en cache un certain nombre d’images. La mise en cache signifie que certaines images resteront ouvertes, ce qui permet à LittlevGL d'y accéder rapidement à partir de `dsc->img_data` au lieu de les décoder à nouveau.

### Taille du cache
Le nombre d'entrées du cache peut être défini par `LV_IMG_CACHE_DEF_SIZE` dans *lv_conf.h*. La valeur par défaut est 1, de sorte que seule la dernière image utilisée reste ouverte.
La taille du cache peut être modifiée en cours d’exécution avec `lv_img_cache_set_size(entry_num)`

### Valeur des images
Si vous utilisez un grand nombre d'images, LittlevGL ne peut pas toutes les mettre en cache. Au lieu de cela, si une nouvelle image doit être ouverte mais qu'il n'y a pas de place dans le cache, la librairie supprimera une image pour libérer de la place.
Pour décider quelle image supprimer, LittlevGL a mesuré combien de temps il a fallu pour ouvrir chaque image. Les images dont l’ouverture prend le plus de temps sont favorisées et LittlevGL essaie de les conserver en cache le plus longtemps.
Vous pouvez définir manuellement la valeur *temps d'ouverture* dans la fonction d'ouverture du décodeur dans `dsc->time_to_open = temps en ms` pour attribuer une valeur supérieure ou inférieure à l'image (laissez inchangé pour laisser LittlevGL le gérer).

Chaque entrée de cache a une valeur *"durée de vie"*. À chaque ouverture d'image par la mémoire cache, la *durée de vie* de toutes les entrées est réduite pour les rendre plus anciennes.
Lorsqu'une image en cache est utilisée, sa *durée de vie* est augmentée de la valeur de *temps d'ouverture* pour la rendre plus importante.

S'il n'y a plus d'espace dans la mémoire cache, l'entrée avec la plus petite durée de vie sera supprimée.

### Utilisation de la mémoire
Notez que l'image en cache peut consommer de la mémoire en permanence. Par exemple, si 3 images PNG sont mises en cache, elles consomment de la mémoire pendant le temps où elle sont ouvertes.
Par conséquent, il incombe à l'utilisateur de s'assurer qu'il y a assez de MEV pour mettre en cache de grandes images en même temps.

### Nettoyer le cache
Supposons que vous ayez chargé une image PNG dans une variable `lv_img_dsc_t my_png` et que vous l'utilisiez dans un objet` lv_img`. Si l'image est déjà mise en cache et que vous modifiez `my_png-> data`, vous devez avertir LittlevGL de mettre en cache l'image à nouveau.
Pour ce faire, utilisez `lv_img_cache_invalidate_src(&my_png)`. Si `NULL` est passé en paramètre, tout le cache sera nettoyé.


## API

### Décodeur d'image

```eval_rst

.. doxygenfile:: lv_img_decoder.h
  :project: lvgl
        
```


### Cache d'images

```eval_rst

.. doxygenfile:: lv_img_cache.h
  :project: lvgl
        
```

```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/fr/overview/font.md
```
# Polices

Dans LittlevGL, les polices sont des collections d'images matricielles et d’autres informations nécessaires au rendu des images des lettres (glyphes). Une police est stockée dans une variable **lv_font_t** et peut être affectée au champ *text.font* du style. Par exemple :
```c
my_style.text.font = &lv_font_roboto_28;  /* Définit une police plus grande */
```

Les polices ont une propriété **bpp (Bits Par Pixel)**. Il indique combien de bits sont utilisés pour décrire un pixel dans la police. La valeur enregistrée pour un pixel détermine l'opacité du pixel.
De cette façon, avec un *bpp* plus important, les bords de la lettre peuvent être lissés. Les valeurs de *bpp* possibles sont 1, 2, 4 et 8 (une valeur plus élevée signifie une meilleure qualité).

Le * bpp * affecte également la taille de la mémoire requise pour utiliser la police. P.ex. *bpp = 4* rend la police environ 4 fois plus volumineuse que *bpp = 1*.

## Support Unicode

LittlevGL prend en charge les caractères Unicode codés **UTF-8**.
Vous devez configurer votre éditeur pour qu'il enregistre votre code/texte au format UTF-8 (généralement par défaut) et assurez-vous que `LV_TXT_ENC` est défini sur `LV_TXT_ENC_UTF8` dans *lv_conf.h* (ceci est la valeur par défaut).

Pour le vérifier, essayez
```c
lv_obj_t * label1 = lv_label_create(lv_scr_act(), NULL);
lv_label_set_text(label1, LV_SYMBOL_OK);
```

Si tout fonctionne bien, un caractère ✓ devrait être affiché.

## Polices intégrées

Il existe plusieurs polices intégrées de différentes tailles qui peuvent être activées dans lv_conf.h par la définition de constantes symboliques *LV_FONT_...* :
- `LV_FONT_ROBOTO_12` 12 px
- `LV_FONT_ROBOTO_16` 16 px
- `LV_FONT_ROBOTO_22` 22 px
- `LV_FONT_ROBOTO_28` 28 px

Les polices intégrées sont des **variables globales** portant des noms tels que `lv_font_roboto_16` pour une police de 16 pixels de haut. Pour les utiliser dans un style, ajoutez simplement un pointeur sur une variable de police, comme indiqué ci-dessus.

Les polices intégrées ont *bpp = 4*, contiennent les caractères ASCII et utilisent la police [Roboto](https://fonts.google.com/specimen/Roboto).

Outre la plage ASCII, les symboles suivants sont également ajoutés aux polices intégrées à partir de la police [FontAwesome](https://fontawesome.com/).

![](/misc/symbols.png "Built-in Symbols in LittlevGL")

Les symboles peuvent être utilisés ainsi :
```c
lv_label_set_text(my_label, LV_SYMBOL_OK);
```

Ou avec des chaînes :
```c
lv_label_set_text(my_label, LV_SYMBOL_OK "Apply");
```

Ou plusieurs symboles ensemble :
```c
lv_label_set_text(my_label, LV_SYMBOL_OK LV_SYMBOL_WIFI LV_SYMBOL_PLAY);
```

## Ajouter une nouvelle police

Il y a plusieurs manières d'ajouter une nouvelle police à votre projet :
1. Le moyen le plus simple consiste à utiliser le [Convertisseur de polices en ligne](https://littlevgl.com/ttf-font-to-c-array). Il suffit de définir les paramètres, de cliquer sur le bouton *Convert*, de copier la police dans votre projet et de l’utiliser.
2. Utilisez le [Convertisseur de polices hors ligne] (https://github.com/littlevgl/lv_font_conv) (nécessite l'installation de Node.js).
3. Si vous voulez créer quelque chose comme les polices intégrées (police Roboto et symboles) mais de tailles et/ou de plages différentes, vous pouvez utiliser le script `built_in_font_gen.py` du dossier `lvgl/scripts/built_in_font`.
Il nécessite que Python et `lv_font_conv` soient installés.

Pour déclarer la police dans un fichier, utilisez `LV_FONT_DECLARE(my_font_name)`.

Pour rendre les polices disponibles globalement, ajoutez-les à `LV_FONT_CUSTOM_DECLARE` dans *lv_conf.h*.

## Ajouter de nouveaux symboles
Les symboles intégrés sont créés à partir de la police [FontAwesome](https://fontawesome.com/). Pour ajouter de nouveaux symboles à partir de la police FontAwesome, procédez comme suit :
1. Recherchez un symbole sur [https://fontawesome.com] (https://fontawesome.com). Par exemple le symbole [USB](https://fontawesome.com)
2. Ouvrez le [Convertisseur de polices en ligne](https://littlevgl.com/font_conv_new), ajoutez [FontAwesome.ttf] (https://littlevgl.com/tools/FontAwesome.ttf) et ajoutez l’ID Unicode du symbole au champ plage. P.ex. `0xf287` pour le symbole USB.
Plusieurs symboles peuvent être énumérés séparés par `,`.
3. Convertissez la police et copiez-la dans votre projet.
4. Convertissez la valeur Unicode en UTF8. Vous pouvez le faire, par exemple, sur ce [site] (http://www.ltg.ed.ac.uk/~richard/utf-8.cgi?input=f287&mode=hex). Pour `0xf287`, les *octets hexadécimaux UTF-8* sont `EF 8A 87`.
5. Créez un `définition de constante symbolique` à partir des valeurs UTF8 : `#define MY_USB_SYMBOL "\ xEF \ x8A \ x87" `
6. Utilisez le symbole comme les symboles intégrés. `lv_label_set_text (label, MY_USB_SYMBOL)`

## Ajouter un nouveau moteur de polices

L'interface de police de LittlevGL est conçue pour être très flexible.
Vous n'avez pas besoin d'utiliser le moteur de polices interne de LittlevGL, mais vous pouvez ajouter le vôtre.
Par exemple, utilisez [FreeType] (https://www.freetype.org/) pour restituer les glyphes en temps réel à partir de polices TTF ou utilisez une mémoire flash externe pour sauvegarder les images matricielles de la police et les lire lorsque la librairie en a besoin.

Pour ce faire, une variable `lv_font_t` personnalisée doit être créée :
```c
/* Décrit les propriétés d'une police */
lv_font_t my_font;
my_font.get_glyph_dsc = my_get_glyph_dsc_cb;        /* Définit une fonction de rappel pour obtenir des informations sur les glyphes */
my_font.get_glyph_bitmap = my_get_glyph_bitmap_cb;  /* Définit une fonction de rappel pour obtenir l'image matricielle d'un glyphe */
my_font.line_height = height;                       /* La hauteur réelle de la ligne où le texte s'inscrit */
my_font.base_line = base_line;                      /* La ligne de base mesurée à partir du haut de la ligne */
my_font.dsc = something_required;                   /*  Enregistre ici toutes les données spécifiques à l'implémentation */
my_font.user_data = user_data;                      /* Éventuellement des données utilisateur supplémentaires */

...

/* Obtient des informations sur le glyphe de `unicode_letter` dans la police `font`. 
 * Enregistre le résultat dans `dsc_out`.
 * La lettre suivante (`unicode_letter_next`) peut être utilisée pour calculer la largeur requise par ce glyphe (crénage)
 */
bool my_get_glyph_dsc_cb(const lv_font_t * font, lv_font_glyph_dsc_t * dsc_out, uint32_t unicode_letter, uint32_t unicode_letter_next)
{
    /* Votre code ici */
  
    /* Enregistre le résultat.
     * Par exemple ... 
     */
    dsc_out->adv_w = 12;        /* Espace horizontal requis par le glyphe en [px] */
    dsc_out->box_h = 8;         /* Hauteur de l'image en [px] */
    dsc_out->box_w = 6;         /* Largeur de l'image en [px] */
    dsc_out->ofs_x = 0;         /* Déplacement X de l'image en [px] */
    dsc_out->ofs_y = 3;         /* Déplacement Y de l'image mesuré depuis la ligne de base */
    dsc_out->bpp   = 2;         /* Bits par pixel : 1/2/4/8 */
    
    return true;                /* true : glyphe trouvé; false : glyphe non trouvé */
}


/* Obtient l'image matricielle de `unicode_letter` à partir de `font`.*/
const uint8_t * my_get_glyph_bitmap_cb(const lv_font_t * font, uint32_t unicode_letter)
{
    /* Votre code ici */
    
    /* L'image matricielle doit être un flux continu de bits où
     * chaque pixel est représenté par `bpp` bits */ 
    
    return bitmap;    /* Ou NULL si non trouvé */
}
```
 



```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/fr/overview/style.md
```
# Styles

Les *styles* sont utilisés pour définir l'apparence des objets. Un style est une variable structurée avec des attributs tels que couleurs, marges, opacité, police, etc.

Il existe un type de style commun nommé **lv_style_t** pour chaque type d'objet.

En définissant les champs des variables `lv_style_t` et en les affectant à un objet, vous pouvez modifier l'apparence des objets.

``` important:: Les objets mémorisent uniquement un pointeur vers un style. Le style ne peut donc pas être une variable locale détruite après la sortie de la fonction. **Vous devez utiliser des variables statiques, globales ou allouées dynamiquement.**
```

```c
lv_style_t style_1;             /* OK ! Les variables globales pour les styles sont adaptées */
static lv_style_t style_2;      /* OK ! Les variables statiques en dehors des fonctions sont adaptées */
void my_screen_create(void) 
{
  static lv_style_t style_3;    /* OK ! Les variables statiques dans les fonctions sont adaptées */
  lv_style_t style_4;           /* Non ! Les styles ne peuvent pas être des variables locales */

  ...
}
```

## Utilisez les styles

Les objets ont un *style principal* qui détermine l'apparence de leur arrière-plan ou de leur partie principale. Cependant, certains types d'objet ont aussi des styles supplémentaires.

Certains objets ont un seul style. P.ex.
- Etiquette
- Image
- Ligne, etc

Par exemple, un curseur a 3 styles :
- Arrière-plan (style principal)
- Indicateur
- Bouton

Chaque type d'objet a ses propres fonctions de gestion des styles. Par exemple
```c
const lv_style_t * btn_style = lv_btn_get_style(btn, LV_BTN_STYLE_REL);
lv_btn_set_style(btn, LV_BTN_STYLE_REL, &new_style);
```

Pour voir les styles pris en charge par un type d'objet (*LV_<OBJ_TYPE>_STYLE_<STYLE_TYPE>*) vérifier la documentation du [Type d'objet](/object-types/index) particulier.

Si vous **modifiez un style déjà utilisé** par un ou plusieurs objets, les objets doivent être avertis du changement de style. Vous avez deux possibilités pour le faire :

```c
/* Notifie un objet que son style est modifié */
void lv_obj_refresh_style(lv_obj_t * obj); 

/* Notifie tous les objets avec un style donné (NULL pour notifier tous les objets) */
void lv_obj_report_style_mod(void * style);
```

`lv_obj_report_style_mod` ne peut actualiser que les *styles principaux*.

## Héritage de styles

Si le *style principal* d'un objet est `NULL`, son style sera hérité du style de son parent. Cela facilite la création d'une interface cohérente. N'oubliez pas qu'un style décrit beaucoup de propriétés en même temps. Ainsi, par exemple, si vous définissez le style d'un bouton et créez une étiquette avec le style `NULL`, l'étiquette sera rendue en fonction du style du bouton. En d'autres termes, le bouton garantit à ses enfants une apparence correcte.

La définition de la propriété de style `glass` empêchera d'hériter ce style. Vous devez l'utiliser si le style est transparent pour que les enfants utilisent les couleurs et autres des grands-parents.

## Propriétés de style
Un style comporte 5 parties principales : commun, corps, texte, image et ligne. Un objet utilisera les champs qui le concernent.
Par exemple, les *lignes* ne se soucient pas de *letter_space*.
Pour voir quels champs sont utilisés par un type d'objet, voir la documentation des [Types d'objet](/object-types/index).

Les champs d'une structure de style sont les suivants :

#### Propriétés communes
  * **glass** 1: Ne pas hériter de ce style

#### Propriétés de style de corps
Utilisé par les objets rectangulaires
  - **body.main_color** Couleur principale (couleur du haut)
  - **body.grad_color** Dégradé de couleur (couleur de fond)
  - **body.radius** Rayon pour arrondir les angles (`LV_RADIUS_CIRCLE` pour dessiner un cercle)
  - **body.opa** Opacité (0..255 ou *LV_OPA_TRANSP*, *LV_OPA_10*, *LV_OPA_20* ... *LV_OPA_COVER*)
  - **body.border.color** Couleur de bord
  - **body.border.width** Largeur de bord
  - **body.border.part** Segments de bord (*LV_BORDER_LEFT/RIGHT/TOP/BOTTOM/FULL* ou 'OR' de plusieurs valeurs)
  - **body.border.opa** Opacité du bord (0..255 ou *LV_OPA_TRANSP*, *LV_OPA_10*, *LV_OPA_20* ... *LV_OPA_COVER*)
  - **body.shadow.color** Couleur de l'ombre
  - **body.shadow.width** Largeur de l'ombre
  - **body.shadow.type** Type d'ombre (*LV_SHADOW_BOTTOM/FULL*)
  - **body.padding.top** Marge haute
  - **body.padding.bottom** Marge basse
  - **body.padding.left** Marge gauche
  - **body.padding.right** Marge droite
  - **body.padding.inner** Marge intérieure (entre les éléments constitutifs ou les enfants)
  
#### Propriétés de style de texte
Utilisés par les objets qui affichent du texte
  - **text.color** Couleur de texte
  - **text.sel_color** Couleur de texte sélectionné
  - **text.font** Pointeur vers une police
  - **text.opa** Opacité du texte (0..255 ou LV_OPA_TRANSP, LV_OPA_10, LV_OPA_20 ... LV_OPA_COVER*)
  - **text.letter_space** Espace de lettre
  - **text.line_space** Espace de ligne

#### Propriétés de style d'image
Utilisé par les objets de type image ou les icônes sur les objets
  - **image.color** Couleur pour la re-coloration de l'image en fonction de la luminosité des pixels
  - **image.intense** Intensité de re-coloration (0..255 ou *LV_OPA_TRANSP*, *LV_OPA_10*, *LV_OPA_20* ... *LV_OPA_COVER*)
  - **image.opa** Opacité de l'image (0..255 ou *LV_OPA_TRANSP*, *LV_OPA_10*, *LV_OPA_20* ... *LV_OPA_COVER*)

#### Propriétés de style de ligne
Utilisé par des objets contenant des lignes ou des éléments de type ligne
  - **line.color** Couleur de ligne
  - **line.width** Largeur de ligne
  - **line.opa** Opacité de ligne (0..255 or *LV_OPA_TRANSP*, *LV_OPA_10*, *LV_OPA_20* ... *LV_OPA_COVER*)

## Styles intégrés
Il existe plusieurs styles intégrés dans la librairie :

![](/misc/style-built-in.png "Built-in styles in LittlevGL Embedded Graphics Library")

Comme vous pouvez le constater, il existe un style pour les écrans, un pour les boutons, des styles simples ou améliorés et des styles transparents.

Les styles `lv_style_transp`, `lv_style_transp_fit` et `lv_style_transp_tight` diffèrent uniquement par les marges : pour `lv_style_transp_tight` les marges sont nulles, pour `lv_style_transp_fit` seules les marges horizontales et verticalles sont nulles mais il y a une marge intérieure.

``` important:: Les styles intégrés transparents ont *glass = 1* par défaut, ce qui signifie que ces styles (les couleurs, par exemple) ne seront pas hérités par les enfants.
```

Les styles intégrés sont des variables globales `lv_style_t`. Vous pouvez les utiliser ainsi :
```c
lv_btn_set_style(obj, LV_BTN_STYLE_REL, &lv_style_btn_rel)
```

## Créer de nouveaux styles
Vous pouvez modifier les styles intégrés ou en créer de nouveaux.

Lors de la création de nouveaux styles, il est recommandé de copier d'abord un style intégré avec `lv_style_copy(&dest_style, &src_style)` pour s'assurer que tous les champs sont initialisés avec une valeur appropriée.

N'oubliez pas que le style créé doit être `statique` ou global. Par exemple :
```c
static lv_style_t my_red_style;
lv_style_copy(&my_red_style, &lv_style_plain);
my_red_style.body.main_color = LV_COLOR_RED;
my_red_style.body.grad_color = LV_COLOR_RED;
```


## Animations de style
Vous modifiez les styles avec des animations en utilisant la fonction `lv_style_anim _... ()`. Deux styles sont requis pour représenter les états *initial* et *final*, et un troisième style qui sera animé. Voici un exemple pour montrer comment cela fonctionne.

```c
lv_anim_t a;
lv_style_anim_init(&a);                                                 /* Initialisation de base */
lv_style_anim_set_styles(&a, &style_to_anim, &style_start, &style_end); /* Définit les styles à utiliser */
lv_style_anim_set_time(&a, duration, delay);                           /* Définit la durée et le délai */
lv_style_anim_create(&a);                                               /* Crée l'animation */
```

Pour découvrir l'intégralité de l'API des animations de style, voir `lv_core/lv_style.h`.

Ici, vous pouvez en apprendre plus sur les [Animations](/overview/animation).

## Exemple de style
L'exemple ci-dessous illustre l'utilisation des styles.

![](/misc/style-example.png "Styles usage example in LittlevGL Embedded Graphics Library")
```c
/* Crée un style */
static lv_style_t style1;
lv_style_copy(&style1, &lv_style_plain);    /* Copie un style intégré pour initialiser le nouveau style */
style1.body.main_color = LV_COLOR_WHITE;
style1.body.grad_color = LV_COLOR_BLUE;
style1.body.radius = 10;
style1.body.border.color = LV_COLOR_GRAY;
style1.body.border.width = 2;
style1.body.border.opa = LV_OPA_50;
style1.body.padding.left = 5;            /* Marge horizontale, utilisée par l'indicateur de barre ci-dessous */
style1.body.padding.right = 5;
style1.body.padding.top = 5;            /* Marge verticale, utilisée par l'indicateur de barre ci-dessous */
style1.body.padding.bottom = 5;
style1.text.color = LV_COLOR_RED;

/* Crée un simple objet */
lv_obj_t *obj1 = lv_obj_create(lv_scr_act(), NULL);
lv_obj_set_style(obj1, &style1);                        /* Applique le style créé */
lv_obj_set_pos(obj1, 20, 20);                           /* Définit la position */

/* Crée une étiquette sur l'objet. Le style de l'étiquette est NULL par défaut */
lv_obj_t *label = lv_label_create(obj1, NULL);
lv_obj_align(label, NULL, LV_ALIGN_CENTER, 0, 0);       /* Aligne l'étiquette au milieu */

/* Crée une barre */
lv_obj_t *bar1 = lv_bar_create(lv_scr_act(), NULL);
lv_bar_set_style(bar1, LV_BAR_STYLE_INDIC, &style1);    /* Modifie le style de l'indicateur */
lv_bar_set_value(bar1, 70);                             /* Définit la valeur de la barre */
```

## Thèmes
Il est difficile de créer des styles pour votre interface graphique, car vous avez besoin d’une profonde compréhension de la librairie et de compétences en matière de conception. En outre, il faut beaucoup de temps pour créer autant de styles.

Pour accélérer la conception les thèmes sont introduits. Un thème est une collection de styles contenant les styles requis pour chaque type d'objet. Par exemple, 5 styles de boutons décrivant leurs 5 états possibles.
Consultez les [Thèmes] (https://littlevgl.com/themes) existants ou essayez-les dans la section [Démonstration en ligne] (https://littlevgl.com/live-demo).

To be more specific a theme is a structure variable which contains a lot of lv_style_t * fields. For buttons:
```c
theme.btn.rel       /*Released button style*/
theme.btn.pr        /*Pressed button style*/
theme.btn.tgl_rel   /*Toggled released button style*/
theme.btn.tgl_pr    /*Toggled pressed button style*/
theme.btn.ina       /*Inactive button style*/
```

A theme can initialized by: `lv_theme_<name>_init(hue, font)`. Where `hue` is a Hue value from [HSV color space](https://en.wikipedia.org/wiki/Hue) (0..360) and `font` is the font applied in the theme (`NULL` to use the `LV_FONT_DEFAULT`)

When a theme is initialized its styles can be used like this:

![](/misc/theme-example.png "Theme usage example in Littlev Embedded Graphics Library")

```c
/*Create a default slider*/
lv_obj_t *slider = lv_slider_create(lv_scr_act(), NULL);
lv_slider_set_value(slider, 70);
lv_obj_set_pos(slider, 10, 10);

/*Initialize the alien theme with a reddish hue*/
lv_theme_t *th = lv_theme_alien_init(10, NULL);

/*Create a new slider and apply the themes styles*/
slider = lv_slider_create(lv_scr_act(), NULL);
lv_slider_set_value(slider, 70);
lv_obj_set_pos(slider, 10, 50);
lv_slider_set_style(slider, LV_SLIDER_STYLE_BG, th->slider.bg);
lv_slider_set_style(slider, LV_SLIDER_STYLE_INDIC, th->slider.indic);
lv_slider_set_style(slider, LV_SLIDER_STYLE_KNOB, th->slider.knob);
```

You can ask the library to automatically apply the styles from a theme when you create new objects. To do this use `lv_theme_set_current(th)`;
```c
/*Initialize the alien theme with a reddish hue*/
lv_theme_t *th = lv_theme_alien_init(10, NULL);
lv_theme_set_current(th);

/*Create a slider. It will use the style from teh current theme.*/
slider = lv_slider_create(lv_scr_act(), NULL);
```

Themes can be enabled or disabled one by on in `lv_conf.h`.

### Live update
By default if `lv_theme_set_current(th)` is called again it won't refresh the styles of the existing objects. To enable live update of themes enable `LV_THEME_LIVE_UPDATE` in `lv_conf.h`.

Live update will update only those objects whose style are from the theme, i.e. created after the first call of `lv_theme_set_current(th)` or the styles were set manually

# Aperçu rapide

Ici, vous pouvez apprendre les points les plus importants sur LittlevGL. 
Vous devriez le lire en premier pour avoir une impression générale, puis les sections détaillées [Portage](/porting/index) et [Vue d'ensemble](/overview/index) après cela.

## Ajouter LittlevGL à votre projet

Les étapes suivantes montrent comment configurer LittlevGL sur un système embarqué avec un écran et un pavé tactile.
Vous pouvez utiliser le [Simulateur](/get-started/pc-simulator) pour obtenir des projets 'prêts à utiliser' pouvant être exécutés sur votre PC.

- [Téléchargez](https://littlevgl.com/download) ou [clonez](https://github.com/littlevgl/lvgl) la librairie
- Copiez le répertoire `lvgl` dans votre projet
- Copiez `lvgl/lv_conf_templ.h` sous le nom `lv_conf.h` au même niveau que le répertoire `lvgl`et définissez au minimum les macros `LV_HOR_RES_MAX`, `LV_VER_RES_MAX` et `LV_COLOR_DEPTH`. 
- Incluez `lvgl/lvgl.h` quand vous devez utiliser les fonctions de LittlevGL.
- Appelez `lv_tick_inc(x)` chaque `x` millisecondes **à partir d'une horloge ou d'une tâche** (`x` doit être compris entre 1 et 10). Ceci est requis pour la synchronisation interne de LittlevGL.
- Appelez `lv_init()`
- Créez un tampon d'affichage pour LittlevGL
```c
static lv_disp_buf_t disp_buf;
static lv_color_t buf[LV_HOR_RES_MAX * 10];                     /* Déclare un tampon  pour 10 lignes */
lv_disp_buf_init(&disp_buf, buf, NULL, LV_HOR_RES_MAX * 10);    /* Initialise le tampon d'affichage */
```
- Implémentez et enregistrez une fonction qui **copie un tableau de pixels**  vers une zone de l'écran :
```c
lv_disp_drv_t disp_drv;               /* Descripteur du pilote d'affichage */
lv_disp_drv_init(&disp_drv);          /* Initialisation de base */
disp_drv.flush_cb = my_disp_flush;    /* Définit la fonction du pilote */
disp_drv.buffer = &disp_buf;          /* Définit le tampon d'affichage */
lv_disp_drv_register(&disp_drv);      /* Finalement, enregistre le pilote */

void my_disp_flush(lv_disp_t * disp, const lv_area_t * area, lv_color_t * color_p)
{
    int32_t x, y;
    for(y = area->y1; y <= area->y2; y++) {
        for(x = area->x1; x <= area->x2; x++) {
            set_pixel(x, y, *color_p);  /* Définit la couleur d'un pixel de l'écran.*/
            color_p++;
        }
    }

    lv_disp_flush_ready(disp);         /* Indique que les données peuvent être transférées à l'écran */
}

```
- Implémentez et enregistrez une fonction qui peut **lire un périphérique d'entrée**. P.ex. pour un pavé tactile :
```c
lv_indev_drv_t indev_drv;                  /* Descripteur du pilote du périphérique d'entrée */
lv_indev_drv_init(&indev_drv);             /* Initialisation de base */
indev_drv.type = LV_INDEV_TYPE_POINTER;    /* Le pavé tactile est un périphérique semblable à un pointeur */
indev_drv.read_cb = my_touchpad_read;     /* Définit la fonction du pilote */
lv_indev_drv_register(&indev_drv);         /* Finalement, enregistre le pilote */

bool my_touchpad_read(lv_indev_t * indev, lv_indev_data_t * data)
{
    static lv_coord_t last_x = 0;
    static lv_coord_t last_y = 0;

    /* Mémorise l'état et les coordonnées, si pressé */
    data->state = touchpad_is_pressed() ? LV_INDEV_STATE_PR : LV_INDEV_STATE_REL;
    if(data->state == LV_INDEV_STATE_PR) touchpad_get_xy(&last_x, &last_y);

    /* Définit les coordonnées (si relâché, les dernières coordonnées quand pressé) */
    data->point.x = last_x;
    data->point.y = last_y;

    return false; /* Retourne `faux` car pas de tampon et plus de données à lire */
}
```
- Appelez `lv_task_handler()` périodiquement, chaque quelques millisecondes, dans la boucle principale `while(1)`, sur interruption d'une horloge ou à partir d'une tâche du système d'exploitation. 
Cela redessine l'écran si nécessaire, gère les périphériques d'entrée, etc. 


## Apprendre les bases

### Les objets (éléments visuels)

Les éléments graphiques tels que les boutons, les étiquettes, les curseurs, les graphiques, etc. sont appelés des objets dans LittlevGL. Allez à [Types d'objet] (/object-types/index) pour voir la liste complète des types disponibles.

Chaque objet possède un objet parent. L'objet enfant se déplace avec le parent et si vous supprimez le parent, les enfants seront également supprimés. Les enfants ne peuvent être visibles que sur leurs parents.

L'*écran* est le parent "racine". Pour obtenir l'écran actuel, appelez `lv_scr_act()`.

Vous pouvez créer un nouvel objet avec `lv_<type>_create(parent, obj_to_copy)`. Une variable `lv_obj_t *` est retournée qui doit être utilisée comme référence à l'objet pour définir ses paramètres.
Le premier paramètre est le *parent* souhaité, le second paramètre peut être un objet à copier (`NULL` si inutilisé).
Par exemple :
```c
lv_obj_t * slider1 = lv_slider_create(lv_scr_act(), NULL);
```

Pour définir certains attributs de base les fonctions `lv_obj_set_<parameter_name>(obj, <value>)` peuvent être utilisées. Par exemple :
```c
lv_obj_set_x(btn1, 30);
lv_obj_set_y(btn1, 10);
lv_obj_set_size(btn1, 200, 50);
```

Les objets ont également des paramètres spécifiques au type qui peuvent être définis par les fonctions `lv_<type>_set_<parameter_name>(obj, <valeur>)`. Par exemple :
```c
lv_slider_set_value(slider1, 70, LV_ANIM_ON);
```

Pour voir l'API complète, consultez la documentation des types d'objet ou le fichier d'en-tête associé (p.ex. `lvgl/src/lv_objx/lv_slider.h`).

### Styles
Les styles peuvent être affectés aux objets pour changer leur apparence. Un style décrit tout à la fois l'apparence des objets de type rectangle (comme un bouton ou un curseur), des textes, des images et des lignes.

Voici comment créer un nouveau style :
```c
static lv_style_t style1;                 /* Déclare un nouveau style. Devrait être `static` */
lv_style_copy(&style1, &lv_style_plain);  /* Copie un style intégré */
style1.body.main_color = LV_COLOR_RED;          /* Couleur principale */
style1.body.grad_color = lv_color_hex(0xffd83c) /* Dégradé de couleur (orange) */
style1.body.radius = 3;
style1.text.color = lv_color_hex3(0x0F0)        /* Couleur de texte (vert) */
style1.text.font = &lv_font_dejavu_22;          /* Change la police */
...
```

Pour appliquer un nouveau style à un objet, utilisez les fonctions `lv_<type>set_style(obj, LV_<TYPE>_STYLE_<NOM>, &my_style)`. Par exemple :
```c
lv_slider_set_style(slider1, LV_SLIDER_STYLE_BG, &slider_bg_style);
lv_slider_set_style(slider1, LV_SLIDER_STYLE_INDIC, &slider_indic_style);
lv_slider_set_style(slider1, LV_SLIDER_STYLE_KNOB, &slider_knob_style);
```

Si le style d'un objet est `NULL`, il héritera du style de son parent. Par exemple, le style des étiquettes est `NULL` par défaut. Si vous les placez sur un bouton, elles utiliseront les propriétés `style.text` du style du bouton.

Apprenez-en plus dans la section [Styles](/overview/style).

### Evénements
Les événements sont utilisés pour informer l'utilisateur si quelque chose s'est produit avec un objet. Vous pouvez affecter une fonction de rappel à un objet qui sera appelée si l'objet est cliqué, relâché, déplacé, en cours de suppression, etc. Voici à quoi cela ressemble :

```c
lv_obj_set_event_cb(btn, btn_event_cb);                 /* Affecte une fonction de rappel au bouton */

...

void btn_event_cb(lv_obj_t * btn, lv_event_t event)
{
    if(event == LV_EVENT_CLICKED) {
        printf("Cliqué\n");
    }
}
```

Apprenez-en plus dans la section [événements](/overview/event). 


## Exemples 

### Bouton avec étiquette
```c
lv_obj_t * btn = lv_btn_create(lv_scr_act(), NULL);     /* Ajoute un bouton à l'écran actuel */
lv_obj_set_pos(btn, 10, 10);                            /* Définit sa position */
lv_obj_set_size(btn, 100, 50);                          /*Définit sa taille */
lv_obj_set_event_cb(btn, btn_event_cb);                 /* Affecte une fonction de rappel au bouton */

lv_obj_t * label = lv_label_create(btn, NULL);          /* Ajoute une étiquette au bouton */
lv_label_set_text(label, "Button");                     /* Définit le texte de l'étiquette */

...

void btn_event_cb(lv_obj_t * btn, lv_event_t event)
{
    if(event == LV_EVENT_CLICKED) {
        printf("Cliqué\n");
    }
}
```
![](/misc/simple_button_example.*)

### Bouton avec styles
Ajoutez des styles au bouton de l'exemple précédent :
```c
static lv_style_t style_btn_rel;                        /* Une variable pour enregistrer le style relâché */
lv_style_copy(&style_btn_rel, &lv_style_plain);         /* Initialise à partir d'un style intégré */
style_btn_rel.body.border.color = lv_color_hex3(0x269);
style_btn_rel.body.border.width = 1;
style_btn_rel.body.main_color = lv_color_hex3(0xADF);
style_btn_rel.body.grad_color = lv_color_hex3(0x46B);
style_btn_rel.body.shadow.width = 4;
style_btn_rel.body.shadow.type = LV_SHADOW_BOTTOM;
style_btn_rel.body.radius = LV_RADIUS_CIRCLE;
style_btn_rel.text.color = lv_color_hex3(0xDEF);

static lv_style_t style_btn_pr;                         /* Une variable pour enregistrer le style pressé */
lv_style_copy(&style_btn_pr, &style_btn_rel);           /* Initialise à partir du style relâché */
style_btn_pr.body.border.color = lv_color_hex3(0x46B);
style_btn_pr.body.main_color = lv_color_hex3(0x8BD);
style_btn_pr.body.grad_color = lv_color_hex3(0x24A);
style_btn_pr.body.shadow.width = 2;
style_btn_pr.text.color = lv_color_hex3(0xBCD);

lv_btn_set_style(btn, LV_BTN_STYLE_REL, &style_btn_rel);    /* Définit le style relâché du bouton */
lv_btn_set_style(btn, LV_BTN_STYLE_PR, &style_btn_pr);      /* Définit le style pressé du bouton */
```

![](/misc/button_style_example.*)

### Curseur et alignement de l'objet
```c
lv_obj_t * label;

...

/* Crée un curseur au centre de l'affichage */
lv_obj_t * slider = lv_slider_create(lv_scr_act(), NULL);
lv_obj_set_width(slider, 200);                        /* Définit la largeur */
lv_obj_align(slider, NULL, LV_ALIGN_CENTER, 0, 0);    /* Aligne au centre du parent (écran) */
lv_obj_set_event_cb(slider, slider_event_cb);         /* Affecte une fonction de rappel */

/* Crée une étiquette sous le curseur */
label = lv_label_create(lv_scr_act(), NULL);
lv_label_set_text(label, "0");
lv_obj_set_auto_realign(slider, true);
lv_obj_align(label, slider, LV_ALIGN_OUT_BOTTOM_MID, 0, 10);

...

void slider_event_cb(lv_obj_t * slider, lv_event_t event)
{
    if(event == LV_EVENT_VALUE_CHANGED) {
        static char buf[4];                                 /* Maximum 3 octets pour le nombre plus 1 octet final nul */
        snprintf(buf, 4, "%u", lv_slider_get_value(slider));
        lv_label_set_text(slider_label, buf);               /* Actualise le texte */
    }
}
```

![](/misc/slider_example.*)

### Liste et thèmes
```c
/* Textes des éléments de la liste */
const char * txts[] = {"First", "Second", "Third", "Fourth", "Fifth", "Sixth", NULL};

/* Initialise et définit un thème. `LV_THEME_NIGHT` doit être activé dans lv_conf.h. */
lv_theme_t * th = lv_theme_night_init(20, NULL);
lv_theme_set_current(th);

/* Crée une liste */
lv_obj_t* list = lv_list_create(lv_scr_act(), NULL);
lv_obj_set_size(list, 120, 180);
lv_obj_set_pos(list, 10, 10);

/* Ajoute des boutons */
uint8_t i;
for(i = 0; txts[i]; i++) {
    lv_obj_t * btn = lv_list_add_btn(list, LV_SYMBOL_FILE, txts[i]);
    lv_obj_set_event_cb(btn, list_event);       /* Affecte une fonction de rappel */
    lv_btn_set_toggle(btn, true);               /* Active la fonction de bascule */
}

/* Initialise et définit un autre thème. `LV_THEME_MATERIAL` doit être activé dans lv_conf.h.
 * Si `LV_THEME_LIVE_UPDATE 1` alors le style de la liste précédente sera également mis à jour. */
th = lv_theme_material_init(210, NULL);
lv_theme_set_current(th);

/* Crée une autre liste */
list = lv_list_create(lv_scr_act(), NULL);
lv_obj_set_size(list, 120, 180);
lv_obj_set_pos(list, 150, 10);

/* Ajoute des boutons avec les mêmes textes */
for(i = 0; txts[i]; i++) {
    lv_obj_t * btn = lv_list_add_btn(list, LV_SYMBOL_FILE, txts[i]);
    lv_obj_set_event_cb(btn, list_event);
    lv_btn_set_toggle(btn, true);
}

...

static void list_event(lv_obj_t * btn, lv_event_t e)
{
    if(e == LV_EVENT_CLICKED) {
        printf("%s\n", lv_list_get_btn_text(btn));
    }

}
```
![](/misc/list_theme_example.*)

### Utiliser LittlevGL avec Micropython
Apprenez-en plus sur [Micropython](/get-started/micropython).
```python
# Crée un bouton et une étiquette
scr = lv.obj()
btn = lv.btn(scr)
btn.align(lv.scr_act(), lv.ALIGN.CENTER, 0, 0)
label = lv.label(btn)
label.set_text("Button")

# Charge l'écran
lv.scr_load(scr)
```



## Contribuer
LittlevGL utilise le [forum](https://forum.littlevgl.com) pour poser et répondre aux questions et  l'[outil de suivi des problèmes de GitHub](https://github.com/littlevgl/lvgl/issues) pour les discussions relatives au développement (comme les rapports de bogues, les suggestions de fonctionnalités etc.).

Il existe de nombreuses possibilités de contribuer à LittlevGL telles que :
- **Aidez les autres** sur le [forum](https://forum.littlevgl.com).
- **Inspirez les gens** en parlant de votre projet dans la catégorie [Mon projet](https://forum.littlevgl.com/c/my-projects) du forum ou en l'ajoutant à la rubrique [Références](https: / /blog.littlevgl.com/2018-12-26/references)
- **Améliorez et/ou traduisez la documentation.** Visitez le dépôt [Documentation](https://github.com/littlevgl/docs) pour en apprendre plus
**Écrivez un article de blog** sur vos expériences. Regardez comment faire dans le dépôt [Blog] (https://github.com/littlevgl/blog).
- **Signalez et/ou corrigez des bogues** avec l'outil de suivi des problèmes de [GitHub](https://github.com/littlevgl/lvgl/issues)
- **Aidez au développement**. Vérifiez les [problèmes en cours](https://github.com/littlevgl/lvgl/issues), en particulier ceux avec la mention [Aide demandée](https://github.com/littlevgl/lvgl/issues?q=is%3Aissue+is%3Aopen+label%3A%22help+wanted%22) et partagez vos idées sur un sujet ou implémentez une fonctionnalité.

Si vous souhaitez contribuer à LittlevGL, veuillez lire les guides ci-dessous pour commencer.

```eval_rst
- `Guide de contribution <https://blog.littlevgl.com/2018-12-06/contributing>`_
- `Guide de convention de code  <https://github.com/littlevgl/lvgl/blob/master/docs/CODING_STYLE.md>`_

```

```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/fr/overview/indev.md
```
# Périphériques d'entrée

Un périphérique d'entrée signifie généralement :
- Périphérique de type pointeur tel que pavé tactile ou souris
- Claviers, normal ou simple pavé numérique 
- Encodeurs avec mouvement rotatif à gauche / droite et bouton
- Boutons matériels externes affectés à des points spécifiques de l'écran


``` important:: Avant de poursuivre votre lecture, veuillez lire la section [Portage](/porting/indev) sur les périphériques d'entrée
```

## Pointeurs

Les périphériques d’entrée de type pointeur peuvent avoir un curseur (typiquement pour les souris).

```c
...
lv_indev_t * mouse_indev = lv_indev_drv_register(&indev_drv);

LV_IMG_DECLARE(mouse_cursor_icon);                          /* Declare le fichier de l'image. */
lv_obj_t * cursor_obj =  lv_img_create(lv_scr_act(), NULL); /* Crée un objet image pour le curseur */
lv_img_set_src(cursor_obj, &mouse_cursor_icon);             /* Définit la source de l'image */
lv_indev_set_cursor(mouse_indev, cursor_obj);               /* Connecte l'objet image au pilote */

```

Notez que l'objet curseur devrait avoir `lv_obj_set_click(cursor_obj, false)`.
Pour les images *cliquer* est désactivé par défaut.

## Clavier et encodeur

Vous pouvez contrôler entièrement l'interface utilisateur sans pavé tactile ou souris à l'aide d'un clavier ou d'un ou plusieurs encodeurs. Cela fonctionne de manière similaire à la touche  *TAB* sur un PC pour sélectionner l'élément dans une application ou une page Web.

### Groupes

Les objets que vous souhaitez contrôler avec un clavier ou un encodeur doivent être ajoutés à un *groupe*.
Dans chaque groupe, il y a exactement un seul objet focalisé qui reçoit les notifications de touche pressée ou les actions de l'encodeur.
Par exemple, si une [Zone de texte](/object-types/ta) est sélectionnée et que vous appuyez sur une lettre d'un clavier, les codes sont envoyés et traités par la zone de texte.
De la même manière, si un [Curseur](/object-types/slider) est sélectionné et que vous appuyez sur les flèches gauche ou droite, la valeur du curseur sera modifiée.

Vous devez associer un périphérique d'entrée à un groupe. Un périphérique d'entrée peut envoyer les codes à un seul groupe, mais un groupe peut recevoir des données de plusieurs périphériques d'entrée.

Pour créer un groupe, utilisez `lv_group_t * g = lv_group_create()` et pour ajouter un objet au groupe, utilisez `lv_group_add_obj(g, obj)`.

Pour associer un groupe à un périphérique d’entrée, utilisez `lv_indev_set_group(indev, g)`, où `indev` est la valeur de retour de `lv_indev_drv_register() `

#### Codes
Certains codes prédéfinis ont une signification particulière :
- **LV_KEY_NEXT** Sélectionne l'objet suivant
- **LV_KEY_PREV** Sélectionne l'objet précédant
- **LV_KEY_ENTER** Génère les événements `LV_EVENT_PRESSED/CLICKED/LONG_PRESSED` etc
- **LV_KEY_UP** Augmente la valeur ou se déplace vers le haut
- **LV_KEY_DOWN** Diminue la valeur ou se déplace vers le bas
- **LV_KEY_RIGHT** Augmente la valeur ou se déplace vers la droite
- **LV_KEY_LEFT** Diminue la valeur ou se déplace vers la gauche
- **LV_KEY_ESC** Ferme ou quitte (p.ex. ferme une [Liste déroulante](/object-types/ddlist))
- **LV_KEY_DEL**  Supprime (p.ex. le caractère à droite dans une [Zone de texte](/object-types/ta))
- **LV_KEY_BACKSPACE** Supprime le caractère à gauche (p.ex. dans une [Zone de texte](/object-types/ta))
- **LV_KEY_HOME** Se déplace au début ou en haut (p.ex. dans une [Zone de texte](/object-types/ta))
- **LV_KEY_END** Se déplace à la fin (p.ex. dans une [Zone de texte](/object-types/ta))

Les codes spéciaux les plus importants sont : `LV_KEY_NEXT/PREV`, `LV_KEY_ENTER` et `LV_KEY_UP/DOWN/LEFT/RIGHT`. 
Dans votre fonction `read_cb`, vous devez traduire certaines de vos codes en ces codes spéciaux pour naviguer dans le groupe et interagir avec l'objet sélectionné.

Habituellement, il suffit d'utiliser uniquement `LV_KEY_LEFT/RIGHT` car la plupart des objets peuvent être entièrement contrôlés avec eux.

Avec un encodeur, vous devez utiliser uniquement `LV_KEY_LEFT`,` LV_KEY_RIGHT` et `LV_KEY_ENTER`.

#### Edition et navigation

Comme les claviers disposent de nombreuses touches, il est facile de naviguer entre les objets et de les éditer. Cependant, les encodeurs ont un nombre très limité de "touches" ce qui rend la navigation difficile pas défaut. Les modes *navigation* et *édition* sont créés afin de résoudre ce problème avec les encodeurs, .

En mode *navigation*, les `LV_KEY_LEFT/RIGHT` des encodeurs sont traduits en` LV_KEY_NEXT/PREV`. Par conséquent, l'objet suivant ou précédent sera sélectionné en tournant l'encodeur.
Un appui sur `LV_KEY_ENTER` passera en mode *édition*.

En mode *édition*, `LV_KEY_NEXT/PREV` sont utilisés normalement pour éditer l'objet.
En fonction du type d'objet, une pression courte ou longue de `LV_KEY_ENTER` repasse en mode *navigation*.
Généralement, un objet sur lequel vous ne pouvez pas appuyer (comme un [Curseur](/object-types/slider)) quitte le mode *édition* en cas de clic bref, mais avec un objet pour lequel un clic court a une signification (par exemple, [Bouton](/object-types/btn)) un appui long est requis.

#### Styliser l'objet sélectionné
Pour mettre en évidence visuellement l'élément sélectionné, son [Style principal] (/overview/style#utiliser-les-styles) sera mis à jour.
Par défaut, de l'orange est mélangé aux couleurs d'origine du style.
Une fonction de rappel pour modifier le style est définie par `lv_group_set_style_mod_cb(g, my_style_mod_cb)`. Cette fonction reçoit un pointeur sur un groupe d'objet et un style à modifier.
Le modificateur de style par défaut ressemble à ceci (légèrement simplifié) :
```c
static void default_style_mod_cb(lv_group_t * group, lv_style_t * style)
{
    /* Rend les corps un peu orange */
    style->body.border.opa = LV_OPA_COVER;
    style->body.border.color = LV_COLOR_ORANGE;
    style->body.border.width = LV_DPI / 20;

    style->body.main_color   = lv_color_mix(style->body.main_color, LV_COLOR_ORANGE, LV_OPA_70);
    style->body.grad_color   = lv_color_mix(style->body.grad_color, LV_COLOR_ORANGE, LV_OPA_70);
    style->body.shadow.color = lv_color_mix(style->body.shadow.color, LV_COLOR_ORANGE, LV_OPA_60);

    /* Recolore le texte*/
    style->text.color = lv_color_mix(style->text.color, LV_COLOR_ORANGE, LV_OPA_70);

    /* Colorise les images */
    if(style->image.intense < LV_OPA_MIN) {
        style->image.color = LV_COLOR_ORANGE;
        style->image.intense = LV_OPA_40;
    }
}
```

Cette fonction de rappel modificateur de style est utilisée pour les claviers et encodeurs en mode *navigation*.
En mode *édition*, une autre fonction de rappel est utilisée qui peut être définie avec `lv_group_set_style_mod_edit_cb()`. Par défaut, il utilise la couleur verte.


### Démonstration en ligne

Essayez cette [Démonstration en ligne](https://littlevgl.com/demo-touchpadless) pour voir comment une navigation de groupe sans pavé tactile fonctionne dans la pratique.

## API


### Périphérique d'entrée

```eval_rst

.. doxygenfile:: lv_indev.h
  :project: lvgl

```

### Groupes

```eval_rst

.. doxygenfile:: lv_group.h
  :project: lvgl

```

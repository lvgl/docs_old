```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/fr/overview/indev.md
```
# Périphériques d'entrée

An input device usually means:
- Pointer-like input device like touchpad or mouse
- Keypads like a normal keyboard or simple numeric keypad
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

Note that the cursor object should have `lv_obj_set_click(cursor_obj, false)`.
For images, *clicking* is disabled by default.

## Clavier et encodeur

You can fully control the user interface without touchpad or mouse using a keypad or encoder(s). It works similar to the *TAB* key on the PC to select the element in an application or a web page.

### Groupes

The objects, you want to control with keypad or encoder, needs to be added to a *Group*.
In every group, there is exactly one focused object which receives the pressed keys or the encoder actions.
For example, if a [Text area](/object-types/ta) is focused and you press some letter on a keyboard, the keys will be sent and inserted into the text area.
Similarly, if a [Slider](/object-types/slider) is focused and you press the left or right arrows, the slider's value will be changed.

You need to associate an input device with a group. An input device can send the keys to only one group but, a group can receive data from more than one input device too.

Pour créer un groupe, utilisez `lv_group_t g = lv_group_create()` et pour ajouter un objet au groupe, utilisez `lv_group_add_obj(g, obj)`.

Pour associer un groupe à un périphérique d’entrée, utilisez `lv_indev_set_group(indev, g)`, où `indev` est la valeur de retour de `lv_indev_drv_register() `

#### Codes
Certains codes prédéfinis ont une signification particulière :
- **LV_KEY_NEXT** Sélectionne l'objet suivant
- **LV_KEY_PREV** Sélectionne l'objet précédant
- **LV_KEY_ENTER** Triggers `LV_EVENT_PRESSED/CLICKED/LONG_PRESSED` etc. events
- **LV_KEY_UP** Increase value or move upwards
- **LV_KEY_DOWN** Diminue la valeur ou se déplace vers le bas
- **LV_KEY_RIGHT** Augmente la valeur ou se déplace vers la droite
- **LV_KEY_LEFT** Diminue la valeur ou se déplace vers la gauche
- **LV_KEY_ESC** Ferme ou quitte (p.ex. ferme une [Liste déroulante](/object-types/ddlist))
- **LV_KEY_DEL**  Supprime (p.ex. le caractère à droite dans une [Zone de texte](/object-types/ta))
- **LV_KEY_BACKSPACE** Supprime le caractère à gauche (p.ex. dans une [Zone de texte](/object-types/ta))
- **LV_KEY_HOME** Se déplace au début ou en haut (p.ex. dans une [Zone de texte](/object-types/ta))
- **LV_KEY_END** Se déplace à la fin (p.ex. dans une [Zone de texte](/object-types/ta))

The most important special keys are `LV_KEY_NEXT/PREV`, `LV_KEY_ENTER` and `LV_KEY_UP/DOWN/LEFT/RIGHT`.
In your `read_cb` function, you should translate some of your keys to these special keys to navigate in the group and interact with the selected object.

Usually, it's enough to use only `LV_KEY_LEFT/RIGHT` because most of the objects can be fully controlled with them.

With an encoder, you should use only `LV_KEY_LEFT`, `LV_KEY_RIGHT`, and `LV_KEY_ENTER`.

#### Edition et navigation

Since keypad has plenty of keys, it's easy to navigate between the objects and edit them using the keypad. But, the encoders have a limited number of "keys" hence, difficult to navigate using the default options. *Navigate* and *Edit* are created to avoid this problem with the encoders.

In *Navigate* mode, the encoders `LV_KEY_LEFT/RIGHT` is translated to `LV_KEY_NEXT/PREV`. Therefore the next or previous object will be selected by turning the encoder.
Un appui sur `LV_KEY_ENTER` passera en mode *édition*.

In *Edit* mode, `LV_KEY_NEXT/PREV` is usually used to edit the object.
Depending on the object's type, a short or long press of `LV_KEY_ENTER` changes back to *Navigate* mode.
Usually, an object which can not be pressed (like a [Slider](/object-types/slider)) leaves *Edit* mode on short click. But with object where short click has meaning (e.g. [Button](/object-types/btn)), long press is required.

#### Styliser l'objet sélectionné
To visually highlight the focused element, its [Main style](/overview/style#use-the-styles) will be updated.
By default, some orange color is mixed with the original colors of the style.
A new style modifier callback be set by `lv_group_set_style_mod_cb(g, my_style_mod_cb)`. A style modifier callback receives a pointer to a caller group and a pointer to a style to modify.
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

This style modifier callback is used for keypads and encoder in *Navigate* mode.
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

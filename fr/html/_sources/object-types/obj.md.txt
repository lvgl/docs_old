```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/fr/object-types/obj.md
```
# Objet de base (lv_obj)

## Vue d’ensemble

The 'Base Object' implements the basic properties of an object on a screen, such as:

- coordonnées
- objet parent
- enfants
- style principal
- des attributs tels que *Clic autorisé*, *Glissé autorisé*, etc.

In object-oriented thinking, it is the base class which all other objects in LittlevGL inherit from. This, among another things, helps reduce code duplication.

### Coordonnées
The object size can be modified on individual axes with `lv_obj_set_width(obj, new_width)` and `lv_obj_set_height(obj, new_height)`, or both axes can be modified at the same time with `lv_obj_set_size(obj, new_width, new_height)`.

You can set the x and y coordinates relative to the parent with `lv_obj_set_x(obj, new_x)` and `lv_obj_set_y(obj, new_y)`, or both at the same time with `lv_obj_set_pos(obj, new_x, new_y)`.

You can align the object to another with `lv_obj_align(obj, obj_ref, LV_ALIGN_..., x_shift, y_shift)`.

- `obj` is the object to align.
- `obj_ref` is a reference object. `obj` will be aligned to it. If `obj_ref = NULL`, then the parent of `obj` will be used.
- The third argument is the *type* of alignment. These are the possible options:
![](/misc/align.png "Alignment types in LittlevGL")

  The alignment types build like `LV_ALIGN_OUT_TOP_MID`.
- The last two arguments allow you to shift the object by a specified number of pixels after aligning it.

For example, to align a text below an image: `lv_obj_align(text, image, LV_ALIGN_OUT_BOTTOM_MID, 0, 10)`.   
Or to align a text in the middle of its parent: `lv_obj_align(text, NULL, LV_ALIGN_CENTER, 0, 0)`.

`lv_obj_align_origo` works similarly to `lv_obj_align` but, it aligns the center of the object rather than the top-left corner.

For example, `lv_obj_align_origo(btn, image, LV_ALIGN_OUT_BOTTOM_MID, 0, 0)` will align the center of the button the bottom of the image.

The parameters of the alignment will be saved in the object if `LV_USE_OBJ_REALIGN` is enabled in *lv_conf.h*. You can then realign the objects simply by calling `lv_obj_realign(obj)`. (It's equivalent to calling `lv_obj_align` again with the same parameters.)

If the alignment happened with `lv_obj_align_origo`, then it will be used when the object is realigned.

If `lv_obj_set_auto_realign(obj, true)` is used the object will be realigned automatically, if its size changes in `lv_obj_set_width/height/size()` functions. It's very useful when size animations are applied to the object and the original position needs to be kept.

**Note that the coordinates of screens can't be changed. Attempting to use these functions on screens will result in undefined behavior.**

### Parents et enfants
You can set a new parent for an object with `lv_obj_set_parent(obj, new_parent)`. To get the current parent, use `lv_obj_get_parent(obj)`.

To get the children of an object, use `lv_obj_get_child(obj, child_prev)` (from last to first) or `lv_obj_get_child_back(obj, child_prev)` (from first to last).
To get the first child, pass `NULL` as the second parameter and use the return value to iterate through the children. The function will return `NULL` if there are no more children. For example:

```c
lv_obj_t * child;
child = lv_obj_get_child(parent, NULL);
while(child) {
    /* Fait quelque chose avec l'"enfant" */
    child = lv_obj_get_child(parent, child);
}
```

`lv_obj_count_children(obj)` indique le nombre d'enfants d'un objet. `lv_obj_count_children_recursive(obj)` indique également le nombre d'enfants mais compte récursivement les enfants d'enfants.

### Ecrans
When you have created a screen like `lv_obj_create(NULL, NULL)`, you can load it with `lv_scr_load(screen1)`. The `lv_scr_act()` function gives you a pointer to the current screen.

Si vous avez plusieurs d’affichages, il est important de savoir que ces fonctions opèrent sur l’affichage créé en dernier ou explicitement sélectionné (avec `lv_disp_set_default`).

To get the screen an object is assigned to, use the `lv_obj_get_screen(obj)` function.

### Couches
Il y a deux couches générées automatiquement :
- la couche supérieure
- la couche système

They are independent of the screens and the same layers will be shown on every screen. The *top layer* is above every object on the screen and the *system layer* is above the *top layer* too.
You can add any pop-up windows to the *top layer* freely. But, the *system layer* is restricted to system-level things (e.g. mouse cursor will be placed here in `lv_indev_set_cursor()`).

Les fonctions `lv_layer_top()` et `lv_layer_sys()` retournent un pointeur sur la couche supérieure ou la couche système.

You can bring an object to the foreground or send it to the background with `lv_obj_move_foreground(obj)` and `lv_obj_move_background(obj)`.

Read the [Layer overview](/overview/layer) section to learn more about layers.

### Style
The base object stores the [Main style](/overview/style) of the object. To set a new style, use `lv_obj_set_style(obj, &new_style)` function. If `NULL` is set as style, then the object will inherit its parent's style.

Note that, you should use `lv_obj_set_style` only for "Base objects". Every other object type has its own style set function which should be used for them. For example, a button should use `lv_btn_set_style()`.

If you modify a style, which is already used by objects, in order to refresh the affected objects you can use either `lv_obj_refresh_style(obj)` on each object using it or to notify all objects with a given style use `lv_obj_report_style_mod(&style)`. If the parameter of `lv_obj_report_style_mod` is `NULL`, all objects will be notified.

Lisez la section [Styles](/overview/style) pour en savoir plus sur les styles.

### Evènements

To set an event callback for an object, use `lv_obj_set_event_cb(obj, event_cb)`,

To manually send an event to an object, use `lv_event_send(obj, LV_EVENT_..., data)`

Lisez [Evénements](/overview/event) pour en savoir plus sur les événements.

### Attributs
Certains attributs peuvent être activés/désactivés avec `lv_obj_set_...(obj, true/false)` :

- **hidden** -  Hide the object. It will not be drawn and will be considered by input devices as if it doesn't exist., Its children will be hidden too.
- **click** -  Allows you to click the object via input devices. If disabled, then click events are passed to the object behind this one. (E.g. [Labels](/object-types/label) are not clickable by default)
- **top** -  If enabled then when this object or any of its children is clicked then this object comes to the foreground.
- **drag** - Enable dragging (moving by an input device)
- **drag_dir** - Enable dragging only in specific directions. Can be `LV_DRAG_DIR_HOR/VER/ALL`.
- **drag_throw** - Enable "throwing" with dragging as if the object would have momentum
- **drag_parent** - If enabled then the object's parent will be moved during dragging. It will look like as if the parent is dragged. Checked recursively, so can propagate to grandparents too.
- **parent_event** - Propagate the events to the parents too. Checked recursively, so can propagate to grandparents too.
- **opa_scale_enable** - Enable opacity scaling. See the [#opa-scale](Opa scale) section.

### Echelle d'opacité
If `lv_obj_set_opa_scale_enable(obj, true)` is set for an object, then the object's and all of its children's opacity can be adjusted with `lv_obj_set_opa_scale(obj, LV_OPA_...)`.
Les opacités enregistrées dans les styles seront modifiées par ce facteur.

C'est très utile pour estomper/révéler un objet avec des enfants en utilisant une [Animation](/overview/animation).

A little bit of technical background: during the rendering process, the opacity of the object is decided by searching recursively up the object's family tree to find the first object with opacity scaling (Opa scale) enabled.

If an object is found with an enabled *Opa scale*, then that *Opa scale* will be used by the rendered object too.

Therefore, if you want to disable the Opa scaling for an object when the parent has Opa scale, just enable Opa scaling for the object and set its value to `LV_OPA_COVER`. It will overwrite the parent's settings.

### Protection
There are some specific actions which happen automatically in the library.
To prevent one or more that kind of actions, you can protect the object against them. The following protections exists:
- **LV_PROTECT_NONE** Aucune protection
- **LV_PROTECT_POS**  Empêche le positionnement automatique (p.ex. mise en page dans les [Conteneurs](/object-types/cont))
- **LV_PROTECT_FOLLOW** Empêche que l'objet soit suivi (effectue un "saut de ligne") dans un ordre automatique (p.ex. mise en page dans les [Conteneurs](/object-types/cont))
- **LV_PROTECT_PARENT** Empêche le changement de parent automatique (p.ex. [Page](/object-types/page) déplace les enfants créés sur l’arrière-plan vers la zone de défilement)
- **LV_PROTECT_PRESS_LOST** Evite de perdre un appui lors d'un déplacement hors de l'objet. (P.ex. un [Bouton](/object-types/btn) peut être relâché en dehors s'il est pressé)
- **LV_PROTECT_CLICK_FOCUS** Empêche la sélection automatique de l'objet s'il se trouve dans un *groupe* et que la sélection sur clic est activé.
- **LV_PROTECT_CHILD_CHG** Désactive le signal de changement d'enfant. Utilisé en interne par la librairie

Les fonctions `lv_obj_set/clear_protect(obj, LV_PROTECT_...)` active/désactive la protection. Vous pouvez également combiner les valeurs des types de protection avec *'OU'*.

### Groupes

Once, an object is added to *group* with `lv_group_add_obj(group, obj)` the object's current group can be get with `lv_obj_get_group(obj)`.

`lv_obj_is_focused(obj)` tells if the object is currently focused on its group or not. If the object is not added to a group, `false` will be returned.

Lisez le [Périphériques d'entrée](/overview/indev) pour en savoir plus sur les *groupes*.

### Zone étendue de clic
By default, the objects can be clicked only on their coordinates, however, this area can be extended with `lv_obj_set_ext_click_area(obj, left, right, top, bottom)`.
`left/right/top/bottom` describes how far the clickable area should extend past the default in each direction.

Cette fonctionnalité doit être activée dans *lv_conf.h* avec `LV_USE_EXT_CLICK_AREA`. Les valeurs possibles sont :
- **LV_EXT_CLICK_AREA_FULL** mémorise les 4 coordonnées en `lv_coord_t`
- **LV_EXT_CLICK_AREA_TINY** n'enregistre que les coordonnées horizontales et verticales (utilise la plus grande valeur de gauche/ droite et haut/bas) en `uint8_t`
- **LV_EXT_CLICK_AREA_OFF** Désactive cette fonctionnalité

## Styles

Use `lv_obj_set_style(obj, &style)` to set a style for a base object.

Toutes les propriétés `style.body` sont utilisées. Le style par défaut pour les écrans est `lv_style_scr` et `lv_style_plain_color` pour les objets normaux


## Evénements
Les [Evénements génériques](/overview/event.html#generic-events) sont envoyés par ce type d'objet.

Apprenez-en plus sur les [Evénements](/overview/event).

## Touches
Aucune *touche* n'est traitée par ce type d'objet.

Apprenez-en plus sur les [touches](/overview/indev).


## Exemple

```eval_rst

.. include:: /lv_examples/src/lv_ex_obj/index.rst

```

## API

```eval_rst

.. doxygenfile:: lv_obj.h
  :project: lvgl

```

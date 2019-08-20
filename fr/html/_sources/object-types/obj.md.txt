```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/fr/object-types/obj.md
```
# Objet de base (lv_obj)

## Vue d’ensemble

L'objet de base contient les attributs les plus fondamentaux des objets :

- coordonnées
- objet parent
- enfants
- style principal
- des attributs tels que *Clic autorisé*, *Glissé autorisé*, etc.

### Coordonnées
La taille de l'objet peut être modifiée avec `lv_obj_set_width(obj, new_width)` et `lv_obj_set_height(obj, new_height)` ou en une seule fonction avec `lv_obj_set_size(obj, new_width, new_height)`.

Vous pouvez définir les coordonnées x et y relativement au parent avec `lv_obj_set_x(obj, new_x)` et `lv_obj_set_y(obj, new_y)` ou en une seule fonction avec `lv_obj_set_pos(obj, new_x, new_y)`.

Vous pouvez aligner l'objet sur un autre avec `lv_obj_align(obj, obj_ref, LV_ALIGN _..., x_shift, y_shift)`.
Le deuxième argument est un objet de référence, sur lequel `obj` sera aligné. Si `obj_ref = NULL`, le parent de` obj` sera utilisé.
Le troisième argument est le *type* d'alignement. Voici les options possibles :
![](/misc/align.png "Alignment types in LittlevGL")

Les types d'alignement sont construits comme `LV_ALIGN_OUT_TOP_MID`.

Les deux derniers arguments spécifient un décalage x et y après l'alignement.

Par exemple, pour aligner un texte sous une image: `lv_obj_align(text, image, LV_ALIGN_OUT_BOTTOM_MID, 0, 10)`.
Ou pour aligner un texte au milieu de son parent : `lv_obj_align(text, NULL, LV_ALIGN_CENTER, 0, 0)`.

`lv_obj_align_origo` fonctionne de manière similaire à `lv_obj_align` mais il aligne le point central de l'objet.
Par exemple, `lv_obj_align_origo(btn, image, LV_ALIGN_OUT_BOTTOM_MID, 0, 0)` alignera le centre du bouton sur le bas de l'image.

Les paramètres de l'alignement seront sauvegardés dans l'objet si `LV_USE_OBJ_REALIGN` est activé dans *lv_conf.h*. Vous pouvez réaligner les objets manuellement avec `lv_obj_realign(obj)`.
Cela revient à appeler `lv_obj_align` à nouveau avec les mêmes paramètres.

Si l'alignement a eu lieu avec `lv_obj_align_origo`, il sera utilisé lorsque l'objet sera réaligné.

Si `lv_obj_set_auto_realign(obj, true)` est utilisé, l'objet sera réaligné automatiquement si sa taille change dans les fonctions `lv_obj_set_width/height/size()`.

C'est très utile lorsque des animations de taille sont appliquées à l'objet et que la position d'origine doit être conservée.

Notez que les coordonnées des écrans ne peuvent pas être modifiées. Tenter d'utiliser ces fonctions sur les écrans entraînera un comportement indéfini.

### Parents et enfants
Vous pouvez définir un nouveau parent pour un objet avec `lv_obj_set_parent(obj, new_parent)`. Pour obtenir le parent actuel, utilisez `lv_obj_get_parent(obj)`.

Pour obtenir les enfants d'un objet, utilisez `lv_obj_get_child (obj, child_prev)` (du dernier au premier) ou `lv_obj_get_child_back(obj, child_prev)` (du premier au dernier).
Pour obtenir le premier enfant, passez `NULL` en tant que second paramètre et utilisez la valeur de retour pour parcourir les enfants. La fonction retournera `NULL` s'il n'y a plus d'enfants. Par exemple:

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
Lorsque vous avez créé un écran avec `lv_obj_create(NULL, NULL)`, vous pouvez le charger avec `lv_scr_load(screen1)`. La fonction `lv_scr_act()` vous donne un pointeur sur l'écran actuel.

Si vous avez plusieurs d’affichages, il est important de savoir que ces fonctions opèrent sur l’affichage créé en dernier ou explicitement sélectionné (avec `lv_disp_set_default`).

Pour obtenir l'écran d'un objet, utilisez la fonction `lv_obj_get_screen(obj)`.

### Couches
Il y a deux couches générées automatiquement :
- la couche supérieure
- la couche système

Elles sont indépendantes des écrans et les mêmes couches seront affichées sur chaque écran. La *couche supérieure* est au-dessus de chaque objet à l'écran et la *couche système* est également au-dessus de la *couche supérieure*.
Vous pouvez ajouter librement n'importe quelle fenêtre contextuelle à la *couche supérieure*. Mais la *couche système* est réservée aux éléments de niveau système (par exemple, le curseur de la souris y sera placé par `lv_indev_set_cursor()`).

Les fonctions `lv_layer_top()` et `lv_layer_sys()` retournent un pointeur sur la couche supérieure ou la couche système.

Vous pouvez déplacer un objet au premier plan ou à l'arrière-plan avec `lv_obj_move_foreground(obj)` et `lv_obj_move_background(obj)`.

Lisez la section [Couches](/overview/layer) pour en savoir plus sur les couches.

### Style
L'objet de base mémorise le [style principal](/overview/style) de l'objet. Pour définir un nouveau style, utilisez la fonction `lv_obj_set_style(obj, & new_style)`. Si `NULL` est défini comme style, l'objet héritera du style de son parent. 

Notez que vous ne devriez pas utiliser `lv_obj_set_style`  pour "les objets évolués". Chaque type d'objet a sa propre fonction de jeu de styles qui doit être utilisée pour eux. P.ex. pour le bouton `lv_btn_set_style()`

Si vous modifiez un style déjà utilisé par des objets afin d'actualiser les objets affectés, vous pouvez utiliser `lv_obj_refresh_style(obj)` ou notifier tous les objets avec un style donné `lv_obj_report_style_mod(&style)`. Si le paramètre de `lv_obj_report_style_mod` est `NULL`, tous les objets seront notifiés.

Lisez la section [Styles](/overview/style) pour en savoir plus sur les styles.

### Evènements

Pour définir une fonction de rappel d'événement pour un objet, utilisez `lv_obj_set_event_cb(obj, event_cb)`

Pour envoyer manuellement un événement à un objet, utilisez `lv_event_send(obj, LV_EVENT_..., data)`

Lisez [Evénements](/overview/event) pour en savoir plus sur les événements.

### Attributs
Certains attributs peuvent être activés/désactivés avec `lv_obj_set_...(obj, true/false)` :

- **hidden** Cache l'objet. Il ne sera pas dessiné et sera considéré comme s'il n'existait pas. Ses enfants seront également cachés.
- **click** Activé pour cliquer sur l'objet via les périphériques d'entrée. Si désactivé, l'objet derrière cet objet sera cliqué. (P.ex. les [Etiquettes](/object-types/label) ne sont pas cliquables par défaut)
- **top** Si activé, alors quand on clique sur cet objet ou sur l'un de ses enfants, cet objet passe au premier plan.
- **glisser** Active le glissé (déplacement par un périphérique d'entrée)
- **drag_dir** Active le glissé uniquement dans certaines directions. Peut être `LV_DRAG_DIR_HOR/VER/ALL`.
- **drag_throw** Active le "lâcher" avec le glissé comme si l'objet avait une impulsion
- ** drag_parent ** Si activé, le parent de l'objet sera déplacé pendant le glissé. Similaire à un glissé du parent. Agit récursivement, peut donc se propager également aux grands-parents.
- **parent_event** Propage également les évènements aux parents.Agit récursivement, peut donc se propager également aux grands-parents.
- **opa_scale_enable** Activer la mise à l'échelle de l'opacité. Voir la section [Echelle d'opacité](#echelle-d-opacite).

### Echelle d'opacité
Si `lv_obj_set_opa_scale_enable(obj, true)` est défini pour un objet, l'opacité de l'objet et de tous ses enfants peut être ajustée avec `lv_obj_set_opa_scale(obj, LV_OPA_...)`.
Les opacités enregistrées dans les styles seront modifiées par ce facteur.

C'est très utile pour estomper/révéler un objet avec des enfants en utilisant une [Animation](/overview/animation).

Un peu de technique : pendant le processus de rendu, l'objet et ses parents sont examinés de manière récursive pour trouver un parent avec *opa_scale_enable* actif.
Si un objet est trouvé avec *opa_scale_enable* actif, alors ce sera également utilisée par l'objet rendu. 
Par conséquent, si vous souhaitez désactiver ce mécanisme, activez simplement la mise à l'échelle d'opacité pour l'objet et définissez sa valeur sur `LV_OPA_COVER`. Les paramètres du parent seront écrasés.

### Protection
Certaines actions spécifiques se produisent automatiquement dans la librairie.
Pour empêcher un ou plusieurs types d'actions, vous pouvez protéger l'objet. Les protections suivantes existent:
- **LV_PROTECT_NONE** Aucune protection
- **LV_PROTECT_POS**  Empêche le positionnement automatique (p.ex. mise en page dans les [Conteneurs](/object-types/cont))
- **LV_PROTECT_FOLLOW** Empêche que l'objet soit suivi (effectue un "saut de ligne") dans un ordre automatique (p.ex. mise en page dans les [Conteneurs](/object-types/cont))
- **LV_PROTECT_PARENT** Empêche le changement de parent automatique (p.ex. [Page](/object-types/page) déplace les enfants créés sur l’arrière-plan vers la zone de défilement)
- **LV_PROTECT_PRESS_LOST** Evite de perdre un appui lors d'un déplacement hors de l'objet. (P.ex. un [Bouton](/object-types/btn) peut être relâché en dehors s'il est pressé)
- **LV_PROTECT_CLICK_FOCUS** Empêche la sélection automatique de l'objet s'il se trouve dans un *groupe* et que la sélection sur clic est activé.
- **LV_PROTECT_CHILD_CHG** Désactive le signal de changement d'enfant. Utilisé en interne par la librairie

Les fonctions `lv_obj_set/clear_protect(obj, LV_PROTECT_...)` active/désactive la protection. Vous pouvez également combiner les valeurs des types de protection avec *'OU'*.

### Groupes

Une fois qu'un objet est ajouté à *group* avec `lv_group_add_obj(group, obj)`, le groupe courant de l'objet peut être obtenu avec `lv_obj_get_group(obj)`.

`lv_obj_is_focused(obj)` indique si l'objet est actuellement sélectionné dans son groupe. Si l'objet n'est pas membre d'un groupe, `false` sera renvoyé.

Lisez le [Périphériques d'entrée](/overview/indev) pour en savoir plus sur les *groupes*.

### Zone étendue de clic
Par défaut, les objets ne peuvent être cliqués que sur leur surface, cependant cette zone peut être étendue avec `lv_obj_set_ext_click_area(obj, left, right, top, bottom)`.
`left/right/top/bottom` indique les extensions de la zone dans chaque direction.

Cette fonctionnalité doit être activée dans *lv_conf.h* avec `LV_USE_EXT_CLICK_AREA`. Les valeurs possibles sont :
- **LV_EXT_CLICK_AREA_FULL** mémorise les 4 coordonnées en `lv_coord_t`
- **LV_EXT_CLICK_AREA_TINY** n'enregistre que les coordonnées horizontales et verticales (utilise la plus grande valeur de gauche/ droite et haut/bas) en `uint8_t`
- **LV_EXT_CLICK_AREA_OFF** Désactive cette fonctionnalité

## Styles

Utilisez `lv_obj_set_style(obj, &style)` pour définir un style pour un objet de base.

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

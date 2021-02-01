```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/fr/object-types/tileview.md
```
# Mosaïque  (lv_tileview)

## Vue d'ensemble

La mosaïque est un objet conteneur dans lequel ses éléments, appelés *tuiles*, peuvent être organisés sous forme de grille. En balayant l'utilisateur peut naviguer entre les tuiles.

Si la mosaïque est de la taille de l'écran, elle fournit une interface utilisateur que vous avez peut-être vue sur les montres intelligentes.

### Positions valides

Les tuiles ne doivent pas nécessairement former une grille complète où chaque élément existe. La grille peut comporter des trous, mais elle doit être continue, c'est-à-dire qu'il ne peut y avoir une ligne ou une colonne vide.

Avec `lv_tileview_set_valid_positions(tileview, valid_pos_array, array_len)`, les positions valides peuvent être définies. Le défilement ne sera possible que vers ces positions. L'indice `0,0` représente la tuile en haut à gauche.
Par exemple `lv_point_t valid_pos_array [] = { { 0, 0 }, { 0, 1 }, { 1, 1 }, { LV_COORD_MIN, LV_COORD_MIN } }` donne une mosaïque en forme  de "L". Cela indique qu'il n'y a pas de tuile dans `{ 1,0 }` et que l'utilisateur ne peut donc pas s'y déplacer.


En d'autres termes, `valid_pos_array` indique où se trouvent les tuiles. Il peut être modifié à la volée pour désactiver certaines positions pour des tuiles spécifiques.
Par exemple, il peut exister une grille 2 x 2 où toutes les tuiles sont présentes, où la première ligne (y = 0) est la "ligne principale" et la deuxième ligne (y = 1) contient des options pour la tuile située au-dessus.
Supposons que le défilement horizontal est possible uniquement dans la ligne principale et impossible entre les options de la deuxième ligne . Dans ce cas, `valid_pos_array` doit être modifié lorsqu'une nouvelle tuile principale est sélectionnée :
- pour la première tuile principale : `{ 0, 0 }, { 0, 1 }, { 1, 0 }` pour désactiver la tuile d'option `{ 1, 1 }`
- pour la deuxième tuile principale : `{ 0, 0 }, { 0, 1 }, { 1, 1 }` pour désactiver la tuile d'option `{ 0, 1 }`

### Ajouter un élément

Pour ajouter des éléments, il suffit de créer un objet sur la mosaïque et d’appeler `lv_tileview_add_element(tileview, element)`.

L'élément doit avoir la même taille que la mosaïque et doit être positionné manuellement à la position souhaitée.

La fonctionnalité de propagation de défilement des objets de type page (comme [liste](/object-types/list)) peut très bien être utilisée ici.
Par exemple, l'utilisateur peut faire défiler les éléments d'une liste et quand le premier ou le dernier élément de la liste est atteint, c'est la mosaïque qui défile à la place.

`lv_tileview_add_element(tileview, element)` devrait être utilisé pour permettre de faire défiler (glisser) la mosaïque par un de ces éléments.
Par exemple, s'il y a un bouton sur une tuile, le bouton doit être explicitement ajouté à la mosaïque pour permettre à l'utilisateur de faire défiler la mosaïque avec le bouton.

Cela vaut aussi pour les boutons d'une [liste](/object-types/list). Chaque bouton de la liste et la liste elle-même doivent être ajoutés avec `lv_tileview_add_element`.

### Définir la tuile

Pour définir la tuile visible, utilisez `lv_tileview_set_tile_act tileview, x_id, y_id, LV_ANIM_ON/OFF)`.

### Durée d'animation

La durée d'animation quand une tuile
-  est sélectionnée par `lv_tileview_set_tile_act`
- est légèrement déplacé, puis relâché (revient à la tuile d'origine)
- est déplacé sur plus de la moitié de sa taille, puis relâché (affiche la tuile suivante)

peut être fixée avec `lv_tileview_set_anim_time(tileview, anim_time)`. 

### Mise en évidence du bord

Un effet de "mise en évidence du bord" peut être ajouté lorsque la mosaïque atteint une position non valide ou une des extrémités lors du défilement.

Utilisez `lv_tileview_set_edge_flash(tileview, true)` pour activer cette fonctionnalité.



## Styles
La mosaïque a un seul style qui peut être changé avec `lv_tileview_set_style(slider, LV_TILEVIEW_STYLE_MAIN, &style)`.

- **LV_TILEVIEW_STYLE_MAIN** style de l'arrière plan. Toutes les propriétés `style.body` sont utilisées.

## Evénements
Outre les [événements génériques](/overview/event.html #evenements-generiques), les [événements spéciaux](/overview/event.html#evenements-speciaux) suivants sont envoyés par la mosaïque :
- **LV_EVENT_VALUE_CHANGED** envoyé quand une nouvelle tuile est affichée par défilement ou appel de la fonction `lv_tileview_set_act`. Les données d'événement sont définies sur l'index de la nouvelle tuile dans `valid_pos_array` (le type est `uint32_t *`).

## Touches
- **LV_KEY_UP**, **LV_KEY_RIGHT** incrémente l'index de la tuile de 1.
- **LV_KEY_DOWN**, **LV_KEY_LEFT** décrémente l'index de la tuile de 1.

Apprenez-en plus sur les [touches](/overview/indev).

## Exemple


```eval_rst

.. include:: /lv_examples/src/lv_ex_tileview/index.rst

```


## API 

```eval_rst

.. doxygenfile:: lv_tileview.h
  :project: lvgl
        
```

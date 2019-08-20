```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/fr/object-types/ddlist.md
```
# Liste déroulante (lv_ddlist)

## Vue d’ensemble

Les listes déroulantes vous permettent de sélectionner simplement un élément parmi plusieurs. La liste déroulante est fermée par défaut et permet d'afficher le texte actuellement sélectionné. Si vous cliquez dessus, la liste s'ouvre et tous les éléments sont affichés.

### Définir les éléments
Les éléments sont transmis à la liste déroulante sous forme de chaîne avec `lv_ddlist_set_options(ddlist, options)`. Les éléments doivent être séparés par `\n`. Par exemple : `"Premier\nDeuxième\nTroisième"`.

Vous pouvez sélectionner un élément manuellement avec `lv_ddlist_set_selected(ddlist, id)`, où _id_ est l'index d'un élément.

### Obtenir l'élément sélectionné
Pour obtenir l'élément actuellement sélectionné, utilisez `lv_ddlist_get_selected(ddlist)`. La fonction retourne l'*index* de l'élément sélectionné.

`lv_ddlist_get_selected_str(ddlist, buf, buf_size)` copie le texte de l'élément sélectionnée dans `buf`.

### Aligner les éléments 
Pour aligner le texte horizontalement, utilisez `lv_ddlist_set_align(ddlist, LV_LABEL_ALIGN_LEFT/CENTER/RIGHT)`.

### Hauteur et largeur
Par défaut, la hauteur de la liste est ajustée automatiquement pour afficher tous les éléments. `lv_ddlist_set_fix_height(ddlist, height)` définit une hauteur fixe pour la liste ouverte. `0` utilise la hauteur automatique.

La largeur est également ajustée automatiquement. Pour éviter cela, utilisez `lv_ddlist_set_fix_width(ddlist, width)`. `0` utilise la largeur automatique.

### Barres de défilement
Comme pour une [page](/object-types/page) de hauteur fixe, la liste déroulante prend en charge divers modes d’affichage avec barres de défilement. Le mode est défini par `lv_ddlist_set_sb_mode(ddlist, LV_SB_MODE_...)`.

### Durée d'animation
La durée d'animation d'ouverture/fermeture de la liste déroulante est spécifié par `lv_ddlist_set_anim_time(ddlist, anim_time)`. Une durée d'animation à zéro supprime l'animation.

### Flèche décorative
Une flèche vers le bas peut être ajoutée à gauche de la liste déroulante avec `lv_ddlist_set_draw_arrow(ddlist, true)`.

### Rester ouvert
Vous pouvez forcer la liste déroulante à rester **ouverte** lorsqu'un élément est sélectionné avec `lv_ddlist_set_stay_open(ddlist, true)`.

## Styles

`lv_ddlist_set_style(ddlist, LV_DDLIST_STYLE_..., &style)` définit les styles d'une liste déroulante.

- **LV_DDLIST_STYLE_BG** style de l'arrière plan. Toutes les propriétés `style.body` sont utilisées. `style.text` est utilisé pour le libellé de l'élément. Par défaut : `lv_style_pretty`,
- **LV_DDLIST_STYLE_SEL** Style de l'élément sélectionné. Les propriétés `style.body` sont utilisées. L'élément sélectionné sera colorée avec `text.color`. Par défaut : `lv_style_plain_color`,
- **LV_DDLIST_STYLE_SB** style de la barre de défilement. Les propriétés `style.body` sont utilisées. Par défaut : `lv_style_plain_color`.

## Evénements
Outre les [événements génériques](/overview/event.html #evenements-generiques), les [événements spéciaux](/overview/event.html#evenements-speciaux) suivants  sont envoyés par les listes déroulantes :
 - **LV_EVENT_VALUE_CHANGED** envoyé lorsque un nouvel élément est sélectionné.

Apprenez-en plus sur les [événements](/overview/event).

## Touches
Les *touches* suivantes sont traitées par les listes déroulantes :
- **LV_KEY_RIGHT/DOWN** sélectionne l'élément suivant,
- **LV_KEY_LEFT/UP** sélectionne l'élément précédent,
- **LY_KEY_ENTER** valide l'élément sélectionné (envoie l'événement `LV_EVENT_VALUE_CHANGED` et ferme la liste déroulante).

## Exemple

```eval_rst

.. include:: /lv_examples/src/lv_ex_ddlist/index.rst

```

## API 

```eval_rst

.. doxygenfile:: lv_ddlist.h
  :project: lvgl
        
```

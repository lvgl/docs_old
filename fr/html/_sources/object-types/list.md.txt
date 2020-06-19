```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/fr/object-types/list.md
```
# Liste (lv_list)

## Vue d'ensemble

Les listes sont construites à partir d'une [page](/object-types/page) d'arrière-plan sur laquelle sont placés des [boutons](/object-types/btn) on it. 
Les boutons contiennent une [image](/object-types/img) comme icône optionnelle (qui peut être un symbole aussi) et une [étiquette](/object-types/label). 
Lorsque la liste est suffisamment longue, vous pouvez la faire défiler.

### Ajouter des boutons
Vous pouvez ajouter de nouveaux éléments de liste avec `lv_list_add_btn(list, &icon_img, "Text")` ou avec symbole `lv_list_add_btn(list, SYMBOL_EDIT, "Edit text")`. 
Si vous ne souhaitez pas ajouter d'image, utilisez `NULL` comme source d'image. La fonction retourne un pointeur sur le bouton créé pour permettre d'autres configurations.

La largeur des boutons est fixée au maximum de la largeur de l'objet.
La hauteur des boutons est ajustée automatiquement en fonction du contenu (*content height* + *padding.top* + *padding.bottom*).

Les étiquettes sont créées avec le mode `LV_LABEL_LONG_SROLL_CIRC` pour faire défiler automatiquement les libellés longs de manière circulaire.

Vous pouvez utiliser `lv_list_get_btn_label(list_btn)` and `lv_list_get_btn_img(list_btn)` pour obtenir le libellé et l'image d'un bouton de liste. Vous pouvez obtenir le texte directement avec `lv_list_get_btn_text(list_btn)`.

### Supprimer des boutons
Pour supprimer un élément de la liste, utilisez simplement `lv_obj_del(btn)` sur la valeur de retour de `lv_list_add_btn()`. 

Pour vider la liste (supprimer tous les boutons), utilisez `lv_list_clean(list)`

### Navigation manuelle
Vous pouvez naviguer manuellement dans la liste avec `lv_list_up(list)` et `lv_list_down(list)`.

Vous pouvez accéder directement  à un bouton en utilisant `lv_list_focus(btn, LV_ANIM_ON/OFF)`.

La **durée d'animation** des déplacements haut/bas/accès direct peut être définie via : `lv_list_set_anim_time(list, anim_time)`. Zéro supprime les animations.

### Mise en page
Par défaut la liste est verticale. Pour obtenir une liste horizontale, utilisez `lv_list_set_layout(list, LV_LAYOUT_ROW_M)`.
 
### Mise en évidence du bord
L'animation d'un cercle peut être affichée quand la liste atteint les positions supérieure ou inférieure.
`lv_list_set_edge_flash(list, en)` active cette fonctionnalité.

### Propagation du défilement
Si la liste est créée sur un autre objet défilant (comme une [page](/object-types/page)) et que la liste ne peut pas être défilées plus, le **défilement peut être propagé au parent**.
De cette manière, le défilement sera poursuivi sur le parent. Cela peut être activé avec `lv_list_set_scroll_propagation(list, true)`.

SI les bouton ont `lv_btn_set_toggle` activé alors `lv_list_set_single_mode(list, true)` est utilisé pour s’assurer qu’un seul bouton ne peut être dans l’état basculé à un instant donné.

## Styles

La fonction `lv_list_set_style(list, LV_LIST_STYLE _..., &style)` définit les styles d'une liste.
- **LV_LIST_STYLE_BG** style d'arrière-plan de liste. Valeur par défaut : `lv_style_transp_fit`
- **LV_LIST_STYLE_SCRL** style de la partie défilante. Valeur par défaut : `lv_style_pretty`
- **LV_LIST_STYLE_SB** style de la barre de défilement. Valeur par défaut : `lv_style_pretty_color`. Pour plus de détails voir l'objet [page](/object-types/page) 
- **LV_LIST_STYLE_BTN_REL** style des boutons relâchés. Valeur par défaut : `lv_style_btn_rel`
- **LV_LIST_STYLE_BTN_PR** style des boutons pressés. Valeur par défaut : `lv_style_btn_pr`
- **LV_LIST_STYLE_BTN_TGL_REL** style des boutons bascules relâchés. Valeur par défaut : `lv_style_btn_tgl_rel`,
- **LV_LIST_STYLE_BTN_TGL_PR** style des boutons bascules pressés. Valeur par défaut : `lv_style_btn_tgl_pr`
- **LV_LIST_STYLE_BTN_INA** style des boutons inactifs. Valeur par défaut : `lv_style_btn_ina`.

Étant donné que *BG* a un style transparent par défaut s'il n'y a que quelques boutons, la liste paraîtra plus courte mais pourra défiler lorsque plusieurs éléments de la liste sont ajoutés.

Pour modifier la hauteur des boutons, ajustez les champs `body.padding.top/bottom` des styles relatifs (`LV_LIST_STYLE_BTN_REL/PR/...`).


## Evénements
Seuls les [événements génériques](/overview/event.html#generic-events) sont envoyés par ce type d'objet.

Apprenez-en plus sur les [événements](/overview/event).

## Touches
Les *touches* suivantes sont traitées par les listes :
- **LV_KEY_RIGHT/DOWN** sélectionne le bouton suivant,
- **LV_KEY_LEFT/UP** sélectionne le bouton précédent,

Notez que, comme d'habitude, l'état de `LV_KEY_ENTER` est traduit en `LV_EVENT_PRESSED/PRESSING/RELEASED` etc.

Les boutons sélectionnés sont dans l'état `LV_BTN_STATE_PR/TG_PR`.

Pour sélectionner manuellement un bouton, utilisez `lv_list_set_btn_selected(list, btn)`. Lorsque la liste est défocalisée et focalisée à nouveau, le dernier bouton sélectionné est restauré.

Apprenez-en plus sur les [touches](/overview/indev).


## Exemple

```eval_rst

.. include:: /lv_examples/src/lv_ex_list/index.rst

```

## API 

```eval_rst

.. doxygenfile:: lv_list.h
  :project: lvgl
        
```

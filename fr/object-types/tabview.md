```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/fr/object-types/tabview.md
```
# Classeur d'onglets (lv_tabview)

## Vue d'ensemble

L’objet classeur d'onglets peut être utilisé pour organiser du contenu dans des onglets.

### Ajouter un onglet
Vous pouvez ajouter de nouveaux onglets avec `lv_tabview_add_tab(tabview, "Tab name")`. La fonction retourneun pointeur sur un objet [page](/object-types/page) dans lequel vous pouvez ajouter le contenu de l'onglet.

### Changer d'onglet
Pour sélectionner un nouvel onglet, vous pouvez :
- Cliquer dessus dans la partie en-tête
- Glisser horizontalement
- Utiliser la fonction  `lv_tabview_set_tab_act(tabview, id, LV_ANIM_ON/OFF)`

Le glissement manuel peut être désactivé avec `lv_tabview_set_sliding(tabview, false)`.

### Position des boutons d'onglet

Par défaut, les boutons de sélection des onglets sont placés en haut du classeur d'onglets. Cela peut être changé avec `lv_tabview_set_btns_pos(tabview, LV_TABVIEW_BTNS_POS_TOP/BOTTOM/LEFT/RIGHT)`

Notez que vous ne pouvez pas modifier la position de haut ou bas vers gauche ou droite lorsque des onglets sont déjà ajoutés.


### Cacher des onglets

Les boutons peuvent être cachés par `lv_tabview_set_btns_hidden(tabview, true)`

### Durée d'animation

La durée d'animation est ajustée par `lv_tabview_set_anim_time(tabview, anim_time_ms)`. Cela est utilisé lorsque le nouvel onglet est affiché.

## Styles

Utilisez `lv_tabview_set_style(tabview, LV_TABVIEW_STYLE_...,  &style)` pour définir un nouveau style pour un élément du classeur d'onglets :

- **LV_TABVIEW_STYLE_BG** arrière-plan principal qui utilise toutes les propriétés `style.body` (valeur par défaut : `lv_style_plain`).
- **LV_TABVIEW_STYLE_INDIC** un fin rectangle pour indiquer l'onglet courant. Utilise toutes les propriétés `style.body`. Sa hauteur provient de `body.padding.inner` (valeur par défaut:` lv_style_plain_color`).
- **LV_TABVIEW_STYLE_BTN_BG** style de l'arrière-plan des boutons d'onglets. Utilise toutes les propriétés `style.body`. La hauteur de l'en-tête sera définie automatiquement en fonction de `body.padding.top/bottom` (valeur par défaut : `lv_style_transp`).
- **LV_TABVIEW_STYLE_BTN_REL** style des boutons d'onglets relâchés. Utilise toutes les propriétés `style.body`  (valeur par défaut : `lv_style_tbn_rel`).
- **LV_TABVIEW_STYLE_BTN_PR** style des boutons d'onglets pressés. Utilise toutes les propriétés `style.body`  (valeur par défaut : `lv_style_tbn_pr`).
- **LV_TABVIEW_STYLE_BTN_TGL_REL** style des boutons d'onglets sélectionnés relâchés. Utilise toutes les propriétés `style.body`  (valeur par défaut : `lv_style_tbn_tgl_rel`).
- **LV_TABVIEW_STYLE_BTN_TGL_PR** style des boutons d'onglets sélectionnés pressés. Utilise toutes les propriétés `style.body`  (valeur par défaut : `lv_style_tbn_tgl_pr`).

La hauteur de l'en-tête est calculée ainsi :
*font height + padding.top + padding.bottom à partir de LV_TABVIEW_STYLE_BTN_REL + padding.top + padding bottom à partir de LV_TABVIEW_STYLE_BTN_BG*

## Evénements
Outre les [événements génériques](/overview/event.html #evenements-generiques), les [événements spéciaux](/overview/event.html#evenements-speciaux) suivants sont envoyés par le classeur d'onglets :
 - **LV_EVENT_VALUE_CHANGED** envoyé lorsque un nouvel onglet est sélectionné par glissé ou clic sur le bouton d'onglet.

Apprenez-en plus sur les [événements](/overview/event).

## Touches

Les *touches* suivantes sont traitées par le classeur d'onglets :
- **LV_KEY_RIGHT/LEFT** sélectionne un onglet.
- **LV_KEY_ENTER** passe à l'onglet sélectionné

Apprenez-en plus sur les [touches](/overview/indev).


## Exemple

```eval_rst

.. include:: /lv_examples/src/lv_ex_tabview/index.rst

```

## API 

```eval_rst

.. doxygenfile:: lv_tabview.h
  :project: lvgl
        
```

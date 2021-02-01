```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/fr/object-types/mbox.md
```
# Boîte de message (lv_mbox)

## Vue d'ensemble

Les boîtes de message font office de fenêtres contextuelles. Elles sont construites à partir d'un [conteneur](/object-types/cont) de fond, d'un [label](/object-types/label) et d'une [matrice de boutons](/object-types/btnm). 


Le texte sera automatiquement divisé en plusieurs lignes (mode `LV_LABEL_LONG_MODE_BREAK`) et la hauteur sera définie automatiquement pour afficher le texte et les boutons (`LV_FIT_TIGHT` ajustement automatique vertical)-

### Définir le texte
Pour définir le texte, utilisez la fonction `lv_mbox_set_text(mbox,"My text")`.

### Ajouter des boutons
Pour ajouter des boutons, utilisez la fonction `lv_mbox_add_btns(mbox, btn_str)`. Vous devez spécifier le texte des boutons ainsi `const char * btn_str[] = {"Apply", "Close", ""}`. 
Pour plus d'informations, consultez la documentation de la [matrice de boutons](/object-types/btnm).

### Fermeture automatique
Avec `lv_mbox_start_auto_close(mbox, delay)` la boîte de message peut être fermée automatiquement après `delay` millisecondes avec une animation. La fonction `lv_mbox_stop_auto_close(mbox)` arrête une fermeture automatique en cours.

La durée de l'animation de fermeture peut être définie par `lv_mbox_set_anim_time(mbox, anim_time)`.

## Styles

Utilisez `lv_mbox_set_style(mbox, LV_MBOX_STYLE _..., &style)` pour définir un nouveau style pour un élément de la boîte de message :

- **LV_MBOX_STYLE_BG** spécifie le style du conteneur d'arrière-plan. `style.body` définit l'arrière-plan et `style.label` définit l'apparence du texte. Valeur par défaut : `lv_style_pretty`
- **LV_MBOX_STYLE_BTN_BG** style de l’arrière-plan de la matrice de boutons. Valeur par défaut : `lv_style_trans`
- **LV_MBOX_STYLE_BTN_REL** style des boutons relâchés. Valeur par défaut : `lv_style_btn_rel`
- **LV_MBOX_STYLE_BTN_PR** style des boutons pressés. Valeur par défaut : `lv_style_btn_pr`
- **LV_MBOX_STYLE_BTN_TGL_REL** style des boutons bascules relâchés. Valeur par défaut : `lv_style_btn_tgl_rel`,
- **LV_MBOX_STYLE_BTN_TGL_PR** style des boutons bascules pressés. Valeur par défaut : `lv_style_btn_tgl_pr`
- **LV_MBOX_STYLE_BTN_INA** style des boutons inactifs. Valeur par défaut : `lv_style_btn_ina`.

La hauteur de la zone des boutons est égal à *font height + padding.top + padding.bottom* de `LV_MBOX_STYLE_BTN_REL`.

## Evénements
Outre les [événements génériques](/overview/event.html #evenements-generiques), les [événements spéciaux](/overview/event.html#evenements-speciaux) suivants  sont envoyés par les boîtes de message :
 - **LV_EVENT_VALUE_CHANGED** envoyé lorsque le bouton est cliqué. Les données d'événement sont l'ID du bouton cliqué.

La boîte de message a une fonction de rappel par défaut qui la referme lorsqu'un clic est effectué sur un bouton.

Apprenez-en plus sur les [événements](/overview/event).

## Touches

Les *touches* suivantes sont traitées par les boutons :
- **LV_KEY_RIGHT/DOWN** sélectionne le bouton suivant,
- **LV_KEY_LEFT/UP** sélectionne le bouton précédent,
- **LV_KEY_ENTER** pour clique le bouton sélectionné.

Apprenez-en plus sur les [touches](/overview/indev).


## Exemple

```eval_rst

.. include:: /lv_examples/src/lv_ex_mbox/index.rst

```

## API 

```eval_rst

.. doxygenfile:: lv_mbox.h
  :project: lvgl
        
```

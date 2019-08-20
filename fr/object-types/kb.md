```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/fr/object-types/kb.md
```
# Clavier (lv_kb)

## Vue d’ensemble

L'objet clavier est une [matrice de boutons](/object-types/btnm) spéciale avec des dispositions de touches prédéfinies et autres fonctionnalités qui implémente un clavier virtuel pour écrire du texte.

### Modes
Les claviers ont deux modes :
- **LV_KB_MODE_TEXT** affiche lettres, chiffres et des caractères spéciaux,
- **LV_KB_MODE_NUM** affiche chiffres, signe +/- et point décimal.

Pour définir le mode, utilisez `lv_kb_set_mode(kb, mode)`. Le défaut est _LV_KB_MODE_TEXT_.

### Zone de texte
Vous pouvez attribuer une [zone de texte](/object-types/ta) au clavier pour insérer automatiquement les caractères sur lesquels vous avez cliqué.
Pour définir la zone de texte, utilisez.`lv_kb_set_ta(kb, ta)`.

Le **curseur de la zone de texte peut être géré** par le clavier : lorsque le clavier est lié, le curseur de la zone de texte est masqué et un nouveau est affiché.
Lorsque le clavier est fermé avec les touches *Ok* ou *Fermer*, le curseur est également masqué. La fonctionnalité de gestion du curseur est activée par `lv_kb_set_cursor_manage(kb, true)`. La valeur par défaut est non géré.


### Nouvelle disposition de touches
Vous pouvez spécifier une nouvelle disposition pour le clavier avec `lv_kb_set_map(kb, map)` et `lv_kb_set_ctrl_map(kb, ctrl_map)`. 
Apprenez en plus sur le sujet avec l'objet [matrice de boutons](/object-types/btnm)
N'oubliez pas que l'utilisation des mots clés suivants aura le même effet qu'avec la disposition de touches d'origine:
- *LV_SYMBOL_OK* appliquer,
- *SYMBOL_CLOSE* fermer,
- *LV_SYMBOL_LEFT* déplacer le curseur à gauche,
- *LV_SYMBOL_RIGHT* déplacer le curseur à droite,
- *"ABC"* charger la disposition des touches majuscules,
- *"abc"* charger la disposition des touches minuscules,
- *"Enter"*nouvelle ligne,
- *"Bkps"* suppression à gauche.

## Styles

Les claviers fonctionnent avec 6 styles : un arrière-plan et 5 styles de boutons pour chaque état.
Vous pouvez définir les styles avec `lv_kb_set_style(cont, LV_KB_STYLE_MAIN, &style)`. 
L'arrière-plan et les boutons utilisent les propriétés `style.body`.
Les étiquettes utilisent les propriétés `style.text` des styles de boutons.

- **LV_KB_STYLE_BG** style d'arrière-plan. Utilise toutes les propriétés `style.body`, y compris `padding`. Par défaut : `lv_style_pretty`
- **LV_KB_STYLE_BTN_REL** style des boutons relâchés. Défaut : `lv_style_btn_rel`
- **LV_KB_STYLE_BTN_PR** style des boutons pressés. Défaut : `lv_style_btn_pr`
- **LV_KB_STYLE_BTN_TGL_REL** style des boutons bascules relâchés. Défaut : `lv_style_btn_tgl_rel`,
- **LV_KB_STYLE_BTN_TGL_PR** style des boutons bascules pressés. Défaut : `lv_style_btn_tgl_pr`
- **LV_KB_STYLE_BTN_INA** style des boutons inactifs. Défaut : `lv_style_btn_ina`.

## Evénements
Outre les [événements génériques](/overview/event.html #evenements-generiques), les [événements spéciaux](/overview/event.html#evenements-speciaux) suivants  sont envoyés par les claviers :
 - **LV_EVENT_VALUE_CHANGED** envoyé lorsque le bouton est enfoncé/relâché ou répété après un appui prolongé. Les données d'événement sont l'ID du bouton enfoncé/relâché.
 - **LV_EVENT_APPLY** le bouton *Ok* est cliqué
 - **LV_EVENT_CANCEL** le bouton *Close* est cliqué
 
Le clavier a une **fonction de rappel par défaut** du gestionnaire d'événements appelée `lv_kb_def_event_cb`.
Cette fonction gère l’appui sur les boutons, le changement de disposition, la zone de texte liée, etc.
Vous pouvez écrire votre gestionnaire d'événements personnalisé et vous pouvez utiliser `lv_kb_def_event_cb` au début de votre gestionnaire pour conserver un comportement par défaut pour certains événements.
 
Apprenez-en plus sur les [événements](/overview/event).

## Touches

Les *touches* suivantes sont traitées par les boutons :
- **LV_KEY_RIGHT/UP/LEFT/RIGHT** pour naviguer parmi les boutons et en sélectionner un,
- **LV_KEY_ENTER** pour presser/relâcher le bouton sélectionné.

Apprenez-en plus sur les [touches](/overview/indev).


## Exemples 


```eval_rst

.. include:: /lv_examples/src/lv_ex_kb/index.rst

```

## API 

```eval_rst

.. doxygenfile:: lv_kb.h
  :project: lvgl
        
```

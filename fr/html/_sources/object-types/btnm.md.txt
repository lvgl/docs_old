```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/fr/object-types/btnm.md
```
# Matrice de boutons (lv_btnm)

## Vue d’ensemble

Les objets matrice de boutons peuvent afficher **plusieurs boutons** en lignes et en colonnes.

### Texte du bouton
Il y a un texte sur chaque bouton. Pour les spécifier, un tableau de chaînes, appelé *mappe*, doit être utilisé.
La mappe peut être définie avec `lv_btnm_set_map(btnm, my_map)`.
La déclaration d'une mappe doit ressembler à `const char * map[] = { "btn1", "btn2", "btn3", "" }`.
Notez que **le dernier élément doit être une chaîne vide** !

Utilisez `"\n"` dans la mappe pour faire **un saut de ligne**. P.ex. `{ "btn1", "btn2", "\n", "btn3", ""}. La largeur du bouton est recalculée dans chaque ligne afin de remplir toute la ligne.

### Contrôle des boutons
La largeur des **boutons** peut être définie par rapport aux autres boutons de la même ligne avec `lv_btnm_set_btn_width(btnm, btn_id, width)`
P.ex. dans une ligne avec deux boutons : *btnA, width = 1* et *btnB, width = 2*, *btnA* occupera 33% et  *btnB * occupera 66% de la largeur de la ligne.

En plus de la largeur, chaque bouton peut être personnalisé avec les paramètres suivants :
- **LV_BTNM_CTRL_HIDDEN** cache le bouton
- **LV_BTNM_CTRL_NO_REPEAT** désactive la répétition lors d'un appui long
- **LV_BTNM_CTRL_INACTIVE** désactive le bouton
- **LV_BTNM_CTRL_TGL_ENABLE** active le mode bascule d'un bouton
- **LV_BTNM_CTRL_TGL_STATE** définit l'état basculé
- **LV_BTNM_CTRL_CLICK_TRIG** si 0 le bouton réagira à l'appui, si 1 réagira au relâché

Pour définir ou effacer un attribut de contrôle d'un bouton utilisez `lv_btnm_set_btn_ctrl(btnm, btn_id, LV_BTNM_CTRL_...)` et `lv_btnm_clear_btn_ctrl(btnm, btn_id, LV_BTNM_CTRL_...)` respectivement. Plusieurs  `LV_BTNM_CTRL_...` peuvent combinées avec *OU*

Pour définir ou effacer un attribut de contrôle pour tous les boutons d'une matrice de boutons utilisez `lv_btnm_set_btn_ctrl_all(btnm, btn_id, LV_BTNM_CTRL_...)` et `lv_btnm_clear_btn_ctrl_all(btnm, btn_id, LV_BTNM_CTRL_...)`.

Pour définir une mappe de contrôle pour une matrice de boutons (comme pour le texte), utilisez `lv_btnm_set_ctrl_map(btnm, ctrl_map)`.
Un élément de `ctrl_map` devrait ressembler à `ctrl_map[0] = width | LV_BTNM_CTRL_NO_REPEAT | LV_BTNM_CTRL_TGL_ENABLE`. Le nombre d'éléments doit être égal au nombre de boutons (en excluant les caractères de saut de ligne).

### Une bascule
La fonctionnalité "Une bascule" peut être activée avec `lv_btnm_set_one_toggle(btnm, true)` pour autoriser un seul bouton basculé à la fois.

### Recolorer
Les **textes** sur les boutons peuvent être **recolorés** de manière semblable à la recoloration de l'objet [Etiquette](/object-types/label). Pour activer cette fonctionnalité, utilisez `lv_btnm_set_recolor(btnm, true)`. Après cela, un bouton avec le texte `#FF0000 Red#` sera rouge.

### Notes
L'objet Matrice de boutons est très léger, car les boutons ne sont pas créés mais simplement dessinés à la volée.
De cette façon, 1 bouton utilise seulement 8 octets supplémentaires au lieu des ~100-150 octets d'un objet [Bouton](/object-types/btn) normal.

## Styles

La Matrice de boutons fonctionne avec 6 styles : un arrière-plan et 5 styles de boutons pour chaque état. Vous pouvez définir les styles avec `lv_btnm_set_style(btn, LV_BTNM_STYLE_..., &style)`.
L'arrière-plan et les boutons utilisent les propriétés `style.body`. Les étiquettes utilisent les propriétés `style.text` des styles de bouton.

- **LV_BTNM_STYLE_BG** style d'arrière-plan. Utilise toutes les propriétés _style.body_, y compris _padding_ Par défaut : _lv_style_pretty_
- **LV_BTNM_STYLE_BTN_REL** style des boutons relâchés. Défaut : _lv_style_btn_rel_
- **LV_BTNM_STYLE_BTN_PR** style des boutons pressés. Défaut : _lv_style_btn_pr_
- **LV_BTNM_STYLE_BTN_TGL_REL** style des boutons basculés relâchés. Défaut : _lv_style_btn_tgl_rel_
- **LV_BTNM_STYLE_BTN_TGL_PR** style des boutons basculés pressés. Défaut :  _lv_style_btn_tgl_pr_
- **LV_BTNM_STYLE_BTN_INA** style des boutons inactifs. Défaut : _lv_style_btn_ina_

## Evénements
Outre les [événements génériques](/overview/event.html #evenements-generiques), les [événements spéciaux](/overview/event.html#evenements-speciaux) suivants sont envoyés par les matrices de boutons :
 - **LV_EVENT_VALUE_CHANGED** envoyé lorsque le bouton est enfoncé/relâché ou répété après un appui prolongé. Les données d'événement sont l'ID du bouton enfoncé/relâché.

Apprenez-en plus sur les [événements](/overview/event).

## Touches

Les *touches* suivantes sont traitées par les boutons :
- **LV_KEY_RIGHT/UP/LEFT/RIGHT** Pour naviguer parmi les boutons pour en sélectionner un
- **LV_KEY_ENTER** Pour appuyer/relâcher le bouton sélectionné

Apprenez-en plus sur les [touches](/overview/indev).

## Exemple

```eval_rst

.. include:: /lv_examples/src/lv_ex_btnm/index.rst

```

## API 

```eval_rst

.. doxygenfile:: lv_btnm.h
  :project: lvgl
        
```

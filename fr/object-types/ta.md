```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/fr/object-types/ta.md
```
# Zone de texte (lv_ta)

## Vue d'ensemble

The Text Area is a [Page](/object-types/page) with a [Label](/object-types/label) and a cursor on it. Texts or characters can be added to it. Long lines are wrapped and when the text becomes long enough the Text area can be scrolled-

### Ajouter du texte

Vous pouvez insérer du texte ou des caractères à la position du curseur actuel avec :

- `lv_ta_add_char(ta, 'c')`
- `lv_ta_add_text(ta, "insert this text")`

Pour ajouter des caractères étendus comme `'á'`, `'ß'` ou des caractères CJK utilisez `lv_ta_add_text(ta, "á")`.

`lv_ta_set_text(ta, "New text")` change le texte en totalité.

### Substitutif

Vous pouvez spécifier un texte de substitution qui s’affiche lorsque la zone de texte est vide avec`lv_ta_set_placeholder_text(ta, "Placeholder text")`

### Supprimer un caractère

Pour supprimer un caractère à gauche de la position actuelle du curseur, utilisez `lv_ta_del_char(ta)`. Pour supprimer à droite, utilisez `lv_ta_del_char_forward(ta)`.

### Déplacer le curseur

La position du curseur peut être modifiée directement avec `lv_ta_set_cursor_pos(ta, 10)`. La position `0` signifie "avant les premiers caractères ", `LV_TA_CURSOR_LAST`signifie "après le dernier caractère".

Vous pouvez déplacer le curseur d'un caractère avec
- `lv_ta_cursor_right(ta)`
- `lv_ta_cursor_left(ta)`
- `lv_ta_cursor_up(ta)`
- `lv_ta_cursor_down(ta)`

Si `lv_ta_set_cursor_click_pos(ta, true)`est appelé le curseur se déplacera à la position où la zone de texte a été cliquée.

### Types de curseur

Il existe plusieurs types de curseur. Vous pouvez en choisir un avec : `lv_ta_set_cursor_type(ta, LV_CURSOR_...)`
- **LV_CURSOR_NONE** pas de curseur
- **LV_CURSOR_LINE** une simple ligne verticale
- **LV_CURSOR_BLOCK** un rectangle plein sur le caractère courant
- **LV_CURSOR_OUTLINE** une bordure rectangulaire autour du caractère courant
- **LV_CURSOR_UNDERLINE** souligne le caractère courant

Vous pouvez faire un ou logique de n'importe quel type de curseur avec `LV_CURSOR_HIDDEN` pour le masquer temporairement .

La durée de clignotement du curseur peut être réglée avec `lv_ta_set_cursor_blink_time(ta, time_ms)`.


### Mode une ligne
La zone de texte peut être configurée en mode une ligne avec `lv_ta_set_one_line(ta, true)`. Dans ce mode, la hauteur est calculée automatiquement pour afficher une seule ligne, les caractères de fin de ligne sont ignorés et le retour à la ligne est désactivé.

### Mode mot de passe
La zone de texte gère un mode de mot de passe qui peut être activé avec `lv_ta_set_pwd_mode(ta, true)`.En mode mot de passe, les caractères saisis sont convertis en `*` après un certain temps ou lorsqu'un nouveau caractère est entré.

En mode mot de passe `lv_ta_get_text(ta)` donne le texte réel et non les astérisques.

La durée de visibilité peut être ajustée avec `lv_ta_set_pwd_show_time(ta, time_ms)`.

### Alignement du texte
Le texte peut être aligné à gauche, au milieu ou à droite avec `lv_label_set_align(label, LV_LABEL_ALIGN_LEFT/CENTER/RIGHT)`.

En mode une ligne, le texte ne peut défiler horizontalement que si le texte est aligné à gauche.

### Caractères autorisés
Vous pouvez définir une liste de caractères autorisés avec `lv_ta_set_accepted_chars(ta, "0123456789.+-")`. Les autres caractères seront ignorés.

### Longueur de texte maximum.
Le nombre maximum de caractères peut être limité avec `lv_ta_set_max_length(ta, max_char_num)`

### Très long texte
S'il y a un texte très long dans la zone de texte (> 20000 caractères ) le défilement et l'affichage pourraient être lents. 
Cependant, en activant `LV_LABEL_LONG_TXT_HINT   1` dans *lv_conf.h* cela peut être grandement amélioré. 
Cela enregistre des informations sur l’étiquette pour accélérer son affichage. En utilisant `LV_LABEL_LONG_TXT_HINT` le défilement et l'affichage sont aussi rapides qu'avec des textes courts "normaux".

### Sélection de texte
Une partie du texte peut être sélectionnée si la fonctionnalité est activée avec `lv_ta_set_text_sel (ta, true)`. Cela fonctionne comme lorsque vous sélectionnez un texte sur votre PC avec votre souris.

### Barres de défilement
Les barres de défilement peuvent être affichées selon différentes stratégies définies par `lv_ta_set_sb_mode(ta, LV_SB_MODE_...)`. Apprenez-en plus sur l'objet [page](/object-types/page).

### Propagation du défilement
Lorsque la zone de texte défile sur un autre objet défilant (comme une page) et que le défilement a atteint le bord de la zone de texte, le défilement peut être propagé au parent.
En d’autres termes, lorsque la zone de texte ne peut continuer à défiler, le parent sera défilé à la place.

Cela peut être activé avec `lv_ta_set_scroll_propagation(ta, true)`.

Apprenez-en plus sur l'objet [page](/object-types/page).

### Mise en évidence du bord
Lorsque vous faites défiler la zone de texte jusqu'à une bordure, l'animation d'un cercle peut être affichée si cela est activé avec`lv_ta_set_edge_flash(ta, true)`

## Styles

Utilisez `lv_ta_set_style(page, LV_TA_STYLE_...,  &style)` pour définir un nouveau style pour un élément de la zone de texte :

- **LV_TA_STYLE_BG** style de l'arrière-plan qui utilise toutes les propriétés `style.body`. L'étiquette utilise `style.label` de ce style (valeur par défaut : `lv_style_pretty`).
- **LV_TA_STYLE_SB** style de la barre de défilement qui utilise toutes les propriétés `style.body` (valeur par défaut : `lv_style_pretty_color`).
- **LV_TA_STYLE_CURSOR** style du curseur. Si `NULL` alors la librairie définit automatiquement un style en fonction de la couleur et de la police de l'étiquette.
    - *LV_CURSOR_LINE*: a `style.line.width` wide line but drawn as a rectangle as `style.body`. `padding.top/left` makes an offset on the cursor
    - *LV_CURSOR_BLOCK*: a rectangle as `style.body`  `padding` makes the rectangle larger
    - *LV_CURSOR_OUTLINE*: an empty rectangle (just a border) as `style.body` `padding` makes the rectangle larger
    - *LV_CURSOR_UNDERLINE*: a `style.line.width` wide line but drawn as a rectangle as `style.body`. `padding.top/left` makes an offset on the cursor 



## Evénements
Outre les [événements génériques](/overview/event.html #evenements-generiques), les [événements spéciaux](/overview/event.html#evenements-speciaux) suivants sont envoyés par la zone de texte :
- **LV_EVENT_INSERT** envoyé avant l'insertion d'un caractère.
La donnée d'événement est le texte qu'il est prévu d'insérer. `lv_ta_set_insert_replace(ta, "New text")` remplace le texte à insérer.
Le nouveau texte ne peut être une variable locale, détruite lorsque la fonction de rappel se termine. `" "` annule l'insertion.
- **LV_EVENT_VALUE_CHANGED** envoyé quand le contenu de la zone de texte a été modifié.

## Touches
- **LV_KEY_UP/DOWN/LEFT/RIGHT** déplace le curseur
- **Tout caractère** insère le caractère à la position du curseur

Apprenez-en plus sur les [touches](/overview/indev).

## Exemple

```eval_rst

.. include:: /lv_examples/src/lv_ex_ta/index.rst

```

## API 

```eval_rst

.. doxygenfile:: lv_ta.h
  :project: lvgl
        
```

```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/fr/object-types/table.md
```
# Table (lv_table)

## Vue d'ensemble

Comme d'habitude, les tables sont construites à partir de lignes, de colonnes et de cellules contenant des textes.

L'objet table est très léger, car seuls les textes sont enregistrés. Aucun objet réel n'est créé pour les cellules, elles sont simplement dessinées à la volée.

### Llignes et colonnes

Pour définir le nombre de lignes et de colonnes, utilisez `lv_table_set_row_cnt(table, row_cnt)` et `lv_table_set_col_cnt(table, col_cnt)`.

### Largeur et hauteur

La largeur des colonnes peut être définie avec `lv_table_set_col_width(table, col_id, width)`. La largeur totale de l'objet table sera définie par la somme des largeurs des colonnes.

La hauteur est calculée automatiquement à partir des styles des cellule (police, marges, etc.) et du nombre de lignes.

### Définir la valeur de la cellule

Les cellules peuvent enregistrer uniquement du texte, il est donc nécessaire de convertir les nombres en texte avant de les afficher dans une table.

`lv_table_set_cell_value(table, row, col, "Content")`. Le texte est sauvegardé par la table et peut donc être une variable locale.

Le saut de ligne peut être utilisé dans le texte comme `"Value\n60.3"`.

### Alignement

L’alignement du texte dans les cellules peut être ajusté individuellement avec `lv_table_set_cell_align(table, row, col, LV_LABEL_ALIGN_LEFT/CENTER/RIGHT)`.

### Type de cellule

Vous pouvez utiliser 4 types de cellules différents. Chacun a son propre style.

Les types de cellules peuvent être utilisés pour ajouter un style différent, par exemple pour :
- en-tête de table
- première colonne
- mise en évidence d'une cellule
- etc

Le type peut être sélectionné avec `lv_table_set_cell_type(table, row, col, type)` `type` peut être 1, 2, 3 ou 4.

### Fusionner des cellules

Les cellules peuvent être fusionnées horizontalement avec `lv_table_set_cell_merge_right(table, col, row, true)`. Pour fusionner davantage de cellules adjacentes, appliquez cette fonction à chaque cellule.


### Crop text
Par défaut, des retours à la ligne sont insérés pour permettre aux texte de s'inscrire dans la largeur de la cellule, et la hauteur de la cellule est définie automatiquement. Pour désactiver ce comportement et conserver le texte tel qu'il est, activez ` lv_table_set_cell_crop(table, row, col, true)`.

### Défilement
Pour pouvoir faire défiler la table, placez-la sur une [page](/object-types/page)

## Styles
  
Utilisez `lv_table_set_style(table, lv_table_set_style..., &style)` pour définir un nouveau style pour un élément de la table :

- **LV_PAGE_STYLE_BG** style de l'arrière-plan qui utilise toutes les propriétés `style.body` (valeur par défaut : `lv_style_plain_color`).
- **LV_PAGE_STYLE_CELL1/2/3/4** 4 styles pour les 4 types de cellules. Toutes les propriétés `style.body` sont utilisées. (valeur par défaut : `lv_style_plain`).

## Evénements
Seuls les [événements génériques](/overview/event.html#generic-events) sont envoyés par ce type d'objet.

Apprenez-en plus sur les [événements](/overview/event).

## Touches

Aucune *touche* n'est traitée par ce type d'objet.

Apprenez-en plus sur les [touches](/overview/indev).

## Exemple

```eval_rst

.. include:: /lv_examples/src/lv_ex_table/index.rst

```

### MicroPython
Pas encore d'exemple.

## API 

```eval_rst

.. doxygenfile:: lv_table.h
  :project: lvgl
        
```

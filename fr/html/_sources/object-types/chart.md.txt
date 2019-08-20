```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/fr/object-types/chart.md
```
# Graphique (lv_chart)

## Vue d’ensemble

Les graphiques ont un arrière-plan rectangulaire avec des lignes de division horizontales et verticales et des séries de données représentées par des lignes, colonnes de points ou zones.

### Série de données
Vous pouvez ajouter un nombre quelconque de séries aux graphiques avec `lv_chart_add_series(chart, color)`. 
Cette fonction alloue la mémoire pour une structure `lv_chart_series_t` qui contient la `couleur` choisie et un tableau pour les points.

### Type de série
Les **types de données** suivants existent :

- **LV_CHART_TYPE_NONE** ne pas afficher de données. Utilisé pour masquer une série.
- **LV_CHART_TYPE_LINE** tracer des lignes entre les points.
- **LV_CHART_TYPE_COL** dessine des barres.
- **LV_CHART_TYPE_POINT** dessine des points.
- **LV_CHART_TYPE_AREA** dessine des zones (remplit la zone en dessous des lignes qui relient les points).
- **LV_CHART_TYPE_VERTICAL_LINE** Dessine uniquement des lignes verticales pour relier les points. Utile si la largeur du graphique est égale au nombre de points.

Vous pouvez spécifier le type de données avec `lv_chart_set_type(chart, LV_CHART_TYPE_...)`. Les types peuvent être combinés par 'OU' (comme `LV_CHART_TYPE_LINE | LV_CHART_TYPE_POINT`).

### Modifier le données
Vous avez plusieurs possibilités pour définir les données de la série :
1. Définir les valeurs manuellement dans le tableau comme `ser1->points[3] = 7` et actualiser le graphique avec `lv_chart_refresh(chart)`.
2. Utiliser `lv_chart_set_next(chart, ser, value)`.
3. Initialiser tous les points avec une valeur donnée : `lv_chart_init_points(chart, ser, value)`.
4. Définir tous les points à partir d'un tableau : `lv_chart_set_points(chart, ser, value_array)`.

Utilisez `LV_CHART_POINT_DEF` comme valeur pour indiquer à la librairie de ne pas tracer un point, une colonne ou un segment de ligne.

### Modes de mise à jour
`lv_chart_set_next` peut se comporter de deux manières selon le *mode de mise à jour* :
- **LV_CHART_UPDATE_MODE_SHIFT** déplacer les anciennes données vers la gauche et ajoute la nouvelle à droite,
- **LV_CHART_UPDATE_MODE_CIRCULAR** Ajoute les nouvelles données de manière circulaire (comme un ECG).

Le mode de mise à jour peut être changé avec `lv_chart_set_update_mode(chart, LV_CHART_UPDATE_MODE_...)`.

### Nombre de points
Le nombre de points de la série peut être modifié par `lv_chart_set_point_count(chart, point_num)`. La valeur par défaut est 10.

### Plage verticale
Vous pouvez spécifier des valeurs minimum et maximum dans la direction y avec `lv_chart_set_range(chart, y_min, y_max)`. La valeur des points sera mise à l'échelle proportionnellement. La plage par défaut est : 0..100.

### Quadrillage
Le nombre de lignes horizontales et verticales du quadrillage peut être modifié par `lv_chart_set_div_line_count(chart, hdiv_num, vdiv_num)`. Les valeurs par défaut sont 3 lignes horizontales et 5 lignes verticales.

Apparence de la série
Pour définir l'**épaisseur de ligne** et le **rayon des points** de la série, utilisez la fonction `lv_chart_set_series_width(chart, size)`. La valeur par défaut est : 2.

L'**opacité des lignes de données** peut être spécifiée par `lv_chart_set_series_opa(chart, opa)`. La valeur par défaut est : OPA_COVER.

Vous pouvez appliquer un **assombrissement** au bas des colonnes et des points avec la fonction `lv_chart_set_series_darking(chart, effect)`. Le niveau par défaut est OPA_50.


### Graduation et étiquettes
Des graduations et étiquettes peuvent être ajoutés.

`lv_chart_set_x_tick_text(chart, list_of_values, num_tick_marks, LV_CHART_AXIS_...)` définit les graduations et les textes sur l'axe des x.
`list_of_values` est une chaîne de textes pour les graduations délimités par des `'\n'` (excepté le dernier). P.ex. `const char * list_of_values = "premier\ndeuxième\ntroisième"`. `list_of_values` peut être `NULL`.
Si `list_of_values` est défini alors `num_tick_marks` indique le nombre de graduations entre deux étiquettes.  Si `list_of_values` est `NULL` alors il spécifie le nombre total de graduations.

Lorsque du texte est ajouté des *lignes principales* de quadrillage sont dessinées, ailleurs des *lignes secondaires*. `lv_chart_set_x_tick_length(chart, major_tick_len, minor_tick_len)` définit l'épaisseur des lignes de graduation sur l'axe des x.

Les mêmes fonctions existent aussi pour l’axe des y :  `lv_chart_set_y_tick_text` et `lv_chart_set_y_tick_length`

`lv_chart_set_margin(chart, 20)` doit être utilisée pour ajouter un espace supplémentaire autour du graphique pour les graduations et les textes.

## Styles
Vous pouvez définir les styles avec `lv_chart_set_style(btn, LV_CHART_STYLE_MAIN, &style)`.
- **style.body** définit l'apparence de l'arrière-plan,
- **style.line** définit l'apparence du quadrillage,
- **style.text** définit l'apparence des étiquettes des axes.


## Evénements
Seuls les [événements génériques](/overview/event.html#generic-events) sont envoyés par ce type d'objet.

Apprenez-en plus sur les [événements](/overview/event).

## Touches
Aucune *touche* n'est traitée par ce type d'objet.

Apprenez-en plus sur les [touches](/overview/indev).

## Exemple

```eval_rst

.. include:: /lv_examples/src/lv_ex_chart/index.rst

```

## API 

```eval_rst

.. doxygenfile:: lv_chart.h
  :project: lvgl
        
```

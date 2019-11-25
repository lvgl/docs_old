```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/fr/object-types/lmeter.md
```
# Compteur (lv_lmeter)

## Vue d'ensemble

L'objet  compteur est constitué de quelques lignes radiales qui dessinent une échelle.

### Définir la valeur
Lors de la définition d'une nouvelle valeur avec `lv_lmeter_set_value(lmeter, new_value)`, la partie proportionnelle de l'échelle sera recolorée.

### Intervalle et angles
La fonction `lv_lmeter_set_range(lmeter, min, max)` définit l'intervalle du compteur linéaire.

Vous pouvez définir l'angle de l'échelle et le nombre de lignes à l'aide de : `lv_lmeter_set_scale(lmeter, angle, line_num)`.
L'angle par défaut est 240 et le nombre de ligne par défaut est 31.

### Angle offset
By default the scale angle is interpreted symmetrically to the y axis. It results in "standing" line meter. With `lv_lmeter_set_angle_offset` an offset can be added the scale angle. 
It can used e.g to put a quarter line meter into a corner or a half line meter to the right or left side. 

## Styles

Le compteur utilise un style qui peut être défini par `lv_lmeter_set_style(lmeter, LV_LMETER_STYLE_MAIN, &style)`. Les propriétés du compteur sont dérivées des attributs de style suivants :

- **line.color** la couleur des "lignes inactives" qui sont supérieure à la valeur actuelle
- **body.main_color** couleur de la "ligne active" au début de l'échelle
- **body.grad_color** couleur de la "ligne active" à la fin de l'échelle (dégradé avec la couleur principale)
- **body.padding.hor** longueur des lignes
- **line.width** largeur des lignes

Le style par défaut est `lv_style_pretty_color`.

## Evénements
Seuls les [événements génériques](/overview/event.html#generic-events) sont envoyés par ce type d'objet.

Apprenez-en plus sur les [événements](/overview/event).

## Touches
Aucune *touche* n'est traitée par ce type d'objet.

Apprenez-en plus sur les [touches](/overview/indev).

## Exemple

```eval_rst

.. include:: /lv_examples/src/lv_ex_lmeter/index.rst

```

## API 

```eval_rst

.. doxygenfile:: lv_lmeter.h
  :project: lvgl
        
```


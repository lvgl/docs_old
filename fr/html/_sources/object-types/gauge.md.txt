```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/fr/object-types/gauge.md
```
# Jauge (lv_gauge)

## Vue d’ensemble

La jauge est semi-circulaire, présente une échelle graduée, des étiquettes et des aiguilles.

###  Echelle graduée
Vous pouvez utiliser la fonction `lv_gauge_set_scale(gauge, angle, line_num, label_cnt)` pour ajuster l'angle, les graduations et les étiquettes de l'échelle graduée.
Les paramètres par défaut sont 220 degrés, 21 graduations et 6 étiquettes.

### Aiguilles
La jauge peut montrer plus d'une aiguille.
Utilisez la fonction `lv_gauge_set_needle_count(gauge, needle_num, color_array)`pour définir le nombre d’aiguilles et un tableau de couleurs pour chaque aiguille. Le tableau doit être une variable statique ou globale car seul son pointeur est sauvegardé.

Vous pouvez utiliser `lv_gauge_set_value(gauge, needle_id, value)` pour définir une aiguille.

### Plage
La plage de la jauge peut être spécifiée par `lv_gauge_set_range(gauge, min, max)`. La plage par défaut est 0..100.

### Valeur critique
Pour définir une valeur critique, utilisez `lv_gauge_set_critical_value(gauge, value)`. La couleur des graduations sera changée en `line.color` après cette valeur (défaut : 80).

## Styles

La jauge utilise un style qui peut être défini par `lv_gauge_set_style(gauge, LV_GAUGE_STYLE_MAIN, &style)`. Les propriétés de la jauge sont dérivées des attributs de style suivants :

- **body.main_color** la couleur des graduations au début de l'échelle graduée,
- **body.grad_color** la couleur des graduations à la fin de l'échelle graduée (dégradé avec la couleur principale),
- **body.padding.left** longueur de graduation,
- **body.padding.inner** distance de l'étiquette par rapport à l'échelle graduée,
- **body.radius** rayon du cercle d'origine de l'aiguille.
- **line.width** épaisseur de graduation
- **line.color** couleur de graduation après la valeur critique,
- **text.font/color/letter_space** attributs de l'étiquette.

## Evénements
Seuls les [événements génériques](/overview/event.html#generic-events) sont envoyés par ce type d'objet.

Apprenez-en plus sur les [événements](/overview/event).

## Touches
Aucune *touche* n'est traitée par ce type d'objet.

Apprenez-en plus sur les [touches](/overview/indev).

## Exemple

```eval_rst

.. include:: /lv_examples/src/lv_ex_gauge/index.rst

```
## API 

```eval_rst

.. doxygenfile:: lv_gauge.h
  :project: lvgl
        
```

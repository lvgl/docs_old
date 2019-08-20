```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/fr/object-types/calendar.md
```
# Calendrier (lv_calendar)

## Vue d’ensemble

L'objet calendrier est un calendrier classique qui peut :
- mettre en évidence le jour et la semaine en cours,
- mettre en évidence les dates définies par l'utilisateur,
- afficher le nom des jours,
- aller au mois suivant/précédent en cliquant sur un bouton,
- mettre en évidence le jour cliqué.

Pour manipuler les dates dans le calendrier, le type `lv_calendar_date_t` est utilisé. Il s'agit d'une structure avec des champs` année`, `mois` et `jour`.

### Date courante
Pour définir la date du jour (aujourd'hui), utilisez la fonction `lv_calendar_set_today_date(calendar, &today_date)`.

### Date affichée
Pour définir la date affichée, utilisez `lv_calendar_set_shown_date(calendar, &shown_date)`.

### Jours mis en évidence
La liste des dates à mettre en évidence doit être mémorisée dans un tableau `lv_calendar_date_t` et chargé par `lv_calendar_set_highlighted_dates(calendar, &highlight_dates)`.
Seul le pointeur sur le tableau sera enregistré. Le tableau doit donc être une variable statique ou globale.

### Nom des jours
Le nom des jours peut être spécifié avec `lv_calendar_set_day_names(calendar, day_names)` où `day_names` ressemble à `const char * day_names [7] = { "Di", "Lu", ... }; `

### Nom des mois
De même que pour le nom des jours, le nom des mois peut être défini avec `lv_calendar_set_month_names(calendar, month_names_array)`.

## Styles
Vous pouvez définir les styles avec `lv_calendar_set_style(btn, LV_CALENDAR_STYLE_..., &style)`. 

- **LV_CALENDAR_STYLE_BG** Style de l'arrière-plan utilisant les propriétés `body` et style des nombres de date utilisant les propriétés `text`. `body.padding.left/rigth/bottom` seront ajoutés autour des numéros de date.
- **LV_CALENDAR_STYLE_HEADER** style de l'en-tête où sont affichés l'année et le mois en cours. Les propriétés `body` et` text` sont utilisées.
- **LV_CALENDAR_STYLE_HEADER_PR** Style d'en-tête utilisé lorsque vous appuyez sur le bouton du mois précédent/suivant. Les propriétés `text` sont utilisées par les flèches.
- **LV_CALENDAR_STYLE_DAY_NAMES** Style des noms de jour. Les propriétés `text` sont utilisées par les textes de jour et `body.padding.top` détermine l'espace au-dessus des noms de jour.
- **LV_CALENDAR_STYLE_HIGHLIGHTED_DAYS** Les propriétés `text` sont utilisées pour ajuster le style des jours mis en évidence
- **LV_CALENDAR_STYLE_INACTIVE_DAYS** Les propriétés `text` sont utilisées pour ajuster le style des jours visibles du mois précédent/suivant.
- **LV_CALENDAR_STYLE_WEEK_BOX** Les propriétés `body` sont utilisées pour définir le style de la boîte de la semaine
- **LV_CALENDAR_STYLE_TODAY_BOX** Les propriétés `body` et` text` sont utilisées pour définir le style de la boîte du jour

## Evénements
Outre les [événements génériques](/overview/event.html #evenements-generiques), les [événements spéciaux](/overview/event.html#evenements-speciaux) suivants  sont envoyés par les calendriers :
**LV_EVENT_VALUE_CHANGED** est envoyé lorsque le mois en cours a changé.

Parmi les événements *liés au périphérique d'entrée* `lv_calendar_get_pressed_date(calendar)` indique quel jour est actuellement sélectionnée ou retourne `NULL` si aucune date n'est sélectionnée.

## Touches
Aucune *touche* n'est traitée par ce type d'objet.

Apprenez-en plus sur les [touches](/overview/indev).


## Exemple

```eval_rst

.. include:: /lv_examples/src/lv_ex_calendar/index.rst

```

## API 

```eval_rst

.. doxygenfile:: lv_calendar.h
  :project: lvgl
        
```

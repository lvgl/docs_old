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

To set and get dates in the calendar, the `lv_calendar_date_t` type is used which is a structure with `year`, `month` and `day` fields.

### Date courante
To set the current date (today), use the `lv_calendar_set_today_date(calendar, &today_date)` function.

### Date affichée
To set the shown date, use `lv_calendar_set_shown_date(calendar, &shown_date)`;

### Jours mis en évidence
The list of highlighted dates should be stored in a `lv_calendar_date_t` array loaded by `lv_calendar_set_highlighted_dates(calendar, &highlighted_dates)`.  
Only the arrays pointer will be saved so the array should be a static or global variable.

### Nom des jours
Le nom des jours peut être spécifié avec `lv_calendar_set_day_names(calendar, day_names)` où `day_names` ressemble à `const char * day_names [7] = { "Di", "Lu", ... }; `

### Nom des mois
Similarly to `day_names`, the name of the month can be set with `lv_calendar_set_month_names(calendar, month_names_array)`.

## Styles
You can set the styles with `lv_calendar_set_style(btn, LV_CALENDAR_STYLE_..., &style)`.

- **LV_CALENDAR_STYLE_BG** - Style of the background using the `body` properties and the style of the date numbers using the `text` properties. `body.padding.left/right/bottom` padding will be added on the edges around the date numbers.
- **LV_CALENDAR_STYLE_HEADER** - Style of the header where the current year and month is displayed. `body` and `text` properties are used.
- **LV_CALENDAR_STYLE_HEADER_PR** - Pressed header style, used when the next/prev. month button is being pressed. `text` properties are used by the arrows.
- **LV_CALENDAR_STYLE_DAY_NAMES** - Style of the day names. `text` properties are used by the 'day' texts and `body.padding.top` determines the space above the day names.
- **LV_CALENDAR_STYLE_HIGHLIGHTED_DAYS** - `text` properties are used to adjust the style of the highlights days.
- **LV_CALENDAR_STYLE_INACTIVE_DAYS** - `text` properties are used to adjust the style of the visible days of previous/next month.
- **LV_CALENDAR_STYLE_WEEK_BOX** - `body` properties are used to set the style of the week box.
- **LV_CALENDAR_STYLE_TODAY_BOX** - `body` and `text` properties are used to set the style of the today box.

## Evénements
Besides the [Generic events](/overview/event.html#generic-events), the following [Special events](/overview/event.html#special-events) are sent by the calendars:
**LV_EVENT_VALUE_CHANGED** est envoyé lorsque le mois en cours a changé.

In *Input device related* events, `lv_calendar_get_pressed_date(calendar)` tells which day is currently being pressed or return `NULL` if no date is pressed.

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

```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/en/object-types/calendar.md
```
# Calendar (lv_calendar)

## Overview

The Calendar object is a classic calendar which can:
- highlight the current day and week
- highlight any user-defined dates
- display the name of the days
- go the next/previous month by button click
- highlight the clicked day

The set and get dates in the calendar the `lv_calendar_date_t` type is used which is a structure with `year`, `month` and `day` fields.

### Current date
To set the current date (today) use the `lv_calendar_set_today_date(calendar, &today_date)` function.

### Shown date
To set the shown date use `lv_calendar_set_shown_date(calendar, &shown_date)`;

### Highlighted days
The list of highlighted dates should be stored in a `lv_calendar_date_t` array a loaded by `lv_calendar_set_highlighted_dates(calendar, &highlighted_dates)`.  
Only the arrays pointer will be saved so the array should be a static or global variable. 

### Name of the days
The name of the days can be adjusted with `lv_calendar_set_day_names(calendar, day_names)` where `day_names` looks like `const char * day_names[7] = {"Su", "Mo", ...};`

### Name of the months
Similarly to day names the name of the month can be set with `lv_calendar_set_month_names(calendar, month_names_array)`.

## Styles
You can set the styles with `lv_calendar_set_style(btn, LV_CALENDAR_STYLE_..., &style)`. 

- **LV_CALENDAR_STYLE_BG** Style of the background using the `body` properties and the style of the date numbers using the `text` properties. `body.padding.left/rigth/bottom` padding will be added on the edges. around the date numbers. 
- **LV_CALENDAR_STYLE_HEADER** Style of the header where the current year and month is displayed. `body` and `text` properties are used.
- **LV_CALENDAR_STYLE_HEADER_PR** Pressed header style, used when the next/prev. month button is being pressed. `text` properties are used by the arrows.
- **LV_CALENDAR_STYLE_DAY_NAMES** Style of the day names. `text` properties are used by the day texts and `body.padding.top` determines the space above the day names.
- **LV_CALENDAR_STYLE_HIGHLIGHTED_DAYS** `text` properties are used to adjust the style of the highlights days
- **LV_CALENDAR_STYLE_INACTIVE_DAYS** `text` properties are used to adjust the style of the visible days of previous/next month.
- **LV_CALENDAR_STYLE_WEEK_BOX** `body` properties are used to set the style of the week box
- **LV_CALENDAR_STYLE_TODAY_BOX** `body` and `text` properties are used to set the style of the today box

## Events
Besides the [Generic events](/overview/event.html#generic-events) the following [Special events](/overview/event.html#special-events) are sent by the calendars:
**LV_EVENT_VALUE_CHANGED** is sent when the current month has changed.

In *Input device related* events `lv_calendar_get_pressed_date(calendar)` tells which day is currently being pressed or return `NULL` if no date is pressed.

## Keys
No *Keys* are processed by the object type.

Learn more about [Keys](/overview/indev).


## Example

```eval_rst

.. include:: /lv_examples/src/lv_ex_calendar/index.rst

```

## API 

```eval_rst

.. doxygenfile:: lv_calendar.h
  :project: lvgl
        
```

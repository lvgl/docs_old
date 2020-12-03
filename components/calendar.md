```eval_rst
.. include:: /header.rst 
:github_url: |github_link_base|/components/calendar.md
```
# Calendar (lv_calendar)

## Overview

The Calendar component is a classic calendar which can:
- show a selected month
- highlight the current day
- highlight any user-defined dates
- display the name of the days
- highlight the clicked day

## Parts and Styles
The calendar is a [Button matrix](/widgets/btnmatrix) which buttons are the dates. 

To calendar can be styled like this:
- **Background** Background related style properties in `LV_BTNMATRIX_PART_MAIN`
- **Day names** Background and text related style properties in `LV_BTNMATRIX_PART_BTN_2` with `LV_STATE_DEFAULT`
- **Normal dates** Background and text related style properties in `LV_BTNMATRIX_PART_BTN` with `LV_STATE_DEFAULT`
- **Highlighted date** Background and text related style properties in `LV_BTNMATRIX_PART_BTN` with `LV_STATE_CHECKED`
- **Today date** Background and text related style properties in `LV_BTNMATRIX_PART_BTN_2` with `LV_STATE_CHECKED`


## Usage

To set and get dates in the calendar, the `lv_calendar_date_t` type is used which is a structure with `year`, `month` and `day` fields.
The values in both `month` and `day` starts from 1.

To create a calendar 
```c
lv_obj_t * calendar = lv_calendar_create(parent, day_names); 
```

`day_names` can be `NULL` to use the default names or a pointer to an array like this:
```c
static const char * day_names[7]    = {"Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"};
```

### Current date
To set the current date (today), use the `lv_calendar_set_today_date(calendar, &today_date)` function.

### Shown date
To set the shown date, use `lv_calendar_set_shown_date(calendar, &shown_date)`;

### Highlighted days
The list of highlighted dates should be stored in a `lv_calendar_date_t` array loaded by `lv_calendar_set_highlighted_dates(calendar, &highlighted_dates)`.  
Only the arrays pointer will be saved so the array should be a static or global variable.

### Get the pressed date
The currently pressed data can be retrieved by `bool valid = lv_calendar_get_pressed_date(calendar, &date)`. The function will return `true` is there is valid pressed date.
It's useful to get the pressed or clicked date in an event function.


## Events
The Calendar reacts on the [Generic events](../overview/event.html#generic-events), the following [Special events](../overview/event.html#special-events) are sent by the calendars:

## Keys
The Calendar works like the [Button matrix](/widgets/btnmatrix) when used with keys. Days can be selected
Learn more about [Keys](/overview/indev).
## Extensions

## Header with arrow

To following function creates a rectangle with two buttons on the left and right and text in the middle: 
```c
lv_obj_t * header = lv_calendar_header_arrow_create(parent, calendar, month_names, btn_size);
```
The buttons can be used to go to the next/previous month, and the text shows the current year and month. 
The `calendar` parameter tell which Calendar object shall it control.
The `month_name` parameter in array with the month names to use or `NULL` to use the default names. E.g. 
```c
static const char * month_names_def[12] = {"January", "February", "March",     "April",   "May",      "June",
                                      "July",    "August",   "September", "October", "November", "December"
                                     };
```
`btn_size` tells how large the buttons should be. The buttons are rectangles so this size applies to width and height too.

To use the header with keys the left and right button can be added to group. Use `lv_obj_get_child_by_id(header, 0)` to get the left button and `lv_obj_get_child_by_id(header, 2)` to get the right button.


## Example

```eval_rst

.. include:: /lv_examples/src/lv_ex_components/lv_ex_calendar/index.rst

```

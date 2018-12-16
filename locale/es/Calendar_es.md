_Written for v5.2_

## Overview

The Calendar object is a classic calendar which can:
- highlight the current day and week
- highlight any user-defined dates
- display the name of the days
- go the next/previous month by button click

The set and get dates in the calendar the `lv_calendar_date_t` type is used which is a structure with `year`, `month` and `day` fields.

To set the **current date** use the `lv_calendar_set_today_date(calendar, &today_date)` function.

To set the **shown date** use `lv_calendar_set_shown_date(calendar, &shown_date)`;

The list of **highlighted dates** should be stired in a `lv_calendar_date_t` array and passed this array can be passed to `lv_calendar_set_hoghlighted_dates(calendar, &highlighted_dates)`.  
Only the arrays pointer will be saved so the array should be a static or global variable. 

The **name of the days** can be adjusted with `lv_calendar_set_day_names(calendar, day_names)` where `day_names` looks like `const char * day_names[7] = {"Su", "Mo", ...};`


A**action to select a date** will be supported in `v5.3` and now available in the `dev-5.3` branch for experimental usage.


## Style usage
- **LV_CALENDAR_STYLE_BG** Style of the background using the `body` properties and the style of the data numbers using the `text` properties. 
- **LV_CALENDAR_STYLE_HEADER** Style of the header where the current year and month is displayed. `body` and `text` properties are used.
- **LV_CALENDAR_STYLE_HEADER_PR** Pressed header style, used when the next/prev. month button is being pressed. `text` properties are used by the arrows.
- **LV_CALENDAR_STYLE_DAY_NAMES** Style of the day names. `text` properties are used by the day texts and `body.padding.ver` determines the space above the day names.
- **LV_CALENDAR_STYLE_HIGHLIGHTED_DAYS** `text` properties are used to adjust the style of the highlights days
- **LV_CALENDAR_STYLE_INACTIVE_DAYS** `text` properties are used to adjust the style of the visible days of previous/next month.
- **LV_CALENDAR_STYLE_WEEK_BOX** `body` properties are used to set the style of the week box
- **LV_CALENDAR_STYLE_TODAY_BOX** `body` and `text` properties are used to set the style of the today box

## Example

![Calendar image](http://docs.littlevgl.com/img/calendar-lv_calendar.png)

```c
/*Create a Calendar object*/
lv_obj_t * calendar = lv_calendar_create(lv_scr_act(), NULL);
lv_obj_set_size(calendar, 240, 220);
lv_obj_align(calendar, NULL, LV_ALIGN_CENTER, 0, 0);

/*Create a style for the current week*/
static lv_style_t style_week_box;
lv_style_copy(&style_week_box, &lv_style_plain);
style_week_box.body.border.width = 1;
style_week_box.body.border.color = LV_COLOR_HEX3(0x333);
style_week_box.body.empty = 1;
style_week_box.body.radius = LV_RADIUS_CIRCLE;
style_week_box.body.padding.ver = 3;
style_week_box.body.padding.hor = 3;

/*Create a style for today*/
static lv_style_t style_today_box;
lv_style_copy(&style_today_box, &lv_style_plain);
style_today_box.body.border.width = 2;
style_today_box.body.border.color = LV_COLOR_NAVY;
style_today_box.body.empty = 1;
style_today_box.body.radius = LV_RADIUS_CIRCLE;
style_today_box.body.padding.ver = 3;
style_today_box.body.padding.hor = 3;
style_today_box.text.color= LV_COLOR_BLUE;

/*Create a style for the highlighted days*/
static lv_style_t style_highlighted_day;
lv_style_copy(&style_highlighted_day, &lv_style_plain);
style_highlighted_day.body.border.width = 2;
style_highlighted_day.body.border.color = LV_COLOR_NAVY;
style_highlighted_day.body.empty = 1;
style_highlighted_day.body.radius = LV_RADIUS_CIRCLE;
style_highlighted_day.body.padding.ver = 3;
style_highlighted_day.body.padding.hor = 3;
style_highlighted_day.text.color= LV_COLOR_BLUE;

/*Apply the styles*/
lv_calendar_set_style(calendar, LV_CALENDAR_STYLE_WEEK_BOX, &style_week_box);
lv_calendar_set_style(calendar, LV_CALENDAR_STYLE_TODAY_BOX, &style_today_box);
lv_calendar_set_style(calendar, LV_CALENDAR_STYLE_HIGHLIGHTED_DAYS, &style_highlighted_day);


/*Set the today*/
lv_calendar_date_t today;
today.year = 2018;
today.month = 10;
today.day = 23;

lv_calendar_set_today_date(calendar, &today);
lv_calendar_set_showed_date(calendar, &today);

/*Highlight some days*/
static lv_calendar_date_t highlihted_days[3];       /*Only it's pointer will be saved so should be static*/
highlihted_days[0].year = 2018;
highlihted_days[0].month = 10;
highlihted_days[0].day = 6;

highlihted_days[1].year = 2018;
highlihted_days[1].month = 10;
highlihted_days[1].day = 11;

highlihted_days[2].year = 2018;
highlihted_days[2].month = 11;
highlihted_days[2].day = 22;

lv_calendar_set_highlighted_dates(calendar, highlihted_days, 3);
```

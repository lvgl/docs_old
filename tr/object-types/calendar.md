```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/tr/object-types/calendar.md
```
# Takvim (lv_calendar)

## Genel Bakış

Takvim nesnesi, klasik takvim özelliklerini içeren bir nesnedir:
- Şuan ki gün ve haftayı vurgula
- Kullanıcı tanımlı tarihleri vurgula
Günlerin ismi göster
- Buton tıklaması yardımıyla sonraki/önceki aya git
Tıklanan günü vurgula

To set and get dates in the calendar, the `lv_calendar_date_t` type is used which is a structure with `year`, `month` and `day` fields.

### Şuan ki tarih
To set the current date (today), use the `lv_calendar_set_today_date(calendar, &today_date)` function.

### Gösterilen tarih
To set the shown date, use `lv_calendar_set_shown_date(calendar, &shown_date)`;

### Vurgulanan günler
The list of highlighted dates should be stored in a `lv_calendar_date_t` array loaded by `lv_calendar_set_highlighted_dates(calendar, &highlighted_dates)`.  
Only the arrays pointer will be saved so the array should be a static or global variable.

### Gün İsimleri
Gün isimleri `lv_calendar_set_day_names(calendar, day_names)` ile ayarlanabilir, `day_names`  şuna benziyorsa `const char * day_names[7] = {"Su", "Mo", ...};`

### Ay İsimleri
Similarly to `day_names`, the name of the month can be set with `lv_calendar_set_month_names(calendar, month_names_array)`.

## Biçim
You can set the styles with `lv_calendar_set_style(btn, LV_CALENDAR_STYLE_..., &style)`.

- **LV_CALENDAR_STYLE_BG** - Style of the background using the `body` properties and the style of the date numbers using the `text` properties. `body.padding.left/right/bottom` padding will be added on the edges around the date numbers.
- **LV_CALENDAR_STYLE_HEADER** - Style of the header where the current year and month is displayed. `body` and `text` properties are used.
- **LV_CALENDAR_STYLE_HEADER_PR** - Pressed header style, used when the next/prev. month button is being pressed. `text` properties are used by the arrows.
- **LV_CALENDAR_STYLE_DAY_NAMES** - Style of the day names. `text` properties are used by the 'day' texts and `body.padding.top` determines the space above the day names.
- **LV_CALENDAR_STYLE_HIGHLIGHTED_DAYS** - `text` properties are used to adjust the style of the highlights days.
- **LV_CALENDAR_STYLE_INACTIVE_DAYS** - `text` properties are used to adjust the style of the visible days of previous/next month.
- **LV_CALENDAR_STYLE_WEEK_BOX** - `body` properties are used to set the style of the week box.
- **LV_CALENDAR_STYLE_TODAY_BOX** - `body` and `text` properties are used to set the style of the today box.

Aksiyonlar
Besides the [Generic events](/overview/event.html#generic-events), the following [Special events](/overview/event.html#special-events) are sent by the calendars:
**LV_EVENT_VALUE_CHANGED** ay değiştiğinde gönderilir.

In *Input device related* events, `lv_calendar_get_pressed_date(calendar)` tells which day is currently being pressed or return `NULL` if no date is pressed.

## Keys
Obje türü tarafından işlenilen *Keys* bulunmamaktadır.

[Keys](/overview/indev) hakkında daha fazlasını öğrenin.


## Örnek

```eval_rst

.. include:: /lv_examples/src/lv_ex_calendar/index.rst

```

## API

```eval_rst

.. doxygenfile:: lv_calendar.h
  :project: lvgl

```

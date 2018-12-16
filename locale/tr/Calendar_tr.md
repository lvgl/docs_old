_Written for v5.2_ (rev.4)

## Genel Bakış

The Calendar object is a classic calendar which can:
Takvim nesnesi klasik takvimdir: 

- Şuanki gün ve haftayı vurgular
- Herhangi kullanıcı tanımlı tarihleri vurgular
- Günün ismini gösterir
- Buton tıklaması ile önceki/sonraki aylara geçiş sağlar

Takvimde tarihleri almak ve ayarlamak, `yıl`, `ay` and `gün` alanlarına sahip bir yapı olan `lv_calendar_date_t` tür kullanılır.

**Mevcut tarihi** ayarlamak için `lv_calendar_set_today_date(calendar, &today_date)` fonksiyonu kullanılır.

Gösterilen **tarihi ayarlamak için** `lv_calendar_set_shown_date(calendar, &shown_date)` kullanın;

**Vurgulanan tarihlerin listesi** bir `lv_calendar_date_t`  dizisinde dizilmelidir ve bu diziyi geçerek `lv_calendar_set_hoghlighted_dates(calendar, &highlighted_dates)`'e geçilebilir.
 
Dizinin yalnızca statik veya global bir değişken olması için yalnızca diziler işaretçisi kaydedilir.

**Günlerin** adları, `lv_calendar_set_day_names(calendar, gun_isismleri)` ile ayarlanabilinir; burada `gun_isismleri`, `const char * gun_isismleri[7] = {"Pazar", "Pazartesi", ...};`

**Bir tarih seçmek için** eylem `v5.3`'te desteklenecek ve deneysel kullanım için şimdi `dev-5.3` dalında mevcut olacaktır.

## Biçim Kullanımı

- **LV_CALENDAR_STYLE_BG** `body` özelliklerini kullanarak arka planın biçimi ve `metin` özelliklerini kullanarak veri numaralarının biçimi.
- **LV_CALENDAR_STYLE_HEADER** Geçerli yıl ve ayın görüntülendiği başlığın biçimi. `body` ve `metin` özellikleri kullanılır.
- **LV_CALENDAR_STYLE_HEADER_PR** Preslenmiş başlık biçimi, sonraki / önceki ay düğmesine basılıyor. `metin` özellikleri oklar tarafından kullanılır.
- **LV_CALENDAR_STYLE_DAY_NAMES** Gün isimlerinin biçimi. `metin` özellikleri gün metinleri tarafından kullanılır ve `body.padding.ver` gün isimlerinin üzerindeki alanı belirler.
- **LV_CALENDAR_STYLE_HIGHLIGHTED_DAYS** `text` özellikleri, öne çıkan günlerin biçimini ayarlamak için kullanılır
- **LV_CALENDAR_STYLE_INACTIVE_DAYS** `text` özellikleri önceki / sonraki ayın görünen günlerinin biçimini ayarlamak için kullanılır.
- **LV_CALENDAR_STYLE_WEEK_BOX** `body` özellikleri, hafta kutusunun biçimini ayarlamak için kullanılır
- **LV_CALENDAR_STYLE_TODAY_BOX** Bugün kutusunun biçimini ayarlamak için `body` ve` text` özellikleri kullanılır

## Örnek

![Takvim resimi](http://docs.littlevgl.com/img/calendar-lv_calendar.png)

```c
/*Takvim nesnesi oluştur*/
lv_obj_t * calendar = lv_calendar_create(lv_scr_act(), NULL);
lv_obj_set_size(calendar, 240, 220);
lv_obj_align(calendar, NULL, LV_ALIGN_CENTER, 0, 0);

/*Geçerli hafta için biçim oluştur*/
static lv_style_t style_week_box;
lv_style_copy(&style_week_box, &lv_style_plain);
style_week_box.body.border.width = 1;
style_week_box.body.border.color = LV_COLOR_HEX3(0x333);
style_week_box.body.empty = 1;
style_week_box.body.radius = LV_RADIUS_CIRCLE;
style_week_box.body.padding.ver = 3;
style_week_box.body.padding.hor = 3;

/*Bugün için biçim oluştur*/
static lv_style_t style_today_box;
lv_style_copy(&style_today_box, &lv_style_plain);
style_today_box.body.border.width = 2;
style_today_box.body.border.color = LV_COLOR_NAVY;
style_today_box.body.empty = 1;
style_today_box.body.radius = LV_RADIUS_CIRCLE;
style_today_box.body.padding.ver = 3;
style_today_box.body.padding.hor = 3;
style_today_box.text.color= LV_COLOR_BLUE;

/*Vurgulanan günler için biçim oluştur*/
static lv_style_t style_highlighted_day;
lv_style_copy(&style_highlighted_day, &lv_style_plain);
style_highlighted_day.body.border.width = 2;
style_highlighted_day.body.border.color = LV_COLOR_NAVY;
style_highlighted_day.body.empty = 1;
style_highlighted_day.body.radius = LV_RADIUS_CIRCLE;
style_highlighted_day.body.padding.ver = 3;
style_highlighted_day.body.padding.hor = 3;
style_highlighted_day.text.color= LV_COLOR_BLUE;

/*Biçimleri uygula*/
lv_calendar_set_style(calendar, LV_CALENDAR_STYLE_WEEK_BOX, &style_week_box);
lv_calendar_set_style(calendar, LV_CALENDAR_STYLE_TODAY_BOX, &style_today_box);
lv_calendar_set_style(calendar, LV_CALENDAR_STYLE_HIGHLIGHTED_DAYS, &style_highlighted_day);


/*Bugün'ü ayarla*/
lv_calendar_date_t today;
today.year = 2018;
today.month = 10;
today.day = 23;

lv_calendar_set_today_date(calendar, &today);
lv_calendar_set_showed_date(calendar, &today);

/*Vurgulanan bazı günler*/
static lv_calendar_date_t highlihted_days[3];       /*Sadece işaretçi kaydedilecek, bu yüzden statik olmalı*/
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

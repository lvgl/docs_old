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

Takvimde tarihleri ayarlama ve alma `year`, `month` ve`day` alanlarını içeren yapı olan `lv_calendar_date_t` türü kullanılır.

### Şuan ki tarih
Şuan ki tarihi(bugün) ayarlamak için  `lv_calendar_set_today_date(calendar, &today_date)` fonksiyonunu kullan.

### Gösterilen tarih
Gösterilen tarihi ayarlamak için `lv_calendar_set_shown_date(calendar, &shown_date)` kullan;

### Vurgulanan günler
Vurgulanan tarih listesi `lv_calendar_date_t` fonksiyonu içinde saklanır ve vurgulanan liste `lv_calendar_set_highlighted_dates(calendar, &highlighted_dates)` fonksiyonu ile takvime yüklenir.
Sadece dizi(liste) göstergeci kaydedileceği için tanımlanmış dizi(liste) statik veya global(evrensel) değişken olmalıdır.

### Gün İsimleri
Gün isimleri `lv_calendar_set_day_names(calendar, day_names)` ile ayarlanabilir, `day_names`  şuna benziyorsa `const char * day_names[7] = {"Su", "Mo", ...};`

### Ay İsimleri
Gün isimlerine benzer şekilde ay isimleri de `lv_calendar_set_month_names(calendar, month_names_array)` ile ayarlanabilir.

## Biçim
Biçimi `lv_calendar_set_style(btn, LV_CALENDAR_STYLE_..., &style)` ile ayarlayabilirsiniz. 

- **LV_CALENDAR_STYLE_BG** `body` özelliklerini kullanan arka plan biçimi ve `text` özelliklerini kullanan tarih numara biçimi. `body.padding.left/rigth/bottom` dolgular tarih  numaraları etrafındaki kenarlar eklenecektir. 
- **LV_CALENDAR_STYLE_HEADER** geçerli yıl ve ay gösterildiğinde ki başlık biçimi. `body` ve `text` özellikleri kullanılır.
- **LV_CALENDAR_STYLE_HEADER_PR** basılı başlık biçimi, used when the önceki/sonraki. ay butonu basılı olduğunda kullanılır. text` özellikleri ok tarafından kullanılır.
- **LV_CALENDAR_STYLE_DAY_NAMES** gün isim biçimi. `text` özellikleri metin tarafından kullanılır ve `body.padding.top` gün isimleri üzerindeki boşluğu belirler.
- **LV_CALENDAR_STYLE_HIGHLIGHTED_DAYS** `text` özellikleri vurgulu günlerin biçimini  ayarlamak için kullanılır
- **LV_CALENDAR_STYLE_INACTIVE_DAYS** `text` özellikleri önceki/sonraki ayın görülen gününün biçimini ayarlamak için kullanılır .
- **LV_CALENDAR_STYLE_WEEK_BOX** `body` özellikleri haftakutucuğunu biçimini ayarlamak için kullanılır
- **LV_CALENDAR_STYLE_TODAY_BOX** `body` and `text` özellikleri gün kutucuğunu biçimini ayarlamak için kullanılır

Aksiyonlar
[Generic events](/overview/event.html#generic-events) dışında [Special events](/overview/event.html#special-events) da  takvim tarafından gönderilir
**LV_EVENT_VALUE_CHANGED** ay değiştiğinde gönderilir.

*Giriş cihazı ile alakalı * aksiyonlarda  `lv_calendar_get_pressed_date(calendar)`  hangi günün şu an basılı olduğunu bildirir veya hiç bir tarih basılı olmasa `NULL` döndürür.

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

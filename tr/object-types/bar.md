```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/tr/object-types/bar.md
```
# Bar (lv_bar)

## Giriş

Bar nesnesi iki ana parçaya sahiptir: 
1. Nesnenin kendi **arka planı**
2. Şekli arka planla aynı olan fakat genişliği/yüksekliği ayarlanabilen bir **gösterge** . 

Barın yönü genişlik/yüksek oranına göre dikey veya yatay olarak ayarlanabilir. Mantıken yatay barlarda göstergenin genişliği, dikey barlarda göstergenin yüksekliği değiştirilebilir.

### Değer ve aralık
Yeni değer `lv_bar_set_value(bar, new_value, LV_ANIM_ON/OFF)`vasıtasıyla ayarlanabilir. 
Bu değer `lv_bar_set_range(bar, min, max)` ile değiştirilen bir aralıkta(minimum ve maksimum değerlerde) değerlendirilir.  
Varsayılan aralık 1..100.

`lv_bar_set_value` deki yeni değer   (`LV_ANIM_ON/OFF`) deki son parametreye bağlı olarak animasyonsuz olarak ayarlanabilir  .  
Animasyon süresi `lv_bar_set_anim_time(bar, 100)` yoluyla ayarlanabilir . Süre birimi milisaniyedir.

### Simetrik
`lv_bar_set_sym(bar, true)` eğer aktif ise, bar sıfıra simetrik çizilebilir(sıfıra soldan sağa çizilmiş) 

## Biçimler

Bir *Bar* nesnesinin biçimi ayarlamak için `lv_bar_set_style(arc, LV_BAR_STYLE_MAIN, &style)` kullanılır

- **LV_BAR_STYLE_BG**  bir [Base object](/object-types/obj) dir. Bu yüzden kendi biçim  unsurları ile kullanılır. it uses its style elements. Its default style is: `lv_style_pretty`. 
- **LV_BAR_STYLE_INDIC** arka plana benzer. *Sol*, *sağ*, *üst* ve *alt* dolgularını arka planın kenarlarından biraz boşluk kalmasını sağlamak için kullanılır. Varsayılan biçim: `lv_style_pretty_color`.

## Olaylar
Nesne türü tarafından sadece [Generic events](/overview/event.html#generic-events) gönderilir.

Learn more about [Events](/overview/event).

## Keys
Nesne türü tarafından işlenecek *Keys*  yoktur.

[Keys](/overview/indev) hakkında fazlasını öğrenin.

## Örnek

```eval_rst

.. include:: /lv_examples/src/lv_ex_bar/index.rst

```

## API 

```eval_rst

.. doxygenfile:: lv_bar.h
  :project: lvgl
        
```

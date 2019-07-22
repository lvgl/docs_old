```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/tr/overview/animation.md
```
# Animasyon

Animasyon yardımıyla bir değişkenin değerini başlangıç ve bitiş değerleri arasında otomatik değiştirebilirsiniz.
Animasyon "animatör" fonksiyonunun ilişkili parametre değerleriyle peryodik çağrılmasıyla gerçekleşir.

*animator* fonksiyonları aşağıdaki prototipe sahiptir:
```c
void func(void * var, lv_anim_var_t value);
```
Bu prototip fonksiyonu, LittlevGL'nin *set* fonksiyonlarının çoğuyla uyumludur. Örneğin `lv_obj_set_x(obj, value)` veya `lv_obj_set_width(obj, value)`.


##  Animasyon Oluşturma
Animasyon oluşturmak için, `lv_anim_t`değişkeni ilklendirilmek zorundadır ve `lv_anim_set_...()` fonksiyonlarıyla ayarlanabilir.

```c
lv_anim_t a;
lv_anim_set_exec_cb(&a, btn1, lv_obj_set_x);    /*animatör fonksiyonunu ve animasyonun gerçekleştirileceği değişkeni ayarla*/ 
lv_anim_set_time(&a, duration, delay);
lv_anim_set_values(&a, start, end);             /*Başlangıç ve bitiş değerlerini ayarla. Ör. 0, 150*/
lv_anim_set_path_cb(&a, lv_anim_path_linear);   /*`lv_anim_path_...` fonksiyonlardan animasyon davranışını ayarla.*/
lv_anim_set_ready_cb(&a, ready_cb);             /*Animasyon tamamlandığında çağrılacak fonksiyonu ayarla. (Seçeneksel)*/
lv_anim_set_playback(&a, wait_time);            /*`wait_time` gecikmesiyle animasyon playback aktive et*/
lv_anim_set_repeat(&a, wait_time);              /*`wait_time` gecikmeyle animasyon tekrarını aktive et. Playback ile derlenebilir*/

lv_anim_create(&a);                             /*Animasyonu başlat*/
```


Aynı zamanda aynı değişken üzerinde **çoklu farklı animasyonlar** uygulanabilir.
Örneğin  `lv_obj_set_x` ve `lv_obj_set_y` ile x ve y koordinatlarını animate eder. Fakat, verilen bir değişken ve fonksiyon çiftile yalnız bir animasyon ilişkilendirilir.
Bu yüzden `lv_anim_create()` zaten var olan değişken-fonksiyon animasyonlarını silecek. 

##  Animasyon davranılı

**Animasyon şeklini** belirleyebilirsiniz. En basit durumda, doğrusaldır, yani * start * ve * end * arasındaki geçerli değer doğrusal olarak değiştirilir.
*Path/yol/şekil*, animasyonun o andaki durumuna göre ayarlanacak bir sonraki değeri hesaplayan bir fonksiyondur. Şu anda, aşağıdaki yerleşik yollar/şekiller vardır:

- **lv_anim_path_linear** doğrusal animasyon
- **lv_anim_path_step** son duruma bir adımda geç
- **lv_anim_path_ease_in** başlangıçta yavaş
- **lv_anim_path_ease_out** sonda yavaş
- **lv_anim_path_ease_in_out** başta ve sonda yavaş
- **lv_anim_path_overshoot** son değeri aşsın
- **lv_anim_path_bounce** son değerden biraz geri zıplar (duvara vurma davranışı gibi)


## Hız mı süre mi
Varsayılan olarak, animasyon zamanını ayarlayabilirsiniz. Ancak bazı durumlarda, **animasyon hızı** daha pratiktir.

`lv_anim_speed_to_time(speed, start, end)` işlevi, verilen hız ile bir başlangıç değerinden bitiş değerine ulaşmak için gereken süreyi milisaniye cinsinden hesaplar.
Hız, _unit/sec_ boyutunda yorumlanır. Örneğin, `lv_anim_speed_to_time(20,0,100)`, 5000 milisaniye verir. Örneğin `lv_obj_set_x` durumunda, *unit* pikseldir. Bu yüzden *20*, *20 pixel/saniye* hız anlamına gelir.

## Animasyonu sil

`lv_anim_del(var, func)` yardımıyla **animasyon silinebilir**. Parametre olarak animasyon değişkeni ve animatör işlevi bekler.

## API

### Giriş aygıtı

```eval_rst

.. doxygenfile:: lv_anim.h
  :project: lvgl
                

```


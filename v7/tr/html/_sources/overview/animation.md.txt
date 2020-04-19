```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/tr/overview/animation.md
```
# Animasyon

You can automatically change the value of a variable between a start and an end value using animations.
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
lv_anim_set_exec_cb(&a, btn1, lv_obj_set_x);    /*Set the animator function and variable to animate*/
lv_anim_set_time(&a, duration, delay);
lv_anim_set_values(&a, start, end);             /*Başlangıç ve bitiş değerlerini ayarla. Ör. 0, 150*/
lv_anim_set_path_cb(&a, lv_anim_path_linear);   /*`lv_anim_path_...` fonksiyonlardan animasyon davranışını ayarla.*/
lv_anim_set_ready_cb(&a, ready_cb);             /*Animasyon tamamlandığında çağrılacak fonksiyonu ayarla. (Seçeneksel)*/
lv_anim_set_playback(&a, wait_time);            /*`wait_time` gecikmesiyle animasyon playback aktive et*/
lv_anim_set_repeat(&a, wait_time);              /*`wait_time` gecikmeyle animasyon tekrarını aktive et. Playback ile derlenebilir*/

lv_anim_create(&a);                             /*Animasyonu başlat*/
```


You can apply **multiple different animations** on the same variable at the same time.
For example, animate the x and y coordinates with `lv_obj_set_x` and `lv_obj_set_y`. However, only one animation can exist with a given variable and function pair.
Therefore `lv_anim_create()` will delete the already existing variable-function animations.

##  Animasyon davranılı

You can determinate the **path of animation**. In the most simple case, it is linear, which means the current value between *start* and *end*  is changed linearly.
A *path* is a function which calculates the next value to set based on the current state of the animation. Currently, there are the following built-in paths:

- **lv_anim_path_linear** doğrusal animasyon
- **lv_anim_path_step** son duruma bir adımda geç
- **lv_anim_path_ease_in** başlangıçta yavaş
- **lv_anim_path_ease_out** sonda yavaş
- **lv_anim_path_ease_in_out** başta ve sonda yavaş
- **lv_anim_path_overshoot** son değeri aşsın
- **lv_anim_path_bounce** bounce back a little from the end value (like hitting a wall)


## Hız mı süre mi
By default, you can set the animation time. But, in some cases, the **animation speed** is more practical.

The `lv_anim_speed_to_time(speed, start, end)` function calculates the required time in milliseconds to reach the end value from a start value with the given speed.
The speed is interpreted in _unit/sec_ dimension. For example,  `lv_anim_speed_to_time(20,0,100)` will give 5000 milliseconds. For example, in case of `lv_obj_set_x` *unit* is pixels so *20* means *20 px/sec* speed.

## Animasyonu sil

`lv_anim_del(var, func)` yardımıyla **animasyon silinebilir**. Parametre olarak animasyon değişkeni ve animatör işlevi bekler.

## API

### Giriş aygıtı

```eval_rst

.. doxygenfile:: lv_anim.h
  :project: lvgl

```

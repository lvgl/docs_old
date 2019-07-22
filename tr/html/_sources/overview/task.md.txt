```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/tr/overview/task.md
```
# Görevler

LittlevGL dahili  görev sistemine sahiptir. Periyodik olarak çağırmak için bir fonksiyon kaydedebilirsiniz. Birkaç saniyede çağrılması gereken bu görevler görevler `lv_task_handler()` ile çağrılır ve işlenir.
Daha fazla bilgi için [Porting](/porting/task-handler) bakınız.

Görevler non-preemptive dir yani bir görev diğerini kesebilir. Bu yüzden görevin içinde herhangi bir LittlevGL fonksiyonunu çağırabilirsiniz.


## Bir görev oluştur
`lv_task_create(task_cb, period_ms, LV_TASK_PRIO_OFF/LOWEST/LOW/MID/HIGH/HIGHEST, user_data)` yeni bir görev oluşturmak için kullanılır. Görevin parametrelerini değiştirmek için sonradan kullanılabilen bir `lv_task_t *` değişkeni oluşturacak.
Ayrıca `lv_task_create_basic()` herhangi bir parametre belirtmeksizin yeni ir görev oluşturmak içinde kullanılabilir.

Bşir görev geri çağırması `void (*lv_task_cb_t)(lv_task_t *);` prototipine sahip olmalı.

Örneğin:
```c
void my_task(lv_task_t * task)
{
  /*Kullanıcı verisini kullan*/
  uint32_t * user_data = task->user_data;
  printf("my_task called with user data: %d\n", *user_data);
  
  /*i LittlevGL ile birşeyler yap*/
  if(something_happened) {
    something_happened = false;
    lv_btn_create(lv_scr_act(), NULL);
  }
}

...

static uint32_t user_data = 10;
lv_task_t * task = lv_task_create(my_task, 500, LV_TASK_PRIO_MID, &user_data);

```

## Hazır ve Reset

`lv_task_ready(task)` görevin `lv_task_handler()` 'ın bir sonraki çağrısında çalışmasını sağlar.

`lv_task_reset(task)` bir görevin periyotunu resetler. Belirlenen milisaniye periyotu süresi sonrasında çağrılır.göre


## Parametreleri ayarlama
Görevlerin bazı parametreleri daha sora değiştirebilirsiniz:
- `lv_task_set_cb(task, new_cb)`
- `lv_task_set_period(task, new_period)`
- `lv_task_set_prio(task, new_priority)`

## Tek seferlik görevler

`lv_task_once(task)`çağırarak bir kez çalışacak bir görev yapabilirsiniz. Bu görev ilk çağırmadan sonra otomatik olarak silinecektir.


## Boş zaman ölçme

`lv_task_get_idle()` ile `lv_task_handler`'ın boş zaman yüzdesini elde edebilirsiniz. Tüm sistemin boş zaman süresini değil, sadece`lv_task_handler`'ın ölçtüğünü unutmayınız. 
Eğer bir işletim sistemi kullanıyorsunuz bir görevde `lv_task_handler`'ı çağırırsanız,yanıltıcı olabilir.

## Eş zamanlı olmayan çağırmalar

Bazı durumlarda, hızlıca bir aksiyon yapamazsınız. Örneğin, bir nesneyi şuan silemezsin çünkü bir şey onu hala kullanılıyor veya yürütmeyi şuan kapatmak istemezsin.
Bazı durumlar için, `lv_task_handler' 'ın bir sonraki çağrısında `my_function` çağrılması için `lv_async_call(my_function, data_p)` kullanılabilir. `data_p` çağrıldığında fonksiyona geçecek. 
Note that, only the pointer of the data is saved so you need to ensure that the variable will be "alive" while the function is called. Global veya dinamik olarak ayrılmış veri, *static* kullanılabilir.

Örneğin:
```c
void my_screen_clean_up(void * scr)
{
  /*`scr` ile ilgili bazı kaynakları serbest bırakın*/
  
  /*En sonunda ekranı sil*/
  lv_obj_del(scr);  
}

...

/*Güncel ekrandaki nesne ile bir şeyler yap*/

/*Bir sonraki `lv_task_handler` çağırmasında ekranı sil. Yani şimdi değil.*/
lv_async_call(my_screen_clean_up, lv_scr_act());

/*Ekran hala geçerlidir, bu yüzden onunla başka şeyler yapabilirsiniz*/

```


## API 

```eval_rst

.. doxygenfile:: lv_task.h
  :project: lvgl
        
```

```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/tr/overview/task.md
```
# Görevler

LittlevGL has a built-in task system. You can register a function to have it be called periodically. The tasks are handled and called in `lv_task_handler()`, which needs to be called periodically every few milliseconds.
Daha fazla bilgi için [Porting](/porting/task-handler) bakınız.

The tasks are non-preemptive, which means a task cannot interrupt another task. Therefore, you can call any LittlevGL related function in a task.


## Bir görev oluştur
To create a new task, use `lv_task_create(task_cb, period_ms, LV_TASK_PRIO_OFF/LOWEST/LOW/MID/HIGH/HIGHEST, user_data)`. It will create an `lv_task_t *` variable, which can be used later to modify the parameters of the task.
`lv_task_create_basic()` can also be used. It allows you to create a new task without specifying any parameters.

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

`lv_task_reset(task)` resets the period of a task. It will be called again after the defined period of milliseconds has elapsed.


## Parametreleri ayarlama
Görevlerin bazı parametreleri daha sora değiştirebilirsiniz:
- `lv_task_set_cb(task, new_cb)`
- `lv_task_set_period(task, new_period)`
- `lv_task_set_prio(task, new_priority)`

## Tek seferlik görevler

You can make a task to run only once by calling`lv_task_once(task)`. The task will automatically be deleted after being called for the first time.


## Boş zaman ölçme

You can get the idle percentage time `lv_task_handler` with `lv_task_get_idle()`. Note that, it doesn't measure the idle time of the overall system, only `lv_task_handler`.
It can be misleading if you use an operating system and call `lv_task_handler` in an  task, as it won't actually measure the time the OS spends in an idle thread.

## Eş zamanlı olmayan çağırmalar

In some cases, you can't do an action immediately. For example, you can't delete an object right now because something else is still using it or you don't want to block the execution now.
For these cases, you can use the `lv_async_call(my_function, data_p)` to make `my_function` be called on the next call of `lv_task_handler`. `data_p` will be passed to function when it's called.
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

If you just want to delete an object, and don't need to clean anything up in `my_screen_cleanup`, you could just use `lv_obj_del_async`, which will delete the object on the next call to `lv_task_handler`.

## API

```eval_rst

.. doxygenfile:: lv_task.h
  :project: lvgl

```

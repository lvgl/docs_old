```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/fr/porting/tick.md
```
# Interface tic

The LittlevGL needs a system tick to know the elapsed time for animation and other tasks.

You need to call the `lv_tick_inc(tick_period)` function periodically and tell the call period in milliseconds. For example, `lv_tick_inc(1)` for calling in every millisecond.

`lv_tick_inc` should be called in a higher priority routine than `lv_task_handler()` (e.g. in an interrupt) to precisely know the elapsed milliseconds even if the execution of `lv_task_handler` takes longer time.

Sur FreeRTOS, `lv_tick_inc` peut être appelée dans `vApplicationTickHook`.

On Linux based operating system (e.g. on Raspberry Pi) `lv_tick_inc` can be called in a thread as below:
```c
void * tick_thread (void *args)
{
      while(1) {
        usleep(5*1000);   /* Dors pendant 5 millisecondes */
        lv_tick_inc(5);      /* Indique à LittlevGL que 5 millisecondes se sont écoulées */
    }
}
```



## API

```eval_rst

.. doxygenfile:: lv_hal_tick.h
  :project: lvgl

```

```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/zh-CN/porting/tick.md
```
# Tick interface

The LittlevGL needs a system tick to know the elapsed time for animation and other task. 

You need to call the `lv_tick_inc(tick_period)` function periodically and tell the call period in milliseconds. For example, if called in every millisecond: `lv_tick_inc(1)`. 

`lv_tick_inc` should be called in a higher priority routine than` lv_task_handler()` (e.g. in an interrupt) to precisely know the elapsed milliseconds even if the execution of `lv_task_handler` takes longer time.

With FreeRTOS `lv_tick_inc` can be called in `vApplicationTickHook`.

On Linux based operation system (e.g. on Raspberry) `lv_tick_inc` can be called in a thread:
```c
void * tick_thread (void *args)
{
      while(1) {
        usleep(5*1000);   /*Sleep for 5 millisecond*/
        lv_tick_inc(5);      /*Tell LittlevGL that 5 milliseconds were elapsed*/
    } 
}
``` 



## API 

```eval_rst

.. doxygenfile:: lv_hal_tick.h
  :project: lvgl
        
```

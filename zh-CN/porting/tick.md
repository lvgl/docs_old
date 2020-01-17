```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/zh-CN/porting/tick.md
```
# Tick interface

LittlevGL 需要一个系统嘀嗒 (tick) 来了解动画和其他任务的运行时间。

您需要定期调用 ' lv_tick_inc(tick_period) ' 函数，并以毫秒为单位告知调用周期。例如，' lv_tick_inc(1) ' 是每毫秒调用一次。

' lv_tick_inc ' 应该在一个比 `lv_task_handler()` 更高优先级的例程中调用(例如在一个中断中)，以精确地知道经过的毫秒数，即使 ' lv_task_handler ' 的执行需要更长的时间。

在 FreeRTOS 中 ' lv_tick_inc ' 可以在 ' vApplicationTickHook ' 中调用。

基于 Linux 的操作系统 (例如在Raspberry Pi上) 可以在线程中调用 ' lv_tick_inc '，如下所示:
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

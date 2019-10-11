```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/fr/porting/os.md
```
# Système d'exploitation et interruptions

LittlevGL is **not thread-safe** by default.

However, in the following conditions it's valid to call LittlevGL related functions:
- Dans les *événements*. Apprenez-en plus dans [Evénements](/overview/event).
- Dans *lv_tasks*.  Apprenez-en plus dans [Tâches](/overview/task).


## Tâches et fils d’exécution
If you need to use real tasks or threads, you need a mutex which should be invoked before the call of `lv_task_handler` and released after it.
Also, you have to use the same mutex in other tasks and threads around every LittlevGL (`lv_...`) related function calls and codes.
This way you can use LittlevGL in a real multitasking environment. Just make use of a mutex to avoid the concurrent calling of LittlevGL functions.

## Interruptions
Try to avoid calling LittlevGL functions from the interrupts (except `lv_tick_inc()` and `lv_disp_flush_ready()`). But, if you need to do this you have to disable the interrupt which uses LittlevGL functions while `lv_task_handler` is running.
It's a better approach to set a flag or some value and periodically check it in an `lv_task`.

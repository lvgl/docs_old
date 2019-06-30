# Use with an operating system

LittlevGL is **not thread-safe** by default. Despite it, it's quite simple to use LittlevGL inside an operating system. 

The **simple scenario** is to don't use the operating system's tasks but use `lv_task`s. An *lv_task* is a function called periodically in `lv_task_handler`. 
In the *lv_task* you can get the state of the sensors, buffers, etc and call LittlevGL functions to refresh the GUI. 

To create an *lv_task* use: 
```c
lv_task_create(my_func, period_ms, LV_TASK_PRIO_LOWEST/LOW/MID/HIGH/HIGHEST, custom_ptr)
```

If you need to **use real tasks or threads** you need one mutex which should be taken before the call of `lv_task_handler` and released after it. 
In addition, you have to use to that mutex in other tasks and threads around every LittlevGL (`lv_...`) related function call and code. 
This way you can use LittlevGL in a real multitasking environment. Just use a mutex to avoid the concurrent calling of LittlevGL functions.

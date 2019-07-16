```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/en/overview/task.md
```
# Tasks

LittlevGL has a built-in task system. You can register a functions to call them periodically. The tasks are handled and called in `lv_task_handler()` which needs to be called periodically in every few milliseconds. 
See [Porting](/porting/task-handler) for more information.

The tasks are non-preemptive which means a task can interrupt an other. Therefore you can call any LittlevGL related function in a task.


## Create a task
To create a new task use `lv_task_create(task_cb, period_ms, LV_TASK_PRIO_OFF/LOWEST/LOW/MID/HIGH/HIGHEST, user_data)`. It will create an `lv_task_t *` variable which can be used later to modify the parameters of the task.
`lv_task_create_basic()` also can be used to create a new task without specifying any parameters.

A task callback should have `void (*lv_task_cb_t)(lv_task_t *);` prototype.

For example:
```c
void my_task(lv_task_t * task)
{
  /*Use the user_data*/
  uint32_t * user_data = task->user_data;
  printf("my_task called with user data: %d\n", *user_data);
  
  /*Do something with LittlevGL*/
  if(something_happened) {
    something_happened = false;
    lv_btn_create(lv_scr_act(), NULL);
  }
}

...

static uint32_t user_data = 10;
lv_task_t * task = lv_task_create(my_task, 500, LV_TASK_PRIO_MID, &user_data);

```

## Ready and Reset

`lv_task_ready(task)` makes the task run on the next call of `lv_task_handler()`.

`lv_task_reset(task)` resets the period of a task. It will be called the defined period milliseconds later.


## Set parameters
You can modify some parameters of the tasks later:
- `lv_task_set_cb(task, new_cb)`
- `lv_task_set_period(task, new_period)`
- `lv_task_set_prio(task, new_priority)`

## One-shot tasks

You can make a task to run only once by calling`lv_task_once(task)`. The task will be automatically deleted when called for the first time.


## Measure idle time

You can get the idle percentage time `lv_task_handler` with `lv_task_get_idle()`. Note that, it doesn't measure the idle time of the overall system, only `lv_task_handler`. 
It might be misleading if you use an operating system and call `lv_task_handler` in a task.

## Asynchronous calls

In some cases, you can't do an action immediately. For example, you can't delete an object right now because something else still uses it or you don't want to block the execution now. 
For these cases, you can use the `lv_async_call(my_function, data_p)` to make `my_function` to be called on the next call of `lv_task_handler`. `data_p` will be passed to function when it's called. 
Note that, only the pointer of the data is saved so you need to ensure that the variable will be "alive" while the function is called. You can use *static*, global or dynamically allocated data.

For example:
```c
void my_screen_clean_up(void * scr)
{
  /*Free some resources related to `scr`*/
  
  /*Finally delete the screen*/
  lv_obj_del(scr);  
}

...

/*Do somethings with the object on the current screen*/

/*Delete screen on next call of `lv_task_handler`. So not now.*/
lv_async_call(my_screen_clean_up, lv_scr_act());

/*The screen is still valid so you can do other things with it*/

```


## API 

```eval_rst

.. doxygenfile:: lv_task.h
  :project: lvgl
        
```

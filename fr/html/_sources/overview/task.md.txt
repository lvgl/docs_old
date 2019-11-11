```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/fr/overview/task.md
```
# Tâches

LittlevGL has a built-in task system. You can register a function to have it be called periodically. The tasks are handled and called in `lv_task_handler()`, which needs to be called periodically every few milliseconds.
Voir [Portage](/porting/task-handler) pour plus d'informations.

The tasks are non-preemptive, which means a task cannot interrupt another task. Therefore, you can call any LittlevGL related function in a task.


## Créer une tâche
To create a new task, use `lv_task_create(task_cb, period_ms, LV_TASK_PRIO_OFF/LOWEST/LOW/MID/HIGH/HIGHEST, user_data)`. It will create an `lv_task_t *` variable, which can be used later to modify the parameters of the task.
`lv_task_create_basic()` can also be used. It allows you to create a new task without specifying any parameters.

La fonction de rappel d'une tâche doit avoir la signature `void (* lv_task_cb_t)(lv_task_t *)`.

Par exemple :
```c
void my_task(lv_task_t * task)
{
  /* Utilise les données de l'utilisateur */
  uint32_t * user_data = task->user_data;
  printf("my_task called with user data: %d\n", *user_data);

  /* Fait quelque chose avec LittlevGL */
  if(something_happened) {
    something_happened = false;
    lv_btn_create(lv_scr_act(), NULL);
  }
}

...

static uint32_t user_data = 10;
lv_task_t * task = lv_task_create(my_task, 500, LV_TASK_PRIO_MID, &user_data);

```

## Exécution et réinitialisation

`lv_task_ready(task)` fait exécuter la tâche lors du prochain appel de `lv_task_handler()`.

`lv_task_reset(task)` resets the period of a task. It will be called again after the defined period of milliseconds has elapsed.


## Paramètres
Vous pouvez modifier ultérieurement certains paramètres des tâches :
- `lv_task_set_cb(task, new_cb)`
- `lv_task_set_period(task, new_period)`
- `lv_task_set_prio(task, new_priority)`

## Tâches uniques

You can make a task to run only once by calling`lv_task_once(task)`. The task will automatically be deleted after being called for the first time.


## Mesurer le temps d'inactivité

You can get the idle percentage time `lv_task_handler` with `lv_task_get_idle()`. Note that, it doesn't measure the idle time of the overall system, only `lv_task_handler`.
It can be misleading if you use an operating system and call `lv_task_handler` in an  task, as it won't actually measure the time the OS spends in an idle thread.

## Appels asynchrones

In some cases, you can't do an action immediately. For example, you can't delete an object right now because something else is still using it or you don't want to block the execution now.
For these cases, you can use the `lv_async_call(my_function, data_p)` to make `my_function` be called on the next call of `lv_task_handler`. `data_p` will be passed to function when it's called.
Notez que seul le pointeur des données est enregistré. Vous devez donc vous assurer que la variable sera "à portée" lors de l'appel de la fonction. Pour cela, vous pouvez utiliser des données *statiques*, globales ou allouées dynamiquement.

Par exemple :
```c
void my_screen_clean_up(void * scr)
{
  /* Libére des ressources liées à `scr` */

  /* Au final supprime l'écran */
  lv_obj_del(scr);  
}

...

/* Fait quelque chose avec l'objet sur l'écran courant */

/* Supprime l'écran lors du prochain appel de `lv_task_handler`. Donc pas maintenant. */
lv_async_call(my_screen_clean_up, lv_scr_act());

/* L'écran est toujours valide donc vous pouvez faire d'autres choses avec */

```

If you just want to delete an object, and don't need to clean anything up in `my_screen_cleanup`, you could just use `lv_obj_del_async`, which will delete the object on the next call to `lv_task_handler`.

## API

```eval_rst

.. doxygenfile:: lv_task.h
  :project: lvgl

```

```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/fr/overview/task.md
```
# Tâches

LittlevGL a un système intégré de tâches. Vous pouvez enregistrer une fonction pour l'appeler périodiquement. Les tâches sont gérées et appelées dans `lv_task_handler()`, qui doit être appelée périodiquement toutes les quelques millisecondes.
Voir [Portage](/porting/task-handler) pour plus d'informations.

Les tâches sont non-préemptives, ce qui signifie qu'une tâche ne peut en interrompre une autre. Par conséquent, vous pouvez appeler n’importe quelle fonction liée à LittlevGL dans une tâche.


## Créer une tâche
Pour créer une nouvelle tâche, utilisez `lv_task_create(task_cb, period_ms, LV_TASK_PRIO_OFF/LOWEST/LOW/MID/HIGH/HIGHEST, user_data)`. Une variable `lv_task_t *` est créée qui peut être utilisée ultérieurement pour modifier les paramètres de la tâche.
`lv_task_create_basic ()` peut également être utilisée pour créer une nouvelle tâche sans spécifier de paramètre.

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

`lv_task_reset(task)` réinitialise la période d'une tâche. La tâche sera appelée après un délai égal à la période définie.


## Paramètres
Vous pouvez modifier ultérieurement certains paramètres des tâches :
- `lv_task_set_cb(task, new_cb)`
- `lv_task_set_period(task, new_period)`
- `lv_task_set_prio(task, new_priority)`

## Tâches uniques

Vous pouvez faire en sorte qu'une tâche ne soit exécutée qu'une seule fois en appelant `lv_task_once(task)`. La tâche sera automatiquement supprimée lors du premier appel.


## Mesurer le temps d'inactivité

Vous pouvez obtenir le pourcentage de temps d'inactivité de `lv_task_handler` avec` lv_task_get_idle()`. Notez que cela ne mesure pas le temps d'inactivité de l'ensemble du système, mais seulement de `lv_task_handler`.
Cela peut être trompeur si vous utilisez un système d'exploitation et appelez `lv_task_handler` dans une tâche.

## Appels asynchrones

Dans certains cas, vous ne pouvez pas faire une action immédiatement. Par exemple, vous ne pouvez pas supprimer un objet pour le moment, car quelque chose d'autre l'utilise encore ou vous ne voulez pas bloquer l'exécution maintenant.
Dans ces cas, vous pouvez utiliser `lv_async_call(my_function, data_p)` pour que `ma_fonction` soit appelée lors du prochain appel de `lv_task_handler`. `data_p` sera passé à fonction lorsqu'elle sera appelée.
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


## API 

```eval_rst

.. doxygenfile:: lv_task.h
  :project: lvgl
        
```

```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/fr/porting/tick.md
```
# Interface tic

LittlevGL a besoin d'un tic système pour connaître le temps écoulé pour l'animation et d'autres tâches.

Vous devez appeler la fonction `lv_tick_inc(tick_period)` périodiquement et indiquer la période d'appel en millisecondes. Par exemple, si elle est appelée chaque milliseconde : `lv_tick_inc(1)`.

`lv_tick_inc` doit être appelée dans une routine de priorité supérieure à `lv_task_handler()` (par exemple, dans une interruption) pour connaître avec précision les millisecondes écoulées, même si l'exécution de `lv_task_handler` prend plus de temps.

Sur FreeRTOS, `lv_tick_inc` peut être appelée dans `vApplicationTickHook`.

Sur les systèmes d'exploitation basés sur Linux (par exemple, sur Raspberry), `lv_tick_inc` peut être appelée dans un fil d'exécution :
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

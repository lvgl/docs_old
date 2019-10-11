```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/fr/porting/sleep.md
```
# Gestion du sommeil

The MCU can go to sleep when no user input happens. In this case, the main `while(1)` should look like this:

```c
while(1) {
  /*Normal operation (no sleep) in < 1 sec inactivity*/
  if(lv_disp_get_inactive_time(NULL) < 1000) {
	  lv_task_handler();
  }
  /* Sommeil après une seconde d'inactivité */
  else {
	  timer_stop();   /* Arrêt de l'horloge où lv_tick_inc() est appelée */
	  sleep();		    /* Place le microcontrôleur en sommeil */
  }
  my_delay_ms(5);
}
```

You should also add below lines to your input device read function if a wake-up (press, touch or click etc.) happens:
```c
lv_tick_inc(LV_DISP_DEF_REFR_PERIOD);  /* Force l'exécution de la tâche au réveil */
timer_start();                         /* Redémarre l'horloge où lv_tick_inc() est appelée */
lv_task_handler();                     /*Call `lv_task_handler()` manually to process the wake-up event*/
```

En plus de `lv_disp_get_inactive_time()`, vous pouvez vérifier `lv_anim_count_running()` pour voir si toutes les animations sont terminées.

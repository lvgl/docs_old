```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/fr/porting/sleep.md
```
# Gestion du sommeil

Le microcontrôleur peut s'endormir lorsque aucune intervention de l'utilisateur n'est effectuée. Dans ce cas, la boucle principale `while (1)` devrait ressembler à ceci :

```c
while(1) {
  /* Fonctionnement normal (pas de sommeil) si moins de 1 seconde d'inactivité */ 
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

Vous devez également ajouter ces lignes à la fonction de lecture de votre périphérique d’entrée si un appui est effectué :
```c
lv_tick_inc(LV_DISP_DEF_REFR_PERIOD);  /* Force l'exécution de la tâche au réveil */
timer_start();                         /* Redémarre l'horloge où lv_tick_inc() est appelée */
lv_task_handler();                     /* Appelle `lv_task_handler()` manuellement pour traiter le réveil */
```

En plus de `lv_disp_get_inactive_time()`, vous pouvez vérifier `lv_anim_count_running()` pour voir si toutes les animations sont terminées.

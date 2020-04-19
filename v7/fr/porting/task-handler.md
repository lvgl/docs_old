```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/fr/porting/task-handler.md
```
# Gestionnaire de tâche

Pour gérer les tâches de LittlevGL, vous devez appeler `lv_task_handler()` régulièrement à partir d'un des éléments suivants :
- boucle *while(1)* de la fonction *main()*
- interruption périodique d'une horloge (priorité plus basse que `lv_tick_inc()`)
- une tâche périodique du SE

Le délai n’est pas critique, mais il faut environ 5 millisecondes pour que le système reste réactif.

Exemple :
```c
while(1) {
  lv_task_handler();
  my_delay_ms(5);
}
```

Pour en savoir plus sur les tâches, visitez la section [Tâches](/overview/task).


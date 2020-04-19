```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/fr/porting/os.md
```
# Système d'exploitation et interruptions

LittlevGL n'est **pas compatible avec les fils d’exécution** par défaut.

Cependant, dans les cas suivants, il est valide d'appeler des fonctions liées à LittlevGL :
- Dans les *événements*. Apprenez-en plus dans [Evénements](/overview/event).
- Dans *lv_tasks*.  Apprenez-en plus dans [Tâches](/overview/task).


## Tâches et fils d’exécution
Si vous avez besoin d'utiliser de vraies tâches ou des fils d'exécution, vous avez besoin d'un mutex qui doit être acquis avant l'appel de `lv_task_handler` et libéré ensuite.
Par ailleurs, vous devez utiliser ce même mutex dans les autres tâches et fils d'exécution lors de chaque appel de fonction et code liés à LittlevGL (`lv_...`).
De cette façon, vous pouvez utiliser LittlevGL dans un environnement réellement multitâche. Utilisez simplement un mutex pour éviter l'appel concurrent des fonctions LittlevGL.

## Interruptions
Essayez d'éviter d'appeler les fonctions LittlevGL à partir d'une interruption (sauf `lv_tick_inc()` et `lv_disp_flush_ready ()`). Mais si vous avez besoin de le faire, vous devez désactiver l’interruption qui utilise les fonctions LittlevGL pendant que `lv_task_handler` est en cours d’exécution.
Il est préférable de positionner un indicateur ou une valeur et de le vérifier périodiquement dans une `lv_task`.

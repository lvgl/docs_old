```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/fr/overview/animation.md
```
# Animations

Vous pouvez faire évoluer automatiquement la valeur d'une variable entre une valeur de début et une valeur de fin en utilisant les animations.
L'animation est réalisée par l'appel périodique d'une fonction "animateur" avec comme paramètre la valeur correspondante.

La fonction "animateur" a la signature suivante :
```c
void func(void * var, lv_anim_var_t value);
```
Cette signature est compatible avec la plupart des fonctions *set* de LittlevGL. Par exemple `lv_obj_set_x(obj, value)` ou `lv_obj_set_width(obj, value)`


## Créer une animation
Pour créer une animation, une variable `lv_anim_t` doit être initialisée et configurée avec les fonctions `lv_anim_set_...()`.

```c
lv_anim_t a;
lv_anim_set_exec_cb(&a, btn1, lv_obj_set_x);    /* Définit la fonction animateur et la variable à animer */ 
lv_anim_set_time(&a, duration, delay);
lv_anim_set_values(&a, start, end);             /* Définit les valeurs de début et de fin. P. ex. 0, 150 */
lv_anim_set_path_cb(&a, lv_anim_path_linear);   /* Définit le chemin à partir d'une des fonctions `lv_anim_path_...` ou d'une fonction spécifique. */
lv_anim_set_ready_cb(&a, ready_cb);             /* Définit une fonction de rappel à exécuter quand l'animation est prête. (Optionnel) */
lv_anim_set_playback(&a, wait_time);            /* Active le déroulé de l'animation après un délai `wait_time` */
lv_anim_set_repeat(&a, wait_time);              /* Active la répétition d'une animation après un délai `wait_time` delay. Peut être associé à la fonction `lv_anim_set_playback`*/

lv_anim_create(&a);                             /* Débute l'animation */
```


Vous pouvez appliquer de **multiples différentes animations** à la même variable au même moment. 
Par exemple animer les coordonnées x et y avec `lv_obj_set_x` et `lv_obj_set_y`. Cependant, une seule animation peut exister avec une variable et une fonction données.
Par conséquent, `lv_anim_create()` supprimera les animations déjà existantes de variable et fonction.

## Chemin d'animation

Vous pouvez déterminer le **chemin de l'animation**. Dans les cas les plus simples, il est linéaire ce qui veut dire que la valeur entre *start* et *end* évolue linéairement. 
Un *chemin* est une fonction qui calcule la prochaine valeur à assigner, basée sur le statut actuel de l'animation. Actuellement, les chemins suivants sont prédéfinis :

- **lv_anim_path_linear** animation linéaire
- **lv_anim_path_step** change en une seule fois à la fin
- **lv_anim_path_ease_in** lent au début
- **lv_anim_path_ease_out** lent à la fin
- **lv_anim_path_ease_in_out** lent au début et à la fin
- **lv_anim_path_overshoot** dépasse la valeur de fin
- **lv_anim_path_bounce** rebondit un peu sur la valeur de fin (comme en frappant un mur)


## Vitesse vs durée
Par défaut, vous pouvez définir la durée de l'animation. Mais dans certains cas, il est plus pratique d'utiliser la **vitesse d'animation**. 

La fonction `lv_anim_speed_to_time(speed, start, end)` calcule la durée requise en millisecondes pour atteindre la valeur de fin à partir de la valeur de départ avec une vitesse donnée. 
La vitesse est interprétée en _unité/seconde_. Par exemple `lv_anim_speed_to_time(20,0,100)` donnera 5000 millisecondes. Par exemple dans le cas de `lv_obj_set_x` l'*unité* est le pixel donc *20* signifie une vitesse de *20 px/s*.

## Supprimer des animations

Vous pouvez **supprimer une animation** par `lv_anim_del(var, func)` en indiquant la variable animée et sa fonction animateur.

## API

### Input device

```eval_rst

.. doxygenfile:: lv_anim.h
  :project: lvgl
        
```


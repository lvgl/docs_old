```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/fr/overview/animation.md
```
# Animations

You can automatically change the value of a variable between a start and an end value using animations.
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
lv_anim_set_exec_cb(&a, btn1, lv_obj_set_x);    /*Set the animator function and variable to animate*/
lv_anim_set_time(&a, duration, delay);
lv_anim_set_values(&a, start, end);             /* Définit les valeurs initiale et finale. P. ex. 0, 150 */
lv_anim_set_path_cb(&a, lv_anim_path_linear);   /* Définit le chemin à partir d'une des fonctions `lv_anim_path_...` ou d'une fonction spécifique. */
lv_anim_set_ready_cb(&a, ready_cb);             /* Définit une fonction de rappel à exécuter quand l'animation est prête (optionnel). */
lv_anim_set_playback(&a, wait_time);            /* Active le déroulé de l'animation après un délai `wait_time` */
lv_anim_set_repeat(&a, wait_time);              /* Active la répétition d'une animation après un délai `wait_time`. Peut être associé à la fonction `lv_anim_set_playback`*/

lv_anim_create(&a);                             /* Débute l'animation */
```


You can apply **multiple different animations** on the same variable at the same time.
For example, animate the x and y coordinates with `lv_obj_set_x` and `lv_obj_set_y`. However, only one animation can exist with a given variable and function pair.
Therefore `lv_anim_create()` will delete the already existing variable-function animations.

## Chemin d'animation

You can determinate the **path of animation**. In the most simple case, it is linear, which means the current value between *start* and *end*  is changed linearly.
A *path* is a function which calculates the next value to set based on the current state of the animation. Currently, there are the following built-in paths:

- **lv_anim_path_linear** animation linéaire
- **lv_anim_path_step** change en une seule fois à la fin
- **lv_anim_path_ease_in** lent au début
- **lv_anim_path_ease_out** lent à la fin
- **lv_anim_path_ease_in_out** lent au début et à la fin
- **lv_anim_path_overshoot** dépasse la valeur finale
- **lv_anim_path_bounce** bounce back a little from the end value (like hitting a wall)


## Vitesse et durée
By default, you can set the animation time. But, in some cases, the **animation speed** is more practical.

The `lv_anim_speed_to_time(speed, start, end)` function calculates the required time in milliseconds to reach the end value from a start value with the given speed.
The speed is interpreted in _unit/sec_ dimension. For example,  `lv_anim_speed_to_time(20,0,100)` will give 5000 milliseconds. For example, in case of `lv_obj_set_x` *unit* is pixels so *20* means *20 px/sec* speed.

## Supprimer des animations

Vous pouvez **supprimer une animation** par `lv_anim_del(var, func)` en indiquant la variable animée et sa fonction animateur.

## API

### Périphérique d'entrée

```eval_rst

.. doxygenfile:: lv_anim.h
  :project: lvgl

```

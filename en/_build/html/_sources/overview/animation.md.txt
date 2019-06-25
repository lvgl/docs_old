# Animations

You can automatically change the value of a variable between a start and an end value using animations. 
The animation will happen by the periodical call of an "animator" function with the corresponding value parameter.

The *animator* functions has the following prototype:
```c
void func(void * var, lv_anim_var_t value);
```
This prototype is compatible with the majority of the *set* function of LittlevGL. For example `lv_obj_set_x(obj, value)` or `lv_obj_set_width(obj, value)`


## Create an animation
To create an animation an `lv_anim_t` variable has to be initialized and configured with `lv_anim_set_...()` functions.

```c
lv_anim_t a;
lv_anim_set_exec_cb(&a, btn1, lv_obj_set_x);    /*Set the animator function and variable to animate*/ 
lv_anim_set_time(&a, duration, delay);
lv_anim_set_values(&a, start, end);             /*Set start and end values. E.g. 0, 150*/
lv_anim_set_path_cb(&a, lv_anim_path_linear);   /*Set path from `lv_anim_path_...` functions or a custom one.*/
lv_anim_set_ready_cb(&a, ready_cb);             /*Set a callback to call then animation is ready. (Optional)*/
lv_anim_set_playback(&a, wait_time);            /*Enable playback of teh animation with `wait_time` delay*/
lv_anim_set_repeat(&a, wait_time);              /*Enable repeat of teh animation with `wait_time` delay. Can be compiled with playback*/

lv_anim_create(&a);                             /*Start the animation*/
```


You can apply **multiple different animations** on the same variable at the same time. 
For example animate the x and y coordinates with `lv_obj_set_x` and `lv_obj_set_y`. However, only one animation can exist with a given variable and function pair. 
Therefore `lv_anim_create()` will delete the already existing variable-function animations. 

## Animation path

You can determinate the **path of animation**. In the most simple case, it is linear which means the current value between *start* and *end*  is changed linearly. 
A *path* is a function which calculates the next value to set based on the current state of the animation. Currently, there are the following built-in paths: 

- **lv_anim_path_linear** linear animation
- **lv_anim_path_step** change in one step at the end
- **lv_anim_path_ease_in** slow at the beginning
- **lv_anim_path_ease_out** slow at the end
- **lv_anim_path_ease_in_out** slow at the beginning and end too
- **lv_anim_path_overshoot** overshoot the end value
- **lv_anim_path_bounce** bonce back a little from the end value (like hitting a wall)


## Speed vs time
By default, you can set the animation time. But in some cases, the **animation speed** is more practical. 

The `lv_anim_speed_to_time(speed, start, end)` function calculates the required time in milliseconds to reach the end value from a start value with the given speed. 
The speed is interpreted in _unit/sec_ dimension. For example `lv_anim_speed_to_time(20,0,100)` will give 5000 milliseconds.For example in case of `lv_obj_set_x` *unit* is pixels so *20* means *20 px/sec* speed.

## Delete animations

You can **delete an animation** by `lv_anim_del(var, func)` by providing the animated variable and its animator function.

## API

### Input device

```eval_rst

.. doxygenfile:: lv_anim.h
  :project: lvgl
        
```


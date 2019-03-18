_Written for v5.1_

You can automatically change the value (animate) of a variable between a start and an end value using an **animator function** with `void func(void* var,int32_t value)` prototype. The animation will happen by the periodical calling of the animator function with the corresponding value parameter.

To **create an animation** you have to initializes an _lv_anim_t_ variable (there is a template in [lv_anim.h](https://github.com/littlevgl/lvgl/blob/master/lv_misc/lv_anim.h)):

```c
lv_anim_t a;								
a.var = button1;							 /*Variable to animate*/						
a.start = 100;								 /*Start value*/
a.end = 300;								 /*End value*/
a.fp = (lv_anim_fp_t)lv_obj_set_height;		                         /*Function to be used to animate*/
a.path = lv_anim_path_linear;                                            /*Path of animation*/
a.end_cb = NULL; 						 	 /*Callback when the animation is ready*/
a.act_time = 0;								 /*Set < 0 to make a delay [ms]*/
a.time = 200;								 /*Animation length [ms]*/
a.playback = 0;								 /*1: animate in reverse direction too when the normal is ready*/
a.playback_pause = 0;						         /*Wait before playback [ms]*/
a.repeat = 0;								 /*1: Repeat the animation (with or without playback)*/
a.repeat_pause = 0;							 /*Wait before repeat [ms]*/

lv_anim_create(&a);                          /*Start the animation*/
```

The `anim_create(&a)` will register the animation and immediately **applies the _start_** value regardless to the set delay.

You can determinate the **path of animation**. In most simple case it is linear which means the current value between _start_ and _end_  is changed linearly. A path is a function which calculates the next value to set based on the current state of the animation. Currently, there are two built-in paths: 

- **lv_anim_path_linear** linear animation
- **lv_anim_path_step** change in one step at the end

By default, you can set the animation time. But in some cases, the **animation speed** is more practical. The `lv_anim_speed_to_time(speed, start, end)` function calculates the required time in milliseconds to reach the end value from a start value with the given speed. The speed is interpreted in _unit/sec_ dimension. For example `lv_anim_speed_to_time(20,0,100)` will give 5000 milliseconds.

You can apply **multiple different animations** on the same variable at the same time. (For example animate the x and y coordinates with _lv_obj_set_x_ end _lv_obj_set_y_). But only one animation can exist with a given variable and function pair. Therefore the _lv_anim_create()_ function will delete the already existing variable-function animations. 

You can **delete an animation** by `lv_anim_del(var, func)` with providing the animated variable and its animator function.
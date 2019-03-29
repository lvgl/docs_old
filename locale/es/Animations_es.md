_Escrito para v5.1_

Puedes cambiar automaticamente el valor (animate) de una variable entre el inicio y el valor final usando una **funcion de animacion** con prototipo `void func(void* var,int32_t value)`. La animacion sucedera llamando periodicamente a la funcion de animacion con el parametro correspondiente.

Para **crear una animacion** debes de inicializar una variable _lv_anim_t (hay un template en [lv_anim.h](https://github.com/littlevgl/lvgl/blob/master/lv_misc/lv_anim.h)):

```c
lv_anim_t a;								
a.var = button1;							 /*Variable a animar*/						
a.start = 100;								 /*Valor inicial*/
a.end = 300;								 /*Valor final*/
a.fp = (lv_anim_fp_t)lv_obj_set_height;		                         /*Funcion utilizada para la animacion*/
a.path = lv_anim_path_linear;                                            /*Path a la animacion*/
a.end_cb = NULL; 						 	 /*Callback cuando la animacion esta lista*/
a.act_time = 0;								 /*Asigna < 0 para hacer un delay [ms]*/
a.time = 200;								 /*Longitud de la animacion [ms]*/
a.playback = 0;								 /*1: tambien anima en direccion inversa cuando la normal esta lista*/
a.playback_pause = 0;						         /*Espera antes del playback [ms]*/
a.repeat = 0;								 /*1: Repite la animacion (con o sin playback)*/
a.repeat_pause = 0;							 /*Espera antes de repetir [ms]*/

lv_anim_create(&a);                          /*Inicia la animacion*/
```

`anim_create(&a)` registrara la animacion e inmediatamente **aplica el valor _start_** independientemente del delay configurado.

Puedes determinar el **path of animation**. En el caso ma simple es lineal, lo cual significa que el valor actual entre _start_ y _end_ cambia linealmente. Un path es una funcion la cual calcula el siguiente valor a establecer basado en el estado actual de la animacion. Actualmente estan disponibles dos paths:

- **lv_anim_path_linear** animacion lineal
- **lv_anim_path_step** cambia en un paso al final

Por defecto puedes establecer el tiempo de animacion. Pero en algunos casos, la **animation speed** es mas practico. La funcion `lv_anim_speed_to_time(speed, start, end)` calcula el tiempo requerido en misisegundos para alcanzar el valor final desde el valor inicial con la velocidad especificada. La velocidad es interpretada en _unit/sec_. Por ejemplo `lv_anim_speed_to_time(20,0,100)` da como resultado 5000 milisegundos.

Puedes aplicar **multiples animaciones diferentes** en la misma variable al mismo tiempo .(Por ejemplo animar las coordenadas x y y con _lv_obj_set_x_ y _lv_obj_set_y_). Pero solamente una animacion puede existir con una variable y una funcion dados. Por lo tanto, la funcion _lv_anim_create()_ borrará las animaciones variable-funcion ya existentes.

Puedes **borrar una animacion** con `lv_anim_del(var, func)` proporcionando la variable animada y su funcion de animacion.
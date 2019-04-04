_Escrito para v5.1_

## Visión general

Los LEDs son objetos rectangulares (o circulares). Puedes establecer su **brillo** con `lv_led_set_bright(led, bright)`. El brillo debe de estar entre 0 (el más oscuro) y 255 (el más brillante).

Usa `lv_led_on(led)` y `lv_led_off(led)` para establecer el brillo a un valor ON o OFF predefinido. La función `lv_led_toggle(led)` togglea entre los estados ON y OFF.

## Uso de estilos

El LED usa un estilo que se puede establecer con `lv_led_set_style(led, &style)`. Para determinadar la apariencia las propiedades **style.body** son usadas. Los colores se oscurecen y el ancho de la sombra se reduce al brillo más bajo y gana su valor original en el brillo 255 para mostrar un efecto de iluminación. El estilo por defecto es: `lv_style_pretty_color`.

## Notas

- Normalmente, el estilo predeterminado no es adecuado, por lo que debes de crear tu propio estilo. Ve los ejemplos.

## Ejemplo
![LED image](http://docs.littlevgl.com/img/led-lv_led.png)
```c
/*Crea un estilo para el LED*/
static lv_style_t style_led;
lv_style_copy(&style_led, &lv_style_pretty_color);
style_led.body.radius = LV_RADIUS_CIRCLE;
style_led.body.main_color = LV_COLOR_MAKE(0xb5, 0x0f, 0x04);
style_led.body.grad_color = LV_COLOR_MAKE(0x50, 0x07, 0x02);
style_led.body.border.color = LV_COLOR_MAKE(0xfa, 0x0f, 0x00);
style_led.body.border.width = 3;
style_led.body.border.opa = LV_OPA_30;
style_led.body.shadow.color = LV_COLOR_MAKE(0xb5, 0x0f, 0x04);
style_led.body.shadow.width = 10;

/*Crea un LED y enciéndelo*/
lv_obj_t * led1  = lv_led_create(lv_scr_act(), NULL);
lv_obj_set_style(led1, &style_led);
lv_obj_align(led1, NULL, LV_ALIGN_IN_TOP_MID, 40, 40);
lv_led_on(led1);

/*Copia el LED previo y establece un brillo*/
lv_obj_t * led2  = lv_led_create(lv_scr_act(), led1);
lv_obj_align(led2, led1, LV_ALIGN_OUT_BOTTOM_MID, 0, 40);
lv_led_set_bright(led2, 190);

/*Copia el LED previo y apágalo*/
lv_obj_t * led3  = lv_led_create(lv_scr_act(), led1);
lv_obj_align(led3, led2, LV_ALIGN_OUT_BOTTOM_MID, 0, 40);
lv_led_off(led3);

/*Crea 3 etiquetas junto a los LEDs*/
lv_obj_t * label = lv_label_create(lv_scr_act(), NULL);
lv_label_set_text(label, "LED On");
lv_obj_align(label, led1, LV_ALIGN_OUT_LEFT_MID, -40, 0);

label = lv_label_create(lv_scr_act(), NULL);
lv_label_set_text(label, "LED half");
lv_obj_align(label, led2, LV_ALIGN_OUT_LEFT_MID, -40, 0);

label = lv_label_create(lv_scr_act(), NULL);
lv_label_set_text(label, "LED Off");
lv_obj_align(label, led3, LV_ALIGN_OUT_LEFT_MID, -40, 0);
```

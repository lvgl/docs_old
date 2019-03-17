_Escrito para v5.1_

## Visão geral

Os LEDs são objetos retângulos (ou círculos). Você pode atribuir seu **brilho** com `lv_led_set_bright(led, bright)`. O brilho deve ser entre 0 (mais escuro) e 255 (mais claro).

Use `lv_led_on(led)` e `lv_led_off(led)` para configurar o brilho para um valor ON ou OFF pré-definido. O `lv_led_toggle(led)` comuta entre os estados ON e OFF.

## Uso do estilo

O LED usa um dos estilos na qual pode ser configurado por `lv_led_set_style(led, &style)`. Para determinar a aparência a propriedade **style.body** são usadas. As cores são mais escuras e mostra o comprimento que é reduzido em um menor brilho e ganho do seu valor originall emm 255 para mostrar um efeito luminoso. O estilo padrão é `lv_style_pretty_color`.

## Notas

- Tipicamente o estilo padrão não está disponível, contudo você pode criar seu próprio estilo. Veja os exemplos.

## Exemplo
![LED image](http://docs.littlevgl.com/img/led-lv_led.png)
```c
/*Cria um estilo para o LED*/
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


/*Cria um LED e liga o LED*/
lv_obj_t * led1  = lv_led_create(lv_scr_act(), NULL);
lv_obj_set_style(led1, &style_led);
lv_obj_align(led1, NULL, LV_ALIGN_IN_TOP_MID, 40, 40);
lv_led_on(led1);

/*Copia o LED anterior e configura seu brilho*/
lv_obj_t * led2  = lv_led_create(lv_scr_act(), led1);
lv_obj_align(led2, led1, LV_ALIGN_OUT_BOTTOM_MID, 0, 40);
lv_led_set_bright(led2, 190);

/*Copia o LED anterior e desliga o LED*/
lv_obj_t * led3  = lv_led_create(lv_scr_act(), led1);
lv_obj_align(led3, led2, LV_ALIGN_OUT_BOTTOM_MID, 0, 40);
lv_led_off(led3);

/*Cria 3 rótulos próximo ao LEDs*/
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

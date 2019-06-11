_Escrito para v5.1_

## Visión general

Los objetos barra tienen dos partes principales: un **fondo** que es el objeto en sí mismo y un **indicador** cuya forma es similar a la del fondo pero su anchura/altura puede ser ajustada.

La orientacion de la barra puede ser **vertical u horizontal** de acuerdo con la relación ancho/alto. Logicamente en barras horizontales el ancho del indicador y en barras verticales el alto del indicador pueden ser cambiados.

Un **nuevo valor** se puede ajustar con: `lv_bar_set_value(bar, new_value)`. El valor es interpretado en **rango** (valores minimo y maximo) que pueden ser modificados con: `lv_bar_set_range(bar, min, max)`. El rango por defecto es: 1..100.

La configuración de un nuevo valor puede ocurrie con una **animación** desde el valor actual hasta el valor deseado. En este caso usa `lv_bar_set_value_anim(bar, new_value, anim_time)`.

## Uso de estilos

- **fondo** es un [[Base object]]por lo tanto utiliza los elementos de su estilo. Su estilo por defecto es: `LV_STYLE_PRETTY`.
- **indicador** es similar al fondo. Su estilo puede ser configurado con: `lv_bar_set_style_indic(bar,&style_indic)`. Etiliza los elementos de estilo _hpad_ y _vpad_ para mantener el espacio con el fondo. Su estilo por defecto es: `LV_STYLE_PRETTY_COLOR`.

## Notas

- El indicador no es un objeto real, solo es dibujado por la barra.

## Ejemplo

![Bar image](http://docs.littlevgl.com/img/bar-lv_bar.png)

```c
/*Crea una barra por defecto*/
lv_obj_t * bar1 = lv_bar_create(lv_scr_act(), NULL);
lv_obj_set_size(bar1, 200, 30);
lv_obj_align(bar1, NULL, LV_ALIGN_IN_TOP_RIGHT, -20, 30);
lv_bar_set_value(bar1, 70);

/*Crea una etiqueta a la derecha de la barra*/
lv_obj_t * bar1_label = lv_label_create(lv_scr_act(), NULL);
lv_label_set_text(bar1_label, "Default");
lv_obj_align(bar1_label, bar1, LV_ALIGN_OUT_LEFT_MID, -10, 0);

/*Crea estilos para la barra y para el indicador*/
static lv_style_t style_bar;
static lv_style_t style_indic;

lv_style_copy(&style_bar, &lv_style_pretty);
style_bar.body.main_color = LV_COLOR_BLACK;
style_bar.body.grad_color = LV_COLOR_GRAY;
style_bar.body.radius = LV_RADIUS_CIRCLE;
style_bar.body.border.color = LV_COLOR_WHITE;

lv_style_copy(&style_indic, &lv_style_pretty);
style_indic.body.grad_color =  LV_COLOR_GREEN;
style_indic.body.main_color=  LV_COLOR_LIME;
style_indic.body.radius = LV_RADIUS_CIRCLE;
style_indic.body.shadow.width = 10;
style_indic.body.shadow.color = LV_COLOR_LIME;
style_indic.body.padding.hor = 3;           /*Hace al indicador un poco mas chico*/
style_indic.body.padding.ver = 3;

/*Create a second bar*/
lv_obj_t * bar2 = lv_bar_create(lv_scr_act(), bar1);
lv_bar_set_style(bar2, LV_BAR_STYLE_BG, &style_bar);
lv_bar_set_style(bar2, LV_BAR_STYLE_INDIC, &style_indic);
lv_obj_align(bar2, bar1, LV_ALIGN_OUT_BOTTOM_MID, 0, 30); /*Alinea abajo de 'bar1'*/

/*Crea una segunda etiqueta*/
lv_obj_t * bar2_label = lv_label_create(lv_scr_act(), bar1_label);
lv_label_set_text(bar2_label, "Modified");
lv_obj_align(bar2_label, bar2, LV_ALIGN_OUT_LEFT_MID, -10, 0);
```

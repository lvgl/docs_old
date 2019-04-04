_Escrito para v5.1_

## Visión general

El indicador es un metro con **etiquetas de escala** y **agujas**. Puedes usar la funcion `lv_gauge_set_scale(gauge, angle, line_num, label_cnt)` Para ajustar el ángulo de la escala y el número de líneas de escala y etiquetas. Los ajustes por defecto son: 220 grados, 6 etiquetas de escala y 21 líneas.

El indicador puede mostrar **mas de una aguja**. Usa la funcion `lv_gauge_set_needle_count(gauge, needle_num, color_array)` para establecer el número de agujas y un arreglo con los colores de cada aguja (El arreglo debe de ser una variable estática o global).

Puedes usar `lv_gauge_set_value(gauge, needle_id, value)` para **establecer el valor de una aguja**.

Para establecer un **valor critico** usa `lv_gauge_set_critical_value(gauge, value)`. El color de la escala será cambiado a _line.color_ después de este valor. (default: 80)

El **rango** de un indicador puede ser especificado con `lv_gauge_set_range(gauge, min, max)`.

## Uso de estilos

El indicador usa un estilo el cual puede ser establecido con `lv_gauge_set_style(gauge, &style)`. Las propiedades del indicador son derivadas de los siguientes atributos de estilo:

- **body.main_color** Color de la línea al inicio de la escala.
- **body.grad_color** Color de la línea al final de la escala (gradiente con el color principal).
- **body.padding.hor** Longitud de la línea.
- **body.padding.inner** Distancia de la etiqueta con las líneas de escala.
- **line.width** Grosor de la línea.
- **line.color** Color de la línea despues del valor critico.
- **text.font/color/letter_space** Atributos de la etiqueta.

## Ejemplo

![Gauge image](http://docs.littlevgl.com/img/gauge-lv_gauge.png)
```c
/*Crea un estilo*/
static lv_style_t style;
lv_style_copy(&style, &lv_style_pretty_color);
style.body.main_color = LV_COLOR_HEX3(0x666);     /*Color de la linea al inicio*/
style.body.grad_color =  LV_COLOR_HEX3(0x666);    /*Color de la linea al final*/
style.body.padding.hor = 10;                      /*Escala la longitud de la linea*/
style.body.padding.inner = 8 ;                    /*Padding de la escala*/
style.body.border.color = LV_COLOR_HEX3(0x333);   /*Color del circulo central de la aguja*/
style.line.width = 3;
style.text.color = LV_COLOR_HEX3(0x333);
style.line.color = LV_COLOR_RED;                  /*Color de la linea despues del valor critico*/


/*Describe el color de las agujas*/
static lv_color_t needle_colors[] = {LV_COLOR_BLUE, LV_COLOR_ORANGE, LV_COLOR_PURPLE};

/*Crea un indicador (gauge)*/
lv_obj_t * gauge1 = lv_gauge_create(lv_scr_act(), NULL);
lv_gauge_set_style(gauge1, &style);
lv_gauge_set_needle_count(gauge1, 3, needle_colors);
lv_obj_align(gauge1, NULL, LV_ALIGN_CENTER, 0, 20);

/*Establece los valores*/
lv_gauge_set_value(gauge1, 0, 10);
lv_gauge_set_value(gauge1, 1, 20);
lv_gauge_set_value(gauge1, 2, 30);
```

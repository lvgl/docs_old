_Escrito para v5.2_

## Visión general

El objeto Arco **dibuja un arco** dentro de **los ángulos de inicio y fin** y con un **grosor** dado.

Para establecer los ángulos usa la función `lv_arc_set_angles(arc, start_angle, end_angle)`. El grado cero esta en la parte inferior del objeto y los ángulos incrementan en el sentido contrario de las manecillas del reloj. Los ángulos deben estar en el rango [0;360].

Para **configurar e estilo** de un objeto Arco usa `lv_arc_set_style(arc, LV_ARC_STYLE_MAIN, &style)`

## Uso de estilos
- **line.rounded** redondea los puntos finales (la opacidad no funciona correctamente se se configura a 1).
- **line.width** el espesor del arco.
- **line.color** el color del arco.

## Notas
- El **ancho y alto** del arco deben ser el **mismo**.
- Actualmente, el objeto arco **no soporta anti-aliasing (suavizado)**.

## Ejemplo

![Arc image](http://docs.littlevgl.com/img/arc-lv_arc.png)

```c
/*Crea un estilo para el arco*/
lv_style_t style;
lv_style_copy(&style, &lv_style_plain);
style.line.color = LV_COLOR_BLUE;           /*Color del arco*/
style.line.width = 8;                       /*Ancho del arco*/

/*Crea un arco*/
lv_obj_t * arc = lv_arc_create(lv_scr_act(), NULL);
lv_arc_set_style(arc, LV_ARC_STYLE_MAIN, &style);          /*Usa el nuevo estilo*/
lv_arc_set_angles(arc, 90, 60);
lv_obj_set_size(arc, 150, 150);
lv_obj_align(arc, NULL, LV_ALIGN_CENTER, 0, 0);

/*Copia el arco previo y estabece un ángulos y tamaño diferentes*/
arc = lv_arc_create(lv_scr_act(), arc);
lv_arc_set_angles(arc, 90, 20);
lv_obj_set_size(arc, 125, 125);
lv_obj_align(arc, NULL, LV_ALIGN_CENTER, 0, 0);

/*Copia el arco previo y estabece un ángulos y tamaño diferentes*/
arc = lv_arc_create(lv_scr_act(), arc);
lv_arc_set_angles(arc, 90, 310);
lv_obj_set_size(arc, 100, 100);
lv_obj_align(arc, NULL, LV_ALIGN_CENTER, 0, 0);
```

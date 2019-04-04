_Escrito para v5.3_

- Esto es un trabajo en progreso

## Visión general



## Uso de estilos

## Notas

- nota

## Ejemplo
![spinbox example](https://user-images.githubusercontent.com/13847288/47869506-6676d000-de07-11e8-807b-1dbaa238e2c8.gif)
```c
static void spinbox_value_changed(lv_obj_t * spinbox)
{

}

.
.
.
spinbox = lv_spinbox_create(lv_scr_act(), NULL);
lv_spinbox_set_style(spinbox, LV_SPINBOX_STYLE_BG, &spinBoxStyle);
lv_spinbox_set_style(spinbox, LV_SPINBOX_STYLE_CURSOR, &spinBoxCursorStyle);
lv_obj_set_size(spinbox, LV_HOR_RES, 80);
lv_obj_align(spinbox, NULL, LV_ALIGN_IN_TOP_LEFT, 4, 0);
```
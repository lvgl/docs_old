_Escrito para v5.1, revision 2_

## Visión general

El Switch puede ser usado para **encender/apagar** algo. Se ven como un slider pequeño. El estado del switch puede ser cambiado con:
- Click en el.
- Sliding en el.
- Usando las funciones `lv_sw_on(sw)` y `lv_sw_off(sw)`.

Puedes asignar una **función de callback** para que sea llamada cuando el usuario usa el switch: `lv_sw_set_action(sw, my_action)`.

**Nuevo en v5.3**: Los Switched pueden ser animados llamando `lv_sw_set_anim_time(sw, anim_ms)`.

## Uso de estilos

Puedes modificar el estilo del Switch con `lv_sw_set_style(sw, LV_SW_STYLE_..., &style)`.

- **LV_SW_STYLE_BG** Estilo del fondo. All _style.body_ properties are used. Los valores _padding_ hacen al Switch más pequeño que la perilla (los valores negativos lo hacen más grande).
- **LV_SW_STYLE_INDIC** Estilo del indicador. Todas las propiedades _style.body_ son usadas. Los valores _padding_ hacen al indicador más pequeño que el fondo.
- **LV_SW_STYLE_KNOB_OFF** Estilo de la perilla cuando el switch esta apagado. Las propiedades _style.body_ son usadas excepto padding.
- **LV_SW_STYLE_KNOB_ON** Estilo de la perilla cuando el switch esta encendido.  Las propiedades _style.body_ son usadas excepto padding.

## Notas

- La perilla no es un objeto real, solo es dibujado sobre la barra.

## Ejemplo
![Switch image](http://docs.littlevgl.com/img/switch-lv_sw.png)
```c
/*Crea estilos para el switch*/
static lv_style_t bg_style;
static lv_style_t indic_style;
static lv_style_t knob_on_style;
static lv_style_t knob_off_style;
lv_style_copy(&bg_style, &lv_style_pretty);
bg_style.body.radius = LV_RADIUS_CIRCLE;

lv_style_copy(&indic_style, &lv_style_pretty_color);
indic_style.body.radius = LV_RADIUS_CIRCLE;
indic_style.body.main_color = LV_COLOR_HEX(0x9fc8ef);
indic_style.body.grad_color = LV_COLOR_HEX(0x9fc8ef);
indic_style.body.padding.hor = 0;
indic_style.body.padding.ver = 0;

lv_style_copy(&knob_off_style, &lv_style_pretty);
knob_off_style.body.radius = LV_RADIUS_CIRCLE;
knob_off_style.body.shadow.width = 4;
knob_off_style.body.shadow.type = LV_SHADOW_BOTTOM;

lv_style_copy(&knob_on_style, &lv_style_pretty_color);
knob_on_style.body.radius = LV_RADIUS_CIRCLE;
knob_on_style.body.shadow.width = 4;
knob_on_style.body.shadow.type = LV_SHADOW_BOTTOM;

/*Crea un switch y aplica los estilos*/
lv_obj_t *sw1 = lv_sw_create(lv_scr_act(), NULL);
lv_sw_set_style(sw1, LV_SW_STYLE_BG, &bg_style);
lv_sw_set_style(sw1, LV_SW_STYLE_INDIC, &indic_style);
lv_sw_set_style(sw1, LV_SW_STYLE_KNOB_ON, &knob_on_style);
lv_sw_set_style(sw1, LV_SW_STYLE_KNOB_OFF, &knob_off_style);
lv_obj_align(sw1, NULL, LV_ALIGN_CENTER, 0, -50);

/*Copia el primer switch y lo enciende*/
lv_obj_t *sw2 = lv_sw_create(lv_scr_act(), sw1);
lv_sw_set_on(sw2);
lv_obj_align(sw2, NULL, LV_ALIGN_CENTER, 0, 50);
```

_Escrito para v5.1_

## Visión general

Los objetos Matriz de botones pueden mostrar **múltiples botones** acorde a un arreglo de cadenas descriptor, llamado _map_. Puedes especificar el map con `lv_btnm_set_map(btnm, my_map)`.

La **declaración de un map** se ve como `const char * map[] = {"btn1", "btn2", "btn3", ""}`. Notar que **el último elemento tiene que ser una cadena vacía**!.

El primer carácter de una cadena puede ser un **carácter de control** para especificar algunos atributos:

- **bit 7..6** Siempre _0b10_ para diferenciar el byte de control de los carácteres de texto.
- **bit 5** Botón inactivo.
- **bit 4** Botón oculto.
- **bit 3** Botón sin presion larga.
- **bit 2..0** Anchura relativa comparada con los botones de la misma fila. [1..7]

Es recomendado especificar el **byte de control como un numero octal**. Por ejemplo `"\213button"`. El número octal siempre inicia con _2_ (bit 7..6) la parte de en medio son los atributos (bit 5..3) y la última parte es el ancho (bit 2..0). Por lo tanto el ejemplo describe un botón de 3 unidades de ancho y oculto.

Usa "\n" en el mapa para hacer un **salto de línea**: `{"btn1", "btn2", "\n", "btn3", ""}`. El ancho de los botones es re calculado en cada línea.

La función `lv_btnm_set_action(btnm, btnm_action)` especifica una acción a llamar cuando se deja de presionar un botón.

Puedes habilitar el **botón para que togglee** cuando son presionados. Solo puede haber un boton toggleado al mismo tiempo. La función `lv_btnm_set_toggle(btnm, true, id)` habilita el toggleo y especifica el _id_ th botón al estado toggleado.

## Uso de estilos

La matriz de botones trabaja con 6 estilos: un fondo y 5 estilos de botones para cada uno de sus estados.
Puedes establecer los estilos con `lv_btnm_set_style(btn, LV_BTNM_STYLE_..., &style)`. El fondo y los botones usan las propiedades _style.body_. Las etiquetas usan las propiedades _style.text_ de los estilos de los botones.

- **LV_BTNM_STYLE_BG** Estilo del fondo. Usa todas las propiedades de _style.body_ incluyendo _padding_ Default: _lv_style_pretty_
- **LV_BTNM_STYLE_BTN_REL** Estilo de los botones sin presionar. Default: _lv_style_btn_rel_
- **LV_BTNM_STYLE_BTN_PR** Estilo de los botones presionados. Default: _lv_style_btn_pr_
- **LV_BTNM_STYLE_BTN_TGL_REL** Estilo de los botones toggleados sin presionar. Default: _lv_style_btn_tgl_rel_
- **LV_BTNM_STYLE_BTN_TGL_PR** Estilo de los botones toggleados presionados. Default: _lv_style_btn_tgl_pr_
- **LV_BTNM_STYLE_BTN_INA** Estilo de los botones inactivos. Default: _lv_style_btn_ina_

## Notas

- La matriz de botones en **muy ligero**. Crea solo un objeto base de fondo y dibuja los botones en el en lugar de crear muchos botones reales.

## Ejemplo
![Button matrix image](http://docs.littlevgl.com/img/button-matrix-lv_btnm.png)
```c
/*Llamada cuando se deja de presionar un botón o cuando tiene una presion larga*/
static lv_res_t btnm_action(lv_obj_t * btnm, const char *txt)
{
    printf("Button: %s released\n", txt);

    return LV_RES_OK; /*Retorna OK porque la matriz de botones no se borro*/
}


.
.
.

/*Crea un arreglo de cadenas que describen la matriz*/
static const char * btnm_map[] = {"1", "2", "3", "4", "5", "\n",
                           "6", "7", "8", "9", "0", "\n",
                           "\202Action1", "Action2", ""};




/*Crea una matriz de botones por default*/
lv_obj_t * btnm1 = lv_btnm_create(lv_scr_act(), NULL);
lv_btnm_set_map(btnm1, btnm_map);
lv_btnm_set_action(btnm1, btnm_action);
lv_obj_set_size(btnm1, LV_HOR_RES, LV_VER_RES / 2);

/*Crea un nuevo estilo para el fondo de la matriz de botones*/
static lv_style_t style_bg;
lv_style_copy(&style_bg, &lv_style_plain);
style_bg.body.main_color = LV_COLOR_SILVER;
style_bg.body.grad_color = LV_COLOR_SILVER;
style_bg.body.padding.hor = 0;
style_bg.body.padding.ver = 0;
style_bg.body.padding.inner = 0;

/*Crea 2 estilos de botones*/
static lv_style_t style_btn_rel;
static lv_style_t style_btn_pr;
lv_style_copy(&style_btn_rel, &lv_style_btn_rel);
style_btn_rel.body.main_color = LV_COLOR_MAKE(0x30, 0x30, 0x30);
style_btn_rel.body.grad_color = LV_COLOR_BLACK;
style_btn_rel.body.border.color = LV_COLOR_SILVER;
style_btn_rel.body.border.width = 1;
style_btn_rel.body.border.opa = LV_OPA_50;
style_btn_rel.body.radius = 0;

lv_style_copy(&style_btn_pr, &style_btn_rel);
style_btn_pr.body.main_color = LV_COLOR_MAKE(0x55, 0x96, 0xd8);
style_btn_pr.body.grad_color = LV_COLOR_MAKE(0x37, 0x62, 0x90);
style_btn_pr.text.color = LV_COLOR_MAKE(0xbb, 0xd5, 0xf1);

/*Crea una segunda matriz de botones con los nuevos estilos*/
lv_obj_t * btnm2 = lv_btnm_create(lv_scr_act(), btnm1);
lv_btnm_set_style(btnm2, LV_BTNM_STYLE_BG, &style_bg);
lv_btnm_set_style(btnm2, LV_BTNM_STYLE_BTN_REL, &style_btn_rel);
lv_btnm_set_style(btnm2, LV_BTNM_STYLE_BTN_PR, &style_btn_pr);
lv_obj_align(btnm2, btnm1, LV_ALIGN_OUT_BOTTOM_MID, 0, 0);
```

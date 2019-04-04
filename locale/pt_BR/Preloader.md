_Escrito para v5.2_

## Visão geral
O objeto pré-carregador é **um arco girante sobre uma borda**.

O **comprimento do arco** pode ser ajustado pelo `lv_preload_set_arc_length(preload, deg)`.

A **velocidade do giro** pode ser ajustada pelo `lv_preload_set_spin_time(preload, time_ms)`.


## Uso do estilo
O estilo `LV_PRELOAD_STYLE_MAIN` descreve ambos estilos de arco e a borda:
- **arco** é descrito pela propriedade de linha
- **borda** é descrito pela propriedade `body.border` incluindo `body.padding.hor/ver` (o menor é usado) para dar um menor raio para a borda.

## Exemplo

![Preloader image](http://docs.littlevgl.com/img/preloader-lv_preload.png)

```c
/*Cria um estilo para o Pré-carregador*/
static lv_style_t style;
lv_style_copy(&style, &lv_style_plain);
style.line.width = 10;                         /*arco de espessura 10 px*/
style.line.color = LV_COLOR_HEX3(0x258);       /*Cor do arco azul*/

style.body.border.color = LV_COLOR_HEX3(0xBBB); /*Cor do arco cinza*/
style.body.border.width = 10;
style.body.padding.hor = 0;

/*Cria um objeto pré-carregador*/
lv_obj_t * preload = lv_preload_create(lv_scr_act(), NULL);
lv_obj_set_size(preload, 100, 100);
lv_obj_align(preload, NULL, LV_ALIGN_CENTER, 0, 0);
lv_preload_set_style(preload, LV_PRELOAD_STYLE_MAIN, &style);
```

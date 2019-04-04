_Escrito para v5.1_

## Visão geral

O objeto linha é capaz de **desenhar linhas retas** entre um conjunto de pontos. Os pontos tem que ser guardados em um vetor `lv_point_t` e passado ao objeto pela função `lv_line_set_points(lines, point_array, point_num)`.

É possível **automaticamente configurar o tamanho** do objeto linha de acordo com seus pontos. Você pode ativá-lo com a função `lv_line_set_auto_size(line, true)`. Se atiado quando os pontos estão configurados então o comprimento do objeto e a altura irão ser mudados de acordo com as coordenadas máximas x e y entre os pontos. O _auto size_ está ativado por padrão.

Basicamente o ponto _y == 0_ está no topo do objeto mas você pode **innverter a coordenada y** com `lv_line_set_y_invert(line, true)`. Depois disso as coordenadas serão subtraídas da altura do objeto.

## Uso do estilo

- Propriedades **style.line** são usadas

## Notas

## Exemplo

![Example of Line in LittlevGL Graphics Library ](http://docs.littlevgl.com/img/line-lv_line.png)

```c
/*Cria um vetor para os pontos da linha*/
static lv_point_t line_points[] = { {5, 5}, {70, 70}, {120, 10}, {180, 60}, {240, 10} };

/*Cria linha com o estilo padrão*/
lv_obj_t * line1;
line1 = lv_line_create(lv_scr_act(), NULL);
lv_line_set_points(line1, line_points, 5);     /*Set the points*/
lv_obj_align(line1, NULL, LV_ALIGN_IN_TOP_MID, 0, 20);

/*Cria novo estilo (azul claro fino)*/
static lv_style_t style_line2;
lv_style_copy(&style_line2, &lv_style_plain);
style_line2.line.color = LV_COLOR_MAKE(0x2e, 0x96, 0xff);
style_line2.line.width = 2;

/*Copia a linha anterior e aplica um novo estilo*/
lv_obj_t * line2 = lv_line_create(lv_scr_act(), line1);
lv_line_set_style(line2, &style_line2);
lv_obj_align(line2, line1, LV_ALIGN_OUT_BOTTOM_MID, 0, -20);

/*Cria um novo estilo (azul escuro espesso)*/
static lv_style_t style_line3;
lv_style_copy(&style_line3, &lv_style_plain);
style_line3.line.color = LV_COLOR_MAKE(0x00, 0x3b, 0x75);
style_line3.line.width = 5;

/*Copia a linha anterior e aplica o novo estilo*/
lv_obj_t * line3 = lv_line_create(lv_scr_act(), line1);
lv_line_set_style(line3, &style_line3);
lv_obj_align(line3, line2, LV_ALIGN_OUT_BOTTOM_MID, 0, -20);
```

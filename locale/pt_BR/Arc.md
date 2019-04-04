_Escrito para v5.2_

## Visão geral

O objeto Arco **desenha um arco** em torno **dos ângulos iniciais e finais** e com uma dada **espessura**.

Para configurar os ângulos, use a função `lv_arc_set_angles(arc, start_angle, end_angle)`. O grau zero está no fundo do objeto e os graus aumentam em um sentido anti-horário. Os ângulos devem estar entre [0;360].

Para **configurar o estilo** de um objeto Arco, use `lv_arc_set_style(arc, LV_ARC_STYLE_MAIN, &style)`

## Uso do estilo
- **line.rounded** faz os as linhas arredondadas (opacidade não funcinará apropriadamente se configurado para 1)
- **line.width** a espessura do arco
- **line.color** a cor do arco.

## Notas
- O **comprimento e altura** do Arco devem ser os **mesmos**
- Atualmente o objeto Arco **não suporta anti-aliasing**.

## Exemplo

![Imagem Arco](http://docs.littlevgl.com/img/arc-lv_arc.png)

```c
/*Cria o estilo para os Arcos*/
lv_style_t style;
lv_style_copy(&style, &lv_style_plain);
style.line.color = LV_COLOR_BLUE;           /*Cor do Arco*/
style.line.width = 8;                       /*Comprimento do Arco*/

/*Cria um Arco*/
lv_obj_t * arc = lv_arc_create(lv_scr_act(), NULL);
lv_arc_set_style(arc, LV_ARC_STYLE_MAIN, &style);          /*Usa o novo estilo*/
lv_arc_set_angles(arc, 90, 60);
lv_obj_set_size(arc, 150, 150);
lv_obj_align(arc, NULL, LV_ALIGN_CENTER, 0, 0);

/*Copia o Arco anterior e configura ângulos diferentes e tamanho*/
arc = lv_arc_create(lv_scr_act(), arc);
lv_arc_set_angles(arc, 90, 20);
lv_obj_set_size(arc, 125, 125);
lv_obj_align(arc, NULL, LV_ALIGN_CENTER, 0, 0);

/*Copia o Arco anterior e configura diferente ângulos e tamanho*/
arc = lv_arc_create(lv_scr_act(), arc);
lv_arc_set_angles(arc, 90, 310);
lv_obj_set_size(arc, 100, 100);
lv_obj_align(arc, NULL, LV_ALIGN_CENTER, 0, 0);
```

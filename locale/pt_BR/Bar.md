_Escrito para v5.1_

## Visão global

Os objetos Barra tem duas partes principais: um **background** na qual é próprio objeto e um **indicador** na qual a forma é similar ao plano de fundo (background) mas seu comprimento/altura pode ser ajustado.

A orientação da barra pode sser **vertical ou horizontal** de acordo com a razão comprimento/altura. Logicamente nas barras horizontais o comprimento do indicador, sobre as barras verticais a altura d indicador pode ser mudado.

Um **novo valor** pode ser ajustado por: `lv_bar_set_value(bar, new_value)`. O valor é interpretado em **alcance** (valores mínimos e máximos) na qual podem ser modificados com `lv_bar_set_range(bar, min, max)`. O alcance padrão é: 1..100.

The setting of a new value can happen with an **animation** from the current value to the desired. In this case use `lv_bar_set_value_anim(bar, new_value, anim_time)`.

## Uso do estilo

- **background** é um [[Base-object]] contudo ele usa seus elementos de estilos. Seu estilo padrão é: `LV_STYLE_PRETTY`.
- **indicador** é similar ao background. Seu estilo pode ser configurado por: `lv_bar_set_style_indic(bar,&style_indic)`. Ele usa o estilo de elemento _hpad_ e _vpad_ para manter o espaço do background. Seu estilo padrão é: `LV_STYLE_PRETTY_COLOR`.

## Notas

- O indicador não é um objeto real; ele é somente desenhado pela barra.

## Exemplo

![Imagem barra](http://docs.littlevgl.com/img/bar-lv_bar.png)

```c
/*Cria uma barra padrão*/
lv_obj_t * bar1 = lv_bar_create(lv_scr_act(), NULL);
lv_obj_set_size(bar1, 200, 30);
lv_obj_align(bar1, NULL, LV_ALIGN_IN_TOP_RIGHT, -20, 30);
lv_bar_set_value(bar1, 70);

/*Cria um rótulo à direita da barra*/
lv_obj_t * bar1_label = lv_label_create(lv_scr_act(), NULL);
lv_label_set_text(bar1_label, "Default");
lv_obj_align(bar1_label, bar1, LV_ALIGN_OUT_LEFT_MID, -10, 0);

/*Cria uma barra e um estilo indicador*/
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
style_indic.body.padding.hor = 3;           /*Faz o indicador ficar um pouco menor*/
style_indic.body.padding.ver = 3;

/*Cria uma segunda barra*/
lv_obj_t * bar2 = lv_bar_create(lv_scr_act(), bar1);
lv_bar_set_style(bar2, LV_BAR_STYLE_BG, &style_bar);
lv_bar_set_style(bar2, LV_BAR_STYLE_INDIC, &style_indic);
lv_obj_align(bar2, bar1, LV_ALIGN_OUT_BOTTOM_MID, 0, 30); /*Alinha abaixo da 'barra1'*/

/*Cria uma segunda barra*/
lv_obj_t * bar2_label = lv_label_create(lv_scr_act(), bar1_label);
lv_label_set_text(bar2_label, "Modified");
lv_obj_align(bar2_label, bar2, LV_ALIGN_OUT_LEFT_MID, -10, 0);
```

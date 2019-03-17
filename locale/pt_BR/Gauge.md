_Escrito para v5.1_
## Visão geral

O indicador é um medidor com **rótulos de escala** e **agulhas**. Você pode usar a função `lv_gauge_set_scale(gauge, angle, line_num, label_cnt)` para ajustar o ânguloa da escala e o número das linhas de escalas e rótulos. As configurações são: 220 graus, 6 rótulos de escala e 21 linhas.

O indicador pode mostrar **mais do que uma agulha**. Use a função `lv_gauge_set_needle_count(gauge, needle_num, color_array)` para configurar o número de agulhas e um vetor com cores para cada agulha. (O vetor precisa ser estático ou variável global).

Você pode usar `lv_gauge_set_value(gauge, needle_id, value)` para **configurar o valor da agulha**.

Para configurar um **valor crítico** use `lv_gauge_set_critical_value(gauge, value)`. A cor de escala será mudada para _line.color_ depois desse valor. (padrão: 80)

O **alcance** do medidor pode ser especificado por `lv_gauge_set_range(gauge, min, max)`.

## Uso do estilo

O medidor usa um estilo na qual pode ser configurado por `lv_gauge_set_style(gauge, &style)`. As propriedades do medidor são derivadas dos atributos dos seguintes estilos:


- **body.main_color** cor da linha no início da escala
- **body.grad_color** cor da linha no fim da escala (gradiente com a cor principal)
- **body.padding.hor** comprimento da linha
- **body.padding.inner** distância do rótulo da linhas de escala
- **line.width** comprimento da linha
- **line.color** cor da linha depois do valor crítico
- **text.font/color/letter_space** atributos do rótulo

## Exemplo

![Gauge image](http://docs.littlevgl.com/img/gauge-lv_gauge.png)
```c
/*Cria um estilo*/
static lv_style_t style;
lv_style_copy(&style, &lv_style_pretty_color);
style.body.main_color = LV_COLOR_HEX3(0x666);     /*Cor da linha no início*/
style.body.grad_color =  LV_COLOR_HEX3(0x666);    /*Cor da linha no fim*/
style.body.padding.hor = 10;                      /*Coomprimento da escala da linha*/
style.body.padding.inner = 8 ;                    /*Escala do espaçamento do rótulo*/
style.body.border.color = LV_COLOR_HEX3(0x333);   /*Cor do círculo do meio da agulha*/
style.line.width = 3;
style.text.color = LV_COLOR_HEX3(0x333);
style.line.color = LV_COLOR_RED;                  /*Cor da linha depois do valor crítico*/


/*Descreve a cor para as agulhas*/
static lv_color_t needle_colors[] = {LV_COLOR_BLUE, LV_COLOR_ORANGE, LV_COLOR_PURPLE};

/*Cria um medidor*/
lv_obj_t * gauge1 = lv_gauge_create(lv_scr_act(), NULL);
lv_gauge_set_style(gauge1, &style);
lv_gauge_set_needle_count(gauge1, 3, needle_colors);
lv_obj_align(gauge1, NULL, LV_ALIGN_CENTER, 0, 20);

/*Configura os valores*/
lv_gauge_set_value(gauge1, 0, 10);
lv_gauge_set_value(gauge1, 1, 20);
lv_gauge_set_value(gauge1, 2, 30);
```

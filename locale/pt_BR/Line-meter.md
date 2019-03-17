_Escrito para v5.1_

## Visão geral

O objeto medidor de linha consiste de algumas **linhas radiais** na qual desenha uma escala. Quando se configura um novo valor com `lv_lmeter_set_value(lmeter, new_value)` a parte proporcional da escala será recolorizada.

A função `lv_lmeter_set_range(lmeter, min, max)` atribui o **alcance** do medidor de linha.

Você pode configurar o **ângulo** da escala e o **número de linhas** pelo: `lv_lmeter_set_scale(lmeter, angle, line_num)`. O ângulo padrão é 240 e o padrão do número da linha é 31

## Uso do estilo

O medidor de linha usa um estilo na qual pode ser configurado pelo `lv_lmeter_set_style(lmeter, &style)`. As propriedades do medidor de linha são derivados dos seguintes atributos de estilo:

- **line.color** cor da "linha inativa" na qual é maior do que o valor atual
- **body.main_color** cor da "linha ativa" no início da escala
- **body.grad_color** cor da "linha ativa" no fim da escala (gradiente com a cor principal)
- **body.padding.hor** comprimento da linha
- **line.width** comprimento da linha

O estilo padrão é _lv_style_pretty_color_.

## Notas

- O medidor de linha não tem background
- É recomendado usar **antialiasing** no menor displays de dpi para mostrar linhas suavizadas
- Números ímpared de escala são melhores
- É melhor se o angulo de escala é: (número de linha - 1) * N, onde N é um inteiro

## Exemplo

![Line meter image](http://docs.littlevgl.com/img/line-meter-lv_lmeter.png)
```c
/**************************************
 * Cria 3 medidores de linha similares
 **************************************/

/*Cria um estilo simples com comprimento de linha grosso*/
static lv_style_t style_lmeter1;
lv_style_copy(&style_lmeter1, &lv_style_pretty_color);
style_lmeter1.line.width = 2;
style_lmeter1.line.color = LV_COLOR_SILVER;
style_lmeter1.body.main_color = LV_COLOR_HEX(0x91bfed);         /*Azul claro*/
style_lmeter1.body.grad_color = LV_COLOR_HEX(0x04386c);         /*Azul escuro*/

/*Cria o primeiro medidor de linha*/
lv_obj_t * lmeter;
lmeter = lv_lmeter_create(lv_scr_act(), NULL);
lv_lmeter_set_range(lmeter, 0, 100);                   /*Configura o alcance*/
lv_lmeter_set_value(lmeter, 30);                       /*Configura o valor atual*/
lv_lmeter_set_style(lmeter, &style_lmeter1);           /*Aplica o novo estilo*/
lv_obj_set_size(lmeter, 80, 80);
lv_obj_align(lmeter, NULL, LV_ALIGN_IN_BOTTOM_LEFT, 20, -20);

/*Adiciona um rótulo para mostrar o valor atual*/
lv_obj_t * label;
label = lv_label_create(lmeter, NULL);
lv_label_set_text(label, "30%");
lv_label_set_style(label, &lv_style_pretty);
lv_obj_align(label, NULL, LV_ALIGN_CENTER, 0, 0);

/*Cria o segundo medidor de linha e um rótulo*/
lmeter = lv_lmeter_create(lv_scr_act(), lmeter);
lv_lmeter_set_value(lmeter, 60);
lv_obj_align(lmeter, NULL, LV_ALIGN_IN_BOTTOM_MID, 0, -20);

label = lv_label_create(lmeter, label);
lv_label_set_text(label, "60%");
lv_obj_align(label, NULL, LV_ALIGN_CENTER, 0, 0);

/*Cria o terceiro medidor de linha e um rótulo*/
lmeter = lv_lmeter_create(lv_scr_act(), lmeter);
lv_lmeter_set_value(lmeter, 90);
lv_obj_align(lmeter, NULL, LV_ALIGN_IN_BOTTOM_RIGHT, -20, -20);

label = lv_label_create(lmeter, label);
lv_label_set_text(label, "90%");
lv_obj_align(label, NULL, LV_ALIGN_CENTER, 0, 0);

/*********************************
 * Cria um medidor de linha maior
 *********************************/

/*Cria um novo estilo*/
static lv_style_t style_lmeter2;
lv_style_copy(&style_lmeter2, &lv_style_pretty_color);
style_lmeter2.line.width = 2;
style_lmeter2.line.color = LV_COLOR_SILVER;
style_lmeter2.body.padding.hor = 16;            /*Comprimento da linha*/
style_lmeter2.body.main_color = LV_COLOR_LIME;
style_lmeter2.body.grad_color = LV_COLOR_ORANGE;

/*Cria o medidor de linha*/
lmeter = lv_lmeter_create(lv_scr_act(), lmeter);
lv_obj_set_style(lmeter, &style_lmeter2);
lv_obj_set_size(lmeter, 120, 120);
lv_obj_align(lmeter, NULL, LV_ALIGN_IN_TOP_MID, 0, 20);
lv_lmeter_set_scale(lmeter, 240, 31);
lv_lmeter_set_value(lmeter, 90);

/*Cria um estilo de rótulo com uma fonte maior*/
static lv_style_t style_label;
lv_style_copy(&style_label, &lv_style_pretty);
style_label.text.font = &lv_font_dejavu_60;
style_label.text.color = LV_COLOR_GRAY;

/*Adiciona um rótulo para mostrar o valor atual*/
label = lv_label_create(lmeter, label);
lv_label_set_text(label, "90%");
lv_obj_set_style(label, &style_label);
lv_obj_align(label, NULL, LV_ALIGN_CENTER, 0, 0);
```

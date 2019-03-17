_Escrito para v5.1_

## Visão geral

Os containeres são **objetos retangulares** com algumas características especiais.

Você pode aplicar um **layout** nos contâineres para automaticamente ordenar seus filhos. O espaçamento do layout vem das propriedades style.body.padding.hor/ver/inner. As possíveis opções de layout:

- LV_LAYOUT_OFF: Não alinha as os filhos
- LV_LAYOUT_CENTER: Alinha os filhos ao centro em colunas e mantém o espaço _pad.inner_ entre eles
- LV_LAYOUT_COL_L: Alinha os filhos na coluna esquerda justificada. Mantém o espaço _pad.hor_ à esquerda, espaço _pad.ver_ no topo e _pad.inner_ entre os filhos.
- LV_LAYOUT_COL_M: Alinha os filhos centralizados em coluna. Mantém o espaço _pad.ver_ no topo e o espaço _pad.inner_ entre os filhos.
- LV_LAYOUT_COL_R: Alinha os filhos na coluna justificada à direita. Mantém o espaço _pad.hor_ à direita, o espaço _pad.ver_ no topo e o espaço _pad.inner_ entre os filhos.
- LV_LAYOUT_ROW_T: Alinha os filhos na linha justificada ao topo. Mantém o espaço _pad.hor_ à esquerda, o espaço _pad.ver_ ao topo e o espaço _pad.inner_ entre os filhos
- LV_LAYOUT_ROW_M: Alinha os filhos em linhas centralizadas. Mantém o espaço _pad.hor_ à esquerda e o espaço _pad.inner_ entre os filhos.
- LV_LAYOUT_ROW_B: Alinha os filhos ao fundo da linha justificada. Mantém o espaço _pad.hor_, o espaço _pad.ver_ ao fundo e o espaço _pad.inner_ entre os filhos.
- LV_LAYOUT_PRETTY: Coloca muitos objetos possíveis em uma linha (com pelo menos o espaço _pad.inner_ e o espaço _pad.hor_ ao lado) e começa uma nova linha. Divide o espaço em cada linha igualmente entre os filhos. Mantém o espaço _pad.ver_ no topo e o espaço _pad.inner_ entre as linhas.
- LV_LAYOUT_GRID: Similar ao PRETTY LAYOUT mas não divide o espaço horizontal igualmente apenas deixa o espaço _pad.hor_

Você pode ativar um método **auto ajuste** na qual automaticamente configura o tamanho do contâiner para incluir todos os filhos. Ele manterá o espaço _pad.hor_ à esquerda e à direita e o espaço _pad.ver_ no topo. O auto ajuste pode ativar horizontalmente, verticalmente o em ambas as direções com a função `lv_cont_set_fit(cont, true, true)`. O segundo parâmetro é a horizontal, o terceiro parâmetro é a ativação do ajuste vertical.

## Uso do estilo

- Propriedades **style.body** são usadas

## Notas

- Você **não pode atribuir a posição do filho com os ajustes hor/ver ativados**. Vamos imaginar o que acontece. Se você mudar a posição de somente um filho quando o ajuste estiver ativado no contâiner irá mover/ajustar "em torno" da nova posição. Se você tem mais objetos em um contâiner então você pode alinhar eles relativamente a cada outro.
Com uma solução alternativa você pode criar um pequeno objeto transparente no contâiner. Ele irá fixar o contâiner para não "seguir" os filhos.

## Exemplo

![Container image](http://docs.littlevgl.com/img/container-lv_cont.png)
```c
lv_obj_t * box1;
box1 = lv_cont_create(lv_scr_act(), NULL);
lv_obj_set_style(box1, &lv_style_pretty);
lv_cont_set_fit(box1, true, true);

/*Adiciona um texto ao contâiner*/
lv_obj_t * txt = lv_label_create(box1, NULL);
lv_label_set_text(txt, "Lorem ipsum dolor\n"
                       "sit amet, consectetur\n"
                       "adipiscing elit, sed do\n"
                       "eiusmod tempor incididunt\n"
                       "ut labore et dolore\n"
                       "magna aliqua.");

lv_obj_align(box1, NULL, LV_ALIGN_IN_TOP_LEFT, 10, 10);      /*Alinha o contâiner*/

/*Cria um estilo*/
static lv_style_t style;
lv_style_copy(&style, &lv_style_pretty_color);
style.body.shadow.width = 6;
style.body.padding.hor = 5;                                 /*Configura um espaçamento grande*/

/*Cria um outro contâiner*/
lv_obj_t * box2;
box2 = lv_cont_create(lv_scr_act(), NULL);
lv_obj_set_style(box2, &style);     /*Configura o novo estilo*/
lv_cont_set_fit(box2, true, false); /*Não ativa o ajuste vertical*/
lv_obj_set_height(box2, 55);        /*Configura uma altura fixa*/

/*Adiciona um texto ao novo contâiner*/
lv_obj_t * txt2 = lv_label_create(box2, NULL);
lv_label_set_text(txt2, "No vertical fit 1...\n"
                        "No vertical fit 2...\n"
                        "No vertical fit 3...\n"
                        "No vertical fit 4...");

/*Alinha o contâiner para o fundo do anterior*/
lv_obj_align(box2, box1, LV_ALIGN_OUT_BOTTOM_MID, 30, -30);
```

_Escrito pora v5.1_

## Visão geral

Os objetos de Matrizes de Botões podem mostrar **múltiplos botões** de acordo para um descritor de vetor de string, chamada _map_. Você pode especificar o mapa com `lv_btnm_set_map(btnm, my_map)`.

A **declaração de um mapa** se parece como `const char * map[] = {"btn1", "btn2", "btn3", ""}`. Nota que **o último elemento tem que ser uma string vazia**!

O primeiro caractere de uma string pode ser um **controle de caractere** para especificar alguns atributos:

- **bit 7..6** Sempre _0b10_ para diferenciar o byte de controle vindo de caractere contextual
- **bit 5** Botão inativo
- **bit 4** Sem pressionamento longo para o botão
- **bit 3** Botões escondidos
- **bit 2..0** Comprimento relativo comparado para os botões na mesma coluna. [1..7]

É recomendado para especificar o **byte de controle como um número octal**. Por exemplo `"\213button"`. O número octal sempre começa com _2_ (bit 7..6) o meia parte é os atributos (bit 5..3) e o última parte é o comprimento (bit 2..0). Assim o exemplo descreve um botão escondido com 3 unidade de comprimento.

Use "\n" no mapa para fazer a **quebra de linha**: `{"btn1", "btn2", "\n", "btn3", ""}`. O comprimento do botão é recalculado em cada linha.

A `lv_btnm_set_action(btnm, btnm_action)` especifica uma ação para chamar quando um botão é liberado.

Você pode ativar as **comutação dos botões** quando eles são clicados. Assim podem somente ser um botão comutado em uma vez. O `lv_btnm_set_toggle(btnm, true, id)` ativa a comutação e configura o _id_ésimo botão para o modo comutável.

## Uso do estilo

O uso da matriz de botão funciona com 6 estilos: um background e 5 estilos de botões para cada estado. Você pode configurar estilos com `lv_btnm_set_style(btn, LV_BTNM_STYLE_..., &style)`. O background e os botões usa a propriedade _style.body_. Os rótulos usam a propriedade _style.text_ do estilo de botão.

- **LV_BTNM_STYLE_BG** Estilo de background. Use toda a propriedade _style.body_ incluindo _padding_ Padrão: _lv_style_pretty_
- **LV_BTNM_STYLE_BTN_REL** estilo do botões liberados. Padrão: _lv_style_btn_rel_
- **LV_BTNM_STYLE_BTN_PR** estilo do botões pressionados. Padrão: _lv_style_btn_pr_
- **LV_BTNM_STYLE_BTN_TGL_REL** estilo dos botões comutado-liberado. Padrão: _lv_style_btn_tgl_rel_
- **LV_BTNM_STYLE_BTN_TGL_PR** estilo dos botões comutado-liberado. Padrão: _lv_style_btn_tgl_pr_
- **LV_BTNM_STYLE_BTN_INA** estilo dos botões inativos. Padrão: _lv_style_btn_ina_

## Notas

- O objeto da matriz de botão é **muito leve**. Ele cria somente a base do objeto do background e desenha os botões nele ao invés de criar muitos botões reais.

## Exemplo
![Button matrix image](http://docs.littlevgl.com/img/button-matrix-lv_btnm.png)
```c
/*Chamado quando um botão é liberado ou pressionado longamente*/
static lv_res_t btnm_action(lv_obj_t * btnm, const char *txt)
{
    printf("Button: %s released\n", txt);

    return LV_RES_OK; /*Retorna OK poque o a matriz de botão não está apagada*/
}


.
.
.

/*Cria um vetor de string dodescritor de botão*/
static const char * btnm_map[] = {"1", "2", "3", "4", "5", "\n",
                           "6", "7", "8", "9", "0", "\n",
                           "\202Action1", "Action2", ""};




/*Cria uma matriz de botão padrão*/
lv_obj_t * btnm1 = lv_btnm_create(lv_scr_act(), NULL);
lv_btnm_set_map(btnm1, btnm_map);
lv_btnm_set_action(btnm1, btnm_action);
lv_obj_set_size(btnm1, LV_HOR_RES, LV_VER_RES / 2);

/*Cira um novo estilo do background para a matriz de botão*/
static lv_style_t style_bg;
lv_style_copy(&style_bg, &lv_style_plain);
style_bg.body.main_color = LV_COLOR_SILVER;
style_bg.body.grad_color = LV_COLOR_SILVER;
style_bg.body.padding.hor = 0;
style_bg.body.padding.ver = 0;
style_bg.body.padding.inner = 0;

/*Cria 2 estilos de botões*/
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

/*Cria uma segunda matriz de botão com novos estilos*/
lv_obj_t * btnm2 = lv_btnm_create(lv_scr_act(), btnm1);
lv_btnm_set_style(btnm2, LV_BTNM_STYLE_BG, &style_bg);
lv_btnm_set_style(btnm2, LV_BTNM_STYLE_BTN_REL, &style_btn_rel);
lv_btnm_set_style(btnm2, LV_BTNM_STYLE_BTN_PR, &style_btn_pr);
lv_obj_align(btnm2, btnm1, LV_ALIGN_OUT_BOTTOM_MID, 0, 0);
```

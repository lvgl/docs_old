_Escrito para v5.1_

## Visão geral

As caixas de mensagens agem como **pop-ups**. Elas são construídas de um **background**, um **texto** e **botões**. O background é um objeto [Contâiner](/Container) com um ajuste vertical para garantir que o texto e os botões são serão sempre visíveis.

Para **configurar o texto** use a função `lv_mbox_set_text(mbox, "My text")`.

Os botões são uma matriz de Botões. Para **adicionar botões** use a função `lv_mbox_add_btns(mbox, btn_str, action)`. Neste você pode especificar o texto ex.: (`const char * btn_str[] = {"btn1", "btn2", ""}`) e adicionar um callback na qual é chamado quando um botão é pressioando. Para mais informações visite a documentação [Matriz de botões](https://github.com/littlevgl/lvgl/wiki/Button-matrix).

Com `lv_mbox_start_auto_close(mbox, delay)` a caixa de mensagem pode ser **fechada automaticamente** depois de _delay_ milisegundos com uma longa animação. A função `lv_mbox_stop_auto_close(mbox)` irá parar um auto fechamento iniciado.

O tempo da animação fechar pode ser ajustado pelo `lv_mbox_set_anim_time(mbox, anim_time)`.

## Uso do estilo

Use `lv_mbox_set_style(mbox, LV_MBOX_STYLE_...,  &style)` para configurar um novo estilo para um elemento da caixa de mensagem:

- **LV_MBOX_STYLE_BG** especifica o background do estilo do contâiner. _style.body_ para o backgrounde _style.label_ para a aparência do texto. Padrão: lv_style_pretty
- **LV_MBOX_STYLE_BTN_BG** estilo dos botões background da (matriz de botões). Padrão: lv_style_transp
- **LV_MBOX_STYLE_BTN_REL** estilo dos botões pressionados. Padrão: lv_style_btn_rel
- **LV_MBOX_STYLE_BTN_PR** estilo dos botões pressionados. Padrão: lv_style_btn_pr
- **LV_MBOX_STYLE_BTN_TGL_REL** estilo dos botões comutados deixados de pressioanar. Padrão: lv_style_btn_tgl_rel
- **LV_MBOX_STYLE_BTN_TGL_PR** estilo dos botões pressionados. Padrão: lv_style_btn_tgl_pr
- **LV_MBOX_STYLE_BTN_INA** estilo dos botões inativos. Padrão: lv_style_btn_ina

## Notas

- A **altura dos botões** vem do _font height_ + 2 x _body.vpad_ de _LV_MBOX_STYLE_BTN_REL_

## Exemplo

![Message box image](http://docs.littlevgl.com/img/message-box-lv_mbox.png)
```c
/*Chamado quando um botão é clicado*/
static lv_res_t mbox_apply_action(lv_obj_t * mbox, const char * txt)
{
    printf("Mbox button: %s\n", txt);

    return LV_RES_OK; /*Retorna OK se a mensagem não é apagada*/
}

.
.
.
.

/************************************
 * Cria uma caixa de mensagem padrão
 ************************************/

lv_obj_t * mbox1 = lv_mbox_create(lv_scr_act(), NULL);
lv_mbox_set_text(mbox1, "Default message box\n"
                        "with buttons");                    /*Configura o texto*/
/*Add two buttons*/
static const char * btns[] ={"\221Apply", "\221Close", ""}; /*Descrição do botão. '\221' controle de caractere lv_btnm*/
lv_mbox_add_btns(mbox1, btns, NULL);
lv_obj_set_width(mbox1, 250);
lv_obj_align(mbox1, NULL, LV_ALIGN_IN_TOP_LEFT, 10, 10); /*Alinha ao canto*/

/***********************************************
 * Cria uma caixa de mensagem com novos estilos
 ***********************************************/

/*Cria um novo estilo de background*/
static lv_style_t style_bg;
lv_style_copy(&style_bg, &lv_style_pretty);
style_bg.body.main_color = LV_COLOR_MAKE(0xf5, 0x45, 0x2e);
style_bg.body.grad_color = LV_COLOR_MAKE(0xb9, 0x1d, 0x09);
style_bg.body.border.color = LV_COLOR_MAKE(0x3f, 0x0a, 0x03);
style_bg.text.color = LV_COLOR_WHITE;
style_bg.body.padding.hor = 12;
style_bg.body.padding.ver = 8;
style_bg.body.shadow.width = 8;

/*Cria um estilo de botões pressionado e deixado de pressionar*/
static lv_style_t style_btn_rel;
static lv_style_t style_btn_pr;
lv_style_copy(&style_btn_rel, &lv_style_btn_rel);
style_btn_rel.body.empty = 1;                    /*Desenha somente a borda*/
style_btn_rel.body.border.color = LV_COLOR_WHITE;
style_btn_rel.body.border.width = 2;
style_btn_rel.body.border.opa = LV_OPA_70;
style_btn_rel.body.padding.hor = 12;
style_btn_rel.body.padding.ver = 8;

lv_style_copy(&style_btn_pr, &style_btn_rel);
style_btn_pr.body.empty = 0;
style_btn_pr.body.main_color = LV_COLOR_MAKE(0x5d, 0x0f, 0x04);
style_btn_pr.body.grad_color = LV_COLOR_MAKE(0x5d, 0x0f, 0x04);

/*Copia a caixa de mensagem (Os botões serão copiados também)*/
lv_obj_t * mbox2 = lv_mbox_create(lv_scr_act(), mbox1);
lv_mbox_set_text(mbox2, "Message box with\n"
                        "with modified styles");
lv_mbox_set_style(mbox2, LV_MBOX_STYLE_BG, &style_bg);
lv_mbox_set_style(mbox2, LV_MBOX_STYLE_BTN_REL, &style_btn_rel);
lv_mbox_set_style(mbox2, LV_MBOX_STYLE_BTN_PR, &style_btn_pr);
lv_obj_align(mbox2, mbox1, LV_ALIGN_OUT_BOTTOM_LEFT, 50, -20);   /*Alinha de acordo com a caixa de mensagem prévia*/
```

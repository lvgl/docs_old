## Visão geral

Os objetos de caixa de checagem são construídos de um Botão **background** na qual contém também um Botão **bala** e um **rótulo** para realizar uma caixa de checagem clássica. O **texto** pode ser modificado pela funcão `lv_cb_set_text(cb, "New text")`.

Uma **ação** pode ser assinada por `lv_cb_set_action(cb, action)`.

Você pode manualmente **marcar / desmarcar** a checagem via `lv_cb_set_checked(cb, state)`.

## Uso do estilo

O estilo da caixa de checagem pode ser modificada com `lv_cb_set_style(cb, LV_CB_STYLE_..., &style)`.

- **LV_CB_STYLE_BG** Estilo do background. Usa todas as propriedades _style.body_. O rótulo do estilo vem de _style.text_. Padrão: _lv_style_transp_
- **LV_CB_STYLE_BOX_REL** Estilo do caixa ao deixar de pressionar. Use a propriedade _style.body_. Padrão: _lv_style_btn_rel_
- **LV_CB_STYLE_BOX_PR** Estilo da caixa pressionada. Use a propriedade _style.body_. Padrão: _lv_style_btn_pr_
- **LV_CB_STYLE_BOX_TGL_REL** Estilo deixar de pressionar caixa de checagem. Use a propriedade _style.body_. Padrão: _lv_style_btn_tgl_rel_
- **LV_CB_STYLE_BOX_TGL_PR** Estilo da caixa de checagem deixar de pressionar. Use a propriedade _style.body_. Padrão: _lv_style_btn_tgl_pr_

## Exemplo
![Checkbox image](http://docs.littlevgl.com/img/check-box-lv_cb.png)
```c
static lv_res_t cb_release_action(lv_obj_t * cb)
{
    /*Um caixa de checagem é clicada*/
    printf("%s state: %d\n", lv_cb_get_text(cb), lv_cb_is_checked(cb));

    return LV_RES_OK;
}

.
.
.


/************************************************
 * Cria um container para as caixas de checagem
 ************************************************/

/*Cria o estilo da borda*/
static lv_style_t style_border;
lv_style_copy(&style_border, &lv_style_pretty_color);
style_border.glass = 1;
style_border.body.empty = 1;

/*Cria um container*/
lv_obj_t * cont;
cont = lv_cont_create(lv_scr_act(), NULL);
lv_cont_set_layout(cont, LV_LAYOUT_COL_L);      /*Organiza os filhos em uma coluna*/
lv_cont_set_fit(cont, true, true);              /*Combina o tamanho para o conteúdo*/
lv_obj_set_style(cont, &style_border);

/*****************************
 * Cria as caixas de checagem
 *****************************/

/*Cria uma caixa de checagem*/
lv_obj_t * cb;
cb = lv_cb_create(cont, NULL);
lv_cb_set_text(cb, "Potato");
lv_cb_set_action(cb, cb_release_action);

/*Copia a caixa de checagem prévia*/
cb = lv_cb_create(cont, cb);
lv_cb_set_text(cb, "Onion");

/*Copia a caixa de checagem prévia*/
cb = lv_cb_create(cont, cb);
lv_cb_set_text(cb, "Carrot");

/*Copia a caixa de checagem prévia*/
cb = lv_cb_create(cont, cb);
lv_cb_set_text(cb, "Salad");

/*Alinha o container para o meio*/
lv_obj_align(cont, NULL, LV_ALIGN_CENTER, 0, 0);
```

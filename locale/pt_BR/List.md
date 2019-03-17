_Escrito para v5.1_

## Visão geral

As listas são construídas de uma **Página** e **Botões** como background. Os Botões contém uma uma imagem opcional (na qual pode ser um símbolo também) e um Rótulo. Quando a lista se torna longa o bastante ela pode ser deslizável. O **comprimento dos botões** é configurado para o máximo de acordo com o comprimento do objeto. A **altura** dos botões sãoo ajustados automaticamente de acordo ao conteúdoo (altura do conteúdo + style.body.padding.ver).

Você pode **adicionar novos elementos na lista** com `lv_list_add(list, "U:/img", "Text", rel_action)` ou com icone de símbolo `lv_list_add(list, SYMBOL_EDIT, "Edit text")`. Se você não quer adicionar imagem use `""` como nome de arquivo. A função retorna com um ponteiro ao botão criado para permitir configurações futuras

Você pode usar `lv_list_get_btn_label(list_btn)` e `lv_list_get_btn_img(list_btn)` para **obter o rótulo e a imagem** de uma lista de botão.
 
Na ação de lançamento de um botãoo você pode obter o **texto do botão** com `lv_list_get_btn_text(button)`. Isto ajuda a identificar a lista do elemento lançada.

Para **apagar a lista de elemento** use `lv_obj_del()` no valor de retorno de `lv_list_add()`.

Você pode **navegar manualmente** na lista com `lv_list_up(list)` e `lv_list_down(list)`.

Você pode focar em um botão diretamente usando `lv_list_focus(btn, anim_en)`.

O **tempo de animação** de movimentos acima/abaixo/foco pode ser configurado via: `lv_list_set_anim_time(list, anim_time)`. Zero animação significa nenhuma animação.

## Uso do estilo

A função `lv_list_set_style(list, LV_LIST_STYLE_..., &style)` configura o estilo de uma lista. Para explicação dos detalhes de _BG_, _SCRL_ e _SB_ veja [Página](/Page)

- **LV_LIST_STYLE_BG** lisa o estilo do background. Padrão: _lv_style_transp_fit_
- **LV_LIST_STYLE_SCRL** parte deslizável do estilo. Padrão: _lv_style_pretty_
- **LV_LIST_STYLE_SB** estilo da barra de rolagem. Padrão: _lv_style_pretty_color_
- **LV_LIST_STYLE_BTN_REL** estilo do botão deixado de pressionar. Padrão: _lv_style_btn_rel_
- **LV_LIST_STYLE_BTN_PR** estilo do botão pressionado. Padrão: _lv_style_btn_pr_
- **LV_LIST_STYLE_BTN_TGL_REL** estilo do botão comutado. Padrão _lv_style_btn_tgl_rel_
- **LV_LIST_STYLE_BTN_TGL_PR** estilo do botão pressionado. Padrão: _lv_style_btn_tgl_pr_
- **LV_LIST_STYLE_BTN_INA** estilo do botão inativo. Padrão: _lv_style_btn_ina_

## Notas

- Você pode configurar um background transparente para a lista. Neste caso, se você tem somente umas poucas listas de botões a lista se parecerar menor mas se torna deslizável quanto mais lista de elementos são adicionadas.
- O modo do comprimento padrão dos rótulos de botão é `LV_LABEL_LONG_ROLL`. Você pode modificá-lo manualmente. Use `lv_list_get_btn_label()` para obter rótulos de botões.
- Para **modificar a altura dos botões** ajuste o campo _body.padding.ver_ do estilo correspondente (LV_LIST_STYLE_BTN_REL , LV_LIST_STYLE_BTN_PR etc.)

## Exemplo
![List image](http://docs.littlevgl.com/img/list-lv_list.png)
```c
/*Serpa chamado no clique na lista de botão*/
static lv_res_t list_release_action(lv_obj_t * list_btn)
{
    printf("List element click:%s\n", lv_list_get_btn_text(list_btn));

    return LV_RES_OK; /*Retorna OK porque a lista não foi apagada*/
}

.
.
.

/************************
 * Cria a lista padrão
 ************************/

/*Cria a lista*/
lv_obj_t * list1 = lv_list_create(lv_scr_act(), NULL);
lv_obj_set_size(list1, 130, 170);
lv_obj_align(list1, NULL, LV_ALIGN_IN_TOP_LEFT, 20, 40);

/*Adiciona a lista de elementos*/
lv_list_add(list1, SYMBOL_FILE, "New", list_release_action);
lv_list_add(list1, SYMBOL_DIRECTORY, "Open", list_release_action);
lv_list_add(list1, SYMBOL_CLOSE, "Delete", list_release_action);
lv_list_add(list1, SYMBOL_EDIT, "Edit", list_release_action);
lv_list_add(list1, SYMBOL_SAVE, "Save", list_release_action);

/*Cria um rótulo acima da lista*/
lv_obj_t * label;
label = lv_label_create(lv_scr_act(), NULL);
lv_label_set_text(label, "Default");
lv_obj_align(label, list1, LV_ALIGN_OUT_TOP_MID, 0, -10);

/*********************
 * Cria novos estilos
 ********************/
/*Cria um estilo de barra de rolagem*/
static lv_style_t style_sb;
lv_style_copy(&style_sb, &lv_style_plain);
style_sb.body.main_color = LV_COLOR_BLACK;
style_sb.body.grad_color = LV_COLOR_BLACK;
style_sb.body.border.color = LV_COLOR_WHITE;
style_sb.body.border.width = 1;
style_sb.body.border.opa = LV_OPA_70;
style_sb.body.radius = LV_RADIUS_CIRCLE;
style_sb.body.opa = LV_OPA_60;

/*Cria estilos para os botões*/
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

/*****************************************
 * Cria uma lista com estilos modificados
 *****************************************/

/*Copia a lista prévia*/
lv_obj_t * list2 = lv_list_create(lv_scr_act(),list1);
lv_obj_align(list2, NULL, LV_ALIGN_IN_TOP_RIGHT, -20, 40);
lv_list_set_sb_mode(list2, LV_SB_MODE_AUTO);
lv_list_set_style(list2, LV_LIST_STYLE_BG, &lv_style_transp_tight);
lv_list_set_style(list2, LV_LIST_STYLE_SCRL, &lv_style_transp_tight);
lv_list_set_style(list2, LV_LIST_STYLE_BTN_REL, &style_btn_rel); /*Configura o estilo do novo botão*/
lv_list_set_style(list2, LV_LIST_STYLE_BTN_PR, &style_btn_pr);

/*Cria um rótulo acima da lista*/
label = lv_label_create(lv_scr_act(), label);       /*Copia o rótulo anterior*/
lv_label_set_text(label, "Modified");
lv_obj_align(label, list2, LV_ALIGN_OUT_TOP_MID, 0, -10);
```

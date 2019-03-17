_Escrito para v5.1, revisão 2_

## Visão geral

Botões podem reagir quando o usuário **pressiona**, **solta** ou **pressiona longamente**, via funções de callback (`lv_action_t` function pointers). Você pode configurar os funções callback com: `lv_btn_set_action(btn, ACTION_TYPE, callback_func)`. Os possíveis tipos de ação são:

- LV_BTN_ACTION_CLICK: o botão é solto depois de pressionado (clicado) ou, quando usar o keypad, depois que a tecla `LV_GROUP_KEY_ENTER` é solta
- LV_BTN_ACTION_PR: o botão é pressionado
- LV_BTN_ACTION_LONG_PR: o botão é pressionado longamente
- LV_BTN_ACTION_LONG_PR_REPEAT: o botão é pressionado e essa ação é gatilhada periodicamente

Botões podem ser um dos **cinco possíveis estados**:

- LV_BTN_STATE_REL Estado solto
- LV_BTN_STATE_PR Estado pressionado
- LV_BTN_STATE_TGL_REL Estado comutado (Estado Ligado)
- LV_BTN_STATE_TGL_PR Estado comutado pressionado (Estado Ligado pressionado)
- LV_BTN_STATE_INA Estado inativo

Os botões podem ser configurados como **botões comutados** com `lv_btn_set_toggle(btn, true)`. Nesse caso ao soltar, o botão vai pra o estado comutado solto.

Você pode configurar os estados dos botões manualmente através do: `lv_btn_set_state(btn, LV_BTN_STATE_TGL_REL)`.

Um botão pode ir para **Estado inativo** somente manualmente (através do _lv_btn_set_state()_). Em um Estado inativo, nehuma das ações será chamada.

Similarmente para [Containers](/Container) botões também possuem **layout** e **auto ajuste**:

- Configuração de layout `lv_btn_set_layout(btn, LV_LAYOUT_...) `. O padrão é LV_LAYOUT_CENTER. Assim, se você adicionar um rótulo ele será automaticamente alinhado ao meio.
- `lv_btn_set_fit(btn, hor_en, ver_en)` ativa para configurar o comprimento do botão e/ou altura automaticamente de acordo com os filhos.

## Uso de estilos

Um botão pode ter 5 estilos independentes para os 5 estados. Você pode configurá-los via: `lv_btn_set_style(btn, LV_BTN_STYLE_..., &style)`. Os estilos usam a propriedade _style.body_.

- **LV_BTN_STYLE_REL** estilo do estado solto. Padrão: _lv_style_btn_rel_
- **LV_BTN_STYLE_PR** estilo do estado pressiondo. Padrão: _lv_style_btn_pr_
- **LV_BTN_STYLE_TGL_REL** estilo do estado comutado. Padrão: _lv_style_btn_tgl_rel_
- **LV_BTN_STYLE_TGL_PR** estilo do estado comutado pressionado. Padrão: _lv_style_btn_tgl_pr_
- **LV_BTN_STYLE_INA** estilo do estado inativo. Padrão: _lv_style_btn_ina_

## Notas

- Se um botão é arrastado seu clique e pressionamento longo as ações não serão chamadas
- Se um botão foi pressionado longamente e sua ação longa ao pressionar foi configurada então sua ação clique não será chamada

## Exemplo
![Button image](http://docs.littlevgl.com/img/button-lv_btn.png)
```c
static lv_res_t btn_click_action(lv_obj_t * btn)
{
    uint8_t id = lv_obj_get_free_num(btn);

    printf("Button %d is released\n", id);

    /* O botão é solto.
     * Faça algo aqui */

    return LV_RES_OK; /*Retorna OK se o botão não está apagado*/
}

.
.
.

/*Cria um rótulo para o título*/
lv_obj_t * label = lv_label_create(lv_scr_act(), NULL);
lv_label_set_text(label, "Default buttons");
lv_obj_align(label, NULL, LV_ALIGN_IN_TOP_MID, 0, 5);

/*Cria um botão normal*/
lv_obj_t * btn1 = lv_btn_create(lv_scr_act(), NULL);
lv_cont_set_fit(btn1, true, true); /*Ativa redimensionamento horizontal e vertical*/
lv_obj_align(btn1, label, LV_ALIGN_OUT_BOTTOM_MID, 0, 10);
lv_obj_set_free_num(btn1, 1);   /*Configura um único número para o botão*/
lv_btn_set_action(btn1, LV_BTN_ACTION_CLICK, btn_click_action);

/*Adiciona um rótulo para o botão*/
label = lv_label_create(btn1, NULL);
lv_label_set_text(label, "Normal");

/*Copia o botão e atribui o estado comutado. (A ação soltar é copiada também)*/
lv_obj_t * btn2 = lv_btn_create(lv_scr_act(), btn1);
lv_obj_align(btn2, btn1, LV_ALIGN_OUT_BOTTOM_MID, 0, 10);
lv_btn_set_state(btn2, LV_BTN_STATE_TGL_REL);  /*Atribui o estado comutado*/
lv_obj_set_free_num(btn2, 2);               /*Atribui um único número para o botão*/

/*Adiciona um rótulo para o botão comutado*/
label = lv_label_create(btn2, NULL);
lv_label_set_text(label, "Toggled");

/*Copia o botão e configura o estado inativo.*/
lv_obj_t * btn3 = lv_btn_create(lv_scr_act(), btn1);
lv_obj_align(btn3, btn2, LV_ALIGN_OUT_BOTTOM_MID, 0, 10);
lv_btn_set_state(btn3, LV_BTN_STATE_INA);   /*Atribui o estado inativo*/
lv_obj_set_free_num(btn3, 3);               /*Atribui um único número para o botão*/

/*Adiciona um rótulo para o botão inativo*/
label = lv_label_create(btn3, NULL);
lv_label_set_text(label, "Inactive");
```

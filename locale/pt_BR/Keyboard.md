_Escrito para v5.1_

## Visão geral

Como o nome mostra o objeto **Teclado** provém um teclado para **escrever texto**. Você pode assinar uma [Área de texto](/Text-area) para o Teclado para colocar os caracteres digitados lá. Para assinar a Área de texto use `lv_kb_set_ta(kb, ta)`.

O Teclado contém um botão _Ok_ e um botão _Hide_. Em ações ok e hide você podem ser especificados por `lv_kb_set_ok_action(kb, action)` e `lv_kb_set_hide_action(kb, action)` para adicionar callbacks para os cliques Ok/Hide. Se nenhuma ação é especificada então os botões irá apagar o Teclado.

A Área de texto assinada **cursor** pode ser **gerenciado** teclado: quando o teclado é assinado a área de texto prévio do cursor será escondido e a nova área de texto será mostrada. Clicando em _Ok_ ou _Hide_ irá também esconder o cursor. O gerenciador do cursor é ativado pelo `lv_kb_set_cursor_manage(kb, true)`. O padrão é não gerenciar.

Os teclados tem dois **modos**:

- LV_KB_MODE_TEXT: mostra letras, números e caracteres especiais
- LV_KB_MODE_NUM: mostra números, sinais +/- e pontos

Para configurar o modo use `lv_kb_set_mode(kb, mode)`. O padrão é _LV_KB_MODE_TEXT_

Você pode especificar um **novo mapa** (layout) para o teclado com `lv_kb_set_map(kb, map)`. Ele funciona como a [Matriz de botões](/Button-matrix) assim, controlar caractere pode ser adicionado ao layout para configurar o comprimento do botão e outros atributos. Mantenha em mente que usar as seguintes palavras-chave terá o mesmo efeito com o mapeamento original: _SYMBOL_OK_, _SYMBOL_CLOSE_, _SYMBOL_LEFT_, _SYMBOL_RIGHT_, _ABC_, _abc_, _Enter_, _Del_, _#1_, _+/-_ .

## Uso do estilo

O teclado funciona com 6 estilos: um background e 5 estilos de botões para cada estado. Você pode confiigurar estilos com `lv_kb_set_style(btn, LV_KB_STYLE_..., &style)`. O background e os botões use a propriedade _style.body_. Para os rótulos use a propriedade _style.text_ dos estilos de botões.

- **LV_KB_STYLE_BG** Estilo do background. Use todas as propriedades _style.body_ incluindo _padding_. Padrão: _lv_style_pretty_
- **LV_KB_STYLE_BTN_REL** estilo ao deixar de pressionar. Padrão: _lv_style_btn_rel_
- **LV_KB_STYLE_BTN_PR** estilo ao pressionar. Padrão: _lv_style_btn_pr_
- **LV_KB_STYLE_BTN_TGL_REL** estilo ao comutar. Padrão: _lv_style_btn_tgl_rel_
- **LV_KB_STYLE_BTN_TGL_PR** estilo do botão comutado. Padrão: _lv_style_btn_tgl_pr_
- **LV_KB_STYLE_BTN_INA** estilo do botão inativo. Padrão: _lv_style_btn_ina_

## Exemplo
![Keyboard image](http://docs.littlevgl.com/img/keyboard-lv_kb.png)
```c
/*Cria estilos para o teclado*/
static lv_style_t rel_style, pr_style;

lv_style_copy(&rel_style, &lv_style_btn_rel);
rel_style.body.radius = 0;

lv_style_copy(&pr_style, &lv_style_btn_pr);
pr_style.body.radius = 0;

/*Cria um teclado e aplica os estilos*/
lv_obj_t *kb = lv_kb_create(lv_scr_act(), NULL);
lv_kb_set_cursor_manage(kb, true);
lv_kb_set_style(kb, LV_KB_STYLE_BG, &lv_style_transp_tight);
lv_kb_set_style(kb, LV_KB_STYLE_BTN_REL, &rel_style);
lv_kb_set_style(kb, LV_KB_STYLE_BTN_PR, &pr_style);

/*Cria uma área de texto. O teclado escreverá aqui*/
lv_obj_t *ta = lv_ta_create(lv_scr_act(), NULL);
lv_obj_align(ta, NULL, LV_ALIGN_IN_TOP_MID, 0, 10);
lv_ta_set_text(ta, "");

/*Assina a área de texto para o teclado*/
lv_kb_set_ta(kb, ta);
```

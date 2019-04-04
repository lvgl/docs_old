_Escrito para v5.1_

## Visão geral

A Área de Texto é **uma página** com um **rótulo** e um **cursor** nele. Você pode **inserir texto ou caracteres** para a posição atual com:

- `lv_ta_add_char(ta, 'c')`
- `lv_ta_add_text(ta, "insert this text")`

O `lv_ta_set_text(ta, "New text")` **muda o texto todo**.

Para **apagar um caractere** da esquerda da posição do cursor use `lv_ta_del_char(ta)`.

A posição do cursor pode ser modificada diretamente como `lv_ta_set_cursor_pos(ta, 10)` ou por passo:

- `lv_ta_cursor_right(ta)`
- `lv_ta_cursor_left(ta)`
- `lv_ta_cursor_up(ta)`
- `lv_ta_cursor_down(ta)`

Existem vários tipos de cursores. Você pode configurar um deles com: `lv_ta_set_cursor_type(ta, LV_CURSOR_...)`

- LV_CURSOR_NONE
- LV_CURSOR_LINE
- LV_CURSOR_BLOCK
- LV_CURSOR_OUTLINE
- LV_CURSOR_UNDERLINE

Você pode 'OR' _LV_CURSOR_HIDDEN_ para qualquer tipo para esconder o cursor.

A área de texto pode ser configurada para ser uma linha com `lv_ta_set_one_line(ta, true)`.

A área de texto suporta **modo de senha**. Ele pode ser ativado com `lv_ta_set_pwd_mode(ta, true)`.

## Uso do estilo

Use `lv_ta_set_style(page, LV_TA_STYLE_...,  &style)` para configurar um novo estilo para um elemento da área de texto:

- **LV_TA_STYLE_BG** estilo do background na qual usa todas as propriedades _style.body_. O rótulo também usa esse _style.label_ deste estilo. (padrão: lv_style_pretty)
- **LV_TA_STYLE_SB** estilo de barra de rolagem na qual usa todas as propriedades do _style.body_ (padrão: lv_style_transp)
- **LV_TA_STYLE_CURSOR** estilo de cursor. Se NULL então a biblioteca configura para nós um estilo automaticamente de acordo com a cor do rótulo e fonte

    - LV_CURSOR_LINE: uma longa _style.line.width_ linha mais desenhado como um retangulo como espaçamento _style.body_ horizontais e verticais dá um espaço sobre o cursor
    - LV_CURSOR_BLOCK: um retangulo como espaçamentos _style.body_ horizontais e verticais que fazem o retangulo mais largo
    - LV_CURSOR_OUTLINE: um retangulo vazio (somente uma borda) como espaçamentos _style.body_ horizontais e verticais que fazem o retangulo mais largo
    - LV_CURSOR_UNDERLINE: uma linha de comprimento _style.line.width_ mas desenhada como retangulo como espaçamentos horizontais e verticais que fazem um offset sobre o cursor

## Notas

- No modo senha `lv_ta_get_text(ta)` te dá o texto real e não o caractere asteristico

## Exemplo
![Text area image](http://docs.littlevgl.com/img/text-area-lv_ta.png)
```c
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

/*Cria uma área de texto normal*/
lv_obj_t * ta1 = lv_ta_create(lv_scr_act(), NULL);
lv_obj_set_size(ta1, 200, 100);
lv_obj_align(ta1, NULL, LV_ALIGN_CENTER, 0, - LV_DPI / 2);
lv_ta_set_style(ta1,LV_TA_STYLE_SB, &style_sb);                     /*Aplica o estilo da barra de rolagem*/
lv_ta_set_cursor_type(ta1, LV_CURSOR_BLOCK);
lv_ta_set_text(ta1, "A text in a Text Area\n"
               "You can scroll it if the text is long enough.");    /*Atribui um texto inicial*/
lv_ta_set_cursor_pos(ta1, 2);                                       /*Configura a posição do cursor*/
lv_ta_add_text(ta1, "long ");                                       /*Insere uma palavra a posição atual do cursor*/

static lv_style_t style_bg;
lv_style_copy(&style_bg, &lv_style_pretty);
style_bg.body.shadow.width = 8;
style_bg.text.color = LV_COLOR_MAKE(0x30, 0x60, 0xd0);              /*Rótulo azul*/

/*Cria um teste alinhado no modo senha*/
lv_obj_t * ta2 = lv_ta_create(lv_scr_act(), ta1);
lv_obj_align(ta2, ta1, LV_ALIGN_OUT_BOTTOM_MID, 0, 50);
lv_ta_set_style(ta2,LV_TA_STYLE_BG, &style_bg);                     /*Aplica o estilo do background*/
lv_ta_set_one_line(ta2, true);
lv_ta_set_cursor_type(ta2, LV_CURSOR_LINE);
lv_ta_set_pwd_mode(ta2, true);
lv_ta_set_text(ta2, "Password");
```

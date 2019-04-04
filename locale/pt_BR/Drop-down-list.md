_Escrito para v5.3, revisão 2_

## Visão geral

Lista suspensa permite a você simplesmente **selecionar uma opção entre várias**. A lista suspensa é fechada por padrão e mostra o texto selecionado corrente. Se você clicar nele nessa lista aberta e todas as opções são mostradas.

As **opções** que são passadas à lista suspensa como um **string** com `lv_ddlist_set_options(ddlist, options)`. As opções devem ser separadas por `\n`. Por exemplo: `"First\nSecond\nThird"`.

Você pode **selecionar uma opção manualmente** com `lv_ddlist_set_selected(ddlist, id)`, onde _id_ é o índice de uma opção.

Uma **função callback** pode ser especificada com `lv_ddlist_set_action(ddlist, my_action)` para chamar quando uma nova opção é selecionada.

Por padrão a **altura** das listas é ajustada automaticamente para mostrar todas as opções. O `lv_ddlist_set_fix_height(ddlist, h)` configura a altura fixa para a lista aberta.

O **comprimento** é também ajustado automaticamente. Para evitar isto aplique `lv_ddlist_set_hor_fit(ddlist, false)` e configure o comprimento manualmente através de `lv_obj_set_width(ddlist, width)`.

Similarmente para [Pagína](/Page) com altura fixada a lista suspensa que suporta vários **modos de barra de rolagem de display**. Ele pode ser configurado por `lv_ddlist_set_sb_mode(ddlist, LV_SB_MODE_...)`.

A animação da lista suspensa do tempo abre/fecha é ajustado por `lv_ddlist_set_anim_time(ddlist, anim_time)`. Tempo zero de animação significa nenhuma animação.

**Novo em v5.3** é a abilidade para ativar um vertor no lado da lista suspensa. Para usar esse recurso você pode chamar `lv_ddlist_set_draw_arrow(ddlist, true)`.

## Uso do estilo

O `lv_ddlist_set_style(ddlist, LV_DDLIST_STYLE_..., &style)` configura os estilos de uma lista suspensa.

- **LV_DDLIST_STYLE_BG** Estilo do background. Toda propriedade _style.body_ são usadas. Ele é usado para o estilo do rótulo do _style.text_. Padrão: _lv_style_pretty_
- **LV_DDLIST_STYLE_SEL** Estilo da opção selecionada. A propriedade _style.body_ é usada. A opção selecionada será recolorida com _text.color_. Padrão: _lv_style_plain_color_
- **LV_DDLIST_STYLE_SB** Estilo da barra de rolagem. A propriedade _style.body_ é usada. Padrão: _lv_style_plain_color_

## Exemplo
![Drop down list image](http://docs.littlevgl.com/img/drop-down-list-lv_ddlist.png)
```c
static lv_res_t ddlist_action(lv_obj_t * ddlist)
{
    uint8_t id = lv_obj_get_free_num(ddlist);

    char sel_str[32];
    lv_ddlist_get_selected_str(ddlist, sel_str);
    printf("Ddlist %d new option: %s \n", id, sel_str);

    return LV_RES_OK; /*Retorna OK se a lista suspensa não foi apagada*/
}


.
.
.

/*Cria uma lista suspensa*/
lv_obj_t * ddl1 = lv_ddlist_create(lv_scr_act(), NULL);
lv_ddlist_set_options(ddl1, "Apple\n"
                            "Banana\n"
                            "Orange\n"
                            "Melon\n"
                            "Grape\n"
                            "Raspberry");
lv_obj_align(ddl1, NULL, LV_ALIGN_IN_TOP_LEFT, 30, 10);
lv_obj_set_free_num(ddl1, 1);               /*Atribui uma única ID*/
lv_ddlist_set_action(ddl1, ddlist_action);  /*Atribui uma função para chamar quando uma nova opção é escolhida*/

/*Cria um estilo*/
static lv_style_t style_bg;
lv_style_copy(&style_bg, &lv_style_pretty);
style_bg.body.shadow.width = 4; /*Ativa a sombra*/
style_bg.text.color = LV_COLOR_MAKE(0x10, 0x20, 0x50);

/*Copia a lista suspensa e configura o novo style_bg*/
lv_obj_t * ddl2 = lv_ddlist_create(lv_scr_act(), ddl1);
lv_obj_align(ddl2, NULL, LV_ALIGN_IN_TOP_RIGHT, -30, 10);
lv_obj_set_free_num(ddl2, 2);       /*Atribui uma única ID*/
lv_obj_set_style(ddl2, &style_bg);
```

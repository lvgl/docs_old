_Escrito para v5.1_
Atualizado para v5.2
## Visão geral

A rolagem permite a você simplesmente **selecionar uma opção de várias** com deslizamento. Suas funcionalidades são similares ao [Lista suspensa](/Drop-down-list).

As **opções** são passadas para a Rolagem como uma **string** com `lv_roller_set_options(roller, options)`. As opções devem ser separadas pelo `\n`. Por exemplo: `"First\nSecond\nThird"`.

Você pode **selecionar uma opção manualmente** com `lv_roller_set_selected(roller, id)`, onde _id_ é o índice de uma opção.

Uma **função callback** pode ser especificada com `lv_roller_set_action(roller, my_action)` para chamar quando uma nova opção é selecionada.

A **altura** da rolagem pode ser ajustada com `lv_roller_set_visible_row_count(roller, row_cnt)` para configurar o número de opções visíveis.

O **comprimento** é ajustado automaticamente. Para evitar isso, aplique `lv_roller_set_hor_fit(roller, false)` e configure o comprimento manualmente pelo `lv_obj_set_width(roller, width)`. Você deve usar `lv_roller_set_hor_fit(roller, false)` ao invés de `lv_cont_set_fit(lv_page_get_scrl(roller), false, false);`, por outro lado você obterá um estilo LV_LABEL_ALIGN_LEFT do texto da lista do rótulo.

O tempo da **animação** abrir/fechar da Lista suspensa é ajusdado pelo `lv_roller_set_anim_time(roller, anim_time)`. Animação zero siginifica nenhuma animação. Esta característica é implementada junto com lv_ddlist.c na v5.2: `lv_ddlist_set_anim_time(roller, anim_time);` deve ser usado para animação.

## Uso do estilo

O `lv_roller_set_style(roller, LV_ROLLER_STYLE_..., &style)` configura o estilo de uma rolagem.

- **LV_ROLLER_STYLE_BG** Estilo do background. Todos as propriedades do _style.body_ são usadas. Ele é usado para o estilo do rótulo de _style.text_. Gradiente é aplicado no topo e no fundo também. Padrão: _lv_style_pretty_
- **LV_DDLIST_STYLE_SEL** Estilo da opção selecionada. As propriedades _style.body_ são usadas. A opção selecionada será recolorida com _text.color_. Padrão: _lv_style_plain_color_

## Exemplo
![Roller image](http://docs.littlevgl.com/img/roller-lv_roller.png)
```c
/*Cria uma lista suspensa padrão*/
lv_obj_t *roller1 = lv_roller_create(lv_scr_act(), NULL);
lv_roller_set_options(roller1, "Apple\n"
                               "Broccoli\n"
                               "Cabbage\n"
                               "Dewberry\n"
                               "Eggplant\n"
                               "Fig\n"
                               "Grapefruit");
lv_obj_set_pos(roller1, 50, 80);


/*Cria estilos*/
static lv_style_t bg_style;
lv_style_copy(&bg_style, &lv_style_pretty);
bg_style.body.main_color = LV_COLOR_WHITE;
bg_style.body.grad_color = LV_COLOR_HEX3(0xddd);
bg_style.body.border.width = 0;
bg_style.text.line_space = 20;
bg_style.text.opa = LV_OPA_40;

static lv_style_t sel_style;
lv_style_copy(&sel_style, &lv_style_pretty);
sel_style.body.empty = 1;
sel_style.body.radius = LV_RADIUS_CIRCLE;
sel_style.text.color = LV_COLOR_BLUE;

/*Cria uma lista suspensa e aplica novos estilos*/
lv_obj_t *roller2 = lv_roller_create(lv_scr_act(), NULL);
lv_roller_set_options(roller2, "0\n"
                               "1\n"
                               "2\n"
                               "3\n"
                               "4\n"
                               "5\n"
                               "6\n"
                               "7\n"
                               "8\n"
                               "9");
lv_roller_set_style(roller2, LV_ROLLER_STYLE_BG, &bg_style);
lv_roller_set_selected(roller2, 3, false);
lv_roller_set_style(roller2, LV_ROLLER_STYLE_SEL, &sel_style);
lv_roller_set_visible_row_count(roller2, 3);
lv_roller_set_hor_fit(roller2, false);
lv_obj_set_width(roller2, 40);
lv_obj_set_pos(roller2, 220, 50);
```

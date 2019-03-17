_Escrito para v5.1_

## Visão geral

O objeto Visualizador de Tab pode ser usado para **organizar conteúdos em tabulações**. Você pode **adicionar uma nova tab** com `lv_tabview_add_tab(tabview, "Tab name")`. Ele retornará com um ponteiro para um objeto [Página](/Page) onde você pode adicionar o conteúdo das tabulações.

Para **selecionar um tab** você pode:

- Clicar nele na parte do cabeçalho
- Deslizar horizontalmente
- Use a função `lv_tabview_set_tab_act(tabview, id, anim_en)`

O **deslizamento manual** pode ser desativado com `lv_tabview_set_sliding(tabview, false)`.

O **tempo de animação** é ajustado pelo `lv_tabview_set_anim_time(tabview, anim_time)`.

Uma **função callback** pode ser assinado para evento **carga de tab** com `lv_tabview_set_tab_load_action(tabview, action)`. A função de chamada precisa ter os seguintes protótipos:

```c
void callback(lv_obj_t * tabview, uint16_t act_id);
```

Onde _act_id_ significa tabulação na qual será carregada. Na ação `lv_tabview_get_tab_act(tabview)` dará a id da tabulação antiga.

## Uso do estilo

Use `lv_tabview_set_style(tabview, LV_TABVIEW_STYLE_...,  &style)` para configurar um novo estilo para um elemento do novo visualizador de tabulação:

- **LV_TABVIEW_STYLE_BG** principal background na qual usa todas as propriedades _style.body_ (padrão: lv_style_plain)
- **LV_TABVIEW_STYLE_INDIC** um fino retângulo no topo para indicar a tabulação atual. Use todas as propriedades _style.body_. Sua altura vem de _body.padding.inner_ (padrão: _lv_style_plain_color_)
- **LV_TABVIEW_STYLE_BTN_BG** estilo dos botões de tabulação do background. Use todas as propriedades do _style.body_. A altura do cabeçalho será configurado automaticamente considerando _body.padding.ver_ (padrão: _lv_style_transp_)
- **LV_TABVIEW_STYLE_BTN_REL** estilo dos botões de tabulação soltos. Use todas propriedades _style,body_. (padrão: _lv_style_tbn_rel_)
- **LV_TABVIEW_STYLE_BTN_PR** estilo dos botões de tabulação pressionado. Use todas propriedades _style.body_. (padrão _lv_style_tbn_rel_)
- **LV_TABVIEW_STYLE_BTN_TGL_REL** estilo de botões de tabulação comutado. Use todas propriedades _style.body_. (padrão: _lv_style_tbn_rel_)
- **LV_TABVIEW_STYLE_BTN_TGL_PR** estilo de botões comutados pressionados. Use todas as propriedades _style.body_. (padrão: _lv_style_btn_tgl_pr_)

## Notas

## Exemplo
![Tabview image](http://docs.littlevgl.com/img/tab-view-lv_tabview.png)
```c
/*Cria um objeto visualizador de tabulação*/
lv_obj_t *tabview;
tabview = lv_tabview_create(lv_scr_act(), NULL);

/*Adiciona 3 tabulações (as tabulações são páginas (lv_page) e pode ser deslizado*/
lv_obj_t *tab1 = lv_tabview_add_tab(tabview, "Tab 1");
lv_obj_t *tab2 = lv_tabview_add_tab(tabview, "Tab 2");
lv_obj_t *tab3 = lv_tabview_add_tab(tabview, "Tab 3");


/*Adiciona conteúdo para as tabulações*/
lv_obj_t * label = lv_label_create(tab1, NULL);
lv_label_set_text(label, "This the first tab\n\n"
                         "If the content\n"
                         "become too long\n"
                         "the tab become\n"
                         "scrollable\n\n");

label = lv_label_create(tab2, NULL);
lv_label_set_text(label, "Second tab");

label = lv_label_create(tab3, NULL);
lv_label_set_text(label, "Third tab");
```

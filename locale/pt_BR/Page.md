_Escrito para v5.1_

## Visão geral

A Página consiste de dois contâiner em cada outro: o botão é o **background** (ou base) e o top é o **deslizável**. Se você criou um filho na página ele será automaticamente movido em um contâiner deslizável. Se o contâiner deslizável se tornar maior do que o background ele **pode ser deslizável pelo arrasto** (como a lista de smart phones).

Por padrão o atributo _auto fit_ do atributo deslizável é ativado verticalmente assim sua altura será aumentada para incluir seus filhos. O comprimento do deslizável é automaticamente ajustado pelo comprimento do background (menos o espaçamento horizontal do background).

O objeto background pode ser referenciado como a página dele mesmo como: `lv_obj_set_width(page, 100)`.

O objeto de rolagem pode ser recuperada com: `lv_page_get_scrl(page)`.

**Barra de rolagem** pode ser mostrado de acordo a quatro políticas:

- LV_SB_MODE_OFF: Nunca mostra barra de rolagem
- LV_SB_MODE_ON: Sempre mostra barra de rolagem
- LV_SB_MODE_DRAG: Mostra barra de rolagens quando a pagina está sendo arrastada
- LV_SB_MODE_AUTO: Mostra barra de rolagem quando o contâiner deslizável é longo o bastante para ser deslizado

Você pode configurar a barra de rolagem mostranto política pelo: `lv_page_set_sb_mode(page, SB_MODE)`. O valor padrão é _LV_PAGE_SB_MODE_ON_; 

Você pode **colar um filho** para a página. Neste caso você pode deslizar a página com arrasto do objeto filho. Ele pode ser ativado pelo `lv_page_glue_obj(child, true)`.

Você pode **focar um objeto** sobre uma página com: `lv_page_focus(page, child, anim_time)`.

Ele moverá o contâiner deslizável para mostrar um filho. Se o último parâmetro não é zero então a página se moverá com uma animação.

**Uma ação ao soltar e ao pressionar** podem ser assinadas para a Página com `lv_page_set_rel_action(page, my_rel_action)` e `lv_page_set_pr_action(page, my_pr_action)`. A ação pode ser gatihada de um Background e um objeto deslizável também.

Existem funções para direcionar **atribuir/obter atributos dos deslizáveis**:

- `lv_page_set_scrl_fit()`
- `lv_page_set_scrl_width()`
- `lv_page_set_scrl_height()`
- `lv_page_set_scrl_layout()`

## Uso do estilo

Use `lv_page_set_style(page, LV_PAGE_STYLE_...,  &style)` para atribuir um novo estilo para um elemento da página:

- **LV_PAGE_STYLE_BG** estilo do background na qual usa todas as propriedades _style.body_ (padrão: lv_style_pretty_color)
- **LV_PAGE_STYLE_SCRL** estilo deslizável na qual usa todas as propriedades _style.body_ (padrão: lv_style_pretty)
- **LV_PAGE_STYLE_SB** estilo da barra deslizável na qual usa todas as propriedades _style.body_. Espaçamentos horizontal/vertical configura o espaçamento da barra de rolagem respectivamente a o espaçamento interno configura o comprimento da barra de rolagem (padrão: lv_style_pretty_color)

## Notas

- **Atribuindo a posição do fillho** não é possível em direções x ou y se o ajuste correspondente _hor_ ou _ver_ estão ativados. É porque se a coordenada _y_ está modificada (com _ajuste ver_ ativado) o objeto deslizável será redimensionado para estar diratamente acima e abaixo do filho. Mas uma parte deslizável não pode estar no meio assim ele será movido de volta ao topo. Para evitar isso use `lv_obj_align()` para trocar o objeto relatiovo a cada outro (um tem que estar no topo/esquerda) ou desativado o ajuste com `lv_page_set_scrl_fit(page, false, false);` e configure seu tamanho `lv_page_set_scrl_width/height(page,  100)`.
- O background desenha sua borda quando o deslizável é desenhado. Ele garante que a página sempre terá que ser uma forma fechada até mesmo se um deslizável tem a mesma cor da página pai

## Exemplo
![Page image](http://docs.littlevgl.com/img/page-lv_page.png)
```c
/*Cria um estilo de barra*/
static lv_style_t style_sb;
lv_style_copy(&style_sb, &lv_style_plain);
style_sb.body.main_color = LV_COLOR_BLACK;
style_sb.body.grad_color = LV_COLOR_BLACK;
style_sb.body.border.color = LV_COLOR_WHITE;
style_sb.body.border.width = 1;
style_sb.body.border.opa = LV_OPA_70;
style_sb.body.radius = LV_RADIUS_CIRCLE;
style_sb.body.opa = LV_OPA_60;
style_sb.body.padding.hor = 3;          /*Espaçamento horizontal à direita*/
style_sb.body.padding.inner = 8;        /*Comprimento da barra de rolagem*/

/*Cria uma página*/
lv_obj_t * page = lv_page_create(lv_scr_act(), NULL);
lv_obj_set_size(page, 150, 200);
lv_obj_align(page, NULL, LV_ALIGN_CENTER, 0, 0);
lv_page_set_style(page, LV_PAGE_STYLE_SB, &style_sb);           /*Configura o estilo da barra de rolagem*/
lv_page_set_sb_mode(page, LV_SB_MODE_AUTO);                     /*Mostra que o deslizamento da barra de rolagem é possível*/

/*Cria um rótulo na página*/
lv_obj_t * label = lv_label_create(page, NULL);
lv_label_set_long_mode(label, LV_LABEL_LONG_BREAK);             /*Automaticamente quebra longas linhas*/
lv_obj_set_width(label, lv_page_get_scrl_width(page));          /*Configura o comprimento. Linhas serão quebradas aqui*/
lv_label_set_text(label, "Lorem ipsum dolor sit amet, consectetur adipiscing elit,\n"
                         "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\n"
                         "Ut enim ad minim veniam, quis nostrud exercitation ullamco\n"
                         "laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure\n"
                         "dolor in reprehenderit in voluptate velit esse cillum dolore\n"
                         "eu fugiat nulla pariatur.\n"
                         "Excepteur sint occaecat cupidatat non proident, sunt in culpa\n"
                         "qui officia deserunt mollit anim id est laborum.");
```

_Escrito para v5.1_

## Visão geral

As janelas são um dos **mais complexos** contâiner similares a objetos. Eles são construídos de duas partes principais: um **cabeçalho** [Contâiner](/Container) no topo e uma [Página](/Page) para o **conteúdo** abaixo do cabeçalho.

Sobre o cabeçalho há um **título** na qual pode ser modificado por: `lv_win_set_title(win, "New title")`. O título sempre herda o estilo do cabeçalho.

Você pode adicionar **botões de controle** para o lado direito do cabeçalho com: `lv_win_add_btn(win, "U:/close", my_close_action)`. O segundo parâmetro é um atalho de arquivo de imagem, o terceiro parâmetro é uma função para chamar quando o botão é solto. Você pode usar **símbolos** como imagens também como: `lv_win_add_btn(win, SYMBOL_CLOSE, my_close_action)`. 

Você pode modificar o **tamanho do controle de botões** com a função `lv_win_set_btn_size(win, new_size)`.

O comportamento da barra de rolagem pode ser configurado pelo `lv_win_set_sb_mode(win, LV_SB_MODE_...)`.

Para confugurar um layout para o conteúdo use `lv_win_set_layout(win, LV_LAYOUT_...)`.

## Uso do estilo

Use `lv_win_set_style(win, LV_WIN_STYLE_...,  &style)` para configurar um novo estilo para um elemento da janela:

- **LV_WIN_STYE_BG** background principal na qual usa todas as propriedades de _style.body_ (cabeçalho e página de conteúdo são colocadas nele) (padrão: lv_style_plain)
- **LV_WIN_STYLE_CONTENT_BG** conteúdo do background da página na qual usa todas as propriedades de _style.body_ (padrão: lv_style_transp)
- **LV_WIN_STYLE_CONTENT_SCRL** conteúdo da página da parte deslizável na qual usa todas as propriedades de _style.body_ (padrão lv_style_transp) 
- **LV_WIN_STYLE_SB** estilo da barra de deslizamento na qual usa todas as propriedades de _style.body_. Espaçamentos hor/ver* configuram o espaçamento da barra de rolagem respectivamente e seus espaçamentos internos configuram o comprimento da barra de rolagem. (padrão: lv_style_pretty_color)
- **LV_WIN_STYLE_HEADER** estilo do cabeçalho na qual usa todas as propriedades de _style.body_ (padrão: lv_style_plain_color)
- **LV_WIN_STYLE_BTN_REL** estilo do botão solto (sobre o cabeçalho) na qual usa todas as propriedades de _style.body_ (padrão: lv_style_btn_rel)
- **LV_WIN_STYLE_BTN_PR** estilo do botão solto (sobre o cabeçalho) na qual usa todas as propriedades de _style.body_ (padrão: lv_style_btn_pr)

## Notas

## Exemplo
![Window image](http://docs.littlevgl.com/img/window-lv_win.png)
```c
/*Cria um estilo de uma barra de rolagem*/
static lv_style_t style_sb;
lv_style_copy(&style_sb, &lv_style_plain);
style_sb.body.main_color = LV_COLOR_BLACK;
style_sb.body.grad_color = LV_COLOR_BLACK;
style_sb.body.border.color = LV_COLOR_WHITE;
style_sb.body.border.width = 1;
style_sb.body.border.opa = LV_OPA_70;
style_sb.body.radius = LV_RADIUS_CIRCLE;
style_sb.body.opa = LV_OPA_60;

/*Cria uma janela*/
lv_obj_t * win = lv_win_create(lv_scr_act(), NULL);
lv_win_set_title(win, "Example window");                        /*Configura o título*/
lv_win_set_style(win, LV_WIN_STYLE_SB, &style_sb);              /*Configura o estilo da barra de rolagem*/


/*Adiciona botão de controle ao cabeçalho*/
lv_win_add_btn(win, SYMBOL_SETTINGS, my_setup_action);            /*Adiciona um botão de configuração*/
lv_win_add_btn(win, SYMBOL_CLOSE, lv_win_close_action);           /*Adiciona botão fechar e usa a ação fechar embutida*/


/*Adiciona alguns conteúdos de exemplo*/
lv_obj_t * txt = lv_label_create(win, NULL);
lv_label_set_text(txt, "This is the content of the window\n\n"
                       "You can add control buttons to\nthe window header\n\n"
                       "You can scroll it\n\n"
                       "See the scroll bar on the right!");
```

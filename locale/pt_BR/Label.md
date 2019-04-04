_Escrito para v5.1_

## Visão geral
Os rótulos são objetos básicos para **mostrar texto**. Não existe limitação no tamanho do texto porque ele é guardado dinamicamente. Você pode modificar o texto em tempo real a qualquer momento com lv_label_set_text().

Você pode usar `\n` para fazer a quebra de linha. Por exemplo: `"line1\nline2\n\nline4"`

O tamaho do objeto rótulo pode ser automaticamente expandido ao tamanho do texto ou o texto pode ser manipulado de acordo com **políticas de modo longo** severas:

* LV_LABEL_LONG_EXPAND: Expande o tamanho do objeto ao tamanho do texto
* LV_LABEL_LONG_BREAK: Mantém o comprimento do objeto, quebra as linhas muito longas e expande a altura do objeto
* LV_LABEL_LONG_DOTS: Mantém o tamanho do objeto, quebra o texto e escreve pontos na última linha
* LV_LABEL_LONG_SCROLL: Expande o tamanho do objeto e desliza o texto no pai (move o objeto rótulo)
* LV_LABEL_LONG_ROLL: Mantém o tamanho e o rolamento somente o texto (não o objeto)

Você pode especificar o modo longo com: `lv_label_set_long_mode(label, long_mode)`

Rótulos são capazes de mostrar texto de um **vetor estático**. Use `lv_label_set_static_text(label, char_array)`. Neste caso, o texto não é guardado na memória dinâmica mas o vetor dado é usado. Mantenha em mente que o vvetor não pode ser uma variável local na qual se destroi quando a função deixa de ser executada.

Você pode também usar um **vetor de caracteres** como um rótulo de texto. O vertor não precisa ser terminado por `\0`. Neste caso, o texto será salvo na memória dinâmica. Para configurar o vetor de caracteres use a função `lv_label_set_array_text(label, char_array)`

O rótulo do **texto pode ser alinhado** à esquerda, direita ou centro com `lv_label_set_align(label, LV_LABEL_ALIGN_LEFT/RIGHT/CENTER)`

Você pode ativar o **desenhar um background** para o rótulo com `lv_label_set_body_draw(label, draw)`

No texto, você pode usar comandos para **recolorizar partes do texto**. `"Write a #ff0000 red# word"`. Por exemplo:  Neste recurso pode ser ativado individualmente para cada rótulo pela função `lv_label_set_recolor()`

Os rótulos podem mostrar símbolos ao lado das letras. Aprenda mais sobre símbolos [aqui](/Fonts)

Os **estilos padrões** dos rótulos é `NULL` assim eles herdam o estilo do pai.

## Uso do estilo
* Use todas as propriedades do `style.text`
* Para um desenho background `propriedades style.body` são usadas

## Notas
Os **atributos clique ativado do rótulo é desativado** por padrão. Você pode ativar o modo clicar com `lv_obj_set_click(label, true)`

## Exemplo
![Example of Label in LittlevGL Graphics Library ](http://docs.littlevgl.com/img/label-lv_label.png)

```c
/*Cria rótulo na tela. Por padrão o estilo será herdado do estilo da tela*/
lv_obj_t * title = lv_label_create(lv_scr_act(), NULL);
lv_label_set_text(title, "Title Label");
lv_obj_align(title, NULL, LV_ALIGN_IN_TOP_MID, 0, 20);  /*Alinha ao topo*/

/*Cria um novo estilo*/
static lv_style_t style_txt;
lv_style_copy(&style_txt, &lv_style_plain);
style_txt.text.font = &lv_font_dejavu_40;
style_txt.text.letter_space = 2;
style_txt.text.line_space = 1;
style_txt.text.color = LV_COLOR_HEX(0x606060);

/*Cria um novo rótulo*/
lv_obj_t * txt = lv_label_create(lv_scr_act(), NULL);
lv_obj_set_style(txt, &style_txt);                    /*Configura o estilo criado*/
lv_label_set_long_mode(txt, LV_LABEL_LONG_BREAK);     /*Quebra as linhas longas*/
lv_label_set_recolor(txt, true);                      /*Ativa recolorizar por comandos no texto*/
lv_label_set_align(txt, LV_LABEL_ALIGN_CENTER);       /*Centraliza linhas alinhadas*/
lv_label_set_text(txt, "Align lines to the middle\n\n"
                       "#000080 Re-color# #0000ff words of# #6666ff the text#\n\n"
                       "If a line become too long it can be automatically broken into multiple lines");
lv_obj_set_width(txt, 300);                           /*Configuura o comprimento*/
lv_obj_align(txt, NULL, LV_ALIGN_CENTER, 0, 20);      /*Alinha ao centro*/
```

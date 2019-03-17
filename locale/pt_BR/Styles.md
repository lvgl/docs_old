_Escrito para v5.1_

Para configurar a aparência dos estilos dos objetos que podem ser usados. Um estilo é uma estrutura variável com atributos como cores, preenchimento, visibilidade entre outros. Existe um estilo comum chamado: **lv_style_t**

Para atribuir os campos de uma estrutura `lv_style_t` você pode influenciar as aparências dos objetos usando aquele estilo.

Os objetos guardam somente um ponteiro para um estilo, então o estilo não pode ser uma variável local na qual é destruida depois que a função existe. **Você deve usar variáveis globais estáticas ou variáveis dinamicamente alocadas**
```c
lv_style_t style_1;             /*OK! Variáveis globais para estilo são ótimas*/
static lv_style_t style_2;      /*OK! Variáveis estáticas fora das funções são ótimas*/
void my_screen_create(void) 
{
  static lv_style_t style_3;    /*OK! Variáveis estáticas nas funções são ótimas*/
  lv_style_t style_1;           /*ERRADO! Estilos não podem ser variáveis locais*/

  ...
}
```


## Propriedade de estilos
Um estilo tem 5 partes principais comuns: comum, corpo, texto, imagem e linha. Um objeto usará aqueles campos na qual são relevante para ele. Por exemplo, Linhas não se importa com letter_space. para ver quais campos são usados por um tipo de objeto veja suas documentações.

Os campos de uma estrutura de estilo são as seguintes:

* **Propriedades comuns**
  * **glass** 1: Não herda este estilo (veja abaixo)
* **Propriedades do estilo do corpo** Usado por um objeto tipo retângulo
  - **body.empty** Não preenche o retângulo (somente desenha a borda e/ou sombra)
  - **body.main_color** Cor principal (top color)
  - **body.grad_color** Cor do gradiente (cor de baixo)
  - **body.radius** Raio do canto. (configure o LV_RADIUS_CIRCLE para desenhar circulos)
  - **body.opa** Opacidade (0..255 ou LV_OPA_TRANSP, LV_OPA_10, LV_OPA_20 ... LV_OPA_COVER)
  - **body.border.color** Cor da borda
  - **body.border.width** Comprimento da borda
  - **body.border.part** Partes da borda (LV_BORDER_LEFT/RIGHT/TOP/BOTTOM/FULL ou valores 'OR'ed)
  - **body.border.opa** Opacidade da borda
  - **body.shadow.color** Cor da sombra
  - **body.shadow.width** Comprimento da sombra
  - **body.shadow.type** Tipo da sombra (LV_SHADOW_BOTTOM ou LV_SHADOW_FULL)
  - **body.padding.hor** Preenchimento horizontal
  - **body.padding.ver** Preenchimento Vertical
  - **body.padding.inner** Preenchimento interno
* **Propriedades de estilos de texto** Usado pelos objetos que mostrem textos
  - **text.color** Cor de texto
  - **text.font** Ponteiro para uma fonte
  - **text.opa** Opacidade do texo (0..255 or LV_OPA_TRANSP, LV_OPA_10, LV_OPA_20 ... LV_OPA_COVER)
  - **text.letter_space** Espaço da letra
  - **text.line_space** Espaço da linha
* **Propriedades do estilo de imagem** Usado por objetos baseado a imagem ou icones sobre objetos
  - **image.color** Cor para imagem baseado em recolorização em brilho de pixels
  - **image.intense** Intensidade de recolorização (0..255 or LV_OPA_TRANSP, LV_OPA_10, LV_OPA_20 ... LV_OPA_COVER)
  - **image.opa** Opacidade da imagem (0..255 or LV_OPA_TRANSP, LV_OPA_10, LV_OPA_20 ... LV_OPA_COVER)
* **Propriedades do estilo de linha** Usado por objetos contendo linhas ou elementos baseado à linhas
  - **line.color** Cor da linha
  - **line.width** Comprimento da linha
  - **line.opa** Opacidade da linha (0..255 or LV_OPA_TRANSP, LV_OPA_10, LV_OPA_20 ... LV_OPA_COVER)

## Usando estilos
Todo tipo de objeto tem uma única função para configurar estilo ou estilos.

Se o objeto tem somente um estilo - como um rótulo - a função `lv_label_set_style(label1, &style)` pode ser usada para configurar um novo estilo.

Se o objeto tem mais estilos (como um botão tem 5 estilos para cada estado) a função `lv_btn_set_style(obj, LV_BTN_STYLE_..., &rel_style` pode ser usada para configurar um novo estilo.

Os estilos e a propriedade de estilo usada por um tipo de objeto são descritas em sua documentação.

Se você **modificar um estilo na qual está sendo usado** por um ou mais objetos, ou objetos terão que ser notificados sobre o estilo que está mudado. Você tem duas opções para fazer que são:

```c
void lv_obj_refresh_style(lv_obj_t * obj);		/*Notifica um objeto sobre seus estilos que estão sendo modificado*/
void lv_obj_report_style_mod(void * style);		/*Notifica para todos os objetos se um estilo está sendo modificado. (NULL para notificar todos objetos)*/
```

Se o **estilo de um objeto é NULL, então seu estilo será herdado do estilo de seu pai**. Isso torna mais fácil criar um design consistente. Não se esqueça que um estilo descreve muita de suas propriedades ao mesmo  tempo. Por exemplo, se você configurou um estilo de botão e criou um rótulo nele com estylo NULL, então o rótulo será renderizado de acordo com o estilo desse botão. Em outras palavas, o botão garante que seu filho se parecerá bem com ele.

Configurando a propriedade //glass irá evitar de herdar aquele estilo//. Você deve usá-lo se o estilo é transparente, então aquele filho usa as cores e outras de seu pai.

## Estilo embutido
Existem muitos estilos embutidos na biblioteca:

![Estilos embutidos na LittlevGL Embedded Graphics Library](http://docs.littlevgl.com/img/style-built-in.png)

Como você pode ver hpa um estilo para telas, para botões, planos e estilos bonitos e transparentes também. O `lv_style_transp`, `lv_style_transp_fit` e `lv_style_transp_tight` diferenciam somente em preenchimentos: para `lv_style_transp_tight` todos os preenchimentos são zeros, para `lv_style_transp_fit`, somente preenchimentos horizontais e verticais são zeros.

Os estilos embutidos são variáveis lv_style_t globais, então você pode usa-los como: lv_btn_set_style(obj, LV_BTN_STYLE_REL, &lv_style_btn_rel)

Você pode modificar os estilos embutidos ou você pode criar novos estilos. Quando criar novos estilos é recomendado primeiro copiar um estilo embutido para garantir que todos os campos são inicializados com valores apropriados. O lv_style_copy(&dest_style, &src_style) pode ser usado para copiar estilos.

## Animações de estilo
Você pode animar estilos usando `lv_style_anim_create(&anim)`. Antes de chamar essa função você tem que inicializar uma variável `lv_style_anim_t`. A animação desaparecerá de um `style_1` para um `style_2`.

```c
lv_style_anim_t a;    /*Será copiado para uma variável local*/
a.style_anim = & style_to_anim;     /*Ponteiro para um estilo a ser animado*/
a.style_start = & style_1;          /*Ponteiro para um estilo incial (somente o ponteiro salvo)*/
a.style_end = & style_2;            /*Ponteiro para o estilo alvo (somente o ponteiro salvo)*/
a.act_time = 0;                     /*Atribui negativo para fazer o atraso*/
a.time = 1000;                      /*Tempo da animaçãoo em milisegundos*/
a.playback = 0;                     /*1: Roda a animação de volta também*/
a.playback_pause = 0;               /*Espera antes de rodar a animação [ms]*/
a.repeat = 0;                       /*1: repetir a animação*/
a.repeat_pause = 0;                 /*Espera antes de repetir [ms]*/
a.end_cb = NULL;                    /*Chame essa animação quando estiver pronta*/
```

## Exemplo de estilo
O exemplo de estilo abaixo mostra o uso do estilo descrito acima

![Exemplo de uso do exemplo do estilo no LittlevGL Embedded Graphics Library](http://docs.littlevgl.com/img/style-example.png)
```c
/*Cria um estilo*/
static lv_style_t style1;
lv_style_copy(&style1, &lv_style_plain);    /*Copia um estilo embutido para iniciar o novo estilo*/
style1.body.main_color = LV_COLOR_WHITE;
style1.body.grad_color = LV_COLOR_BLUE;
style1.body.radius = 10;
style1.body.border.color = LV_COLOR_GRAY;
style1.body.border.width = 2;
style1.body.border.opa = LV_OPA_50;
style1.body.padding.hor = 5;            /*Preenchimento Horizontal usado para o indicador de barras abaixo*/
style1.body.padding.ver = 5;            /*Preenchimento usado para o indicador de barras abaixo*/
style1.text.color = LV_COLOR_RED;

/*Cria um objeto simples*/
lv_obj_t *obj1 = lv_obj_create(lv_scr_act(), NULL);
lv_obj_set_style(obj1, &style1);                        /*Aplica o estilo criado*/
lv_obj_set_pos(obj1, 20, 20);                           /*Atribui a posição*/

/*Cria um rótulo no objeto. O estilo do rótulo é NULL por padrão*/
lv_obj_t *label = lv_label_create(obj1, NULL);
lv_obj_align(label, NULL, LV_ALIGN_CENTER, 0, 0);       /*Alinha o rótulo no meio*/

/*Cria uma barra*/
lv_obj_t *bar1 = lv_bar_create(lv_scr_act(), NULL);
lv_bar_set_style(bar1, LV_BAR_STYLE_INDIC, &style1);    /*Modifica o estilo do indicador*/
lv_bar_set_value(bar1, 70);                             /*Atribui o valor da barra*/
```

## Temas
Para criar estilos para seu GUI é um desafio porque você precisa de um profundo conhecimento da biblioteca e você precisa ter algumas habilidades de design. Em adição a isso, isto toma muito tempo para criar muitos estilos.

Para acelerar o projeto, alguns temas são introduzidos. Um tema é uma coleção de estilos na qual contém o estilo requerido para cada tipo de objeto. Por exemplo 5 estilos de botões para descrever 5 estados possíveis.
Verifique os [Temas existentes](https://littlevgl.com/themes).

Para ser mais específico um tema é uma estrutura de variável na qual contém vários campos lv_style_t *. Para botões:
```c
theme.btn.rel       /*Estilo de botão não pressionado*/
theme.btn.pr        /*Estilo de botão pressionado*/
theme.btn.tgl_rel   /*Estilo de botão alternado não pressionado*/
theme.btn.tgl_pr    /*Estilo de botão alternado pressionado*/
theme.btn.ina       /*Estilo de botão inativo*/
```

Um tema pode ser inicializado por: `lv_theme_xxx_init(hue, font)`. Onde xxx é o nome do tema, *hue* é uma valor de matiz do espaço de cor HSV (0..360) e a *font* é a fonte aplicada no tema (`NULL` para usar a fonte padrão `LV_FONT_DEFAULT`)

Quando um tema é inicializado seus estilos pode ser usados como esse:

![Exemplo de uso de tema no Littlev Embedded Graphics Library](http://docs.littlevgl.com/img/theme-example.png)
```c
/*Cria um deslizador padrão*/
lv_obj_t *slider = lv_slider_create(lv_scr_act(), NULL);
lv_slider_set_value(slider, 70);
lv_obj_set_pos(slider, 10, 10);

/*Inicializa o tema alien com uma matiz avermelhada*/
lv_theme_t *th = lv_theme_alien_init(10, NULL);

/*Cria um novo deslizador e aplica o estilo do tema*/
slider = lv_slider_create(lv_scr_act(), NULL);
lv_slider_set_value(slider, 70);
lv_obj_set_pos(slider, 10, 50);
lv_slider_set_style(slider, LV_SLIDER_STYLE_BG, th->slider.bg);
lv_slider_set_style(slider, LV_SLIDER_STYLE_INDIC, th->slider.indic);
lv_slider_set_style(slider, LV_SLIDER_STYLE_KNOB, th->slider.knob);
```

Você pode pedir para a biblioteca aplicar os estilos de um tema quando você cria novos objetos. Para fazer, use `lv_theme_set_current(th)`;

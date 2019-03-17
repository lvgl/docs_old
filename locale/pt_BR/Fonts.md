_Escrito para v5.1_

As fontes LittlevGL são bitmaps e outros descritores para guardar as imagens das letras (glyph) e algumas informações adicionais. Uma fonte é armazenada em uma variável **lv_font_t** e pode ser configurado no campo de estilo _text.font_.
 
As fontes tem uma propriedade **bpp (Bit-Per-Pixel)**. Ele mostra como o bit é usado para descrever um pixel na fonte. O valor armazenado para um pixel determina a opacidade do pixel. O jeito que a imagem das letras (especialmente sobre as bordas) podem ser suavizada. O valor bpp são 1, 2, 4 e 8 (maior valor significa melhor qualidade). O bpp também afeta o tamanho da memória requirida para armazenar a fonte. Ex.: bpp = 4 faz a memória da fonte 4 vezes maior do que bpp = 1.

#### Fontes embutidas

Existe muitas fontes embutidas na qual podem ser ativadas em lv_conf.h pelas definições _USE_LV_FONT_..._. Exinte fontes embutidas em **estilos diferentes**:

- 10 px
- 20 px
- 30 px
- 40 px

Você pode ativar as fontes com valores 1, 2, 4 ou 8 para configurar seus bpp (ex.: `#define USE_LV_FONT_DEJAVU_20 4` no `lv_conf.h`).

As fontes embutidas existem com **multiplicar caracteres** em cada tamanho:

- ASCII (Unicode 32..126)
- Suplemento Latim (Unicode 160..255)
- Cirilico (Unicode 1024..1279)

As fontes embutidas usa a fonte _Dejavu_.

As fontes embutidas são **variáveis globais** com nomes como:

- `lv_font_dejavu_20` (fonte ASCII de 20 px)
- `lv_font_dejavu_20_latin_sup` (Fontes suplementar em Latin de 20 px)
- `lv_font_dejavu_20_cyrillic` (Fonte cirílico de 20 px)

#### Suporte unicode

O LittlevGL suporta letras Unicode apartir da codificação de caracteres **UTF-8**. Você precisa configurar seu editor para salvar seu código/texto como UTF-8 (usualmente este é o padrão) e ativado _LV_TXT_UTF8_ no lv_conf.h. Sem a ativação do _LV_TXT_UTF8_ somente fontes ASCII e símbolos pode ser usado (veja os símbolos abaixo)

Depois disso os textos serão decodificados para determinar os valores Unicode. Para mostrar as letras sua fonte precisa conter a imagem (glyph) dos caracteres.

Você pode assinar mais fontes para criar um **conjunto de caracteres maior**. Para fazer isso escolha a fonte base (tipicamente fonte ASCII) e adiciona a extensão a ele `lv_font_add(child, parent)`. Somente fonte com mesmo tamanho serão assinadas.

As fontes embutidas já estão adicionadas ao mesmo tamanho da fonte ASCII. Por exemplo, se estão ativados os _USE_LV_FONT_DEJAVU_20_ e _USE_LV_FONT_DEJAVU_20_LATIN_SUP_ dentro do `lv_conf.h` então o texto _"abcÁÖÜ"_ pode ser renderizado quando usar _lv_font_dejavu_20_.

#### Fontes de símbolos

O fonte de símbolos são fontes especiais na qual contém símbolos ao invés de letras. Há **fontes símbolos nas fontes embutidas** também e elas são assinadas para fontes ASCII do mesmo tamanho. Em um texto, um símbolo pode ser referenciado como _SYMBOL_LEFT_, _SYMBOL_RIGHT_ etc; VocÇe pode mixar estes nomes de símbolos com strings:

```c
lv_label_set_text(label1,"Right "SYMBOL_RIGHT);
```

Os símbolos podem ser usado sem suporte UTF-8 também. (_LV_TXT_UTF8 0_)

As listas acima mostra os símbolos existentes:

![Símbolos básicos](https://littlevgl.com/docs/symbols.png)

#### Adicionar nova fonte

Se voccê quer **adicionar nova fonte para a biblioteca** você pode usar a [Ferramenta de Conversão de Fonte](https://littlevgl.com/ttf-font-to-c-array). Ele pode criar um array em C de um arquivo TTF na qual pode ser copiado para o seu projeto. Você pode especificar o tamanho, o alcance dos caracteres e o bpp. Opcionalmente você pode enumerar os caracteres para incluir eles na fonte final. Para usar a fonte gerada, declare isso com _LV_FONT_DECLARE(my_font_name)_. Depois disto, a fonte pode ser usada como fonte embutida.

#### Fonte de exemplo

![Fontes de exemplo](https://littlevgl.com/docs/example-fonts.png)

```c
/*Cria um novo estilo para o rótulo*/
static lv_style_t style;
lv_style_copy(&style, &lv_style_plain);
style.text.color = LV_COLOR_BLUE;
style.text.font = &lv_font_dejavu_40;   /*Fontes e símbolos unicode já assinadas para a biblioteca*/

lv_obj_t *label;

/*Use letras ASCII e Unicode*/
label = lv_label_create(lv_scr_act(), NULL);
lv_obj_set_pos(label, 20, 20);
lv_label_set_style(label, &style);
lv_label_set_text(label, "aeuois\n"
                         "äéüöíß");

/*Misturando textos e símbolos*/
label = lv_label_create(lv_scr_act(), NULL);
lv_obj_set_pos(label, 20, 100);
lv_label_set_style(label, &style);
lv_label_set_text(label, "Right "SYMBOL_RIGHT);
```

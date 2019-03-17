_Escrito para v5.1_

## Visão geral

As imagens são os objetos básicos para **mostrar imagens**. Para promover máxima flexibilidade da **origem da imagem** você pode:

- uma variável no código (uma matriz C com pixels)
- um arquivo armazenado externamente (como um SD card)
- um texto com [Símbolos](/Fonts)

Para configurar a origem de uma imagem a função `lv_img_set_src` pode ser usada.

Para gerar um vetor de pixel de uma imagem **de um PNG, JPG ou BMP** use o [Conversor de imagem online](https://littlevgl.com/image-to-c-array) e personalize a imagem convertida com o seu ponteiro:

```c
lv_img_set_src(img1, &converted_img_var);
```

Para usar **arquivos externos** você precisa converter os arquivos de imagem usando a ferramenta de conversão online mas agora você deve selecionar o formato da saída binária. Para ver como carregar a imagem externa do LittlevGL veja o [Tutorial] (https://github.com/littlevgl/lv_examples/tree/master/lv_tutorial/6_images).

You can set a **symbol**  from lv_symbol_def.h too. In this case, the image will be rendered as text according to the **font** specified in the style.  It enables to use light weighted mono-color 
Neste caso, a imagem será renderizada como texto de acordo com a **fonte** especificada no estilo. Ele ativa o uso leve de "letras" monocromáticas ao invés de imagens reais. Você pode atribuir símbolos como este:

```c
lv_img_set_src(img1, SYMBOL_OK);
```

A (variável) interna e as imagens externas suporta 2 métodos de **carregadores de transparencia**:

- **Croma key** `LV_COLOR_TRANSP` (lv_conf.h) será transparente
- **Byte alfa** Adiciona um byte alfa para cada pixel

Essas opções podem ser selecionadas no conversor online de fonte.

As imagens podem ser **recolorizadas em tempo real de execução** para qualquer cor de acordo com o brilho dos pixels. Isto é muito útil para mostrar diferentes estados (selecionado, inativo, pressionado, etc) de uma uma imagem sem guardar mais versões da mesma imagem. Esta característica pode ser ativada no estilo ao atribuir `img.intense` entre `LV_OPA_TRANSP` (nenhuma cor, valor: 0) e `LV_OPA_COVER` (total recolorização, valor: 255). O padrão é `LV_OPA_TRANSP` então assim esta esta atribuição é desativada.

É possível **automaticamente atribuir o tamanho** do comprimento e a altura da origem do objeto da imagem aplicando a função `lv_img_set_auto_size(image, true)`. Se _auto size_ estiver ativado, então um novo arquivo é atribuido ao tamanho do objeto é automaticamente mudado. Posteriormente você poderá mudar o tamanho manualmente. Se o objeto é maior do que o tamanho da imagem em qualquer direção entãoo a imagem será repetida como um mosaico. O tamanho automático é ativado por padrão se a imagem não é uma tela.

Os estilos das imagens padrões é NULL assim elas **herdam o estilo do pai**.

## Uso do estilo

- Para imagens **style.img**
- Para símbolos **style.text**

## Notas

- Nomes de símbolos (como SYMBOL_EDIT) são strings curtas, contudo, você pode concatenar eles para mostrar mais símbolos

## Exemplo


![Example of Image in LittlevGL Graphics Library ](http://docs.littlevgl.com/img/image-lv_img.png)

```c
/*Declara uma uma imagem roda dentada*/
LV_IMG_DECLARE(img_cw);

[...]

/***************************************
 * Cria três imagens e recoloriza elas
 ***************************************/

/*Cria a primeira imagem sem recolorizar*/
lv_obj_t * img1 = lv_img_create(lv_scr_act(), NULL);
lv_img_set_src(img1, &img_cw);
lv_obj_align(img1, NULL, LV_ALIGN_IN_TOP_LEFT, 20, 40);

/*Cria estilo para recolorizar com a cor azul claro*/
static lv_style_t style_img2;
lv_style_copy( &style_img2, &lv_style_plain);
style_img2.image.color = LV_COLOR_HEX(0x003b75);
style_img2.image.intense = LV_OPA_50;

/*Cria uma imagem com o estilo azul claro*/
lv_obj_t * img2 = lv_img_create(lv_scr_act(), img1);
lv_obj_set_style(img2, &style_img2);
lv_obj_align(img2, NULL, LV_ALIGN_IN_TOP_MID, 0, 40);

/*Cria estilo para recolorizar com a cor azul escuro*/
static lv_style_t style_img3;
lv_style_copy(&style_img3, &lv_style_plain);
style_img3.image.color = LV_COLOR_HEX(0x003b75);
style_img3.image.intense = LV_OPA_90;

/*Cria uma imagem com o estilo azul escuro*/
lv_obj_t * img3 = lv_img_create(lv_scr_act(), img2);
lv_obj_set_style(img3, &style_img3);
lv_obj_align(img3, NULL, LV_ALIGN_IN_TOP_RIGHT, -20, 40);


/**************************************
 * Cria uma imagem com símbolos
 **************************************/

/*Cria uma string de símbolos*/
char buf[32];
sprintf(buf, "%s%s%s%s%s%s%s",
             SYMBOL_DRIVE, SYMBOL_FILE, SYMBOL_DIRECTORY, SYMBOL_SETTINGS,
             SYMBOL_POWER, SYMBOL_GPS, SYMBOL_BLUETOOTH);

/*Cria estilo com uma fonte de símbolo*/
static lv_style_t style_sym;
lv_style_copy(&style_sym, &lv_style_plain);
// As fontes embutidas são extendidas com símbolos
style_sym.text.font = &lv_font_dejavu_60;
style_sym.text.letter_space = 10;

/*Cria uma imagem e usa a string como origem*/
lv_obj_t * img_sym = lv_img_create(lv_scr_act(), NULL);
lv_img_set_src(img_sym, buf);
lv_img_set_style(img_sym, &style_sym);
lv_obj_align(img_sym, NULL, LV_ALIGN_IN_BOTTOM_MID, 0, -30);


/*Cria rótulos de descrição*/
lv_obj_t * label = lv_label_create(lv_scr_act(), NULL);
lv_label_set_text(label, "Re-color the images in run time");
lv_obj_align(label, NULL, LV_ALIGN_IN_TOP_MID, 0, 15);

label = lv_label_create(lv_scr_act(), NULL);
lv_label_set_text(label, "Use symbols from fonts as images");
lv_obj_align(label, NULL, LV_ALIGN_IN_BOTTOM_MID, 0, -80);
```

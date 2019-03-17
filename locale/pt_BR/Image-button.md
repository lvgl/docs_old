_Escrito para v5.2_

## Visão geral

No botão de imagem é muito similar ao objeto Botão. A única diferença é que seu visual é definido pela imagem que o usuário usa em cada estado ao invés de desenhar um botão. Antes de ler isto, por favorr, aprenda como os Botões funcionam no LittelvGL: link para o botão

Para configurar a imagem em um estado a `lv_imgbtn_set_src(imgbtn, LV_BTN_STATE_..., &img_src)` A origem da imagem funciona da mesma forma como descrito no objeto Imagem
TODO link

Similarmente ao objeto Botão **as ações (callbacks) podem ser assinadas** pelo `lv_imgbtn_set_action(imgbtn, LV_BTN_ACTION_..., my_action)`.

Os **estados** também funcionam com objeto Botão. Ele pode ser configurado com `lv_imgbtn_set_state(imgbtn, LV_BTN_STATE_...)`.

Os recursod de **comutações** podem ser ativadas com `lv_imgbtn_set_toggle(imgbtn, true)`

## Uso do estilo

Os Botõees de imagem podem ter estilos únicos para cada estilo. Todos as propriedades `style.image` usada pelo botão de imagem:

- **image.color** Recoloriza a imagem para essa cor de acordo com `intense`
- **image.intense** A extensão da recolorização (0..255 or `LV_OPA_0/10/20..100`)
- **image.opa** A opacidade do objeto (0..255 or `LV_OPA_0/10/20..100`)

## Notas


## Exemplo
![Image button image](http://docs.littlevgl.com/img/image-button-lv_imgbtn.png)
```c
/*Cria estilo para fazer o botão mais escuro quando pressionado*/
lv_style_t style_pr;
lv_style_copy(&style_pr, &lv_style_plain);
style_pr.image.color = LV_COLOR_BLACK;
style_pr.image.intense = LV_OPA_50;
style_pr.text.color = LV_COLOR_HEX3(0xaaa);

LV_IMG_DECLARE(imgbtn_green);
LV_IMG_DECLARE(imgbtn_blue);

/*Cria um botão de imagem*/
lv_obj_t * imgbtn1 = lv_imgbtn_create(lv_scr_act(), NULL);
lv_imgbtn_set_src(imgbtn1, LV_BTN_STATE_REL, &imgbtn_green);
lv_imgbtn_set_src(imgbtn1, LV_BTN_STATE_PR, &imgbtn_green);
lv_imgbtn_set_src(imgbtn1, LV_BTN_STATE_TGL_REL, &imgbtn_blue);
lv_imgbtn_set_src(imgbtn1, LV_BTN_STATE_TGL_PR, &imgbtn_blue);
lv_imgbtn_set_style(imgbtn1, LV_BTN_STATE_PR, &style_pr);        /*Usa o estilo mais escuro no estado pressionado*/
lv_imgbtn_set_style(imgbtn1, LV_BTN_STATE_TGL_PR, &style_pr);
lv_imgbtn_set_toggle(imgbtn1, true);
lv_obj_align(imgbtn1, NULL, LV_ALIGN_CENTER, 0, -40);

/*Cria um rótulo no botão de imagem*/
lv_obj_t * label = lv_label_create(imgbtn1, NULL);
lv_label_set_text(label, "Button");

/*Copia a primeira imagem do botão e configura modo comutável*/
lv_obj_t * imgbtn2 = lv_imgbtn_create(lv_scr_act(), imgbtn1);
lv_btn_set_state(imgbtn2, LV_BTN_STATE_TGL_REL);
lv_obj_align(imgbtn2, imgbtn1, LV_ALIGN_OUT_BOTTOM_MID, 0, 20);

/*Cria um rótulo no botão de imagem*/
label = lv_label_create(imgbtn2, NULL);
lv_label_set_text(label, "Button");

```

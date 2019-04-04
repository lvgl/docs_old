_Escrito para v5.1_

## Visão geral

O objeto Controle Deslizante parece como uma **Barra** suplementada **com uma Alça**. A Alça pode ser **arrastada para configurar um valor**. O controle deslizante pode ser vertical ou horizontal.

Para configurar um **valor inicial** use a função `lv_slider_set_value(slider, new_value)` ou `lv_slider_set_value_anim(slider, new_value, anim_time)` para configurar o valor com uma animação.

Para especificar o **alcance** (valores min, máx) o `lv_slider_set_range(slider, min , max)` pode ser usado.

Uma **função callback** pode ser assinada para chamar quando um novo valor é configurado pelo usuário `lv_slider_set_action(slider, my_action)`.

A **alça pode ser trocada** de dois jeitos:

- dentro do background sobre valores min/máx
- sobre as bordas sobre valores mim/máx

Use o `lv_slider_set_knob_in(slider, true/false)` para escolher entre os modos. (*knob_in* == _false_ é o padrão)

## Uso do estilo

Você pode modificar o estilo do controle deslizante com `lv_slider_set_style(slider, LV_SLIDER_STYLE_..., &style)`.

- **LV_SLIDER_STYLE_BG** Estilo do background. Todas as propriedades _style.body_ são usadas. O valor _padding_ faz o controle deslizante menor do que a alça (valor negativo faz dele maior)
- **LV_SLIDER_STYLE_INDIC** Estilo do indicador. Todas as propriedades _style.body_ são usadas. O valores _padding_ fazem o indicador menor do que o background.
- **LV_SLIDER_STYLE_KNOB** Estilo da alça. As propriedades _style.body_ são usadas exceto espaçamento

## Notas

- A alça não é um objeto real, ele é somente desenhado acima da Barra

## Exemplo
![Slider image](http://docs.littlevgl.com/img/slider-lv_slider.png)
```c
/*Called when a new value id set on the slider*/
static lv_res_t slider_action(lv_obj_t * slider)
{
    printf("New slider value: %d\n", lv_slider_get_value(slider));

    return LV_RES_OK;
}

.
.
.

/*Cria um controle deslizante padrão*/
lv_obj_t * slider1 = lv_slider_create(lv_scr_act(), NULL);
lv_obj_set_size(slider1, 160, 30);
lv_obj_align(slider1, NULL, LV_ALIGN_IN_TOP_RIGHT, -30, 30);
lv_slider_set_action(slider1, slider_action);
lv_bar_set_value(slider1, 70);


/*Criar um rótulo à direita ao controle deslizante*/
lv_obj_t * slider1_label = lv_label_create(lv_scr_act(), NULL);
lv_label_set_text(slider1_label, "Default");
lv_obj_align(slider1_label, slider1, LV_ALIGN_OUT_LEFT_MID, -20, 0);

/*Criai uma barra, um indicador e um estilo de alça*/
static lv_style_t style_bg;
static lv_style_t style_indic;
static lv_style_t style_knob;

lv_style_copy(&style_bg, &lv_style_pretty);
style_bg.body.main_color =  LV_COLOR_BLACK;
style_bg.body.grad_color =  LV_COLOR_GRAY;
style_bg.body.radius = LV_RADIUS_CIRCLE;
style_bg.body.border.color = LV_COLOR_WHITE;

lv_style_copy(&style_indic, &lv_style_pretty);
style_indic.body.grad_color =  LV_COLOR_GREEN;
style_indic.body.main_color =  LV_COLOR_LIME;
style_indic.body.radius = LV_RADIUS_CIRCLE;
style_indic.body.shadow.width = 10;
style_indic.body.shadow.color = LV_COLOR_LIME;
style_indic.body.padding.hor = 3;
style_indic.body.padding.ver = 3;

lv_style_copy(&style_knob, &lv_style_pretty);
style_knob.body.radius = LV_RADIUS_CIRCLE;
style_knob.body.opa = LV_OPA_70;
style_knob.body.padding.ver = 10 ;

/*Cria um segundo controle deslizante*/
lv_obj_t * slider2 = lv_slider_create(lv_scr_act(), slider1);
lv_slider_set_style(slider2, LV_SLIDER_STYLE_BG, &style_bg);
lv_slider_set_style(slider2, LV_SLIDER_STYLE_INDIC,&style_indic);
lv_slider_set_style(slider2, LV_SLIDER_STYLE_KNOB, &style_knob);
lv_obj_align(slider2, slider1, LV_ALIGN_OUT_BOTTOM_MID, 0, 30); /*Alinha abaixo da 'bar1'*/

/*Cria um segundo rótulo*/
lv_obj_t * slider2_label = lv_label_create(lv_scr_act(), slider1_label);
lv_label_set_text(slider2_label, "Modified");
lv_obj_align(slider2_label, slider2, LV_ALIGN_OUT_LEFT_MID, -30, 0);
```

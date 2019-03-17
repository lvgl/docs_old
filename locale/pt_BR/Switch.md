_Escrito para v5.1, revisão 2_

## Visão geral

A chave pode ser usado para **ligar/desligar** algo. A aparência se assemelha a um deslizador. O estado da chave pode ser mudado quando:

- Clicando sobre ele
- Deslizando ele
- Usando as funções `lv_sw_on(sw)` e `lv_sw_off(sw)`

Uma **função callback** pode ser assinada para chamar quando o usuário usa a chave: `lv_sw_set_action(sw, my_action)`.

**Novo em v5.3**: Chaves podem ser animadas ao ser chamada por `lv_sw_set_anim_time(sw, anim_ms)`.

## Uso do estilo

Você pode modificar o estilo da chave com `lv_sw_set_style(sw, LV_SW_STYLE_..., &style)`.

- **LV_SW_STYLE_BG** Estilo do background. Todas as propriedades de _style.body_ são usadas. O valores de _padding_ fazem a Chave menor do que a alça. (valor negativo faz ela mais larga)
- **LV_SW_STYLE_INDIC** Estilo do indicador. Todas as propriedades _style.body_ são usadas. Os valores de _padding_ fazem o indicador menor do que o background.
- **LV_SW_STYLE_KNOB_OFF** Estilo da alça quando ela estiver desligada. A propriedade _style.body_ é usada exceto o espaçamento.
- **LV_SW_STYLE_KNOB_ON** Estilo da alça quando a chave está ativada. A propriedade _style.body_ é usada exceto o espaçamento.

## Notes

- A alça não é um objeto real ele somente é um desenho acima da barra

## Exemplo
![Switch image](http://docs.littlevgl.com/img/switch-lv_sw.png)
```c
/*Cria estilo para a chave*/
static lv_style_t bg_style;
static lv_style_t indic_style;
static lv_style_t knob_on_style;
static lv_style_t knob_off_style;
lv_style_copy(&bg_style, &lv_style_pretty);
bg_style.body.radius = LV_RADIUS_CIRCLE;

lv_style_copy(&indic_style, &lv_style_pretty_color);
indic_style.body.radius = LV_RADIUS_CIRCLE;
indic_style.body.main_color = LV_COLOR_HEX(0x9fc8ef);
indic_style.body.grad_color = LV_COLOR_HEX(0x9fc8ef);
indic_style.body.padding.hor = 0;
indic_style.body.padding.ver = 0;

lv_style_copy(&knob_off_style, &lv_style_pretty);
knob_off_style.body.radius = LV_RADIUS_CIRCLE;
knob_off_style.body.shadow.width = 4;
knob_off_style.body.shadow.type = LV_SHADOW_BOTTOM;

lv_style_copy(&knob_on_style, &lv_style_pretty_color);
knob_on_style.body.radius = LV_RADIUS_CIRCLE;
knob_on_style.body.shadow.width = 4;
knob_on_style.body.shadow.type = LV_SHADOW_BOTTOM;

/*Cria uma chave e aplica os estilos*/
lv_obj_t *sw1 = lv_sw_create(lv_scr_act(), NULL);
lv_sw_set_style(sw1, LV_SW_STYLE_BG, &bg_style);
lv_sw_set_style(sw1, LV_SW_STYLE_INDIC, &indic_style);
lv_sw_set_style(sw1, LV_SW_STYLE_KNOB_ON, &knob_on_style);
lv_sw_set_style(sw1, LV_SW_STYLE_KNOB_OFF, &knob_off_style);
lv_obj_align(sw1, NULL, LV_ALIGN_CENTER, 0, -50);

/*Copia a primeira chave e o liga*/
lv_obj_t *sw2 = lv_sw_create(lv_scr_act(), sw1);
lv_sw_set_on(sw2);
lv_obj_align(sw2, NULL, LV_ALIGN_CENTER, 0, 50);
```

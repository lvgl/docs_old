_Escrito para v5.2_

## Visão geral

O objeto calendário é um calendário clássico na qual pode:
- enfatizar o dia atual e semana
- enfatizar qualquer data definida pelo usuário
- mostrar o nome dos dias
- vai para o mês próximo/anterior pelo clique do botão

A atribuição e a obtenção de datas no calendário o tipo `lv_calendar_date_t` é usada na qual é uma estrutura com os campos`ano`, `mês` e `dia`.

Para configurar a **data atual** use a função `lv_calendar_set_today_date(calendar, &today_date)`.

Para configurar **a data mostrada** use `lv_calendar_set_shown_date(calendar, &shown_date)`;

A lista das **datas enfatizadas** devem ser mexido e um vetor `lv_calendar_date_t` e esse vetor pode ser passado para `lv_calendar_set_hoghlighted_dates(calendar, &highlighted_dates)`. Somente os ponteiros de vetor será salvo e então o vetor deve ser uma variável global ou estática.

O **nome dos dias** podem ser ajustados com lv_calendar_set_day_names(calendar, day_names)` onde `day_names` looks like `const char * day_names[7] = {"Su", "Mo", ...};`


Uma **ação para selecionar uma data** será suportada em `v5.3` e aogra disponível no ramo da `dev-5.3` para uso experimental.



## Uso do estilo
- **LV_CALENDAR_STYLE_BG** Estilo do background usando a propriedade do `corpo` e o estilo dos dados dos números usando propriedade `texto`.
- **LV_CALENDAR_STYLE_HEADER** Estilo do cabeçalho onde o ano atual e mês são mostrados. Propriedades de `corpo` e `texto` são usados
- **LV_CALENDAR_STYLE_HEADER_PR** Estilo cabeçalho pressionado, usado quando o botáo próximo/anterior está sendo pressionado. Propriedade de `texto` são usados pelos vetores.
- **LV_CALENDAR_STYLE_DAY_NAMES** Estilo de nomes dos dias. Propriedade de `texto` são usados pelo o textos do dia e o `body.padding.ver` determina o espaço acima dos nomes do dia.
- **LV_CALENDAR_STYLE_HIGHLIGHTED_DAYS** Propriedade de `texto` são usados para ajustar o estilo dos dias enfatizados
- **LV_CALENDAR_STYLE_INACTIVE_DAYS** Propriedad de `texto` são usados para ajustar o estilo dos dias visíveis do mês próximo/anterior.
- **LV_CALENDAR_STYLE_WEEK_BOX** Propriedade de `corpo` são usadas para configurar o estilo da caixa de mês
- **LV_CALENDAR_STYLE_TODAY_BOX** Propeirdades de `corpo` e `texto` são usados para confifurar o estilo da caixa de hoje

## Example

![Calendar image](http://docs.littlevgl.com/img/calendar-lv_calendar.png)

```c
/*Ceia um Objeto Calendário*/
lv_obj_t * calendar = lv_calendar_create(lv_scr_act(), NULL);
lv_obj_set_size(calendar, 240, 220);
lv_obj_align(calendar, NULL, LV_ALIGN_CENTER, 0, 0);

/*Cria um estilo para o mês atual*/
static lv_style_t style_week_box;
lv_style_copy(&style_week_box, &lv_style_plain);
style_week_box.body.border.width = 1;
style_week_box.body.border.color = LV_COLOR_HEX3(0x333);
style_week_box.body.empty = 1;
style_week_box.body.radius = LV_RADIUS_CIRCLE;
style_week_box.body.padding.ver = 3;
style_week_box.body.padding.hor = 3;

/*Cria um estilo para hoje*/
static lv_style_t style_today_box;
lv_style_copy(&style_today_box, &lv_style_plain);
style_today_box.body.border.width = 2;
style_today_box.body.border.color = LV_COLOR_NAVY;
style_today_box.body.empty = 1;
style_today_box.body.radius = LV_RADIUS_CIRCLE;
style_today_box.body.padding.ver = 3;
style_today_box.body.padding.hor = 3;
style_today_box.text.color= LV_COLOR_BLUE;

/*Cria um estilo para os dias enfatizados*/
static lv_style_t style_highlighted_day;
lv_style_copy(&style_highlighted_day, &lv_style_plain);
style_highlighted_day.body.border.width = 2;
style_highlighted_day.body.border.color = LV_COLOR_NAVY;
style_highlighted_day.body.empty = 1;
style_highlighted_day.body.radius = LV_RADIUS_CIRCLE;
style_highlighted_day.body.padding.ver = 3;
style_highlighted_day.body.padding.hor = 3;
style_highlighted_day.text.color= LV_COLOR_BLUE;

/*Aplica os estilos*/
lv_calendar_set_style(calendar, LV_CALENDAR_STYLE_WEEK_BOX, &style_week_box);
lv_calendar_set_style(calendar, LV_CALENDAR_STYLE_TODAY_BOX, &style_today_box);
lv_calendar_set_style(calendar, LV_CALENDAR_STYLE_HIGHLIGHTED_DAYS, &style_highlighted_day);


/*Configura hoje*/
lv_calendar_date_t today;
today.year = 2018;
today.month = 10;
today.day = 23;

lv_calendar_set_today_date(calendar, &today);
lv_calendar_set_showed_date(calendar, &today);

/*Enfatiza alguns dias*/
static lv_calendar_date_t highlihted_days[3];       /*Somente seu ponteiro será salvo sendo assim deve ser estático*/
highlihted_days[0].year = 2018;
highlihted_days[0].month = 10;
highlihted_days[0].day = 6;

highlihted_days[1].year = 2018;
highlihted_days[1].month = 10;
highlihted_days[1].day = 11;

highlihted_days[2].year = 2018;
highlihted_days[2].month = 11;
highlihted_days[2].day = 22;

lv_calendar_set_highlighted_dates(calendar, highlihted_days, 3);
```

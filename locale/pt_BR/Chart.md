_Escrito para v5.1_

## Visão geral

Gráficos tem um background tipo retângulo com linhas de divisões horizontais e verticais. Você pode adicionar qualquer número de **séries** para os gráficos pelo `lv_chart_add_series(chart, color)`. Ele aloca dados por uma estrutura `lv_chart_series_t` na qual contem a _cor_ escolhida e um vetor para os dados.

Você tem várias opções para configurar os dados de séries:

1. Configurar os valores manualmente em um vetor como `ser1-&gt;points[3] = 7` e atualizar o gráfico com `lv_chart_refresh(chart)`.
2. Usar a função `lv_chart_set_next(chart, ser, value)` para deslocar todos os dados da esquerdas e configurar um novo dado na posição à esquerda.
3. Inicializar todos os pontos para um dado valor com: `lv_chart_init_points(chart, ser, value)`.
4. Configurar todos os pontos de um vetor com: `lv_chart_set_points(chart, ser, value_array)`.

Existem quatro **tipos de display de dados**:

- LV_CHART_TYPE_NONE: não mostra os pontos. Isto pode ser usado se você gostaria de adicionar seu próprio método de desenho.
- LV_CHART_TYPE_LINE: desenha linhas entre os pontos
- LV_CHART_TYPE_COL: Desenha colunas
- LV_CHART_TYPE_POINT: Desenha pontos

Você pode especificar os tipos de display com `lv_chart_set_type(chart, TYPE)`. O tipo `LV_CHART_TYPE_LINE | LV_CHART_TYPE_POINT` é também válido para desenhar ambas linhas e pontos.

Você pode especificar os **valores das direções min. e max. em y** com `lv_chart_set_range(chart, y_min, y_max)`. O valor dos pontos serão escaladas proporcionalmente. O alcance padrão é: 0..100.

O **número de pontos** na linhas de dados podem ser modificados por `lv_chart_set_point_count(chart, point_num)`. O valor padrão é 10.

O **número das linhas de divisões horizontais e verticais** podem ser modificados por `lv_chart_set_div_line_count(chart, hdiv_num, vdiv_num)`. O padrão de configurações são linhas de divisão de 3 horizontais e 5 verticais.

Para configurar o **comprimento de linha** e **ponto do raio** use a função `lv_chart_set_series_width(chart, size)`. O padrão é: 2.

A *_opacidade das linhas de dados_ podem ser especificadas pelo `lv_chart_set_series_opa(chart, opa)`. O valor padrão é: OPA_COVER.

Você pode aplicar um **desaparecimento de cor escura** sobre o fundo das colunas e pontos pela função `lv_chart_set_series_darking(chart, effect)`. O padrão de nível de escuridão é OPA_50.

## Uso de estilo

- **style.body** propriedade para configurar a aparência de background
- **style.line** propriedade para configurar a aparência de linhas de divisão

The series related parameters can be set directly for each chart with `lv_chart_set_series_width()`, `lv_chart_set_series_opa()` and  `lv_chart_set_series_dark()`.
Os parâmetros das séries relatadas pode ser configurado diretamente para cada gráfico com `lv_chart_set_series_width()`, `lv_chart_set_series_opa()` e  `lv_chart_set_series_dark()`.

## Exemplo

![Chart image](http://docs.littlevgl.com/img/chart-lv_chart.png)

```c
/*Criar um estilo para o gráfico*/
static lv_style_t style;
lv_style_copy(&style, &lv_style_pretty);
style.body.shadow.width = 6;
style.body.shadow.color = LV_COLOR_GRAY;
style.line.color = LV_COLOR_GRAY;

/*Criar um gráfico*/
lv_obj_t * chart;
chart = lv_chart_create(lv_scr_act(), NULL);
lv_obj_set_size(chart, 200, 150);
lv_obj_set_style(chart, &style);
lv_obj_align(chart, NULL, LV_ALIGN_CENTER, 0, 0);
lv_chart_set_type(chart, LV_CHART_TYPE_POINT | LV_CHART_TYPE_LINE);   /*Mostra linhas e pontos também*/
lv_chart_set_series_opa(chart, LV_OPA_70);                            /*Opacidade da séries de dados*/
lv_chart_set_series_width(chart, 4);                                  /*Comprimento da linha e o ponto de radio*/

lv_chart_set_range(chart, 0, 100);

/*Adiciona duas séries de dados*/
lv_chart_series_t * ser1 = lv_chart_add_series(chart, LV_COLOR_RED);
lv_chart_series_t * ser2 = lv_chart_add_series(chart, LV_COLOR_GREEN);

/*Configurar o próximo pontos em 'dl1'*/
lv_chart_set_next(chart, ser1, 10);
lv_chart_set_next(chart, ser1, 50);
lv_chart_set_next(chart, ser1, 70);
lv_chart_set_next(chart, ser1, 90);

/*Diretamente configura pontos sobre 'dl2'*/
ser2->points[0] = 90;
ser2->points[1] = 70;
ser2->points[2] = 65;
ser2->points[3] = 65;
ser2->points[4] = 65;
ser2->points[5] = 65;

lv_chart_refresh(chart); /*Requerido depois da configuração direta*/
```

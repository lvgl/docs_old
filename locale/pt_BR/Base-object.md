_Escrito para v5.1_

## Visão geral

O objeto base contém os **atributos mais básicos** dos objetos:

- Coordenadas
- Objeto pai
- Filhos
- Estilo
- Atributos como ativar Clique, ativar Arrasto etc.

Você pode atribuit a **coordenadas x e y** relativa ao pai com `lv_obj_set_x(obj, new_x)` e `lv_obj_set_y(obj, new_y)` ou em uma função com `lv_obj_set_pos(obj, new_x, new_y)`.

O **tamanho do objteto** pode ser modificado com `lv_obj_set_width(obj, new_width)` e `lv_obj_set_height(obj, new_height)` ou em uma função com `lv_obj_set_size(obj, new_width, new_height)`.

Você pode **alinhar** o objeto para um outro `lv_obj_align(obj1, obj2, LV_ALIGN_TYPE, x_shift, y_shift)`. O último dois argumentos significa um desllocamento x e y depois do alinhamento. O segundo argumento é outro objeto na qual alinha o primeiro (`NULL` significa: alinhamento ao pai). O terceiro argumento é o tipo de alinhamento:
![Tipos de alinhamento](http://docs.littlevgl.com/img/align.png)

Os tipos de alinhamento construídos como `LV_ALIGN_OUT_TOP_MID`. Por exemplo alinha um texto abaixo de uma imagem: `lv_obj_align(text, image, LV_ALIGN_OUT_BOTTOM_MID, 0, 10)`. Ou para alinhar um texto no meio de seus pais: `lv_obj_align(text, NULL, LV_ALIGN_CENTER, 0, 0)`.

Você pode atribuir um **novo pai** para um objeto como `lv_obj_set_parent(obj, new_parent)`.

Para obter o filho de um objeto use `lv_obj_get_child(obj, child_prev)` (do últimmo ao primeiro) ou `lv_obj_get_child_back(obj, child_prev)` (do primiro ao último). Para obter o primeiro filho passe _NULL_ como o segundo parâmetro e então os filhos prévios (retornam valores). A função irá retornar _NULL_ quando não mais existir nenhum filho.

Quando você tiver criado uma **tela** como `lv_obj_create(NULL, NULL)` você pode **carregar** ele com `lv_scr_load(screen1)`. A `lv_scr_act()` função te dá um ponteiro para a **tela atual**

Existem **duas camadas** geradas automaticamente:

- camada de topo
- camada do sistema

Eles são independentes das telas assim objetos criados tal que essas camadas será mostradas em todas as telas. A _camada do topo_ está acima de todos objetos da tela e a _camada do sistemma_ está na camada topo também. Você pode adicionar qualquer _camada de topo_ de janela pop-up livremente. Mas a _camada de sistema_ estará restrito as coisas do nível do sistema (ex.: cursor do mouse será movido aqui). As funções `lv_layer_top()` e `lv_layer_sys()` dá um ponteiro para a camada de topo ou sistema.

Você pode configurar **novo estilo** para um objeto com a função `lv_obj_set_style(obj, &new_style)`. Se `NULL` é atribuido como estilo então o objeto irá inserir seu estilo do pai. Se você **modificar um estilo** você tem que **notificar os objetos** na qual estão usando o sistema modificado. Você pode usar também `lv_obj_refresh_style(obj)` ou para notificar todos objetos com um dado estilo `lv_obj_report_style_mod(&style)`. Atribui o parâmetro _lv_obj_report_style_mod_' para `NULL` para notificar todos os objetos.

Há alguns atributos na qual podem ser ativados/desativados por `lv_obj_set_...(obj, true/false)`:

- **hidden** Esconde o objeto. Ele não irá ser desenhado e não ocupará espaço. Seus filhos serão escondidos também.
- **click** Ativado para o objeto clique via um dispositivo de entrada (ex.: touch pad). Se desativado então o objeto atrás dele irá ser checado durante o clique no carregador do dispositivo de entrada (útil com objetos não clicáveis como Rótulos)
- **top** Se ativado então quando esse objeto ou qualquer de seus filhos forem clicados então esse objeto vem para frente.
- **drag** Etiva o arrasto (movendo por um dispositivo de entrada)
- **drag_throw** Ativa "lançamento" com arrasto como o objeto tivesse momento
- **drag_parent** Se ativado então o pai do objeto será movido durante o arrasto.

Há algumas ações específicas na qual acontecem automaticamente na biblioteca. Para prevenir um ou mais deste tipos de ações você pode **proteger o objeto**. As seguintes proteções são:

- **LV_PROTECT_NONE** Sem proteção
- **LV_PROTECT_POS**  Evita posicionamento automático (Ex.: Layout em [lv_cont](/Container))
- **LV_PROTECT_FOLLOW** Evita que o objeto seja seguido em ordem automática (ex.: Layout em [lv_cont](/Container))
- **LV_PROTECT_PARENT** Evita mudança automática do pai
- **LV_PROTECT_CHILD_CHG** Desativa a mudança do sinal do filho. Usado pela biblioteca.

O `lv_obj_set/clr_protect(obj, LV_PROTECT_...)` atribui/limpa a proteção. Você pode usar valores _'OR'ed_ de tipos de proteção também.

Há **animações embutidas** para os objetos. As seguintes animações são:

- **LV_ANIM_FLOAT_TOP** Flutua do/para o topo
- **LV_ANIM_FLOAT_LEFT** Flutua da/para a esquerda
- **LV_ANIM_FLOAT_BOTTOM** Flutua de/para o fundo
- **LV_ANIM_FLOAT_RIGHT** Flutua de/para a direita
- **LV_ANIM_GROW_H** Cresce/encolhe horizontalmente
- **LV_ANIM_GROW_V** Cresce/encolhe verticalmente

O lv_obj_animate(obj, anim_type, time, delay, callback)` aplica uma animação sobre _obj_. Para determinar a direção da animação _OR_ _ANIM_IN_ ou _ANIM_OUT_ com o tipo de animação. O padrão é _ANIM_IN_ se não especificado. Você pode aprender mais sobre a [animations](/Animations).

## Uso do estilo

Todas as propriedades _style.body_ são usadas. Os padrões para telas _lv_style_plain_  e _lv_style_plain_color_ para objetos normais

## Examplo
![Base object image](http://docs.littlevgl.com/img/base-obj-lv_obj.png)
```c
/*Cria um simples objeto de base*/
lv_obj_t * obj1;
obj1 = lv_obj_create(lv_scr_act(), NULL);
lv_obj_set_size(obj1, 150, 40);
lv_obj_set_style(obj1, &lv_style_plain_color);
lv_obj_align(obj1, NULL, LV_ALIGN_IN_TOP_MID, 0, 40);

/*Copia o objeto anterior e ativa o arrasto*/
lv_obj_t * obj2;
obj2 = lv_obj_create(lv_scr_act(), obj1);
lv_obj_set_style(obj2, &lv_style_pretty_color);
lv_obj_set_drag(obj2, true);
lv_obj_align(obj2, NULL, LV_ALIGN_CENTER, 0, 0);

static lv_style_t style_shadow;
lv_style_copy(&style_shadow, &lv_style_pretty);
style_shadow.body.shadow.width = 6;
style_shadow.body.radius = LV_RADIUS_CIRCLE;

/*Copia o objeto anterior (arrasta se já estiver ativado)*/
lv_obj_t * obj3;
obj3 = lv_obj_create(lv_scr_act(), obj2);
lv_obj_set_style(obj3, &style_shadow);
lv_obj_align(obj3, NULL, LV_ALIGN_IN_BOTTOM_MID, 0, -40);
```

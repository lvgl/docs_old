_Escrito para v5.1_

Para interagir com o objeto criado o _Input devices_ será requirido. Por exemplo touchpad, mouse, teclado ou até mesmo um codificador. Para aprender como adicionar uma entrada, leia o [Guia de portabilidade](/Porting).

Quando você registrar um dispositivo de entrada a biblioteca adiciona algumas informações extras para ela descrever o estado deste dispositivo em mais detalhes. Quando uma ação do usuário (ex.: pressionar botão) acontece uma função de ação (callback) é gatilhada e sempre há um dispositivo na qual gatilhou essa ação. Você pode obter esse dispositivo de entrada com

```c
lv_indev_t *indev = lv_indev_get_act();
```

Isto pode ser inportante quando você precisa saber algumas informações especial sobre o dispositivo de entrada como o ponto pressionado frequentemente, ou arrastar um objeto ou não, etc.

Os dispositivos de entrada tem uma API muito simples:

```c
/*Obter o último ponto na entrada do display*/
void lv_indev_get_point(lv_indev_t * indev, point_t * point);

/*Checa se existe arrasto no dispositivo de entrada ou não*/
bool lv_indev_is_dragging(lv_indev_t * indev);

/*Obtém o vetor do arrasto no dispositivo de entrada*/
void lv_indev_get_vect(lv_indev_t * indev, point_t * point);

/*Não faz nada até o próximo "deixar de pressionar"*/
void lv_indev_wait_release(lv_indev_t * indev);

/*Não faz nada até o próximo "deixar de pressionar"*/
void lv_indev_wait_release(lv_indev_t * indev);

/*Reseta um dispositivo de entrada ou todos (use NULL)*/
void lv_indev_reset(lv_indev_t * indev);

/*Reseta o estado de pressionamento longo de um dispositivo de entrada*/
void lv_indev_reset_lpr(lv_indev_t * indev);

/*Configura um curso para um ponteiro de um dispositivo de entrada*/
void lv_indev_set_cursor(lv_indev_t * indev, lv_obj_t * cur_obj);

/*Configura um grupo de destino para um dispositivo de entrada para um keypad*/
void lv_indev_set_group(lv_indev_t * indev, lv_group_t * group);
```

* * *

### Navegação sem touchpad

Os objetos pode ser agrupado em ordem para facilmente **controlar** eles **sem touchpad ou mouse**. Ele permite a você usar

- Teclado ou keypad
- Botões de hardware
- Codificadores

para navegar entre objetos.

Primeiramente você tem que **criar um grupo de objeto** com `lv_group_t *group = lv_group_create()` e adicionar objetos para ele com `lv_group_add_obj(group, obj)`. Em um grupo sempre existe um objeto _focused_. Todos os botões pressionados serão "enviados" aos objetos focados.

Para navegar entre os objetos em um grupo (mundança no objeto focados) e interagir com eles, um tipo _LV_INDEV_TYPE_KEYPAD_ é requerido dispositivo de entrada. Nele a função _read_ você pode pedir a biblioteca informar qual tecla é pressionada ou deixou de ser pressionada. Para aprender como adicionar um dispositivo de entrada, leia o [Guia de portabilidade](/Porting).

Assim você tem que **assinar ao grupo para um dispositivo de entrada** com

```c
lv_indev_set_group(indev, group)
```

Existem alguns **controles de caracteres** especiais na qual podem ser usadas na função _read_:

- **LV_GROUP_KEY_NEXT** Foca no próximo objeto
- **LV_GROUP_KEY_PREV** Foca no objeto prévio
- **LV_GROUP_KEY_UP** Incrementa o valor, move acima ou clica no objeto focado (mover acima significa por exemplo selecionar um objeto acima em uma lista de elemento)
- **LV_GROUP_KEY_DOWN** Decrementa o valor ou mover para baixo no objeto focado (mover para baixo significa por exemplo selecionar um objeto abaixo na lista de elemento)
- **LV_GROUP_KEY_RIGHT** Incrementa o valor ou clique no objeto focado
- **LV_GROUP_KEY_LEFT** Decrementa o valor do objeto focado
- **LV_GROUP_KEY_ENTER** Clica no objeto focado ou em um elemento selecinado (ex: lista de elemento)
- **LV_GROUP_KEY_ESC** Fecha o objeto (ex: lista drop-down)

Em alguns casos (ex: quando uma janela pop-up aparece) é útil para congelar o foco sobre um objeto. Significa que _LV_GROUP_KEY_NEXT/PREV_ será ignorado. Você pode fazer isso com `lv_group_focus_freeze(group,true)`.

O **estilo do objeto em foco** é modificado por uma função. Por padrão, ele faz as cores do objeto alaranjada mas você pode especificar seu próprio estilo com uma função atualizadora em cada grupo com

```c
void lv_group_set_style_mod_cb(group, style_mod_cb). 
```

O _style_mod_cb_ precisa de um parâmetro `lv_style_t *` na qual é uma cópia do estilo do objeto focado. Em um callback, você pode mixar algumas cores para o objeto em questão e modificar parâmetros mas **não é permitido atribuir "modificar o tamanho"** (como _letter_space_, _padding_ etc.)

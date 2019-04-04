_Escrito para v5.2_

## Arquitetura do sistema

![Arquitetura do sistema do Littlev Graphics Library](http://docs.littlevgl.com/img/sys.png)

**Aplicação**    

Sua aplicação na qual cria o GUI e controlador (handle) para a tarefa específica.

**LittlevGL**  

Os próprios gráficos da biblioteca. Sua aplicação pode comunicar com a biblioteca para criar a GUI. Ele contém uma interface HAL (Camada Abstrata de Hardware) para registrar seu display e drivers de entrada de dispositivos.

**Driver**  

Junto ao seu driver específico, a biblioteca contém funções para controlar seu display, opcionalmente uma GPU e leitura do touchpad ou botões.

* * *

Existem **duas configurações típicas para hardware** dependendo da MCU que pussui um driver periférico LCD/TFT ou não. Em ambos os casoos, um frame buffer será necessário para armazenar a imagem atual na tela.

**MCU com driver TFT/LCD**    

Se sua MCU tem um driver TFT/LCD então você pode conectar um display diretamente via interface RGB. Neste caso, o frame buffer pode estar na sia RAM interna (se o MCU possui RAM suficiente) ou na RAM externa (se a MCU possui uma interface de memória).

**Controlador de display externo** 

Se o MCU não possui um driver TFT/LCD então contrlador de display externo (I.e. SSD1963, SSD1306, ILI9341) precisa ser usado. Neste caso, o MCU pode se comunicar com o contralador do display via porta paralela, SPI ou algumas vezes I2C. O frame buffer é usualmente localizado no controlador de display na qual economiza muita RAM para a MCU.

* * *

## Requerimentos

- **Microcontrolador ou processador de 16, 32 ou 64 bit**
- **Velocidade de clock de 16 MHz**
- **8 KB de RAM** para dados estáticos e **&gt;2 KB de RAM** para dados dinâmicos (objetos gráficos)
- **64 KB de memória permanente** (flash)
- **Opcionalmente ~1/10 do tamanho da tela de memória** para buffer interno (em 240 x 320, com cores de 16 bit é de aprox. 15 KB)

O LittlevGL é projetado para ser altamente portavel e não necessitar de nenhum **recurso externo**:

- Nenhuma RAM externa é requerida (mas suportado)
- Nenhum número de vírgula flutuante são usados
- Nenhuma GPU é necessária (mas suportado)
- Somente um único frame buffer é requerido e localizado em:
    - RAM interna ou
    - RAM externa ou
    - Controlador da memória do display externo

Se você quiser **reduzir** o **recurso de hardware** requerido você pode:

- Desativar tipos de objetos não usados para economizar RAM e ROM
- Mudar o tamanho do buffer gráfico para economizar RAM
- Usar estilos mais simples para reduzir o tempo de renderização

* * *

## Preparação do projeto

### Obtendo a biblioteca

O Littlev Graphics Library está disponível no GitHub: [https://github.com/littlevgl/lvgl](https://github.com/littlevgl/lvgl). Você pode clonar ou fazer download da última versão da biblioteca daqui ou você pode usar a página de [Download](https://littlevgl.com/download) também.

As bibliotecas gráficas está no diretório **lvgl** na qual deve ser copiado dentro do seu projeto.

### Arquivo de configuração

Existe um arquivo cabeçalho de configuração para o LittlevGL: **lv_conf.h**. Ele configura o comportamento básico da biblioteca durante o tempo de compilação. Desative os módulos não usados, configurações e ajuste do tamanho da memória de buffers, etc.


Copie _lvgl/lv_conf_templ.h_ próximo ao diretório _lvgl_ e renomeie-o para _lv_conf.h_. Abra o arquivo e apague o primeiro _#if_ e o último _#endif_ para ativar o conteúdo. No arquivo de configuração, comentários explicam o siginificado das opções. Verifique pelo menos essas três opções e modifique-as de acordo com seu hardware.

1. **LV_HOR_RES** Resolução horizontal de seu display
2. **LV_VER_RES** Resolução vertical de seu display
3. **LV_COLOR_DEPTH** 8 para (RG332), 16 para (RGB565) ou 32 para (RGB888 and ARGB8888).

### Inicialização

Para usar a biblioteca você tem que inicializá-la além de outros componentes também. A ordem da inicialização é:

1. Chamar _lv_init()_
2. Inicializar seus drivers
3. Registrar o display e a entrada de dispositivos dos drives dentro do LittlevGL. (Veja abaixo)

* * *

## Portando a biblioteca

Para colocar o LittlevGL dentro do seu projeto, primeiramente você tem que providenciar algumas funções e registrá-la na biblioteca de gráficos.

### Interface do display

Para configurar um display uma variável do tipo **lv_disp_drv_t** deve ser inicializada:

```c
lv_disp_drv_t disp_drv;
lv_disp_drv_init(&disp_drv); /*Inicialização básica*/
disp_drv. ...=...; /*Inicializar os campos aqui. Veja abaixo.*/
lv_disp_drv_register(&disp_drv); /*Registrar o driver dentro do LittlevGL*/
```

Você pode configurar o driver para diferentes modos de operação. Para aprender mais sobre modos de desenho, visite [Desenhando e renderizando](/Drawing).

#### Bufferização interna (VDB)

A biblioteca de gráficos funciona com mecanismo de buffer para criar características de avanços gráficos com somente um frame buffer. Um buffer interno é chamado de VDB (Display Virtual de Buffer) a seu tamanho pode ser ajustado dentro do lv_conf.h com _LV_VDB_SIZE_. quando _LV_VDB_SIZE_ &gt; 0 então a bufferização interna é usada e você tem que providenciar uma função na qual esvazie o conteúdo desse buffer para o seu display:

```c
disp_drv.disp_flush = my_disp_flush;
...
void my_disp_flush(int32_t x1, int32_t y1, int32_t x2, int32_t y2, const lv_color_t* color_p)
{
    /*TODO Copie 'color_p' para a área específica*/
    /*Chame 'lv_flush_ready()' quando estiver pronto*/lv_flush_ready();
}
```

Na função flush, você pode usar DMA ou qualquer hardware para fazer o despejo para o background, mas quando o despejo estiver pronto você tem que chamar
```c
lv_flush_ready();
```
##### Aceleração de Hardware (GPU)

Primeiramente, usar GPU é totalmente opcional. Mas se sua MCU suporta aceleração gráfica então você pode usá-la. Os campos _mem_blend_ e _mem_fill_ do driver do display é usado para interfacear com a GPU.
As funções relacionadas à GPU pode ser usada somente se o buffer interno (VDB) estiver desativada.

```c
disp_drv.mem_blend = my_mem_blend;     /*Mistura os dois vetores de cores usando opacidade*/
disp_drv.mem_fill = my_mem_fill;       /*Preenche um vetor com uma cor*/
...
void my_mem_blend(lv_color_t* dest, constlv_color_t* src, uint32_t length, lv_opa_t opa)
{
  /*TODO Copie 'src' para 'dest' mas misture isso com 'opa' alpha*/
}

void my_mem_fill(lv_color_t* dest, uint32_t length, lv_color_t color)
{
  /*TODO Preencha os pixels 'length' dentro do 'dest' com 'color'*/
}
```

##### Tirando o buffer do desenho

É possível desenhar diretamente para um frame buffer quando o buffer interno está desativado (LV_VDB_SIZE = 0).

```c
disp_drv.disp_fill = my_disp_fill;/*Preenche uma área no frame buffer*/
disp_drv.disp_map = my_disp_map;/*Copia uma color_map (e.g. imagem) dentro do frame buffer*/
...
void my_disp_map(int32_t x1,int32_t y1,int32_t x2,int32_t y2,constlv_color_t* color_p)
{
  /*TODO Copia 'color_p' para uma área específica*/
}

void my_disp_fill(int32_t x1,int32_t y1,int32_t x2,int32_t y2,lv_color_t color)
{
  /*TODO Preenche a área especificada com 'color'*/
}
```

Mantenha em mente que desse jeito durante o 'refresh' alguns artefatos pode estar visível porque as camadas estão desenhadas entre elas. E alguns gráficos de características alto nível como anti-aliasing, opacidade ou sombras não estão disponíveis nesta configuração.

Se você usa um controlador de display externo na qual suporta preenchimento acelerado (e.g. RA8876) então você pode usar este recurso no _disp_fill()_

### Interface de dispotitivo de entrada

Para configurar um dispositivo de entrada uma variável **lv_indev_drv_t** precisa ser inicializada:

```c
lv_indev_drv_t indev_drv;lv_indev_drv_init(&indev_drv);  /*Inicialização básica*/
indev_drv.type =.../*Veja abaixo.*/
indev_drv.read =.../*Veja abaixo.*/
lv_indev_drv_register(&indev_drv);  /*Registra o driver no LittlevGL*/
```

**type** pode ser
- LV_INDEV_TYPE_POINTER: touchpad ou mouse
- LV_INDEV_TYPE_KEYPAD: teclado
- LV_INDEV_TYPE_ENCODER: esquerda, direita, apertar
- LV_INDEV_TYPE_BUTTON: botão externo pressionando a tela
  
**read** é um função ponteiro na qual será chamada periodicamente para reportar o estado corrente de um dispositivo de entrada. Ele pode também dar um buffer de dados e retornar _false_ quando nenhum dados podem ser lidos ou _true_ quando o buffer não está vazio.

To learn more about input devices visit [Input devices](Input-devices).
Para aprender mais sobre os dispositivos de entrada, visite [Dispositivo de entrada](Input-devices).

#### Touchpad, mouse ou qualquer ponteiro

```c
indev_drv.type = LV_INDEV_TYPE_POINTER;
indev_drv.read = my_input_read;
```

A leitura da função deve ser algo parecido como:

```c
bool my_input_read(lv_indev_data_t*data)
{
    data->point.x = touchpad_x;   
    data->point.y = touchpad_y;
    data->state = LV_INDEV_STATE_PR or LV_INDEV_STATE_REL;
    return false; /*Sem mais bufferização, sendo assim, sem mais dados para ler*/
}
```

> **NOTA IMPORTANTE:** Drivers de touchpad devem retornar os últimas coordenadas X/Y até mesmo quando o estado é `LV_INDEV_STATE_REL`.

#### Keypad ou teclado
```c
indev_drv.type = LV_INDEV_TYPE_KEYPAD;
indev_drv.read = my_input_read;
```
A leitura da função deve ser algo parecido como:
```c
bool keyboard_read(lv_indev_data_t*data){
  data->key = last_key();            /*Obtém o última tecla pressionada ou liberada*/
  if(key_pressed()){
    data->state = LV_INDEV_STATE_PR;
  }
  else{
    data->state = LV_INDEV_STATE_REL;
  }
  return false; /*Sem mais bufferização, sendo assim, sem mais dados para ler*/
}
```
Para usar um teclado:
-  Registre uma função _read_ (como acima) com o tipo _LV_INDEV_TYPE_KEYPAD_.
- O _USE_LV_GROUP_ tem que estar ativado dentro do _lv_conf.h_
-  Um grupo de objeto tem que ser criado: _lv_group_create()_ e objetos tem que ser adicionado: _lv_group_add_obj()_
-  O grupo criado tem que se assinado para um dispositivo de entrada: _lv_indev_set_group(my_indev, group1);_
-  Use _LV_GROUP_KEY_..._ para navegar entre os objetos no grupo

Visite [Touchpad-less navigation](Input-devices) para aprender mais.

#### Codificador
Com um codificador você pode fazer 4 coisas:
1. pressionar seu botão
2. pressionar longamente seu botão
3. virar para esquerda
4. virar para direita

Ao ligar o codificador você pode focar no objeto próximo/anterior. Quando você pressiona o codificador em um simples objeto (como um botão). ele será clicado. Se você pressiona o codificador sobre um objeto complexo (como uma lista, caixa de mensagem, etc.) o objeto irá para o modo edição onde ligará o codificador, você pode navegar dentro do objeto. Para deixar o modo de edição pressione longamente o botão

```c
indev_drv.type = LV_INDEV_TYPE_ENCODER;
indev_drv.read = my_input_read;
```
A função de leitura deve se parecer como:
```c
bool encoder_read(lv_indev_data_t*data){
  data->enc_diff = enc_get_new_moves();
  if(enc_pressed()){
    data->state = LV_INDEV_STATE_PR;
  }
  else{
    data->state = LV_INDEV_STATE_REL;
  }

  return false; /*Sem bufferização então nennhum dado para ler*/
}
```

- Para usar um `ENCODER`, igualmente ao `KEYPA`, os objetos devem ser adicionados aos grupos.

#### Botão
```c
indev_drv.type = LV_INDEV_TYPE_BUTTON;
indev_drv.read = my_input_read;
```
A função de leitura deve se parecer como:
```c
bool button_read(lv_indev_data_t*data){
    static uint32_t last_btn = 0;   /*Armazena o último botão pressionado*/ 
    int btn_pr = my_btn_read();     /*Obtém o ID (0,1,2...) do botão pressionado*/
    if(btn_pr >= 0) {               /*Existe botão pressionado?*/  
       last_btn = btn_pr;           /*Salva o ID do botão pressionado*/
       data->state = LV_INDEV_STATE_PR;  /*Adiciona ao estado pressionado*/
    } else {
       data->state = LV_INDEV_STATE_REL; /*Adiciona ao estado liberado*/
    }
  
    data->btn = last_btn;            /*Adiciona o último botão*/         
   
    return false;                    /*Sem bufferização então nennhum dado para ler*/
}
```
   
- Os botões precisam ser assinados para pixels na tela usando `lv_indev_set_button_points(indev, points_array)`. Onde _points_array_ se parece como `const lv_point_t points_array[] = { {12,30},{60,90}, ...}`

### Interface tick

O LittlevGL usa um sistema tick. Chame a função `lv_tick_inc(tick_period)` periodicamente e chame o período de chamada em milisegundos. Por exemplo, se você chama em cada milisegundos: `lv_tick_inc(1)`

### Carregamento de chamada

Para carregar as chamadas do LittlevGL você precisa chamar `lv_task_handler()` periodicamente em uma das seguintes:

- _while(1)_ da função _main()_
- interrupção de temporizadores periodicos
- uma tarefa do OS periódica

A temporização não é critica mas deve se em torno de 5 milisegundos para manter o sistema responsível.

Exemplo:
```c

while(1) {
  lv_task_handler();
  my_delay_ms(5);
}
```

O MCU pode ficar no estado **sleep** quando nenhuma entrada acontece. Nesse caso o main `while(1)` deve se parecer como:
```c
while(1) {
  /*Operação normal em 1 seg*/ 
  if(lv_indev_get_inactive_time(NULL) < 1000) {    
	lv_task_handler();
  } 
  /*Dorme depois de 1 segundo inativo*/
  else {                                         
	timer_stop();               /*Para o temporizador quando lv_tick_inc() é chamado*/
	sleep();		    /*Faz o MCU dormir*/
  }
  my_delay_ms(5);
}
```

Você deve também adicionar essas linhas para seu dispositivo de entrara para ler a função quando um pressionamento acontece:
```c
/*Força a tarefa de execução quando acorda*/
lv_tick_inc(LV_REFR_PERIOD);
timer_start();               /*Reinicia o temporizador quando lv_tick_inc() é chamado*/
lv_task_handler();
``` 

Em adição à `lv_indev_get_inactive_time()` você pode checar `lv_anim_count_running()` para ver se cada animação foi finalizada.

### Usando com um sistema operacional
LittlevGL é **not thread-safe**. Além disso, ele é muito simples de usar dentro de um sistema operacional.

O **cenário simples** é não usar a tarefa do sistema operacional mas usar o `lv_task`s. Um _lv_task_ é uma fuunção chamada periodicamente em `lv_task_handler`. No _lv_task_ você pode obter os estados dos sensores, buffers etc e chamar as funções do LittlevGL para atualizar a GUI. Para criar um _lv_task_ use: `lv_task_create(my_func, period_ms, LV_TASK_PRIO_LOWEST/LOW/MID/HIGH/HIGHEST, custom_ptr)`

Se você precisa **usar outras tarefas ou threads** você precisa de um mutex na qual deve ser tomado antes de ser chamado `lv_task_handler` e lançado depois dele. Em adição, você terá que usar para esse mutex em outras tarefas e threads em volta de todo código relacionado ao LittlevGL (`lv_...`). Desse jeito você pode usar o LittlevGL em um ambiente real de multitarefa. Use um mutex para evitar chamadas concorrente das funções LittlevGL.

### Exemplo de portabilidade

Aqui você encontrará um exemplo de codígo de portabilidade: [Tutorial de portabilidada](https://github.com/littlevgl/lv_examples/blob/beta/lv_tutorial/0_porting/lv_tutorial_porting.c).

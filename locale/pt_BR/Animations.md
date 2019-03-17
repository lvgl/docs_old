_Escrito por v5.1_

Você pode automaticamente mudar o valor (animar) de uma variável entre um início e um valor fim usando **função animar** com o protótipo `void func(void* var,int32_t value). A animação acontecerá por uma chamada periódica da função animadora com o parâmetro correspondente.

Para **criar uma animação** você tem que inicializar uma variável _lv_anim_t_ (existe um template em [lv_anim.h](https://github.com/littlevgl/lvgl/blob/master/lv_misc/lv_anim.h)):

```c
lv_anim_t a;								
a.var = button1;							 /*Variável para animar*/						
a.start = 100;								 /*Valor inicial*/
a.end = 300;								 /*Valor final*/
a.fp = (lv_anim_fp_t)lv_obj_set_height;		                         /*Função para ser usada para animar*/
a.path = lv_anim_path_linear;                                            /*Caminho da animação*/
a.end_cb = NULL; 						 	 /*Callback quando a animação estiver pronta*/
a.act_time = 0;								 /*Configura o tempo < 0 para um atraso [ms]*/
a.time = 200;								 /*Comprimento da animação [ms]*/
a.playback = 0;								 /*1: anima em direção reversa também quando o normal estiver pronto*/
a.playback_pause = 0;						         /*Espera antes do playback [ms]*/
a.repeat = 0;								 /*1: Repete a animação (com ou sem playback)*/
a.repeat_pause = 0;							 /*Espera antes de repetir [ms]*/

lv_anim_create(&a);                          /*Inicia a animação*/
```

A `anim_create(&a)` irá registrar a animação e imediatamente **aplicar o valor _start_** independentemente para configurar o atraso.

Você pode determinar o **atalho da animação**. Na maioria simples do caso ele é linear na qual significa os valores corrente _start_ e _end_ é mudado linearmente. O atalho é uma função na qual calcula o próximo valor para configurar baseado no estado corrente da animação. Correntemente há dois atalhos embutidos:

- **lv_anim_path_linear** animação linear
- **lv_anim_path_step** muda em um passo no fim

Por padrão, você pode configurar o tempo da animação. Mas em alguns casos, a **velocidade de animação** é mais prática. A função `lv_anim_speed_to_time(speed, start, end)` calcula o tempo requerido em milisegundos para alcançar o fim do valor apartir de um valor inicial com a dada velocidade. A velocidade é interpretado em dimensão _unit/sec_. Por exemplo `lv_anim_speed_to_time(20,0,100)` nos dará 5000 milisegundos.

Você pode aplicar **animações diferentes múltiplas** na mesma variável no mesmo tempo. (Por exemplo, animar as coordenadas x e y com _lv_obj_set_x_ e _lv_obj_set_y_). Mas somente uma animação pode existir com um uma dada variável e um par de funções. Contudo a função _lv_anim_create()_ apagará a função existente de animação.

Você pode **apagar uma animação** por `lv_anim_del(var, func)` com a variável animada providenciada e sua função animadora.

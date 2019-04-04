_Escrito para v5.1_

Os carregadores do módulo de cor, todas as funções de cores relacionadas como mudar profundidade de cor, criando cor apartir do código hexadecimal, converter profundidade de cor, mixando cores, etc.

Os tipos de variáveis seguintes são definidos pelo modulo da cor:

- **lv_color1_t** Guarda cor monocromática. Para compatibilidade também contém campos R,G,B mas eles são sempre os mesmos (1 Byte)
- **lv_color8_t** Uma estrutura para guardar componentes R (3 bit), G (3 bit), B (2 bit) para cores de 8 bits (1 Byte)
- **lv_color16_t** Uma estrutura para guardar componentes R (5 bit), G (6 bit), B (5 bit) para cores de 16 bits (2 Bytes)
- **lv_color24_t** Uma estrutura para guardar componentes R (8 bit), G (8 bit), B (8 bit) para cores de 24 bits (4 Bytes)
- **lv_color_t** Igual para color 1/8/16/24_t de acordo para as configurações de profundidade
- **lv_color_int_t** uint8_t, uint16_t ou uint32_t de acordo para a configuraçõa de profundidade de cor. Usada para construir vetores de cor através de números planos.
- **lv_opa_t** Uma tipo simples uint8_t para descrever a opacidade.

Os tipos _lv_color_t_, _lv_color1_t__lv_color8_t_, _lv_color16_t_ e _lv_color24_t_ tem 4 campos:

- **red** Canal vermelho
- **green** Canal verde
- **blue** Canal azul
- **full** vermelho + verde + azul como um número

Você pode configurar **comprimento de cor atual** em _lv_conf.h_ atualizando e definindo o _LV_COLOR_DEPTH_ para 1 (monocromático), 8, 16 ou 24.

Você pode **converter uma cor de uma profundidade de cor atual** para um outro. As funções conversoras retorna com um número, então você pode usar o campo _full_:

```c
lv_color_t c;
c.red   = 0x38;
c.green = 0x70;
c.blue  = 0xCC;

lv_color1_t c1;
c1.full = lv_color_to1(c);		/*Retorna 1 para cores de luzes, 0 para cores escuras*/

lv_color8_t c8;
c8.full = lv_color_to8(c);		/*Dá um número de 8 bit com a cor convertida*/ 

lv_color16_t c16;
c16.full = lv_color_to16(c); 	/*Dá um número de 16 bit com a cor convertida*/

lv_color24_t c24;
c24.full = lv_color_to24(c);	/*Dá um número de 32 bit com a cor convertida*/
```

Você pode **criar uma cor** com a profundidade de cor atual usando a macro **LV_COLOR_MAKE**. Ele exige 3 argumentos (vermelho, verde, azul) como número de 8 bit. Por exemplo, para criar uma cor vermelho claro: `my_color = COLOR_MAKE(0xFF,0x80,0x80)`. Cores podem ser criadas de **código HEX** também: `my_color = LV_COLOR_HEX(0xFF8080)` ou `my_color = LV_COLOR_HEX3(0xF88)`.

**Mixando duas cores** é possível com `mixed_color = lv_color_mix(color1, color2, ratio)`. A razão pode ser 0..255. 0 (zero) resulta completamente color2, 255 resulta completamente color1.

Para descrever a **opacidade** o tipo _lv_opa_t_ é criado como embrulho para _uint8_t_. Algumas definições são introduzidos:

- **LV_OPA_TRANSP** Valor: 0, significa a opacidade faz a cor completamente transparente
- **LV_OPA_10** Valor: 25, significa que a cor cobre um pouco
- **LV_OPA_20 ... OPA_80** segue a lógica
- **LV_OPA_90** Valor: 229, significa que a cor está perto de cobrir completamente
- **LV_OPA_COVER** Valor: 255, significa que a cor cobre completamente

Você pode também usar a _LV_OPA_*_ definido em _lv_color_mix() como razão._


O módulo de cor define as **cores mais básicas**:

- ![#000000](https://placehold.it/15/000000/000000?text=+) `LV_COLOR_BLACK`
- ![#808080](https://placehold.it/15/808080/000000?text=+) `LV_COLOR_GRAY`
- ![#c0c0c0](https://placehold.it/15/c0c0c0/000000?text=+) `LV_COLOR_SILVER`
- ![#ff0000](https://placehold.it/15/ff0000/000000?text=+) `LV_COLOR_RED`
- ![#800000](https://placehold.it/15/800000/000000?text=+) `LV_COLOR_MARRON`
- ![#00ff00](https://placehold.it/15/00ff00/000000?text=+) `LV_COLOR_LIME`
- ![#008000](https://placehold.it/15/008000/000000?text=+) `LV_COLOR_GREEN`
- ![#808000](https://placehold.it/15/808000/000000?text=+) `LV_COLOR_OLIVE`
- ![#0000ff](https://placehold.it/15/0000ff/000000?text=+) `LV_COLOR_BLUE`
- ![#000080](https://placehold.it/15/000080/000000?text=+) `LV_COLOR_NAVY`
- ![#008080](https://placehold.it/15/008080/000000?text=+) `LV_COLOR_TAIL`
- ![#00ffff](https://placehold.it/15/00ffff/000000?text=+) `LV_COLOR_CYAN`
- ![#00ffff](https://placehold.it/15/00ffff/000000?text=+) `LV_COLOR_AQUA`
- ![#800080](https://placehold.it/15/800080/000000?text=+) `LV_COLOR_PURPLE`
- ![#ff00ff](https://placehold.it/15/ff00ff/000000?text=+) `LV_COLOR_MAGENTA`
- ![#ffa500](https://placehold.it/15/ffa500/000000?text=+) `LV_COLOR_ORANGE`
- ![#ffff00](https://placehold.it/15/ffff00/000000?text=+) `LV_COLOR_YELLOW`

como também `LV_COLOR_WHITE`.

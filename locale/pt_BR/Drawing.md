_Escrito para v5.1_

No _LittlevGL_ você pode pensar em objetos gráficos e não precisa se preocupar de como os desenhos acontecem. Você pode configurar o tamanho, posição ou qualquer atributo do objeto e aa biblioteca irá atualizar as áreas antigas (inválidas) e redesenhará as novas. Contudo, você deve saber o básico dos métodos de desenho para saber em qual deva escolher.

### Desenho buferizado e sem buffer

#### Desenho sem buffer

Os desenhos sem buffer coloca os pixels diretamente no display (frame buffer). Contudo durante o processo de desenho, alguma cintilação pode ser visível porque primeiramente o background tem que ser desenhado e depois os objetos sobre ele. Por essa razão, este tipo não está disponível quando deslizar, arrastar e animações são usadas. Por outro lado, ele tem a menor memória porque nenhum buffer extra para gráfico é requerido

Para usar desenho não bufferizado configure _LV_VDB_SIZE_ para 0 dentro do _lv_conf.h_ e registre o _disp_map_ e _disp_fill_functions. Aqui você pode aprender mais sobre [Portabilidade](/Porting).

#### Desenho bufferizado

O desenho bufferizado é similar a bufferização dupla quando duas telas com buffer dimensionado são usados (um para renderização e outro para mostrar o último quadro disponível). Contudo, o algoritmo do desenho bufferizado do LittlevGL usa somente um frame buffer e um pequeno buffer chamado Virtual Display Buffer (VDB). Para o tamanho do VDB ~1/10 do tamanho da tela é tipicamente o suficiente. Para uma tela de 320 x 240 com cores de 16-bit, é necessário somente 15 KB de RAM extra.

Com o desenho bufferizado não há cintilação porque a imagem é criada primeiramente na memória (VDB), contudo deslizar, arrastas e animações podem ser usadas. Em adição, ela também ativa o uso de outros efeitos gráficos como anti-aliasing, transparencia (opacidade) e sombras.

Para usar desenho bufferizado configure _LV_VDB_SIZE_ para &gt; LV_HOR_RES dentro do _lv_conf.h_ e registre uma função _disp_flush_.

No modo bufferizado, você pode usar **VDB duplo** para paralelamente executar renderização dentro de um VDB e copiar pixels para seu frame buffer de um para outro. A cópia deve usar DMA ou outra aceleração de hardware para funcionar em background para deixar a CPU fazer outras tarefas. Dentro do _lv_conf.h_ o _LV_VDB_DOUBLE 1_ ativa esta característica.

#### Desenho bufferizado vs desenho não bufferizado

Mantenha em mente que não é garantido que o desenho não bufferizado é mais rápido. Durante o processo de renderização, um pixel é sobrescrevido múltiplas vezes (ex.: backgroundm botão, texto estão acima um dos outros). Deste jeito em um modo não bufferizado a biblioteca precisa acessar a memória externa ou o controlador do display múltiplas vezes na qual é mais lento do que escrever/ler a memória interna da RAM.

As tabelas seguintes resume as diferenças entre os dois métodos de desenho:

|               | Des. não buffer.   | Des. bufferizado |
|---------------|--------------------|------------------|
|Uso da memória | Sem extra          | >~1/10 da tela   |
| Qualidade     | Cintilização       | Sem falha        |
|  Antialiasing | Não suportado      | Suportado        |
| Transparência | Não suportado      | Suportado        |
| Sombras       | Não suportado      | Suportado        |

### Anti-aliasing

Dentro do lv_conf.h você pode ativar o anti-aliasing com _LV_ANTIALIAS 1_. O anti-aliasing é suportado somente no mode bufferizado (LV_VDB_SIZE &gt; LV_HOR_RES).

Os algoritmo anti-aliasing coloca alguns pixels transluzente (pixels com opacidade) para produzir linhas e curvas (incluindo bordas com raio) e até mesmo suavizamento. Porque ele coloca somente pixels anti-aliasing que requer somente um pouco de poder computacional extra (~1.1x do tempo extra comparado ao não configuração anti-aliasing)

Como descrito em [Seção de fonte](/Fonts) as fontes podem ser anti-aliased por usar uma fonte diferente com um bpp (Bit-Per-Pixel) maior. Deste jeito os pixels de uma fonte pode não somente ser 0 ou 1 mas ser transluzente. Os bpp-s suportados são 1, 2, 4 e 8. Mantenha na mente uma fonte com um maior bpp requer mais ROM.

*Revisão 2*

## Formato de arquivo
Use [lv_misc/lv_templ.c](https://github.com/littlevgl/lvgl/blob/master/lv_misc/lv_templ.c) e [lv_misc/lv_templ.h](https://github.com/littlevgl/lvgl/blob/master/lv_misc/lv_templ.h)

## Convenção de nomes
* Palavras são separados por '_'
* Em variável e nomes de funções os nomes estão em minúsculas (ex.: *height_tmp*)
* Em enumerações e definições, usar somente maiúsculas (ex.: MAX_LINE_NUM*)
* Nomes globais (API):
  * começa com *lv*
  * seguido por nome de módulo: *btn*, *label*, *style* etc.
  * seguido pela ação (para funções): *set*, *get*, *refr* etc.
  * fechado com o sujeito: *name*, *size*, *state* etc. 
* Typedefs
  * preferir `typedef struct` e `typedef enum` ao invés de `struct name` e `enum name`
  * sempre finalize `typedef struct` e `typedef enum` que finalize com `_t`
* Abreviações:
  * Use abreviações em nomes públicos somente se eles se tornarem maiores que 32 caracteres
  * Use somente muita abreviações diretas como (e.g. pos: posição) ou abreviações bem estabelecidas (ex.: pr: pressionar).

## Guia de codigo
* Funções:
  * Tente escrever funções menores que 50 linhas
  * Sempre menor que 100 linhas (exceto algo mais aprimorado)
* Variáveis:
  * Uma linha, uma declaração (RUIM: char x, y;)
  * Use `<stdint.h>` (*uint8_t*, *int32_t* etc)
  * Declare variáveis quando necessário (nem todas no início da função)
  * Use o menor escopo requerido
  * Variáveis dentro de um arquivo (fora das funções) serão sempre *static*
  * Não use variáveis globais (use funções para configurar/obter variáveis estáticas)

## Comentários
Antes de toda função ter um comentário como este:

```c
/**
 * Rerotna com a tela de um objeto
 * @param obj aponta para um objeto
 * @return ponteiro para uma tela
 */
lv_obj_t * lv_obj_get_scr(lv_obj_t * obj); 
```

Use sempre o formato `/* Alguma coisa */` e NÃO `//Alguma coisa`

Escreva o código escrito para evitar comentários descritivos como:
`x++; /* Adiciona 1 a x */`. 
O código deve mostrar claramente o que você está fazendo.

Você deve escrever **por que** você fez isso:
`x++; /*Porque ao fechar '\0' de um string*/`

"Código resumidos" curtos de umas poucas linhas são aceitáveis. Ex.: `/*Calcular as novas coordenadas*/` 

Nos comentários use \` \` quando referenciar para uma variável. Ex.: ``/*Atualizar o valor de `x_act`*/``

### Formatando
Aqui é exemplo de como aplicar colchetes e usar espaços em branco:
```c
/**
 * Configura um novo texto para um rótulo. Memória será alocada para guardar o texto para um rótulo.
 * @param ponteiro do rótulo para um rótulo do objeto
 * @param texto terminado com string de caractere '\0'. NULL para atualizar o texto atual
 */
void lv_label_set_text(lv_obj_t * label, const char * text)
{   /* Colchetes principais da função em nova linha*/
    
    if(label == NULL) return; /*Nenhum colchete, somente se o comando em linha com a condição if*/
    
    lv_obj_inv(label);
    
    lv_label_ext_t * ext = lv_obj_get_ext(label);

    /*Comente antes uma seção*/
    if(text == ext->txt || text == NULL) {  /*Colchete de uma condiçção começa em linha*/
        lv_label_refr_text(label);
        return;   
    }
    
    ...
}
```

Use identação de 4 espaços ao invés de tab.

Você pode usar **astyle** para formatar o código. As configurações requeridas estão: `docs/astyle_c` e `docs/astyle_h`
Para formatar os arquivos dos códigos:
 `$ find . -type f -name "*.c" | xargs astyle --options=docs/astyle_c`
 
Para formatar os arquivos de cabeçalho:
 `$ find . -type f -name "*.h" | xargs astyle --options=docs/astyle_h`
 
Adicione `-n` para o fim para pular a criação de arquivo de backup OU use `$ find . -type f -name "*.bak"  -delete` (para backups de arquivo fonte) and `find . -type f -name "*.orig" -delete` (para backup de arquivos de cabeçalho)

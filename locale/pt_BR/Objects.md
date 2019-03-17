_Escrito para v5.1_

No Littlev Graphics Library os **blocos básicos para construção** de uma interface de usuário são os objetos. Por exemplo:

- [Botão](/Button)
- [Rótulo](/Label)
- [Imagem](/Image)
- [Lista](/List)
- [Gráfico](/Chart)
- [Área de texto](/Text-area)

Clique para checar todos os [tipos de Objetos](Object-types) existentes

#### Atributos de objetos

##### Atributos básicos

Os objetos tem um atributos básicos na qual são independentemente comum de seus tipos:

- Posição
- Tamanho
- Pai
- Desenho ativado
- Clique ativado, etc.

Você pode assinar/obter esses atributos com funções `lv_obj_set_...` e `lv_obj_get_...`. Por exemplo:

```c
/*Atribui ao objeto atributos básicos*/
lv_obj_set_size(btn1, 100, 50);						/*Tamanho do botão*/
lv_obj_set_pos(btn1, 20,30);						/*Posição do botão*/
```

Para ver todas as funções disponíveis, visite os objetos de base da [documentação](/Base-object)

##### Atributos específicos

O tipos de objeto tem atributos especiais. Por exemplo um deslizador tem:

- Valores mínimos e máximos
- Valores atuais
- Função callback para novos valores
- Estilos

Para esses atributos, todos tipos de objetos tem uma única função API. Por exemplo para um deslizador:

```c
/*Atribui ao deslizador os atributos específicos*/
lv_slider_set_range(slider1, 0, 100);			/*Atribui os valores mínimo e máximo*/
lv_slider_set_value(slider1, 40);			/*Atribui o valor (posição)*/
lv_slider_set_action(slider1, my_action);		/*Adiciona uma função callback*/
```

#### Mecanismo de trabalho dos objetos

##### Estrutura pai-filho

Um pai pode ser considerado como o container de seus filhos. Todos os objetos tem exatamente um objeto pai (exceto as telas), mas um pai pode ter ilimitado número de filhos. Não existe nenhuma limitação para o tipo de pai, mas há tipicamente objetos pai (ex.: botão) e filho (ex.: rótulo).

##### Tela – o pai mais básico

A tela é um objeto especial na qual não possui um objeto pai. Sempre existe uma tela ativa. Por padrão, a biblioteca cria e carrega um. Para obter a tela ativa use a função `lv_scr_act()`.

Uma tela pode ser criada com qualquer tipo de objeto, por exemplo, um objeto básico ou uma imagem para fazer um papel de parede.

##### Movendo junto

Se a posição do pai é mudada, o filho irá mover junto com o pai. Contudo todas as posições são relativas ao pai. Para a coordenada (0;0), significa que os objetos permanecerão no topo ao lado esquerdo do pai, independentemente da posição do pai.

![Objetos estão movendo junto 1](https://littlevgl.com/docs/par_child1.png)  

```c
lv_obj_t * par = lv_obj_create(lv_scr_act(), NULL); 	/*Cria um objeto pai na tela atual*/
lv_obj_set_size(par, 100, 80);		                /*Atribui um tamanho ao pai*/

lv_obj_t * obj1 = lv_obj_create(par, NULL);	        /*Cria um objeto dentro do objeto pai criado anteriormente*/
lv_obj_set_pos(obj1, 10, 10);			        /*Atribui a posição do novo objeto*/
```

Modificar a posição do pai
  
![Objetos gráficos estão movendo juntos 2](https://littlevgl.com/docs/par_child2.png)  

```c
lv_obj_set_pos(par, 50, 50);		/*Move o pai. O filho irá se mover junto com ele.*/
```

##### Visibilidade somente no pai

Se um filho parcialmente ou totalmente está fora de seu pai então as partes fora não será visível.
  
![Um objeto gráfico é visível no seu pai](https://littlevgl.com/docs/par_child3.png)  

```c
lv_obj_set_x(obj1, -30);		/*Move o filho um pequeno pedaçõ do pai*/
```

#### Criar - apagar objetos

Nos objetos de biblioteca gráfica podem somente ser criados ou apagados dinamicamente em tempo real. Significa que somente objetos criados consome RAM. Por exemplo, se voccê precisa de um gráfico, você pode criá-lo somente quando é requerido e apagá-lo depois de ter usado.

Todos os tipos de objetos tem sua própria função **criar** com um protótipo unificado. Ele precisa de dois parâmetros: um ponteiro do pai e opcionalmente um ponteiro para um outro objeto do mesmo tipo. Se o segundo parâmetro não é _NULL_ então esses objetos será copiado para um novo. Para criar uma tela dê umm _NULL_ como pai. O valor de retorno da função criada é um ponteiro ao objeto criado. Independentemente do tipo do objeto da variável comum **lv_obj_t** que será usado. Esse ponteiro pode ser usado mais tarde para atribuir ou obter atributos desse objeto. As funções de criação deve se parecer como essas:

```c
lv_obj_t * lv_type_create(lv_obj_t * parent, lv_obj_t * copy);
```

Existe uma comum função **delete** para todos os tipos de objetos. Ela apaga o objeto e todos os seus filhos.

```c
void lv_obj_del(lv_obj_t * obj);
```

Você pode apagar somente os filhos de um objeto mas deixar o objeto pai "vivo":

```c
void lv_obj_clean(lv_obj_t * obj);
```

#### Camadas

O objeto previamente criado (e seus filhos) serão desenhados anteriormente (mais perto do background). Em outras palavras, os objetos criados por último serão seus irmãos. Isto é muito importante, a ordem é calculada entre os objetos do mesmo nível ("irmãos").

Camadas podem ser adicionada facilmente criando 2 objetos (na qual podem ser transparentes) primeiramente 'A' e segundamente 'B'. 'A' e todos objetos sobre ele estarão no atrás (background_ e podem ser cobertos por 'B' e seus filhos.

  
![Criando objetos gráficos no Littlev Graphics Library](https://littlevgl.com/docs/par_child4.png)  

```c
/*Cria uma tela*/
lv_obj_t * scr = lv_obj_create(NULL, NULL);
lv_scr_load(scr);       						    /*Carrega a tela*/

/*Cria 2 botões*/
lv_obj_t * btn1 = lv_btn_create(scr, NULL);         /*Cria um botão na tela*/
lv_btn_set_fit(btn1, true, true);                   /*Ativa automaticamente o tamanho de acordo com o conteúdo*/
lv_obj_set_pos(btn1, 60, 40);              		    /*Atribui a posição do botão*/

lv_obj_t * btn2 = lv_btn_create(scr, btn1);         /*Copia o primeiro botão*/
lv_obj_set_pos(btn2, 180, 80);                 	    /*Atribui a posição do botão*/

/*Adiciona rótulos aos botões*/
lv_obj_t * label1 = lv_label_create(btn1, NULL);	/*Cria um rótulo nos primeiros botões*/
lv_label_set_text(label1, "Button 1");          	/*Atribui o texto ao rótulo*/

lv_obj_t * label2 = lv_label_create(btn2, NULL);  	/*Cria um rótulo no segundo botão*/
lv_label_set_text(label2, "Button 2");            	/*Atribui o texto ao rótulo*/

/*Apaga o segundo rótulo*/
lv_obj_del(label2);
```

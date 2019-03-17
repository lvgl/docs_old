_Escrito para v5.1_

Você pode testar o Littlev Graphics Library **usando somente seu PC** sem qualquer placa de desenvolvimento. Escreva um código, rode no seu PC e veja o resultado no monitor. O software é de plataforma cruzada: São suportados Windows, Linux e OSX!

- Precisa somente de poucos minutos de configuração
	
- Custa $0. Sem custo para PCB e não precisa pagar por nenhum software
	
- Um display TFT é simulado e mostrado no monitor de seu PC
	
- O touch pad é substituido pelo seu mouse
	
- O código escrito é portável, você pode simplesmente copiar ele quando estiver usando um hardware embutido

#### Instalando o Eclipse CDT

Eclipse CDT é um IDE C/C++. Você pode usar outras IDEs também, mas neste tutorial é mostrado a configuração para o Eclipse CDT.

Eclipse é um software baseado em Java, certifique-se de que **Java Runtime Environment** está instalado no seu sistema.

Em distros baseado em pacotes Debian (ex.: Ubuntu): `sudo apt-get install default-jre`

Você pode fazer download do Eclipse CDT do [https://eclipse.org/cdt/](http://www.eclipse.org/downloads/). Inicie o instalador e escolha *Eclipse CDT* da lista.

#### Instalando o SDL 2

O simulador PC usa a biblioteca de plataforma cruzada [SDL 2](https://www.libsdl.org/download-2.0.php) para simular um display TFT e o touch pad.

##### Linux

No **Linux** você pode facilmente instalar o SDL2 usando um terminal:

1. Encontre a versão atual do SDL2: `apt-cache search libsdl2 (Ex.: libsdl2-2.0-0)`
2. Instale o SDL2: `sudo apt-get install libsdl2-2.0-0` (troque com a versão encontrada)
3. Instale o pacote de desenvolvimento SDL2: `sudo apt-get install libsdl2-dev`
4. Se os pacotes essenciais não estão instalados ainda: `sudo apt-get install build-essential`

##### Windows

Se você está usando o **Windows** primeiramente você precisa instalar o MinGW ([64 bit version](http://mingw-w64.org/doku.php/download)). Depois disto siga os passoas para adicionar o SDL2:

1. Faça download das bibliotecas do SDL.
Vá para [https://www.libsdl.org/download-2.0.php](https://www.libsdl.org/download-2.0.php) e faça download do _Development Libraries: SDL2-devel-2.0.5-mingw.tar.gz_
2. Descompacte o arquivo e va para o diretório _x86_64-w64-mingw32_ (para MinGW 64 bit) ou para _i686-w64-mingw32_ (para MinGW 32 bit)
3. Copie a pasta _..._mingw32/include/SDL2_ para _C:/MinGW/.../x86_64-w64-mingw32/include_
4. Copie o conteúdo _..._mingw32/lib/_ para _C:/MinGW/.../x86_64-w64-mingw32/lib_
5. Copie _..._mingw32/bin/SDL2.dll_ para _{eclipse_worksapce}/pc_simulator/Debug/_.  Faça isso depois do Eclipse ser instalado.

Nota: Se você usar o **Microsoft Visual Studio** ao invés do Eclipse então você não precisa instalar o MinGW

##### OSX

No **OSX** você pode facilmente instalar o SDL2 com brew: `brew install sdl2`

Se algo não está funcionando eu sugiro [esse tutorial](http://lazyfoo.net/tutorials/SDL/01_hello_SDL/index.php) para iniciar com o SDL.

### Projeto pré-configurado

Um projeto de biblioteca gráfica pré-configurada (baseada no último lançamento) está sempre disponível no projeto do simulador PC. Você pode encontrá-lo no [GitHub](https://github.com/littlevgl/proj_pc) ou na página [Download](https://littlevgl.com/download). O projeto está configurado para o Eclipse CDT.

#### Adicionar o projeto pré-configurado ao Eclipse CDT

Rode o Eclipse CDT. Ele mostrará um diálogo sobre o **atalho do espaço de trabalho*. Antes de aceitá-lo, cheque que o atalho e a cópia do download do projeto pré-configurado esteja lá. Agora você pode aceitar o atalho do espaço de trabalho. É claro que você pode modificar esse atalho mas no caso de copiar o projeto para aquela localização.

Feche a janela de início e vá para o **File-&gt;Import** e escolha **General-&gt;Existing project into Workspace**. **Browse the root directory** do seu projeto e clique **Finish**

No **Windows** você tem que fazer duas coias adicionais:

- Copie o **SDL2.dll** dentro da pasta Debug do seu proojeto
- Botão direito no progeto -&gt; Project properties -&gt; C/C++ Build -&gt; Settings -&gt; Libraries -&gt; Add ... e adicione _mingw32_ acima do SDLmain e do SDL. (A ordem é importante: mingw32, SDLmain, SDL)

#### Compilar e rodar

Agora que você está pronto, rode o Littlev Graphics Library no seu PC. Clique no Hammer Icon no topo da barra de menu para construir (Build) o projeto. Se você tiver feito tudo certo e não obtiver nenhum erro. Note que em alguns sistemas, alguns passos adicionais serão necessários para "ver" SDL 2 no Eclipse mas na maioria dos casos as configurações no projeto baixado é suficiente.

Depois do sucesso da compilação, clique no botão Play na barra de topo do menu para rodar o projeto. Agora a janela deve aparecer no meio da sua tela.

Agoora tudo está pronto para usar o Littlev Graphics Library na prática ou começar o desenvolvimento no seu PC.

#### Próximos passos

Para criar seu primeiro GUI LittlevGL você deve ler as páginas abaixo [[Portabilidade]] no conteúdo ao lado.

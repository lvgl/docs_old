```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/fr/get-started/pc-simulator.md
```
# Simulateur sur PC


You can try out the LittlevGL **using only your PC** (i.e. without any development boards). The LittlevGL will run on a simulator environment on the PC where anyone can write and experiment the real LittlevGL applications.

Simulator on the PC have the following advantages:
- Hardware independent - Write a code, run it on the PC and see the result on the PC monitor.
- Cross-platform - Any Windows, Linux or OSX PC can run the PC simulator.  
- Portability - the written code is portable, which means you can simply copy it when using an embedded hardware.
- Easy Validation - The simulator is also very useful to report bugs because it means common platform for every user. So it's a good idea to reproduce a bug in simulator and use the code snippet in the [Forum](https://forum.littlevgl.com).

## Choisir un IDE

The simulator is ported to various IDEs (Integrated Development Environments). Choose your favorite IDE, read its README on GitHub, download the project, and load it to the IDE.

```eval_rst
.. raw:: html

  <table style="width:100%">
  <thead>
  <tr>
  <th>Eclipse</th>
  <th>CodeBlocks</th>
  <th>Visual Studio</th>
  <th>PlatformIO</th>
  <th>Qt Creator</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><a href="https://github.com/littlevgl/pc_simulator_sdl_eclipse"><img src="https://littlevgl.com/logo/ide/eclipse.jpg"></a> </td>
  <td><a href="https://github.com/littlevgl/pc_simulator_win_codeblocks"><img src="https://littlevgl.com/logo/ide/codeblocks.jpg"></a></td>
  <td><a href="https://github.com/littlevgl/visual_studio_2017_sdl_x64"><img src="https://littlevgl.com/logo/ide/visualstudio.jpg"></a></td>
  <td><a href="https://github.com/littlevgl/pc_simulator_sdl_platformio"><img src="https://littlevgl.com/logo/ide/platformio.jpg"></a></td>
  <td><a href="https://blog.littlevgl.com/2019-01-03/qt-creator"><img src="https://littlevgl.com/logo/ide/qtcreator.jpg"> </a></td>
  </tr>

  <tr>
  <td>Multi-plateforme<br>avec SDL 
  </td><td>Natif Windows  </td>
  <td>Multi-plateforme<br>avec SDL  </td>
  <td>Multi-plateforme<br>avec SDL </td>
  <td>Multi-plateforme<br>avec SDL  </td>
  </tr>
  </tbody></table>
```


You can use any IDEs for the development but, for simplicity, the configuration for Eclipse CDT is focused in this tutorial.
The following section describes the set-up guide of Eclipse CDT in more details.

**Note: If you are on Windows, it's usually better to use the Visual Studio or CodeBlocks projects instead. They work out of the box without requiring extra steps.**

## Configurer Eclipse CDT

### Installer Eclipse CDT

[Eclipse CDT](https://eclipse.org/cdt/) is a C/C++ IDE.

Eclipse est un logiciel écrit en Java de ce fait, soyez certain que l'**environnement d'exécution Java** est installé sur votre système.   

Sur les distribution basée sur Debian (p.ex. Ubuntu) : `sudo apt-get install default-jre`

Note: If you are using other distros, then please refer and install 'Java Runtime Environment' suitable to your distro.

You can download Eclipse's CDT from: [https://www.eclipse.org/cdt/downloads.php](https://www.eclipse.org/cdt/downloads.php). Start the installer and choose *Eclipse CDT* from the list.

### Installer SDL 2

Le simulateur PC utilise la librairie multi-plateforme [SDL 2](https://www.libsdl.org/download-2.0.php) pour simuler un écran TFT et un pavé tactile. 

#### Linux
Sur **Linux** vous pouvez installer facilement SDL 2 à partir d'un terminal :

1. Trouvez la version actuelle de SDL 2 : `apt-cache search libsdl2 (e.g. libsdl2-2.0-0)`
2. Installez SDL 2 : `sudo apt-get install libsdl2-2.0-0` (remplacez par la version trouvée)
3. Installez le paquet de dévellopement de SDL 2 : `sudo apt-get install libsdl2-dev`
4. Si les paquets de construction essentiels ne sont pas déjà installés : `sudo apt-get install build-essential`

#### Windows
If you are using **Windows** firstly you need to install MinGW ([64 bit version](http://mingw-w64.org/doku.php/download)). After installing MinGW, do the following steps to add SDL2:

1. Téléchargez les libraries de développement de SDL.   
Allez sur [https://www.libsdl.org/download-2.0.php](https://www.libsdl.org/download-2.0.php) et téléchargez _Development Libraries: SDL2-devel-2.0.5-mingw.tar.gz_
2. Décompressez l'archive et allez dans le répertoire _x86_64-w64-mingw32_ (pour MinGW 64 bits) ou _i686-w64-mingw32_ (pour MinGW 32 bits)
3. Copiez le répertoire _..._mingw32/include/SDL2_ vers _C:/MinGW/.../x86_64-w64-mingw32/include_
4. Copiez le contenu de _..._mingw32/lib/_ dans _C:/MinGW/.../x86_64-w64-mingw32/lib_
5. Copiez _..._mingw32/bin/SDL2.dll_ dans _{eclipse_workspace}/pc_simulator/Debug/_.  Faites le plus tard quand Eclipse est installé. 

Note: If you are using **Microsoft Visual Studio** instead of Eclipse then you don't have to install MinGW. 

#### OS X
Sur **OS X** vous pouvez facilement installer SDL 2 avec brew : `brew install sdl2`

If something is not working, then please refer [this tutorial](http://lazyfoo.net/tutorials/SDL/01_hello_SDL/index.php) to get started with SDL.

### Projet pré-configuré

A pre-configured graphics library project (based on the latest release) is always available to get started easily. 
You can find the latest one on [GitHub](https://github.com/littlevgl/proj_pc) or on the [Download](https://littlevgl.com/download) page. 
(Please note that, the project is configured for Eclipse CDT). 

### Ajouter le projet pré-configuré à Eclipse CDT.

Run Eclipse CDT. It will show a dialogue about the **workspace path**. Before accepting the path, check that path and copy (and unzip) the downloaded pre-configured project there. After that, you can accept the workspace path. Of course you can modify this path but, in that case copy the project to the corresponding location.

Fermez la fenêtre de démarrage et allez à **Fichier-&gt;Importer...** et choisissez **Généralités-&gt;Projets existants dans l'espace de travail**. **Allez au répertoire racine** du projet et cliquez **Terminer**

Sur **Windows** vous devez effectuer deux actions additionnelles :

- Copiez le fichier **SDL2.dll** dans le répertoire Debug du projet
- Faites un clic droit sur le projet -&gt; Propriétés -&gt; Génération C/C++ -&gt; Paramètres -&gt; Bibliothèques -&gt; Ajouter... et ajoutez _mingw32_ au-dessus de SDLmain et SDL. L'ordre est important : mingw32, SDLmain, SDL

### Compilation et exécution

Now you are ready to run the LittlevGL Graphics Library on your PC. Click on the Hammer Icon on the top menu bar to Build the project. If you have done everything right, then you will not get any errors. Note that on some systems additional steps might be required to "see" SDL 2 from Eclipse but, in most of cases the configurations in the downloaded project is enough.

After a success build, click on the Play button on the top menu bar to run the project. Now a window should appear in the middle of your screen.

Tout est prêt pour utiliser la librairie graphique LittlevGL pour l'apprentissage ou pour débuter le développement sur votre PC.

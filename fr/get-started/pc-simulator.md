```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/fr/get-started/pc-simulator.md
```
# Simulateur sur PC


Vous pouvez essayer LittlevGL **en utilisant uniquement votre PC** (c’est-à-dire sans carte de développement). LittlevGL fonctionnera sur un environnement de simulation sur le PC dans lequel il est possible d'écrire et d'expérimenter de réelles applications LittlevGL.

Le simulateur sur PC présente les avantages suivants :
- Indépendant du matériel - Écrivez du code, exécutez-le sur PC et visualisez le résultat sur le moniteur du PC.
- Multi-plateforme - Tous les ordinateurs Windows, Linux ou OS X peuvent exécuter le simulateur PC.
- Portabilité - Le code écrit est portable, ce qui signifie qu'il suffit de le copier pour l'utiliser sur un matériel embarqué.
- Validation facile - Le simulateur est également très utile pour signaler des bogues car il représente une plateforme commune pour chaque utilisateur. C'est donc une bonne idée de reproduire un bogue dans le simulateur et d'utiliser l'extrait de code dans le [forum](https://forum.littlevgl.com).

## Choisir un EDI

Le simulator est portés sur plusieurs EDIs (Environnement de Développement Intégré). Choisissez votre EDI préféré, lisez son README sur GitHub, téléchargez le projet, et chargez le dans EDI.

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


Vous pouvez utiliser n’importe quel EDI pour le développement mais, pour des raisons de simplicité, ce didacticiel est axé sur la configuration d’Eclipse CDT.
La section suivante décrit la configuration d’Eclipse CDT de manière plus détaillée.

**Note : si vous utilisez Windows, il est généralement préférable d'utiliser Visual Studio ou CodeBlocks. Ils fonctionnent directement sans nécessiter d'étapes supplémentaires.**

## Configurer Eclipse CDT

### Installer Eclipse CDT

[Eclipse CDT](https://eclipse.org/cdt/) iest un IDE C/C++.

Eclipse est un logiciel écrit en Java de ce fait, soyez certain que l'**environnement d'exécution Java** est installé sur votre système.   

Sur les distribution basée sur Debian (p.ex. Ubuntu) : `sudo apt-get install default-jre`

Note : si vous utilisez d'autres distributions, installez un 'Java Runtime Environment' adapté à votre distribution.

Vous pouvez télécharger Eclipse CDT à partir de : [https://eclipse.org/cdt/downloads.php](http://www.eclipse.org/downloads/downloads.php). Démarrez l'installeur est choisissez *Eclipse CDT* dans la liste.

### Installer SDL 2

Le simulateur PC utilise la librairie multi-plateforme [SDL 2](https://www.libsdl.org/download-2.0.php) pour simuler un écran TFT et un pavé tactile. 

#### Linux
Sur **Linux** vous pouvez installer facilement SDL 2 à partir d'un terminal :

1. Trouvez la version actuelle de SDL 2 : `apt-cache search libsdl2 (e.g. libsdl2-2.0-0)`
2. Installez SDL 2 : `sudo apt-get install libsdl2-2.0-0` (remplacez par la version trouvée)
3. Installez le paquet de dévellopement de SDL 2 : `sudo apt-get install libsdl2-dev`
4. Si les paquets de construction essentiels ne sont pas déjà installés : `sudo apt-get install build-essential`

#### Windows
Si vous utilisez **Windows** vous devez en premier lieu installer MinGW ([version 64 bits](http://mingw-w64.org/doku.php/download)). Après ça, effectuez les étapes suivantes pour ajouter SDL 2 :

1. Téléchargez les libraries de développement de SDL.   
Allez sur [https://www.libsdl.org/download-2.0.php](https://www.libsdl.org/download-2.0.php) et téléchargez _Development Libraries: SDL2-devel-2.0.5-mingw.tar.gz_
2. Décompressez l'archive et allez dans le répertoire _x86_64-w64-mingw32_ (pour MinGW 64 bits) ou _i686-w64-mingw32_ (pour MinGW 32 bits)
3. Copiez le répertoire _..._mingw32/include/SDL2_ vers _C:/MinGW/.../x86_64-w64-mingw32/include_
4. Copiez le contenu de _..._mingw32/lib/_ dans _C:/MinGW/.../x86_64-w64-mingw32/lib_
5. Copiez _..._mingw32/bin/SDL2.dll_ dans _{eclipse_workspace}/pc_simulator/Debug/_.  Faites le plus tard quand Eclipse est installé. 

Note : si vous utilisez **Microsoft Visual Studio** à la place d'Eclipse alors vous n'avez pas besoin d'installer MinGW.

#### OS X
Sur **OS X** vous pouvez facilement installer SDL 2 avec brew : `brew install sdl2`

Si quelque chose ne fonctionne pas, alors référez-vous à ce [tutoriel](http://lazyfoo.net/tutorials/SDL/01_hello_SDL/index.php) pour débuter avec SDL.

### Projet pré-configuré

Un projet pré-configuré pour la librairie graphique, basé sur la dernière version publiée, est toujours disponible. 
Vous pouvez trouver le plus récent sur [GitHub](https://github.com/littlevgl/proj_pc) ou sur la page de [téléchargement](https://littlevgl.com/download). 
Notez que le projet est configuré pour Eclipse CDT.

### Ajouter le projet pré-configuré à Eclipse CDT.

Lancez Eclipse CDT. Une boîte de dialogue au sujet du **chemin de l'espace de travail** est affichée. Avant de la valider, vérifiez le chemin et copiez à cet emplacement, puis décompressez, le projet pré-configuré préalablement téléchargé. Après ça vous pouvez accepter le chemin de l'espace de travail. Bien entendu, ce chemin peut être modifié mais dans ce cas il faut copier le projet vers l'emplacement correspondant.

Fermez la fenêtre de démarrage et allez à **Fichier-&gt;Importer...** et choisissez **Généralités-&gt;Projets existants dans l'espace de travail**. **Allez au répertoire racine** du projet et cliquez **Terminer**

Sur **Windows** vous devez effectuer deux actions additionnelles :

- Copiez le fichier **SDL2.dll** dans le répertoire Debug du projet
- Faites un clic droit sur le projet -&gt; Propriétés -&gt; Génération C/C++ -&gt; Paramètres -&gt; Bibliothèques -&gt; Ajouter... et ajoutez _mingw32_ au-dessus de SDLmain et SDL. L'ordre est important : mingw32, SDLmain, SDL

### Compilation et exécution

Vous êtes maintenant prêt à utiliser la librairie graphique LittlevGL sur votre PC. Cliquer sur l'icône Marteau de la barre de menu pour compiler le projet. Si vous avez tout fait correctement aucune erreur ne se produira. Notez que sur certains systèmes des étapes additionnelles peuvent être requises pour qu'Eclipse prenne en compte SDL 2, mais dans la plupart des cas, la configuration du projet téléchargé est suffisante.

Après avoir compiler avec succès, cliquez sur le bouton Jouer de la barre de menu pour démarrer le projet. Maintenant une fenêtre doit apparaître au milieu de l'écran.

Tout est prêt pour utiliser la librairie graphique LittlevGL pour l'apprentissage ou pour débuter le développement sur votre PC.

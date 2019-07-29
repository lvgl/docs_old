```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/fr/porting/project.md
```

# Configurer un projet

## Obtenir la librairie

LittlevGL Graphics Library est disponible sur GitHub : [https://github.com/littlevgl/lvgl](https://github.com/littlevgl/lvgl). 

Vous pouvez la cloner ou télécharger la dernière version de la librairie depuis GitHub ou vous pouvez également utiliser la page [Télécharger] (https://littlevgl.com/download).

La librairie graphique est le répertoire **lvgl** qui doit être copié dans votre projet.

## Fichier de configuration

Il existe un fichier d’en-tête de configuration pour LittlevGL appelé **lv_conf.h**. Il définit le comportement de base de la bibliothèque, désactive les modules et fonctionnalités inutilisés, ajuste la taille des tampons au moment de la compilation, etc.
 
Copiez **lvgl/lv_conf_template.h** au même niveau que le répertoire *lvgl* et renommez-le en *lv_conf.h*. Ouvrez le fichier et changez le `#if 0` du début en` #if 1` pour activer son contenu.

* lv_conf.h * peut également être copié à d’autres emplacements, mais vous devez ensuite ajouter `LV_CONF_INCLUDE_SIMPLE` à vos options de compilation (p.ex. `-DLV_CONF_INCLUDE_SIMPLE` pour gcc) et définir le chemin d’inclusion manuellement.

Dans le fichier de configuration, les commentaires expliquent la signification des options. Vérifiez au moins ces trois options de configuration et modifiez-les en fonction de votre matériel :
1. **LV_HOR_RES_MAX** la résolution horizontale de votre écran
2. **LV_VER_RES_MAX** la résolution verticale de votre écran
3. **LV_COLOR_DEPTH** 8 pour (RG332), 16 pour (RGB565) ou 32 pour (RGB888 et ARGB8888). 

## Initialisation

Pour utiliser la librairie graphique, vous devez l'initialiser ainsi que les autres composants. Voici l'ordre d'initialisation :

1. Appelez *lv_init()*
2. Initialisez vos pilotes
3. Enregistrez les pilotes de périphérique d’affichage et d’entrée dans LittlevGL. En savoir plus sur l'enregistrement : [Affichage](/porting/display) et [Périphérique d'entrée](/porting/indev).
4. Appelez `lv_tick_inc(x)` toutes les `x` millisecondes dans une interruption pour indiquer le temps écoulé. [En savoir plus](/porting/tick).
5. Appelez `lv_task_handler()` périodiquement toutes les quelques millisecondes pour gérer les tâches liées à LittlevGL. [En savoir plus](/porting/task-handler).

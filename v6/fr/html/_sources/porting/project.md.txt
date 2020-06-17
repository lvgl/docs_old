```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/fr/porting/project.md
```

# Configurer un projet

## Obtenir la librairie

LittlevGL Graphics Library is available on GitHub: [https://github.com/littlevgl/lvgl](https://github.com/littlevgl/lvgl).

You can clone it or download the latest version of the library from GitHub or you can use the [Download](https://littlevgl.com/download) page as well.

La librairie graphique est le répertoire **lvgl** qui doit être copié dans votre projet.

## Configuration file

There is a configuration header file for LittlevGL called **lv_conf.h**. It sets the library's basic behaviour, disables unused modules and features, adjusts the size of memory buffers in compile-time, etc.

Copy **lvgl/lv_conf_template.h** next to the *lvgl* directory and rename it to *lv_conf.h*. Open the file and change the `#if 0` at the beginning to `#if 1` to enable its content.

*lv_conf.h* can be copied other places as well but then you should add `LV_CONF_INCLUDE_SIMPLE` define to your compiler options (e.g. `-DLV_CONF_INCLUDE_SIMPLE` for gcc compiler) and set the include path manually.

Dans le fichier de configuration, les commentaires expliquent la signification des options. Vérifiez au moins ces trois options de configuration et modifiez-les en fonction de votre matériel :
1. **LV_HOR_RES_MAX** Your display's horizontal resolution.
2. **LV_VER_RES_MAX** Your display's vertical resolution.
3. **LV_COLOR_DEPTH** 8 for (RG332), 16 for (RGB565) or 32 for (RGB888 and ARGB8888).

## Initialisation

To use the graphics library you have to initialize it and the other components too. The order of the initialization is:

1. Call *lv_init()*.
2. Initialize your drivers.
3. Enregistrez les pilotes de périphérique d’affichage et d’entrée dans LittlevGL. En savoir plus sur l'enregistrement : [Affichage](/porting/display) et [Périphérique d'entrée](/porting/indev).
4. Appelez `lv_tick_inc(x)` toutes les `x` millisecondes dans une interruption pour indiquer le temps écoulé. [En savoir plus](/porting/tick).
5. Appelez `lv_task_handler()` périodiquement toutes les quelques millisecondes pour gérer les tâches liées à LittlevGL. [En savoir plus](/porting/task-handler).

```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/fr/porting/indev.md
```
# Interface de périphérique d'entrée

## Types de périphériques d'entrée

Pour configurer un périphérique d'entrée, une variable `lv_indev_drv_t` doit être initialisée :

```c
lv_indev_drv_t indev_drv;
lv_indev_drv_init(&indev_drv);      /* Initialisation de base */
indev_drv.type =...                 /* Voir ci-dessous. */
indev_drv.read_cb =...              /* Voir ci-dessous. */
/* Enregistre le pilote dans LittlevGL et sauvegarde l'objet de périphérique d'entrée créé */
lv_indev_t * my_indev = lv_indev_drv_register(&indev_drv);
```

**type** can be
- **LV_INDEV_TYPE_POINTER** pavé tactile ou souris
- **LV_INDEV_TYPE_KEYPAD** clavier
- **LV_INDEV_TYPE_ENCODER** encodeur avec options gauche, droite et appui
- **LV_INDEV_TYPE_BUTTON** bouton externe

**read_cb** is a function pointer which will be called periodically to report the current state of an input device.
Les données peuvent être placées dans un tampon, la fonction retourne `false` lorsqu'il ne reste plus de données à lire ou` true` lorsque le tampon n'est pas vide.


Visitez [Périphériques d'entrée](/overview/indev) pour en savoir plus sur les périphériques d'entrée en général.


###  Pavé tactile, souris ou autre pointeur
Input devices which can click points of the screen belong to this category.

```c
indev_drv.type = LV_INDEV_TYPE_POINTER;
indev_drv.read_cb = my_input_read;

...

bool my_input_read(lv_indev_drv_t * drv, lv_indev_data_t*data)
{
    data->point.x = touchpad_x;
    data->point.y = touchpad_y;
    data->state = LV_INDEV_STATE_PR or LV_INDEV_STATE_REL;
    return false; /* Pas de tampon donc plus de données à lire */
}
```

``` important::  Les pilotes de pavé tactile doivent renvoyer les dernières coordonnées X/Y même lorsque l'état est *LV_INDEV_STATE_REL*.
```

To set a mouse cursor use `lv_indev_set_cursor(my_indev, &img_cursor)`. (`my_indev` is the return value of `lv_indev_drv_register`)

### Keypad or keyboard

Les claviers complets avec toutes les lettres ou plus simples avec quelques boutons de navigation sont décrits ici.

Pour utiliser un clavier :
- Enregistrez une fonction `read_cb` avec le type` LV_INDEV_TYPE_KEYPAD`.
- Activez `LV_USE_GROUP` dans *lv_conf.h*
- Un groupe d'objets doit être créé : `lv_group_t * g = lv_group_create()` et des objets doivent y être ajoutés avec `lv_group_add_obj(g, obj)`
- Le groupe créé doit être affecté à un périphérique d'entrée : `lv_indev_set_group(my_indev, g)` (`my_indev` est la valeur de retour de` lv_indev_drv_register`)
- Utilisez `LV_KEY_...` pour naviguer parmi les objets du groupe. Voir `lv_core/lv_group.h` pour les touches disponibles.

```c
indev_drv.type = LV_INDEV_TYPE_KEYPAD;
indev_drv.read_cb = my_input_read;

...

bool keyboard_read(lv_indev_drv_t * drv, lv_indev_data_t*data){
  data->key = last_key();            /* Obtient  la dernière touche pressée ou relâchée */

  if(key_pressed()) data->state = LV_INDEV_STATE_PR;
  else data->state = LV_INDEV_STATE_REL;

  return false; /* Pas de tampon donc plus de données à lire */
}
```

### Encoder
Avec un encodeur, vous pouvez réaliser 4 actions :
1. Appuyer son bouton
2. Long-press its button
3. Tourner à gauche
4. Tourner à droite

En bref, les encodeurs fonctionnent comme ceci :
- By turning the encoder you can focus on the next/previous object.
- When you press the encoder on a simple object (like a button), it will be clicked.
- If you press the encoder on a complex object (like a list, message box, etc.) the object will go to edit mode whereby turning the encoder you can navigate inside the object.
- Pour quitter le mode édition, appuyez longuement sur le bouton.


Pour utiliser un *encodeur* (comme un *clavier*), des objets doivent être ajoutés aux groupes.


```c
indev_drv.type = LV_INDEV_TYPE_ENCODER;
indev_drv.read_cb = my_input_read;

...

bool encoder_read(lv_indev_drv_t * drv, lv_indev_data_t*data){
  data->enc_diff = enc_get_new_moves();

  if(enc_pressed()) data->state = LV_INDEV_STATE_PR;
  else data->state = LV_INDEV_STATE_REL;

  return false; /* Pas de tampon donc plus de données à lire */
}
```

### Button
*Buttons* mean external "hardware" buttons next to the screen which are assigned to specific coordinates of the screen.
Si un bouton est pressé, il simule l'appui sur la coordonnée attribuée (comme un pavé tactile)

Pour affecter des boutons aux coordonnées, utilisez `lv_indev_set_button_points(my_indev, points_array)`.  
`points_array` doit ressembler à `const lv_point_t points_array[] = { {12, 30}, {60, 90}, ... }`

``` important:: points_array ne peut être hors de portée. Déclarez-le en tant que variable globale ou en tant que variable statique dans une fonction.
```

```c
indev_drv.type = LV_INDEV_TYPE_BUTTON;
indev_drv.read_cb = my_input_read;

...

bool button_read(lv_indev_drv_t * drv, lv_indev_data_t*data){
    static uint32_t last_btn = 0;   /*Store the last pressed button*/
    int btn_pr = my_btn_read();     /* Obtient l'ID (0, 1, 2 ...) du bouton pressé */
    if(btn_pr >= 0) {               /* Un bouton est-il pressé ? P.ex. -1 indique qu'aucun bouton n'est pressé */
       last_btn = btn_pr;           /* Sauvegarde l'ID du bouton pressé */
       data->state = LV_INDEV_STATE_PR;  /* Définit l'état pressé */
    } else {
       data->state = LV_INDEV_STATE_REL; /* Définit l'état relâché */
    }

    data->btn = last_btn;            /* Enregistre le dernier bouton */

    return false;                    /* Pas de tampon donc plus de données à lire */
}
```

## Autres fonctionnalités

Besides `read_cb` a `feedback_cb` callback can be also specified in `lv_indev_drv_t`.
`feedback_cb` is called when any type of event is sent by the input devices. (independently from its type). It allows making feedback for the user e.g. to play a sound on `LV_EVENT_CLICK`.

La valeur par défaut des paramètres suivants peut être définie dans *lv_conf.h* mais la valeur par défaut peut être surchargée dans `lv_indev_drv_t` :
- **drag_limit** Nombre de pixels à parcourir avant de faire glisser l'objet
- **drag_throw** Ralentissement du glissé après lâché en [%]. Une valeur haute signifie un ralentissement plus rapide
- **long_press_time** Temps d'appui avant de générer `LV_EVENT_LONG_PRESSED` (en millisecondes)
- **long_press_rep_time** Intervalle de temps entre deux envois `LV_EVENT_LONG_PRESSED_REPEAT` (en millisecondes)
- **read_task** pointer to the `lv_task` which reads the input device. Its parameters can be changed by `lv_task_...()` functions


Every Input device is associated with a display. By default, a new input device is added to the lastly created or the explicitly selected (using `lv_disp_set_default()`) display.
L’affichage associé est sauvegardé et peut être modifié dans le champ `disp` du pilote.


## API

```eval_rst

.. doxygenfile:: lv_hal_indev.h
  :project: lvgl

```

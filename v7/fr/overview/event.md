```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/fr/overview/event.md
```
# Evénements

Les événements sont déclenchés dans LittlevGL quand il se produit quelque chose d'intéressant pour l'utilisateur, par exemple si un objet :
- est cliqué
- est déplacé
- sa valeur a changé, etc.

L'utilisateur peut affecter une fonction de rappel à un objet pour voir ces événements. En pratique, cela ressemble à ceci :
```c
lv_obj_t * btn = lv_btn_create(lv_scr_act(), NULL);
lv_obj_set_event_cb(btn, my_event_cb);   /* Assigne une fonction de rappel */

...

static void my_event_cb(lv_obj_t * obj, lv_event_t event)
{
    switch(event) {
        case LV_EVENT_PRESSED:
            printf("Pressed\n");
            break;

        case LV_EVENT_SHORT_CLICKED:
            printf("Short clicked\n");
            break;

        case LV_EVENT_CLICKED:
            printf("Clicked\n");
            break;

        case LV_EVENT_LONG_PRESSED:
            printf("Long press\n");
            break;

        case LV_EVENT_LONG_PRESSED_REPEAT:
            printf("Long press repeat\n");
            break;

        case LV_EVENT_RELEASED:
            printf("Released\n");
            break;
    }

       /* Etc. */
}
```

Plusieurs objets peuvent utiliser la même *fonction de rappel*.

## Types d'événements

Les types d'événements suivants existent :

### Evénements génériques

Tous les objets (tels que boutons/étiquettes/curseurs etc.) reçoivent ces événements génériques quel que soit leur type.

## Relatifs aux  périphériques d'entrée
Ils sont envoyés lorsqu'un objet est pressé/relâché etc. par l'utilisateur. Ils sont utilisés pour les périphériques d'entrée *clavier*, *encodeur* et *bouton*, ainsi que pour les *pointeurs*. Consultez la section [Périphériques d'entrée](/overview/indev) pour en savoir plus à leur sujet.
- **LV_EVENT_PRESSED** L'objet a été pressé
- **LV_EVENT_PRESSING** L'objet est pressé(envoyé continuellement pendant l'appui)
- **LV_EVENT_PRESS_LOST** Le périphérique d'entrée est toujours pressé mais hors de l'objet
- **LV_EVENT_SHORT_CLICKED** Relâché avant un délai `LV_INDEV_LONG_PRESS_TIME`. Pas généré si l'objet est déplacé.
- **LV_EVENT_LONG_PRESSED**  Pressé durant `LV_INDEV_LONG_PRESS_TIME`. Pas généré si l'objet est déplacé.
- **LV_EVENT_LONG_PRESSED_REPEAT** Généré après `LV_INDEV_LONG_PRESS_TIME` à chaque `LV_INDEV_LONG_PRESS_REP_TIME` ms. Pas généré si l'objet est déplacé.
- **LV_EVENT_CLICKED** Généré au relâché si l'objet n'est pas déplacé (indépendamment d'un appui long)
- **LV_EVENT_RELEASED** Généré dans tous les cas lorsque l'objet a été relâché, même s'il a été déplacé. Non généré si il y a eu déplacement pendant l'appui et si le relâché intervient en dehors de l'objet. Dans ce cas, `LV_EVENT_PRESS_LOST` est généré.

#### Relatif au pointeur
Ces événements sont envoyés uniquement par des périphériques d’entrée de type pointeur (p.ex. souris ou pavé tactile).
- **LV_EVENT_DRAG_BEGIN** le glissé de l'objet a débuté,
- **LV_EVENT_DRAG_END** le glissé de l'objet est terminé (lancé inclus),
- **LV_EVENT_DRAG_THROW_BEGIN** le lancé de l'objet a débuté (généré après un glissé avec "élan")

#### Relatif au pavé numérique et encodeur
Ces événements sont envoyés par les périphériques d’entrée clavier et encodeur. En savoir plus sur les *groupes* dans la section [Périphériques d'entrée] (overview/indev).
- **LV_EVENT_KEY** Une *touche* est envoyée à l'objet. Typiquement quand elle a été pressée ou répétée après un appui long 
- **LV_EVENT_FOCUSED** L'objet est activé dans son groupe
- **LV_EVENT_DEFOCUSED** L'objet est désactivé dans son groupe

#### Evénements généraux
Autres événements généraux envoyés par la librairie.
- **LV_EVENT_DELETE** L'objet est en cours de suppression. Libérez les données associées allouées par l'utilisateur.

### Evénements spéciaux
Ces événements sont spécifiques à un type particulier d'objet.
- **LV_EVENT_VALUE_CHANGED** La valeur de l'objet a changé (p.ex. pour un [Curseur](/object-types/slider))
- **LV_EVENT_INSERT** Quelque chose est inséré dans l'objet (typiquement à une [Zone de texte](/object-types/ta))
- **LV_EVENT_APPLY**  "Ok", "Appliquer" ou un bouton spécifique similaire a été cliqué (typiquement à partir d'un objet [Clavier](/object-types/kb))
- **LV_EVENT_CANCEL** "Fermer", "Annuler" ou un bouton spécifique similaire a été cliqué (typiquement à partir d'un objet [Clavier](/object-types/kb))
- **LV_EVENT_REFRESH** Demande à actualiser l'objet. Jamais généré par la lirbarie mais peut l'être par l'utilisateur.

Visitez la documentation spécifique à partir de [Types d'objet](/object-types/index) pour comprendre quels événements sont utilisés par un type d'objet.

## Données personnalisées
Certains événements peuvent comporter des données personnalisées. Par exemple, `LV_EVENT_VALUE_CHANGED` indique dans certains cas la nouvelle valeur. Pour plus d'informations, voir la documentation des [Types d'objet](/object-types/index).
Pour obtenir les données personnalisées dans la fonction de rappel, utilisez `lv_event_get_data()`.

Le type des données personnalisées dépend de l’objet, mais si c’est un
- entier alors c'est un `uint32_t *` ou un  `int32_t *`
- texte alors c'est un `char *` ou un `const char *`


## Envoyer des événements manuellement

Pour envoyer manuellement des événements à un objet, utilisez `lv_event_send(obj, LV_EVENT_..., &custom_data)`. 

Par exemple, cela peut être utilisé pour fermer manuellement une boîte de message en simulant un appui sur un bouton, bien qu'il existe des manières plus simples de faire cela :
```c
/* Simuler l'appui du premier bouton (les index partent de zéro) */
uint32_t btn_id = 0;
lv_event_send(mbox, LV_EVENT_VALUE_CHANGED, &btn_id);
```

Ou pour effectuer une actualisation générique :
```c
lv_event_send(label, LV_EVENT_REFRESH, NULL);
```

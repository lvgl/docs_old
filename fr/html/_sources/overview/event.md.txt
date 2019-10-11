```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/fr/overview/event.md
```
# Evénements

Events are triggered in LittlevGL when something happens which might be interesting to the user, e.g. if an object:
- est cliqué
- est déplacé
- sa valeur a changé, etc.

The user can assign a callback function to an object to see these events. In practice, it looks like this:
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

All objects (such as Buttons/Labels/Sliders etc.) receive these generic events regardless of their type.

#### Related to the input devices
These are sent when an object is pressed/released etc. by the user. They are used not only for *Pointers* but can used for *Keypad*, *Encoder* and *Button* input devices as well. Visit the [Overview of input devices](/overview/indev) section to learn more about them.
- **LV_EVENT_PRESSED** L'objet a été pressé
- **LV_EVENT_PRESSING** L'objet est pressé(envoyé continuellement pendant l'appui)
- **LV_EVENT_PRESS_LOST** The input device is still being pressed but is no longer on the object
- **LV_EVENT_SHORT_CLICKED** Released before `LV_INDEV_LONG_PRESS_TIME` time. Not called if dragged.
- **LV_EVENT_LONG_PRESSED**  Pressé durant `LV_INDEV_LONG_PRESS_TIME`. Pas généré si l'objet est déplacé.
- **LV_EVENT_LONG_PRESSED_REPEAT** Généré après `LV_INDEV_LONG_PRESS_TIME` à chaque `LV_INDEV_LONG_PRESS_REP_TIME` ms. Pas généré si l'objet est déplacé.
- **LV_EVENT_CLICKED** Généré au relâché si l'objet n'est pas déplacé (indépendamment d'un appui long)
- **LV_EVENT_RELEASED**  Called in every case when the object has been released even if it was dragged. Not called if slid from the object while pressing and released outside of the object. In this case, `LV_EVENT_PRESS_LOST` is sent.

#### Related to pointer
Ces événements sont envoyés uniquement par des périphériques d’entrée de type pointeur (p.ex. souris ou pavé tactile).
- **LV_EVENT_DRAG_BEGIN** le glissé de l'objet a débuté,
- **LV_EVENT_DRAG_END** le glissé de l'objet est terminé (lancé inclus),
- **LV_EVENT_DRAG_THROW_BEGIN** le lancé de l'objet a débuté (généré après un glissé avec "élan")

#### Related to keypad and encoder
Ces événements sont envoyés par les périphériques d’entrée clavier et encodeur. En savoir plus sur les *groupes* dans la section [Périphériques d'entrée] (overview/indev).
- **LV_EVENT_KEY** A *Key* is sent to the object. Typically when it was pressed or repeated after a long press
- **LV_EVENT_FOCUSED** L'objet est activé dans son groupe
- **LV_EVENT_DEFOCUSED** L'objet est désactivé dans son groupe

#### Evénements généraux
Autres événements généraux envoyés par la librairie.
- **LV_EVENT_DELETE** L'objet est en cours de suppression. Libérez les données associées allouées par l'utilisateur.

### Evénements spéciaux
These events are specific to a particular object type.
- **LV_EVENT_VALUE_CHANGED** La valeur de l'objet a changé (p.ex. pour un [Curseur](/object-types/slider))
- **LV_EVENT_INSERT** Quelque chose est inséré dans l'objet (typiquement à une [Zone de texte](/object-types/ta))
- **LV_EVENT_APPLY**  "Ok", "Appliquer" ou un bouton spécifique similaire a été cliqué (typiquement à partir d'un objet [Clavier](/object-types/kb))
- **LV_EVENT_CANCEL** "Fermer", "Annuler" ou un bouton spécifique similaire a été cliqué (typiquement à partir d'un objet [Clavier](/object-types/kb))
- **LV_EVENT_REFRESH** Demande à actualiser l'objet. Jamais généré par la lirbarie mais peut l'être par l'utilisateur.

Visit particular [Object type's documentation](/object-types/index) to understand which events are used by an object type.

## Données personnalisées
Some events might contain custom data. For example, `LV_EVENT_VALUE_CHANGED` in some cases tells the new value. For more information, see the particular [Object type's documentation](/object-types/index).
Pour obtenir les données personnalisées dans la fonction de rappel, utilisez `lv_event_get_data()`.

The type of the custom data depends on the sending object but if it's a
- entier alors c'est un `uint32_t *` ou un  `int32_t *`
- texte alors c'est un `char *` ou un `const char *`


## Envoyer des événements manuellement

To manually send events to an object, use `lv_event_send(obj, LV_EVENT_..., &custom_data)`.

For example, it can be used to manually close a message box by simulating a button press (although there are simpler ways of doing this):
```c
/* Simuler l'appui du premier bouton (les index partent de zéro) */
uint32_t btn_id = 0;
lv_event_send(mbox, LV_EVENT_VALUE_CHANGED, &btn_id);
```

Or to perform refresh generically:
```c
lv_event_send(label, LV_EVENT_REFRESH, NULL);
```

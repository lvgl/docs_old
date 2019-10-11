```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/fr/overview/object.md
```
# Objets

In the LittlevGL the **basic building blocks** of a user interface are the objects, also called *Widgets*.
Par exemple, un [Bouton](/object-types/btn), une [Etiquette](/object-types/label), une [Image](/object-types/img), une [Liste](/object-types/list), un [Graphique](/object-types/chart) ou une [Zone de texte](/object-types/ta).

Découvrez tous les [Types d'objet](/object-types/index) ici.

## Attributs d'objet

### Attributs de base

All object types share some basic attributes:
- Position
- Taille
- Parent
- Autorisation du glissé
- Autorisation du clic etc.

You can set/get these attributes with `lv_obj_set_...` and `lv_obj_get_...` functions. For example:

```c
/* Définit les attributs de base de l'objet */
lv_obj_set_size(btn1, 100, 50);	 /* Taille du bouton */
lv_obj_set_pos(btn1, 20,30);      /* Position du bouton */
```

Pour voir toutes les fonctions disponibles, visitez la [documentation](/object-types/obj) de l'objet de base.

### Attributs spécifiques

Les types d'objet ont aussi des attributs spéciaux. Par exemple, un curseur a
- Des valeurs minimum et maximum
- Une valeur courante
- Des styles personnalisés

For these attributes, every object type have unique API functions. For example for a slider:

```c
/* Définit les attributs spécifiques du curseur */
lv_slider_set_range(slider1, 0, 100);	   /* Définit les valeurs minimum et maximum */
lv_slider_set_value(slider1, 40, LV_ANIM_ON);	/* Définit la valeur courante (position) */
lv_slider_set_action(slider1, my_action);     /* Définit une fonction de rappel */
```

Les API des types d’objet sont décrites dans leur [Documentation](/object-types/index) mais vous pouvez également consulter les fichiers d’en-tête respectifs (p.ex. *lv_objx/lv_slider.h*).

## Mécanismes de fonctionnement de l'objet

### Structure parent-enfant

A parent object can be considered as the container of its children. Every object has exactly one parent object (except screens), but a parent can have an unlimited number of children.
There is no limitation for the type of the parent but, there are typical parent (e.g. button) and typical child (e.g. label) objects.

### Se déplacer ensemble

If the position of the parent is changed the children will move with the parent.
Therefore all positions are relative to the parent.

Les coordonnées (0, 0) signifient que les objets resteront dans le coin supérieur gauche du parent indépendamment de la position du parent.

![](/misc/par_child1.png "Objects are moving together 1")

```c
lv_obj_t * par = lv_obj_create(lv_scr_act(), NULL); /* Crée un objet parent sur l'écran actuel */
lv_obj_set_size(par, 100, 80);	                   /* Définit la taille du parent */

lv_obj_t * obj1 = lv_obj_create(par, NULL);	         /* Crée un objet sur l'objet parent créé précédemment */
lv_obj_set_pos(obj1, 10, 10);	                   /* Définit la position du nouvel objet */
```

Modifiez la position du parent :

![](/misc/par_child2.png "Graphical objects are moving together 2")  

```c
lv_obj_set_pos(par, 50, 50);	/* Déplacez le parent. L'enfant va bouger avec. */
```

Pour simplifier, la définition des couleurs des objets n'est pas montrée dans l'exemple.

### Visibilité uniquement sur le parent

If a child is partially or fully out of its parent then the parts outside will not be visible.

![](/misc/par_child3.png "A graphical object is visible on its parent")  

```c
lv_obj_set_x(obj1, -30);	/* Déplace l'enfant en partie en dehors du parent */
```

### Créer - supprimer des objets

In LittlevGL objects can be created and deleted dynamically in run-time.
It means only the currently created objects consume RAM.
For example, if you need a chart, you can create it when required and delete it when it is not visible or necessary.

Every object type has its own **create** function with a unified prototype.
It needs two parameters:
- A pointer to the *parent* object. To create a screen give *NULL* as parent.
- Optionally, a pointer to *copy* object with the same type to copy it. This *copy* object can be *NULL* to avoid the copy operation.

All objects are referenced in C code using an `lv_obj_t` pointer as a handle. This pointer can later be used to set or get the attributes of the object.

Les fonctions de création ressemblent à ceci :

```c
lv_obj_t * lv_ <type>_create(lv_obj_t * parent, lv_obj_t * copy);
```

Il existe une fonction commune de **suppression** pour tous les types d'objet. Il supprime l'objet et tous ses enfants.

```c
void lv_obj_del(lv_obj_t * obj);
```

`lv_obj_del` will delete the object immediately.
If for any reason you can't delete the object immediately you can use `lv_obj_del_async(obj)`.
It is useful e.g. if you want to delete the parent of an object in the child's `LV_EVENT_DELETE` signal.

You can remove all the children of an object (but not the object itself) using `lv_obj_clean`:

```c
void lv_obj_clean(lv_obj_t * obj);
```

### Ecran - le parent le plus élémentaire

Les écrans sont des objets spéciaux qui n'ont pas d'objet parent. Il est donc créé ainsi :
```c
lv_obj_t * scr1 = lv_obj_create(NULL, NULL);
```

There is always an active screen on each display. By default, the library creates and loads a "Base object" as the screen for each display.  
To get the currently active screen use the `lv_scr_act()` function. To load a new one, use `lv_scr_load(scr1)`.

Les écrans peuvent être créés avec n'importe quel type d'objet. Par exemple, un [Objet de base](/object-types/obj) ou une image pour créer un fond d'écran.


Screens are created on the currently selected *default display*.
The *default screen* is the last registered screen with `lv_disp_drv_register` or you can explicitly select a new default display using `lv_disp_set_default(disp)`.
`lv_scr_act()` and `lv_scr_load()` operate on the currently default screen.

Visit [Multi-display support](/overview/display) to learn more.

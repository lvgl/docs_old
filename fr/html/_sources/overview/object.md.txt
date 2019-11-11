```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/fr/overview/object.md
```
# Objets

Dans LittlevGL, les **éléments de base** d'une interface utilisateur sont les objets, également appelés *éléments visuels*.
Par exemple, un [Bouton](/object-types/btn), une [Etiquette](/object-types/label), une [Image](/object-types/img), une [Liste](/object-types/list), un [Graphique](/object-types/chart) ou une [Zone de texte](/object-types/ta).

Découvrez tous les [Types d'objet](/object-types/index) ici.

## Attributs d'objet

### Attributs de base

Tous les types d'objet partagent certains attributs de base :
- Position
- Taille
- Parent
- Autorisation du glissé
- Autorisation du clic etc.

Vous pouvez définir/obtenir ces attributs avec les fonctions `lv_obj_set _...` et `lv_obj_get _...`. Par exemple :

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

Pour ces attributs, chaque type d'objet possède des fonctions API uniques. Par exemple pour un curseur :

```c
/* Définit les attributs spécifiques du curseur */
lv_slider_set_range(slider1, 0, 100);	   /* Définit les valeurs minimum et maximum */
lv_slider_set_value(slider1, 40, LV_ANIM_ON);	/* Définit la valeur courante (position) */
lv_slider_set_action(slider1, my_action);     /* Définit une fonction de rappel */
```

Les API des types d’objet sont décrites dans leur [Documentation](/object-types/index) mais vous pouvez également consulter les fichiers d’en-tête respectifs (p.ex. *lv_objx/lv_slider.h*).

## Mécanismes de fonctionnement de l'objet

### Structure parent-enfant

Un objet parent peut être considéré comme le conteneur de ses enfants. Chaque objet a exactement un objet parent (à l'exception des écrans), mais un parent peut avoir un nombre illimité d'enfants.
Il n'y a pas de contrainte pour le type du parent, mais il existe des objets parent typiques (par exemple un bouton) et enfants (par exemple une étiquette).

### Se déplacer ensemble

Si la position du parent est modifiée, les enfants se déplaceront avec lui.
Par conséquent, toutes les positions sont relatives au parent.

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

Si un enfant est partiellement ou complètement hors de son parent, les parties extérieures ne seront pas visibles.

![](/misc/par_child3.png "A graphical object is visible on its parent")  

```c
lv_obj_set_x(obj1, -30);	/* Déplace l'enfant en partie en dehors du parent */
```

### Créer - supprimer des objets

Dans LittlevGL, les objets peuvent être créés et supprimés dynamiquement à l'exécution.
Cela signifie que seuls les objets actuellement créés consomment de la MEV.
Par exemple, si vous avez besoin d'un graphique, vous pouvez le créer à l'utilisation et le supprimer s'il n'est pas visible ou plus nécessaire.

Chaque type d'objet a sa propre fonction **create** avec une signature unifiée.
Deux paramètres sont nécessaires :
- un pointeur sur l'objet parent. Pour créer un écran, donnez *NULL* comme parent.
- éventuellement un pointeur sur un autre objet du même type pour copie. Peut être *NULL* pour ne pas copier un autre objet.

Tous les objets sont référencés dans le code C en utilisant un pointeur `lv_obj_t`. Ce pointeur peut ensuite être utilisé pour définir ou obtenir les attributs de l'objet.

Les fonctions de création ressemblent à ceci :

```c
lv_obj_t * lv_ <type>_create(lv_obj_t * parent, lv_obj_t * copy);
```

Il existe une fonction commune de **suppression** pour tous les types d'objet. Il supprime l'objet et tous ses enfants.

```c
void lv_obj_del(lv_obj_t * obj);
```

`lv_obj_del` supprimera immédiatement l'objet.
Si pour une quelconque raison vous ne pouvez pas supprimer l'objet immédiatement, vous pouvez utiliser `lv_obj_del_async(obj)`.
Utile, par exemple si vous voulez supprimer le parent d'un objet dans le traitement de l’événement `LV_EVENT_DELETE`.

Vous pouvez supprimer tous les enfants d'un objet (mais pas l'objet lui-même) en utilisant `lv_obj_clean` :

```c
void lv_obj_clean(lv_obj_t * obj);
```

### Ecran - le parent le plus élémentaire

Les écrans sont des objets spéciaux qui n'ont pas d'objet parent. Il est donc créé ainsi :
```c
lv_obj_t * scr1 = lv_obj_create(NULL, NULL);
```

Il y a toujours un écran actif sur chaque affichage. Par défaut, la librairie crée et charge un "objet de base" comme écran pour chaque affichage.
Pour obtenir l’écran actuellement actif, utilisez la fonction `lv_scr_act()`. Pour en charger un nouveau, utilisez `lv_scr_load(scr1)`.

Les écrans peuvent être créés avec n'importe quel type d'objet. Par exemple, un [Objet de base](/object-types/obj) ou une image pour créer un fond d'écran.


Les écrans sont créés sur l' *affichage par défaut* actuellement sélectionné.
L'écran *par défaut* est le dernier écran enregistré avec `lv_disp_drv_register` ou vous pouvez explicitement sélectionner un nouvel affichage par défaut avec `lv_disp_set_default (disp)`.
`lv_scr_act()` et `lv_scr_load()` opèrent sur l'écran courant par défaut.

Visitez [Support multi-affichage](/overview/display) pour en savoir plus.

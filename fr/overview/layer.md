```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/fr/overview/layer.md
```

# Couches

## Ordre de création

L'objet créé le plus tôt (et ses enfants) sera dessiné le plus tôt (au plus près de l'arrière-plan). En d'autres termes, le dernier objet créé sera au-dessus de ses frères et sœurs. 
C'est très important, l'ordre est calculé entre les objets de même niveau ("frères et sœurs").

Des couches peuvent être facilement ajoutées en créant 2 objets (qui peuvent être transparents). D'abord 'A' et ensuite 'B'. 'A' et tous les objets qu'il contient seront à l'arrière-plan et pourront être couverts par 'B' et ses enfants.

  
![](/misc/layers.png "Creating graphical objects in Littlev Graphics Library")  

```c
/* Crée un écran */
lv_obj_t * scr = lv_obj_create(NULL, NULL);
lv_scr_load(scr);          /* Charge l'écran */

/* Crée 2 boutons */
lv_obj_t * btn1 = lv_btn_create(scr, NULL);         /* Crée un bouton sur l'écran */
lv_btn_set_fit(btn1, true, true);                   /* Permet de définir automatiquement la taille en fonction du contenu */
lv_obj_set_pos(btn1, 60, 40);              	   /* Définit la position du bouton */

lv_obj_t * btn2 = lv_btn_create(scr, btn1);         /* Copie le premier bouton */
lv_obj_set_pos(btn2, 180, 80);                    /* Définit la position du bouton */

/* Ajoute des étiquettes aux boutons */
lv_obj_t * label1 = lv_label_create(btn1, NULL);	/* Crée une étiquette sur le premier bouton */
lv_label_set_text(label1, "Button 1");          	/* Définit le texte de l'étiquette */

lv_obj_t * label2 = lv_label_create(btn2, NULL);  	/* Crée une étiquette sur le deuxième bouton */
lv_label_set_text(label2, "Button 2");            	/* Définit le texte de l'étiquette */

/* Supprime la deuxième étiquette */
lv_obj_del(label2);
```

## Amener au premier plan

Il y a plusieurs façons d'amener un objet au premier plan :
- Utilisez `lv_obj_set_top(obj, true)`. Si vous cliquez sur `obj` ou l'un de ses enfants, LittlevGL amènera automatiquement l'objet au premier plan.
Cela fonctionne de manière similaire aux fenêtres sur PC. Lorsque vous cliquez sur une fenêtre en arrière-plan, elle apparaît automatiquement au premier plan.
- Utilisez `lv_obj_move_foreground(obj)` et `lv_obj_move_background(obj)` pour indiquer explicitement à la librairie de placer un objet au premier plan ou de le passer à l'arrière-plan.
- Quand `lv_obj_set_parent(obj, new_parent)` est utilisé, `obj` sera au premier plan sur le nouveau parent.


## Couches supérieure et système

Il y a deux couches spéciales appelées `layer_top` et `layer_sys`.
Les deux sont visibles et identiques sur tous les écrans d'un affichage. `layer_top` est au-dessus de "l'écran normal" et `layer_sys` lui-même au-dessus de `layer_top`.

`layer_top` peut être utilisé par l'utilisateur pour créer du contenu visible partout. Par exemple, une barre de menus, une fenêtre contextuelle, etc. Si l'attribut `click` est activé,` layer_top` absorbera tous les clics de l'utilisateur et agira comme modal.
```c
lv_obj_set_click(lv_layer_top(), true);
``` 

`layer_sys` est utilisé par LittlevGL. Par exemple, la librairie y place le curseur de la souris pour s’assurer qu’il est toujours visible.

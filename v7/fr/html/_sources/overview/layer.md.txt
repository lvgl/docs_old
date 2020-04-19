```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/fr/overview/layer.md
```

# Couches

## Ordre de création

By default, LittlevGL draws old objects on the background and new objects on the foreground.

For example, assume we added a button to a parent object named button1 and then another button named button2. Then button1 (with its child object(s)) will be in the background and can be covered by button2 and its children.


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
- Use `lv_obj_set_top(obj, true)`. If `obj` or any of its children is clicked, then LittlevGL will automatically bring the object to the foreground.
It works similarly to a typical GUI on a PC. When a window in the background is clicked, it will come to the foreground automatically.
- Use `lv_obj_move_foreground(obj)` to explicitly tell the library to bring an object to the foreground. Similarly, use `lv_obj_move_background(obj)` to move to the background.
- When `lv_obj_set_parent(obj, new_parent)` is used, `obj` will be on the foreground on the `new_parent`.


## Top and sys layers

LittlevGL uses two special layers named as `layer_top` and `layer_sys`.
Both are visible and common on all screens of a display. **They are not, however, shared among multiple physical displays.** The `layer_top` is always on top of the default screen (`lv_scr_act()`), and `layer_sys` is on top of `layer_top`.

The `layer_top` can be used by the user to create some content visible everywhere. For example, a menu bar, a pop-up, etc. If the `click` attribute is enabled, then `layer_top` will absorb all user click and acts as a modal.
```c
lv_obj_set_click(lv_layer_top(), true);
```

The `layer_sys` is also using for similar purpose on LittlevGL. For example, it places the mouse cursor there to be sure it's always visible.

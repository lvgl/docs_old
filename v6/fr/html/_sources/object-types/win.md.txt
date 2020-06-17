```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/fr/object-types/win.md
```
# Fenêtre (lv_win)

## Vue d'ensemble

Les fenêtres sont l’un des objets les plus complexes du type conteneur. Ils sont construits à partir de deux parties principales :
1. un en-tête [conteneur](/object-types/cont) en haut
2. une [page](/object-types/page) pour le contenu situé sous l'en-tête.

### Titre
Sur l'en-tête, il y a un titre qui peut être modifié par : `lv_win_set_title(win, "Nouveau titre")`. Le titre hérite toujours du style de l'en-tête.

### Boutons de contrôle
Vous pouvez ajouter des boutons de contrôle à la droite de l'en-tête avec : `lv_win_add_btn(win, LV_SYMBOL_CLOSE)`.
Le deuxième paramètre est une [image](/object-types/img) source.

`lv_win_close_event_cb` peut être utilisé comme fonction de rappel d'événement pour fermer la fenêtre.

Vous pouvez modifier la taille des boutons de contrôle avec la fonction `lv_win_set_btn_size(win, new_size)`.

### Barres de défilement

Le comportement de la barre de défilement peut être défini par `lv_win_set_sb_mode(win, LV_SB_MODE _...)`. Voir [page](/object-types/page pour plus de détails.

### Défilement manuel et focus
Pour faire défiler la fenêtre directement, vous pouvez utiliser `lv_win_scroll_hor(win, dist_px)` ou `lv_win_scroll_ver(win, dist_px)`.

Pour que la fenêtre affiche un de ses objets, utilisez `lv_win_focus (win, child, LV_ANIM_ON/OFF)`.

La durée des animations de défilement et de focus peut être ajusté avec `lv_win_set_anim_time(win, anim_time_ms)`.

### Mise en page
Pour définir une disposition du contenu, utilisez `lv_win_set_layout (win, LV_LAYOUT_...)`. Voir [conteneur](/object-types/cont) pour plus de détails.

## Styles

Utilisez `lv_win_set_style(win, LV_WIN_STYLE_..., &style)` pour définir un nouveau style pour un élément de la fenêtre :

- **LV_WIN_STYE_BG** arrière-plan principal (l'en-tête et la page de contenu sont placés dessus) qui utilise toutes les propriétés `style.body` (valeur par défaut : `lv_style_plain`)
- **LV_WIN_STYLE_CONTENT** partie déroulante de la page de contenu qui utilise toutes les propriétés `style.body` (valeur par défaut :` lv_style_transp`)
- **LV_WIN_STYLE_SB** le style de la barre de défilement qui utilise toutes les propriétés `style.body`. `body.padding.left/top` définit les marges des barres de défilement et `body.inner.padding` définit la largeur de la barre de défilement (valeur  par défaut: `lv_style_pretty_color`)
- **LV_WIN_STYLE_HEADER** style de l'en-tête qui utilise toutes les propriétés `style.body` (valeur par défaut : `lv_style_plain_color`)
- **LV_WIN_STYLE_BTN_REL** style du bouton relâché (sur l'en-tête) qui utilise toutes les propriétés `style.body` (valeur par défaut : `lv_style_btn_rel`)
- **LV_WIN_STYLE_BTN_PR** style du bouton pressé (sur l'en-tête) qui utilise toutes les propriétés `style.body` (valeur par défaut : `lv_style_btn_pr`)

La hauteur de l'en-tête est définie par la plus grande valeur de *hauteur des boutons* (définie par `lv_win_set_btn_size`) et *hauteur de titre* (provenant de `header_style.text.font`), plus les éléments `body.padding.top` et `body.padding.bottom` du style de l'en-tête.

## Evénements
Seuls les [événements génériques](/overview/event.html#generic-events) sont envoyés par ce type d'objet.

Apprenez-en plus sur les [événements](/overview/event).

## Touches

Les *touches* suivantes sont traitées par la page :
- **LV_KEY_RIGHT/LEFT/UP/DOWN** font défiler la page

Apprenez-en plus sur les [touches](/overview/indev).


## Exemple

```eval_rst

.. include:: /lv_examples/src/lv_ex_win/index.rst

```


## API 

```eval_rst

.. doxygenfile:: lv_win.h
  :project: lvgl
        
```

```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/fr/object-types/imgbtn.md
```
# Bouton image (lv_imgbtn)

## Vue d’ensemble

Le bouton Image est très similaire à l'objet bouton simple. La seule différence est qu'il affiche des images définies par l'utilisateur pour chaque état au lieu de dessiner un bouton.
Avant de lire ceci, veuillez lire la section sur l'objet [bouton](/object-types/btn).

### Images sources
Pour définir l'image d'un état, utilisez `lv_imgbtn_set_src(imgbtn, LV_BTN_STATE_..., &img_src)`.Les images sources fonctionnent comme décrit dans l'objet [image](/object-types/img) excepté que les "Symboles" ne sont pas pris en charge.

Si `LV_IMGBTN_TILED` est activé dans *lv_conf.h* trois sources peuvent être définies pour chaque état :
- gauche,
- centre,
- droit.

L'image *centre* sera répétée pour remplir l'objet sur toute sa largeur. Par conséquent, avec `LV_IMGBTN_TILED`, vous pouvez définir la largeur du bouton Image, sans quoi la largeur sera toujours identique à la largeur de l'image source.


### Etats
Les états sont semblables à ceux de l'objet bouton. Il peut être défini avec `lv_imgbtn_set_state(imgbtn, LV_BTN_STATE_...)`. 

### Bascule
La fonctionnalité bascule peut être activée avec `lv_imgbtn_set_toggle(imgbtn, true)`.

## Styles

Comme pour les boutons normaux, les boutons image ont également 5 styles indépendants pour les 5 états. Vous pouvez les définir via `lv_imgbtn_set_style(btn, LV_IMGBTN_STYLE_..., &style)`. Les styles utilisent les propriétés `style.image`.

- **LV_IMGBTN_STYLE_REL** style de l'état relâché. Défaut : `lv_style_btn_rel`,
- **LV_IMGBTN_STYLE_PR** style de l'état pressé. Défaut : `lv_style_btn_pr`,
- **LV_IMGBTN_STYLE_TGL_REL** style de l'état bascule relâché. Défaut : `lv_style_btn_tgl_rel`,
- **LV_IMGBTN_STYLE_TGL_PR** style de l'état bascule pressé. Défaut : `lv_style_btn_tgl_pr`,
- **LV_IMGBTN_STYLE_INA** style de l'état inactif. Défaut : `lv_style_btn_ina`.

Quand vous créez une étiquette sur un bouton image, la bonne pratique consiste à définir les propriétés `style.text` du bouton image. Comme les étiquettes ont `style = NULL` par défaut, elles héritent du style du parent, le bouton image.
De ce fait, vous n'avez pas besoin de créer un nouveau style pour l'étiquette.

## Evénements
Outre les [événements génériques](/overview/event.html #evenements-generiques), les [événements spéciaux](/overview/event.html#evenements-speciaux) suivants  sont envoyés par les boutons image :
 - **LV_EVENT_VALUE_CHANGED** envoyé lorsque le bouton image est basculé.

Notez que les événements génériques liés au périphérique d'entrée (tels que `LV_EVENT_PRESSED`) sont également envoyés dans l'état inactif. Vous devez vérifier l'état avec `lv_imgbtn_get_state(imgbtn)` pour ignorer les événements des boutons inactifs.
 
Apprenez-en plus sur les [événements](/overview/event).

## Touches
Les *touches* suivantes sont traitées par les cases à cocher:
- **LV_KEY_RIGHT/UP** passe à l'état bascule pressé si le mode bascule est actif
- **LV_KEY_LEFT/DOWN** passe à l'état bascule relâché si le mode bascule est actif

Notez que, comme d'habitude, l'état de `LV_KEY_ENTER` est traduit en `LV_EVENT_PRESSED/PRESSING/RELEASED` etc.

Apprenez-en plus sur les [touches](/overview/indev).

## Exemple

```eval_rst

.. include:: /lv_examples/src/lv_ex_obj/index.rst

```

## API 

```eval_rst

.. doxygenfile:: lv_imgbtn.h
  :project: lvgl
        
```

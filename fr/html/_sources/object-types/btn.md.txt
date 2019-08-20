```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/fr/object-types/btn.md
```
# Bouton (lv_btn)

## Vue d'ensemble

Les boutons sont de simples objets rectangulaires dont le style et l'état changent quand ils sont pressés ou relâchés. 

### Etats
Les boutons peuvent prendre l'un des 5 états possibles :
- **LV_BTN_STATE_REL** état relâché
- **LV_BTN_STATE_PR** état  pressé
- **LV_BTN_STATE_TGL_REL** état bascule relâché
- **LV_BTN_STATE_TGL_PR** état bascule pressé
- **LV_BTN_STATE_INA** état désactivé

L'état passe automatiquement de `..._REL` à `..._PR` quand le bouton est pressé et inversement quand il est relâché.

L'état peut être défini par programmation avec `lv_btn_set_state(btn, LV_BTN_STATE_...)`.

### Bascule
Les boutons peuvent être configurés comme *bouton bascule* avec`lv_btn_set_toggle(btn, true)`. Dans ce cas, au relâchement, le bouton prend l'état *bascule relâché*.

### Mise en page et adaptation
De la même manière que les [conteneurs](/object-types/cont), les boutons ont des attributs de mise en page et d'adaptation.
- `lv_btn_set_layout(btn, LV_LAYOUT_...)` définit une mise en page. La valeur par défaut est `LV_LAYOUT_CENTER`. 
Ainsi, si vous ajoutez une étiquette, elle sera automatiquement alignée au milieu et ne pourra pas être déplacée avec `lv_obj_set_pos()`.
La mise en page peut être désactivée avec `lv_btn_set_layout(btn, LV_LAYOUT_OFF)`
- `lv_btn_set_fit/fit2/fit4(btn, LV_FIT_..)` permet d'adapter automatiquement la largeur et/ou la hauteur du bouton en fonction des enfants, du parent et du type d'adaptation.

### Effet d'encre
Vous pouvez activer une animation spéciale sur les boutons : quand un bouton est pressé, l’état pressé est tracé dans un cercle grandissant à partir de l'endroit de l'appui. C'est comme une gouttelette d'encre qui s'étale dans l'eau.
Lorsque le bouton est relâché, l'état relâché est visualisé en estompant le cercle. C'est comme si l'encre s'était complètement mélangée à l'eau et devenait invisible.

Pour contrôler cette animation, utilisez les fonctions suivantes :
- `lv_btn_set_ink_in_time(btn, time_ms)` temps de croissance du cercle
- `lv_btn_set_ink_wait_time(btn, time_ms)` durée minimum d'affichage du cercle complet à l'état pressé
- `lv_btn_set_ink_out_time(btn, time_ms)` temps de passage à l'état relâché

Cette fonctionnalité doit être activée avec `LV_BTN_INK_EFFECT 1` dans *lv_conf.h*.


## Styles

Un bouton peut avoir 5 styles indépendants pour les 5 états. Vous pouvez les définir via : `lv_btn_set_style(btn, LV_BTN_STYLE_..., &style)`. Les styles utilisent les propriétés `style.body`.

- **LV_BTN_STYLE_REL** style de l'état relâché. Défaut : `lv_style_btn_rel`
- **LV_BTN_STYLE_PR**  style de l'état pressé. Défaut : `lv_style_btn_pr`
- **LV_BTN_STYLE_TGL_REL**  style de l'état bascule relâché. Défaut : `lv_style_btn_tgl_rel`
- **LV_BTN_STYLE_TGL_PR** style de l'état bascule pressé. Défaut : `lv_style_btn_tgl_pr`
- **LV_BTN_STYLE_INA** style de l'état désactivé. Défaut : `lv_style_btn_ina`

Quand vous créez une étiquette sur un bouton, la bonne pratique consiste à définir les propriétés `style.text` du bouton. Comme les étiquettes ont `style = NULL` par défaut, elles héritent du style du parent, le bouton.
De ce fait, vous n'avez pas besoin de créer un nouveau style pour l'étiquette.


## Evénements
Outre les [événements génériques](/overview/event.html #evenements-generiques), les [événements spéciaux](/overview/event.html#evenements-speciaux) suivants  sont envoyés par les boutons :
 - **LV_EVENT_VALUE_CHANGED** envoyé lorsque le bouton est basculé.

Notez que les événements génériques liés au périphérique d'entrée (tels que `LV_EVENT_PRESSED`) sont également envoyés dans l'état désactivé. Vous devez vérifier l'état avec `lv_btn_get_state(btn)` pour ignorer les événements des boutons désactivés.
 
Apprenez-en plus sur les [événements](/overview/event).

## Touches
Les *touches* suivantes sont traitées par les boutons:
- **LV_KEY_RIGHT/UP** passe à l'état bascule pressé si le mode bascule est activé
- **LV_KEY_LEFT/DOWN** passe à l'état bascule relâché si le mode bascule est activé

Notez que, comme d'habitude, l'état de `LV_KEY_ENTER` est traduit en `LV_EVENT_PRESSED/PRESSING/RELEASED` etc.

Apprenez-en plus sur les [touches](/overview/indev).
  
## Exemple
```eval_rst

.. include:: /lv_examples/src/lv_ex_btn/index.rst

```

## API 

```eval_rst

.. doxygenfile:: lv_btn.h
  :project: lvgl
        
```

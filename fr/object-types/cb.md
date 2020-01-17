```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/fr/object-types/cb.md
```
# Case à cocher (lv_cb)
## Vue d’ensemble

Les objets case à cocher sont construits à partir d'un [bouton](/object-types/btn) en arrière-plan qui contient un second bouton (la marque) et une [étiquette](/object-types/label) pour créer une case à cocher classique.

### Texte
Le texte peut être modifié par la fonction `lv_cb_set_text(cb, "Nouveau texte")`. Le texte est alloué dynamiquement.

Pour définir un texte statique utilisez `lv_cb_set_static_text(cb, txt)`. De cette façon, seul un pointeur vers `txt` sera sauvegardé et il ne doit pas être désalloué tant que la case à cocher existe.

### Cocher/décocher
Vous pouvez manuellement cocher/décocher la case à cocher via `lv_cb_set_checked(cb, true/false)`. La valeur `true` coche la case à cocher, la valeur `false` la décoche.

### Désactiver
Pour désactiver la case à cocher utilisez `lv_cb_set_inactive(cb, true)`.

## Styles

Les styles de case à cocher peuvent être modifiés avec `lv_cb_set_style(cb, LV_CB_STYLE_..., &style)`.

- **LV_CB_STYLE_BG**  - Style d'arrière-plan. Utilise toutes les propriétés `style.body`. Le style de l'étiquette provient de `style.text`. Défaut : `lv_style_transp`.
- **LV_CB_STYLE_BOX_REL** - Style de la marque décochée relâchée. Utilise les propriétés `style.body`. Défaut : `lv_style_btn_rel`.
- **LV_CB_STYLE_BOX_PR** - Style de la marque décochée pressée. Utilise les propriétés `style.body`. Défaut : `lv_style_btn_pr`.
- **LV_CB_STYLE_BOX_TGL_REL**  - Style de la marque cochée relâchée. Utilise les propriétés `style.body`. Défaut : `lv_style_btn_tgl_rel`
- **LV_CB_STYLE_BOX_TGL_PR** - Style de la marque cochée pressée. Utilise les propriétés `style.body`. Défaut : `lv_style_btn_tgl_pr`
- **LV_CB_STYLE_BOX_INA** - Style de la marque désactivée. Utilise les propriétés `style.body`. Défaut : `lv_style_btn_ina`


## Evénements
Outre les [événements génériques](/overview/event.html #evenements-generiques), les [événements spéciaux](/overview/event.html#evenements-speciaux) suivants sont envoyés par les case à cocher :
 - **LV_EVENT_VALUE_CHANGED** - Envoyé lorsque le bouton image est basculé.

Notez que les événements génériques liés au périphérique d'entrée (tels que `LV_EVENT_PRESSED`) sont également envoyés dans l'état désactivé. Vous devez vérifier l'état avec `lv_cb_is_inactive(cb)` pour ignorer les événements des cases à cocher désactivées.

Apprenez-en plus sur les [événements](/overview/event).


## Touches
Les *touches* suivantes sont traitées par les 'boutons' :
- **LV_KEY_RIGHT/UP** - Passe à l'état bascule pressé si le mode bascule est actif
- **LV_KEY_LEFT/DOWN** - Passe à l'état bascule relâché si le mode bascule est actif

Notez que, comme d'habitude, l'état de `LV_KEY_ENTER` est traduit en `LV_EVENT_PRESSED/PRESSING/RELEASED` etc.

Apprenez-en plus sur les [touches](/overview/indev).


## Exemple

```eval_rst

.. include:: /lv_examples/src/lv_ex_cb/index.rst

```

## API

```eval_rst

.. doxygenfile:: lv_cb.h
  :project: lvgl

```

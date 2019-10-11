```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/fr/object-types/page.md
```
# Page (lv_page)

## Vue d'ensemble

La page se compose de deux [conteneurs](/object-types/cont) l'un sur l'autre : 
- un **arrière-plan** (ou base)
- un plan supérieur **pouvant défiler**. 

L'objet d'arrière-plan peut être référencé comme la page elle-même : `lv_obj_set_width(page, 100)`.

Si vous créez un enfant sur la page, celui-ci sera automatiquement déplacé vers le conteneur pouvant défiler.
Si le conteneur pouvant défiler devient plus grand que l'arrière-plan, vous pouvez le faire *défiler en le faisant glisser (comme dans les listes sur les smartphones).

By default, the scrollable's has `LV_FIT_FILL`auto fit in all directions. 
It means the scrollable size will be the same as the background's size (minus the paddings) while the children are in the background. 
But when an object is positioned out of the background the scrollable size will be increased to involve it.
  
### Barres de défilement
 
Les barres de défilement peuvent être affichées selon quatre stratégies :

- **LV_SB_MODE_OFF** les barres de défilement ne sont jamais affichées
- **LV_SB_MODE_ON** les barres de défilement sont toujours affichées
- **LV_SB_MODE_DRAG** les barres de défilement sont affichées quand la page est tirée
- **LV_SB_MODE_AUTO** affiche les barres de défilement quand le conteneur est suffisamment grand pour être défilé

Vous pouvez définir la politique d'affichage de la barre de défilement avec : `lv_page_set_sb_mode(page, SB_MODE)`. La valeur par défaut est `LV_SB_MODE_AUTO`.

### Objet collé
Vous pouvez coller des enfants à la page. Dans ce cas, vous pouvez faire défiler la page en faisant glisser l'objet enfant.
It can be enabled by the `lv_page_glue_obj(child, true)`.

### Focus object
You can focus on an object on a page with `lv_page_focus(page, child, LV_ANIM_ONO/FF)`.
It will move the scrollable container to show a child. The time of the animation can be set by `lv_page_set_anim_time(page, anim_time)` in milliseconds.

### Manual navigation
You can move the scrollable object manually using `lv_page_scroll_hor(page, dist)` and `lv_page_scroll_ver(page, dist)`

### Edge flash
A circle-like effect can be shown if the list reached the most top/bottom/left/right position. `lv_page_set_edge_flash(list, en)` enables this feature.

### Scroll propagation

If the list is created on an other scrollable element (like an other page) and the Page can't be scrolled further the scrolling can be propagated to the parent to continue the scrolling on the parent. 
It can be enabled with `lv_page_set_scroll_propagation(list, true)`

### Scrollable API
There are functions to directly set/get the scrollable's attributes: 
- `lv_page_get_scrl()`
- `lv_page_set_scrl_fit/fint2/fit4()`
- `lv_page_set_scrl_width()`
- `lv_page_set_scrl_height()`
- `lv_page_set_scrl_layout()`

### Notes
The background draws its border when the scrollable is drawn. It ensures that the page always will have a closed shape even if the scrollable has the same color as the Page's parent.

## Styles

Use `lv_page_set_style(page, LV_PAGE_STYLE_...,  &style)` to set a new style for an element of the page:

- **LV_PAGE_STYLE_BG** background's style which uses all `style.body` properties (default: `lv_style_pretty_color`)
- **LV_PAGE_STYLE_SCRL** scrollable's style which uses all `style.body` properties (default: `lv_style_pretty`)
- **LV_PAGE_STYLE_SB** scrollbar's style which uses all `style.body` properties. `padding.right/bottom` sets horizontal and vertical the scrollbars' padding respectively and the `padding.inner` sets the scrollbar's width. (default: `lv_style_pretty_color`)

## Events
Only the [Generic events](/overview/event.html#generic-events) are sent by the object type.

The scrollable object has a default event callback which propagates the following events to the background object:
`LV_EVENT_PRESSED`, `LV_EVENT_PRESSING`, `LV_EVENT_PRESS_LOST`,`LV_EVENT_RELEASED`, `LV_EVENT_SHORT_CLICKED`, `LV_EVENT_CLICKED`, `LV_EVENT_LONG_PRESSED`, `LV_EVENT_LONG_PRESSED_REPEAT` 

Learn more about [Events](/overview/event).

##Keys

The following *Keys* are processed by the Page:
- **LV_KEY_RIGHT/LEFT/UP/DOWN** Scroll the page

Learn more about [Keys](/overview/indev).

## Example

```eval_rst

.. include:: /lv_examples/src/lv_ex_page/index.rst

```

## API 

```eval_rst

.. doxygenfile:: lv_page.h
  :project: lvgl
        
```

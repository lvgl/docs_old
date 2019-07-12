# Page (lv_page)

## Overview

The Page consist of two [Containers](/object-types/page) on each other: 
- a **background** (or base)
- a top which is **scrollable**. 

The background object can be referenced as the page itself like: `lv_obj_set_width(page, 100)`.

If you create a child on the page it will be automatically moved to the scrollable container. 
If the scrollable container becomes larger then the background it can be *scrolled by dragging (like the lists on smartphones).

By default, the scrollable's has `LV_FIT_FILL`auto fit in all directions. 
It means the scrollable size will be the same as the background's size (minus the paddings) while the children are in the background. 
But when an object is positioned out of the background the scrollable size will be increased to involve it.
  
### Scrollbars
 
Scrollbars can be shown according to four policies:

- **LV_SB_MODE_OFF** Never show scrollbars
- **LV_SB_MODE_ON** Always show scrollbars
- **LV_SB_MODE_DRAG** Show scrollbars when the page is being dragged
- **LV_SB_MODE_AUTO** Show scrollbars when the scrollable container is large enough to be scrolled

You can set scroll bar show policy by: `lv_page_set_sb_mode(page, SB_MODE)`. The default value is `LV_SB_MODE_AUTO`.

### Glue object
You can glue children to the page. In this case, you can scroll the page by dragging the child object. 
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

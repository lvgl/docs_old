```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/en/object-types/cont.md
```
# Container (lv_cont)

## Overview

The containers are essentially a **basic object** with some special features.

### Layout
You can apply a layout on the containers to automatically order their children. The layout spacing comes from `style.body.padding. ...` properties. The possible layout options:

- **LV_LAYOUT_OFF** - Do not align the children.
- **LV_LAYOUT_CENTER** - Align children to the center in column and keep `padding.inner` space between them.
- **LV_LAYOUT_COL_L** - Align children in a left-justified column. Keep `padding.left` space on the left, `pad.top` space on the top and `padding.inner` space between the children.
- **LV_LAYOUT_COL_M** - Align children in centered column. Keep `padding.top` space on the top and `padding.inner` space between the children.
- **LV_LAYOUT_COL_R** - Align children in a right-justified column. Keep `padding.right` space on the right, `padding.top` space on the top and `padding.inner` space between the children.
- **LV_LAYOUT_ROW_T** - Align children in a top justified row. Keep `padding.left` space on the left, `padding.top` space on the top and `padding.inner` space between the children.
- **LV_LAYOUT_ROW_M** - Align children in centered row. Keep `padding.left` space on the left and `padding.inner` space between the children.
- **LV_LAYOUT_ROW_B** - Align children in a bottom justified row. Keep `padding.left` space on the left, `padding.bottom` space on the bottom and `padding.inner` space between the children.
- **LV_LAYOUT_PRETTY** - Put as many objects as possible in a row (with at least `padding.inner` space and `padding.left/right` space on the sides). Divide the space in each line equally between the children.
Keep `padding.top` space on the top and `pad.inner` space between the lines.
- **LV_LAYOUT_GRID** - Similar to `LV_LAYOUT_PRETTY` but not divide horizontal space equally just let `padding.left/right` on the edges and `padding.inner` space between the elements.

### Autofit
Container have an autofit feature which can automatically change the size of the container according to its children and/or parent. The following options exist:
- **LV_FIT_NONE** - Do not change the size automatically.
- **LV_FIT_TIGHT** - Shrink-wrap the container around all of its children, while keeping `padding.top/bottom/left/right` space on the edges.
- **LV_FIT_FLOOD** - Set the size to the parent's size minus `padding.top/bottom/left/right` (from the parent's style) space.
- **LV_FIT_FILL** - Use `LV_FIT_FLOOD` while smaller than the parent and `LV_FIT_TIGHT` when larger. It will ensure that the container is, at minimum, the size of its parent.

To set the auto fit mode for all directions, use `lv_cont_set_fit(cont, LV_FIT_...)`.
To use different auto fit horizontally and vertically, use `lv_cont_set_fit2(cont, hor_fit_type, ver_fit_type)`.
To use different auto fit in all 4 directions, use `lv_cont_set_fit4(cont, left_fit_type, right_fit_type, top_fit_type, bottom_fit_type)`.

## Styles
You can set the styles with `lv_cont_set_style(btn, LV_CONT_STYLE_MAIN, &style)`.
- **style.body** properties are used.

## Events
Only the [Generic events](/overview/event.html#generic-events) are sent by the object type.

Learn more about [Events](/overview/event).

## Keys
No *Keys* are processed by the object type.

Learn more about [Keys](/overview/indev).


## Example

```eval_rst

.. include:: /lv_examples/src/lv_ex_cont/index.rst

```

## API

```eval_rst

.. doxygenfile:: lv_cont.h
  :project: lvgl

```

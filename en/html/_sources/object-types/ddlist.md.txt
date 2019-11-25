```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/en/object-types/ddlist.md
```
# Drop-down list (lv_ddlist)

## Overview

The drop-down list allows the user to select one value from a list. The drop-down list is closed (inactive) by default. When a drop-down list is inactive, it displays a single value. When activated (by click on the drop-down list), it displays a list of values from which the user may select one. When the user selects a new value, the drop-down list reverts to the inactive state and displays the new value.

### Set options
The options are passed to the drop-down list as a string with `lv_ddlist_set_options(ddlist, options)`. The options should be separated by `\n`. For example: `"First\nSecond\nThird"`.

You can select an option manually with `lv_ddlist_set_selected(ddlist, id)`, where _id_ is the index of an option.

### Get selected option
The get the currently selected option, use `lv_ddlist_get_selected(ddlist)`. It will return the *index* of the selected option.

`lv_ddlist_get_selected_str(ddlist, buf, buf_size)` copies the name of the selected option to a `buf`.

### Align the options
To align the label horizontally, use `lv_ddlist_set_align(ddlist, LV_LABEL_ALIGN_LEFT/CENTER/RIGHT)`.

### Height and width
By default, the list's height is adjusted automatically to show all options. The `lv_ddlist_set_fix_height(ddlist, height)` sets a fixed height for the opened list. The user can put `0` to use auto height.

The width is also adjusted automatically. To prevent this, apply `lv_ddlist_set_fix_width(ddlist, width)`. The user can put `0` to use auto width.

### Scrollbars
Similarly to [Page](/object-types/page) with fix height, the drop-down list supports various scrollbar display modes. It can be set by `lv_ddlist_set_sb_mode(ddlist, LV_SB_MODE_...)`.

### Animation time
The drop-down list's open/close animation time is adjusted by `lv_ddlist_set_anim_time(ddlist, anim_time)`. Zero animation time means no animation.

### Decoration arrow
A down arrow can be added to the left side of the drop-down list with `lv_ddlist_set_draw_arrow(ddlist, true)`.

### Manually open/close
To manually open or close the drop-down list the `lv_ddlist_open/close(ddlist)` function can be used.

### Stay open
You can force the drop-down list to **stay opened**, when an option is selected with `lv_ddlist_set_stay_open(ddlist, true)`.

## Styles

The `lv_ddlist_set_style(ddlist, LV_DDLIST_STYLE_..., &style)` set the styles of a drop-down list.

- **LV_DDLIST_STYLE_BG** - Style of the background. All `style.body` properties are used. `style.text` is used for the option's label. Default: `lv_style_pretty`.
- **LV_DDLIST_STYLE_SEL** - Style of the selected option.  The `style.body` properties are used. The selected option will be recolored with `text.color`. Default: `lv_style_plain_color`.
- **LV_DDLIST_STYLE_SB** - Style of the scrollbar. The `style.body` properties are used. Default: `lv_style_plain_color`.

## Events
Besides the [Generic events](/overview/event.html#generic-events), the following [Special events](/overview/event.html#special-events) are sent by the drop-down list:
 - **LV_EVENT_VALUE_CHANGED** - Sent when the new option is selected.

Learn more about [Events](/overview/event).

## Keys
The following *Keys* are processed by the Buttons:
- **LV_KEY_RIGHT/DOWN** - Select the next option.
- **LV_KEY_LEFT/UP** - Select the previous option.
- **LY_KEY_ENTER** - Apply the selected option (Send `LV_EVENT_VALUE_CHANGED` event and close the drop-down list).

## Example

```eval_rst

.. include:: /lv_examples/src/lv_ex_ddlist/index.rst

```

## API

```eval_rst

.. doxygenfile:: lv_ddlist.h
  :project: lvgl

```

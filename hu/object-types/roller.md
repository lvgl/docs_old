```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/hu/object-types/roller.md
```
# Roller (lv_roller)

## Overview

Roller allows you to simply select one option from more with scrolling. Its functionalities are similar to [Drop down list](/object-types/ddlist).

### Set options
The options are passed to the Roller as a string with `lv_roller_set_options(roller, options, LV_ROLLER_MODE_NORMAL/INFINITE)`. The options should be separated by `\n`. For example: `"First\nSecond\nThird"`.

`LV_ROLLER_MODE_INIFINITE` make the roller circular.

You can select an option manually with `lv_roller_set_selected(roller, id)`, where *id* is the index of an option.

### Get selected option
The get the currently selected option use `lv_roller_get_selected(roller)` it will return the *index* of the selected option.

`lv_roller_get_selected_str(roller, buf, buf_size)` copy the name of the selected option to `buf`.

### Align the options
To align the label horizontally use `lv_roller_set_align(roller, LV_LABEL_ALIGN_LEFT/CENTER/RIGHT)`.

### Height and width
You can set the number of visible rows with `lv_roller_set_visible_row_count(roller, num)`

The width is adjusted automatically according to the width of the options. To prevent this apply `lv_roller_set_fix_width(roller, width)`. `0` means to use auto width.

### Animation time
When the Roller is scrolled and doesn't stop exactly on an option it will scroll to the nearest valid option automatically.
The time of this scroll animation can be changed by `lv_roller_set_anim_time(roller, anim_time)`. Zero animation time means no animation.

## Styles

The `lv_roller_set_style(roller, LV_ROLLER_STYLE_..., &style)` set the styles of a Roller.

- **LV_ROLLER_STYLE_BG** Style of the background. All `style.body` properties are used. `style.text` is used for the option's label. Default: `lv_style_pretty`
- **LV_ROLLER_STYLE_SEL** Style of the selected option.  The `style.body` properties are used. The selected option will be recolored with `text.color`. Default: `lv_style_plain_color`

## Events
Besides, the [Generic events](/overview/event.html#generic-events) the following [Special events](/overview/event.html#special-events) are sent by the Drop down lists:
 - **LV_EVENT_VALUE_CHANGED** sent when a new option is selected

Learn more about [Events](/overview/event).

## Keys
The following *Keys* are processed by the Buttons:
- **LV_KEY_RIGHT/DOWN** Select the next option
- **LV_KEY_LEFT/UP** Select the previous option
- **LY_KEY_ENTER** Apply the selected option (Send `LV_EVENT_VALUE_CHANGED` event) 

## Example

```eval_rst

.. include:: /lv_examples/src/lv_ex_roller/index.rst

```

## API 

```eval_rst

.. doxygenfile:: lv_roller.h
  :project: lvgl
        
```

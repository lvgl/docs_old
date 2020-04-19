```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/tr/object-types/spinbox.md
```
# Spinbox (lv_spinbox)

## Overview
The Spinbox contains a number as text which can be increased or decreased by *Keys* or API functions. 
The Spinbox is a modified [Text area](/object-types/ta).

### Set format
`lv_spinbox_set_digit_format(spinbox, digit_count, separator_position)` set the format of the number. 
`digit_count` sets the number of digits. Leading zeros are added to fill the space on the left. 
`separator_position` sets the number of digit before the decimal point. `0` means no decimal point.

`lv_spinbox_set_padding_left(spinbox, cnt)` add `cnt` "space" characters between the sign an the most left digit.

### Value and ranges
`lv_spinbox_set_range(spinbox, min, max)` sets the range of the Spinbox.

`lv_spinbox_set_value(spinbox, num)` sets the Spinbox's value manually. 

`lv_spinbox_increment(spinbox)` and `lv_spinbox_decrement(spinbox)` increments/decrements the value of the Spinbox. 

`lv_spinbox_set_step(spinbox, step)` sets the amount to increment decrement.


## Style usage

The `lv_spinbox_set_style(roller, LV_SPINBOX_STYLE_..., &style)` set the styles of a Spinbox.

- **LV_SPINBOX_STYLE_BG** Style of the background. All `style.body` properties are used. `style.text` is used for label. Default: `lv_style_pretty`
- **LV_SPINBOX_STYLE_SB** Scrollbar's style which uses all `style.body` properties. `padding.right/bottom` sets horizontal and vertical the scrollbars' padding respectively and the `padding.inner` sets the scrollbar's width. (default: `lv_style_pretty_color`)
- **LV_SPINBOX_STYLE_CURSOR** Style of the cursor which uses all `style.body` properties including `padding` to make the cursor larger then the digits. 


## Events
Besides the [Generic events](/overview/event.html#generic-events) the following [Special events](/overview/event.html#special-events) are sent by the Drop down lists:
- **LV_EVENT_VALUE_CHANGED** sent when the value has changed. (the value is set as event data as `int32_t`)
- **LV_EVENT_INSERT** sent by the ancestor Text area but shouldn't be used.

Learn more about [Events](/overview/event).

## Keys
The following *Keys* are processed by the Buttons:
- **LV_KEY_LEFT/RIGHT** With *Keypad* move the cursor left/right. With *Encoder* decrement/increment the selected digit. 
- **LY_KEY_ENTER** Apply the selected option (Send `LV_EVENT_VALUE_CHANGED` event and close the Drop down list) 
- **LV_KEY_ENTER** With *Encoder* got the net digit. Jump to the first after the last. 


## Example

```eval_rst

.. include:: /lv_examples/src/lv_ex_spinbox/index.rst

```

## API 

```eval_rst

.. doxygenfile:: lv_spinbox.h
  :project: lvgl
        
```
## Example

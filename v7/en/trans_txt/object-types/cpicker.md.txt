```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/en/object-types/cpicker.md
```
# Color picker (lv_cpicker)

## Overview

The *color picker* object **draws a color band and knob** that enable users to **choose a color's hue, saturation, and/or value**.

### Types of color pickers

The color band of a *color picker* can currently be drawn in two ways:

* As a linear bar (`LV_CPICKER_TYPE_RECT`).
* As a circular ring (`LV_CPICKER_TYPE_DISC`).

You can switch between these modes with `lv_cpicker_set_type(cpicker, type`).

### Notes

In circular mode, the **width and height** of the *color picker* should be the **same**.

## Styles
To set the style of a *color picker* object, use `lv_cpicker_set_style(cpicker, LV_CPICKER_STYLE_XXX, &style)`. `XXX` can either be `MAIN` or `INDICATOR`, which represent the color band and knob, respectively.

- **line.width** - the thickness of the color ring (in `DISC` mode)
- **body.[main/grad]_color** - the background color of the color picker

## Events
Besides the [Generic events](/overview/event.html#generic-events) the following [Special events](/overview/event.html#special-events) are sent by color pickers:
 - **LV_EVENT_VALUE_CHANGED** - sent when the color changes.

Learn more about [Events](/overview/event).

## Keys
No *Keys* are processed by the object type.

Learn more about [Keys](/overview/indev).


## Example

There is no official example available for this object type yet, but here is some sample test code:

```c
    const lv_coord_t pickerSize = 200;

	/* Set the style of the color ring */
    static lv_style_t styleMain;
    lv_style_copy(&styleMain, &lv_style_plain);
    styleMain.line.width = 30;
	/* Make the background white */
    styleMain.body.main_color = styleMain.body.grad_color = LV_COLOR_WHITE;

	/* Set the style of the knob */
    static lv_style_t styleIndicator;
    lv_style_copy(&styleIndicator, &lv_style_pretty);
    styleIndicator.body.border.color = LV_COLOR_WHITE;
	/* Ensure that the knob is fully opaque */
    styleIndicator.body.opa = LV_OPA_COVER;
    styleIndicator.body.border.opa = LV_OPA_COVER;

    lv_obj_t * scr = lv_scr_act();

    lv_obj_t * colorPicker = lv_cpicker_create(scr, NULL);
    lv_obj_set_size(colorPicker, pickerSize, pickerSize);
	/* Choose the 'DISC' type */
    lv_cpicker_set_type(colorPicker, LV_CPICKER_TYPE_DISC);
    lv_obj_align(colorPicker, NULL, LV_ALIGN_CENTER, 0, 0);
	/* Set the styles */
    lv_cpicker_set_style(colorPicker, LV_CPICKER_STYLE_MAIN, &styleMain);
    lv_cpicker_set_style(colorPicker, LV_CPICKER_STYLE_INDICATOR, &styleIndicator);
	/* Change the knob's color to that of the selected color */
    lv_cpicker_set_indic_colored(colorPicker, true);

```

## API

```eval_rst

.. doxygenfile:: lv_cpicker.h
  :project: lvgl

```

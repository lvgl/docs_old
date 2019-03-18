_Written for v5.1, revision 2_

## Overview

The Switch can be used to **turn on/off**  something. The look like a little slider. The state of the switch can be changed by:

- Clicking on it
- Sliding it
- Using `lv_sw_on(sw)` and `lv_sw_off(sw)` functions

A **callback function** can be assigned to call when the user uses the switch: `lv_sw_set_action(sw, my_action)`.

**New in v5.3**: Switches can be animated by calling `lv_sw_set_anim_time(sw, anim_ms)`.

## Style usage

You can modify the Switch's styles with `lv_sw_set_style(sw, LV_SW_STYLE_..., &style)`.

- **LV_SW_STYLE_BG** Style of the background. All _style.body_ properties are used. The _padding_ values make the Switch smaller then the knob. (negative value makes is larger)
- **LV_SW_STYLE_INDIC** Style of the indicator. All _style.body_ properties are used. The _padding_ values make the indicator smaller then the background. 
- **LV_SW_STYLE_KNOB_OFF** Style of the knob when the switch is off.  The _style.body_ properties are used except padding.
- **LV_SW_STYLE_KNOB_ON** Style of the knob when the switch is on.  The _style.body_ properties are used except padding.

## Notes

- The Knob is not a real object it is only drawn above the Bar

## Example
![Switch image](http://docs.littlevgl.com/img/switch-lv_sw.png)
```c
/*Create styles for the switch*/
static lv_style_t bg_style;
static lv_style_t indic_style;
static lv_style_t knob_on_style;
static lv_style_t knob_off_style;
lv_style_copy(&bg_style, &lv_style_pretty);
bg_style.body.radius = LV_RADIUS_CIRCLE;

lv_style_copy(&indic_style, &lv_style_pretty_color);
indic_style.body.radius = LV_RADIUS_CIRCLE;
indic_style.body.main_color = LV_COLOR_HEX(0x9fc8ef);
indic_style.body.grad_color = LV_COLOR_HEX(0x9fc8ef);
indic_style.body.padding.hor = 0;
indic_style.body.padding.ver = 0;

lv_style_copy(&knob_off_style, &lv_style_pretty);
knob_off_style.body.radius = LV_RADIUS_CIRCLE;
knob_off_style.body.shadow.width = 4;
knob_off_style.body.shadow.type = LV_SHADOW_BOTTOM;

lv_style_copy(&knob_on_style, &lv_style_pretty_color);
knob_on_style.body.radius = LV_RADIUS_CIRCLE;
knob_on_style.body.shadow.width = 4;
knob_on_style.body.shadow.type = LV_SHADOW_BOTTOM;

/*Create a switch and apply the styles*/
lv_obj_t *sw1 = lv_sw_create(lv_scr_act(), NULL);
lv_sw_set_style(sw1, LV_SW_STYLE_BG, &bg_style);
lv_sw_set_style(sw1, LV_SW_STYLE_INDIC, &indic_style);
lv_sw_set_style(sw1, LV_SW_STYLE_KNOB_ON, &knob_on_style);
lv_sw_set_style(sw1, LV_SW_STYLE_KNOB_OFF, &knob_off_style);
lv_obj_align(sw1, NULL, LV_ALIGN_CENTER, 0, -50);

/*Copy the first switch and turn it ON*/
lv_obj_t *sw2 = lv_sw_create(lv_scr_act(), sw1);
lv_sw_set_on(sw2);
lv_obj_align(sw2, NULL, LV_ALIGN_CENTER, 0, 50);
```

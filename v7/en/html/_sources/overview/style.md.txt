```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/en/overview/style.md
```
# Styles


*Styles* are used to set the appearance of the objects. Styles in lvgl are heavily inspired by CSS. The concept in nutshell is the following:
- A style is an `lv_style_t` variable which can hold properties, for example border width, text color and so on. It's similar to `class` in CSS. 
- Not all properties have to be specified. Unspecified properties will use a default value.
- Styles can be assigned to objects to change their appearance.
- A style can be used by any number of objects.
- Styles can be cascaded which means multiple styles can be assigned to an object and each style can have different properties.  
For example `style_btn` can result in a default gray button and `style_btn_red` can add only a `background-color=red` to overwrite the background color.
- Later added styles have higher precedence. It means if a property is specified in two styles the later added will be used.
- Some properties (e.g. text color) can be inherited from the parent(s) if it's not specified in the object. 
- Objects can have local styles which has higher precedence than "normal" styles.
- Unlike CSS (where pseudo classes describes different states, e.g. `:hover`), in lvgl a property is assigned to a given state.
- Transition can be applied when the object changes state.


## States
The objects can be in the following states:
- **LV_STATE_DEFAULT** (0x00): Normal, released
- **LV_STATE_CHECKED** (0x01): Toggled or checked
- **LV_STATE_FOCUSED** (0x02): Focused via keypad or encoder or clicked via touchpad/mouse 
- **LV_STATE_EDITED**  (0x04): Edit by an encoder
- **LV_STATE_HOVERED** (0x08): Hovered by mouse (not supported now)
- **LV_STATE_PRESSED** (0x10): Pressed
- **LV_STATE_DISABLED** (0x20): Disabled or inactive
	
Combination of states are	also possible, for example `LV_STATE_FOCUSED | LV_STATE_PRESSED`. 

The styles properties can be defined in every state and state combination. For example setting different background color for default and pressed state. 
If a property is not defined in a state the best matching state's property will be used. Typically it means the property with `LV_STATE_DEFAULT` state.˛
If the property is not set even for the default state the default value will be used. (See later)

But what does the "best matching state's property" really means? 
States has a precedence which is shown by their value (see in the above list). A higher value means a higher precedence.
To determine which state's property to use let's use an example. Let's see the background color is defined like this:
- `LV_STATE_DEFAULT`: white
- `LV_STATE_PRESSED`: gray
- `LV_STATE_FOCUSED`: red

1. By the default the object is in default state, so it's a simple case: the property is perfectly defined in object's current state as white
2. When the object is pressed there are 2 related properties: default with white (default is related to every state) and pressed with gray. 
The pressed state has 0x10 precedence which is higher than the default state's 0x00 precedence, so gray color will be used.
3. When the object is focused the same thing happens as in pressed state and red color will be used.
4. When the object is focused and pressed both gray and red would work, but the pressed state has higher precedence than focused so gray color will be used.
5. It's possible to set e.g rose color for `LV_STATE_PRESSED | LV_STATE_FOCUSED`. 
In this case this combined state has 0x2 + 0x10 = 0x12 precedence, which higher than the pressed states precedence so rose color would be used.
6. When the object is checked there is no property to set the background color for this state. So in lack of a better option the object remains white from the default state's property.
 

## Cascading styles
It's not required to set all the properties in one style. It's possible add more styles to an object and the let the later added style to modify or extend the properties in the other styles.
For example, create a general gray button style and create a new for red buttons where only the new background color is set. 

It's the same concept when in CSS all the used classes are listed like `<div class=".btn .btn-red">`.

The later added styles has higher precedence over the earlier ones. So from the previous gray/red the red background color will overwrite the gray background color. 
However the precedence coming from states are still taken into account. 
So let's examine the following case:
- the basic button style defines dark-gray color for default state and light-gray color pressed state
- the red button styles sets the background color to red only in the default state

In this case when the button is pressed the light-gray color is a better match because it describes the the current state perfectly. 

## Inheritance 
Some properties (typically that are related to texts) can be inherited from the parent object's styles. Inheritance is applied only if the given property is not set in the object's styles (even in default state). 
In this case, if the property is inheritable, the properties value will be searched in the parent too until a part can tell a value for the property. The parents will use their own state to tell the value. 
So is button is pressed, and text color comes from here, the pressed text color will be used.


## Part of the objects
Objects can have *parts* which can have their own style. For example a [page](/widgets/page) has four parts:
- Background
- Scrollable
- Scrollbar
- Edge flash

![page_small.png](A scrollable page in lvgl)

There is three type of of object parts **main**, **virtual** and **real**. 

The main part is usually the background and largest part of the object. Some object has only has main part. For example a button has only a background.

The virtual parts are additional parts just drawn on the fly to the main part. There is no "real" object behind them. 
For example the page's scrollbar is not a real object, it's just drawn when the page's background is drawn. 
The virtual parts always have the same state as the main part. 
If the property can be inherited, the main part will be also considered before going to the parent.

The real parts are real objects created and managed by the main object. For example the page's scrollable part is real object. 
Real parts can be in different state than the main part.

To see which parts an object has see their documentation.

## Initialize styles and set/get properties

Styles are stored in `lv_style_t` variables. Style variables should be `static`, global or dynamically allocated. In other words they can not be local variables in functions which are destroyed when the function exists. 
Before using a style it should be initialized with `lv_style_init(&my_style)`. 
After initializing the style properties can be set added to it.
Property set functions looks like this: `lv_style_set_<property_name>(&style, <state>, <value>);`
For example the [above mentioned](#states) example looks like this:
```c
static lv_style_t style1;
lv_style_set_bg_color(&style1, LV_STATE_DEFAULT, LV_COLOR_WHITE);
lv_style_set_bg_color(&style1, LV_STATE_PRESSED, LV_COLOR_GRAY);
lv_style_set_bg_color(&style1, LV_STATE_FOCUSED, LV_COLOR_RED);
lv_style_set_bg_color(&style1, LV_STATE_FOCUSED | LV_STATE_PRESSED, lv_color_hex(0xf88));
```

It's possible to copy a style with `lv_style_copy(&style_destination, &style_source)`. After copy properties still can be added freely. 

To remove a property use:

```c
lv_style_remove_prop(&style, LV_STYLE_BG_COLOR | (LV_STATE_PRESSED << LV_STYLE_STATE_POS));
```

To get the value from style in a state functions with the following prototype are available: `lv_style_get_<prperty_name>(&style, <state>, <result poiner>);`.
The the best matching property will be selected and it's precedence will be returned. `-1` will be returned if the property is not found. For example:

```c
lv_color_t color;
int16_t res;
res = lv_style_get_bg_color(&style1, LV_STATE_PRESSED, &color);
if(res >= 0) {
	//the bg_color is loaded into `color`
}
```

To reset a style (free all it's data) use 
```c
lv_style_reset(&style);
```

## Managing style list
A style on it's own not that useful. It should be assigned to an object to take its effect.
Every part of the objects store a *style list* which is the list of assigned styles.

To add a style to an object use `lv_obj_add_style(obj, <part>, &style)`
For example:
```c
lv_obj_add_style(btn, LV_BTN_PART_MAIN, &btn);			/*Default button style*/
lv_obj_add_style(btn, LV_BTN_PART_MAIN, &btn_red);  /*Overwrite only a some colors to red*/
```

An objects style list can be reset with `lv_obj_reset_style_list(obj, <part>)` 

If a style which is already assigned to an object changes (i.e. one of it's property is set to a new value) the objects using that style should be notified with `lv_obj_refresh_style(obj)`

To get a final value of property, including cascading, inheritance, local styles and transitions (see below), get functions like this can be used: `lv_obj_get_style_<property_name>(obj, <part>)`. 
These functions uses the object's current state and if no better candidate returns a default value.  
For example:
```c
lv_color_t color = lv_obj_get_style_bg_color(btn, LV_BTN_PART_MAIN);
```

## Local styles
In the object's style lists so called local properties can be stored as well. It's the same concept than CSS's `<div style="color:red">`.
The local style just like a normal style created only for a given object.

To set a local property use functions like `lv_obj_set_style_local_<property_name>(obj, <part>, <state>, <value>);`  
For example:
```c
lv_obj_set_style_local_bg_color(btn, LV_BTN_PART_MAIN, LV_STATE_DEFAULT, LV_COLOR_RED);
```

## Transitions
By default, when an object changes state (e.g. it's pressed) the new properties from the new state are set immediately. However with transitions it's possible to play an animation of value change.
For example, on pressing a button its background color can be animated to the pressed color over 300 ms.

The parameters of the transitions are stored in the styles. It's possible to set 
- the time of the transition
- the delay before starting the transition 
- the animation path (also known as timing function)
- the properties to animate 

The transition properties can be defined for each state. 
For example setting 500 ms transition time in default state will mean that when the object goes to default state 500 ms transition time will be applied. 
Setting 100 ms transition time in pressed state will mean 100 ms transition time when going to presses state.
In summary, this configuration will result in fast going to presses state and slow going back to default. 



## Properties

The following properties can be used in the styles.

### Mixed properties
- **radius** (`lv_style_int_t`): Set the radius of the background. 0: no radius, `LV_RADIUS_CIRCLE`: maximal radius. 
- **clip_corner** (`bool`): `true`: enable to clip the overflowed content on the rounded (radius > 0) corners.
- **size** (`lv_style_int_t`): Size of internal elements of the widgets. See the documentation of the widgets if this property is used or not.
- **transform_width**  (`lv_style_int_t`): Make the object wider on both sides with this value.
- **transform_height**  (`lv_style_int_t`) Make the object higher on both sides with this value.
- **opa_scale** (`lv_style_int_t`): Inherited. Scale down all opacity values of the object by this factor. As it's inherited the children objects will be affected too. 

### Padding properties
Set the space on the edges and between the children objects. Typically used by [Container](/widgets/cont) object if [layout](/widgets/cont#layout) or 
[auto fit](/widgets/cont#auto-fit) is enabled. However other widgets also use them to set spacing. See the documentation of the widgets for the details. 
 - **pad_top** (`lv_style_int_t`): Set the padding on the top.
 - **pad_bottom** (`lv_style_int_t`): Set the padding on the bottom.
 - **pad_left** (`lv_style_int_t`): Set the padding on the left.
 - **pad_right** (`lv_style_int_t`): Set the padding on the right.
 - **pad_inner** (`lv_style_int_t`): Set the padding inside the object between children.

### Background properties
The background is a simple rectangle which can have gradient and `radius` rounding.
- **bg_color** (`lv_color_t`) Specifies the color of the background. Default value: `LV_COLOR_WHITE`
- **bg_opa** (`lv_opa_t`) Specifies opacity of the background. Default value: `LV_OPA_TRANSP`.
- **bg_grad_color** (`lv_color_t`) Specifies the color of the background's gradient. The color on the right or bottom is `bg_grad_dir != LV_GRAD_DIR_NONE`. Default value: `LV_COLOR_WHITE`.
- **bg_main_stop** (`uint8_t`): Specifies where should the gradient start. 0: at left/top most position, 255: at right/bottom most position.
- **bg_grad_stop** (`uint8_t`): Specifies where should the gradient start. 0: at left/top most position, 255: at right/bottom most position. Default value: 255.
- **bg_grad_dir** (`lv_grad_dir_t`) Specifies the direction of the gradient. Can be `LV_GRAD_DIR_NONE/HOR/VER`. Default value: `LV_GRAD_DIR_NONE`. 
- **bg_blend_mode** (`lv_blend_mode_t`): Set the blend mode the background. Can be `LV_BLEND_MODE_NORMAL/ADDITIVE/SUBTRACTIVE`). Default value: `LV_BLEND_MODE_NORMAL`.

```eval_rst
.. image:: /lv_examples/src/lv_ex_style/lv_ex_style_1.*
  :alt: Styling the background in lvgl

.. literalinclude:: /lv_examples/src/lv_ex_style/lv_ex_style_1.c
  :language: c
```

### Border properties
The border in drawn on to of the *background*. It has `radius` rounding.
- **border_color** (`lv_color_t`) Specifies the color of the border. 
- **border_opa** (`lv_opa_t`) Specifies opacity of the border.
- **border_width** (`lv_style_int_t`): Set the width of the border.
- **border_side** (`lv_border_side_t`) Specifies which sides of the border to draw. Can be `LV_BORDER_SIDE_NONE/LEFT/RIGHT/TOP/BOTTOM/FULL`. ORed values are also possible. Default value: `LV_BORDER_SIDE_FULL`.
- **border_post** (`bool`): If `true` the border will be drawn all children has been drawn.
- **border_blend_mode** (`lv_blend_mode_t`): Set the blend mode of the border. Can be `LV_BLEND_MODE_NORMAL/ADDITIVE/SUBTRACTIVE`). Default value: `LV_BLEND_MODE_NORMAL`.

```eval_rst
.. image:: /lv_examples/src/lv_ex_style/lv_ex_style_2.*
  :alt: Styling the border in lvgl

.. literalinclude:: /lv_examples/src/lv_ex_style/lv_ex_style_2.c
  :language: c
```

### Outline properties
The outline is similar to *border* but is drawn outside of the object.
- **outline_color** (`lv_color_t`) Specifies the color of the outline.
- **outline_opa** (`lv_opa_t`) Specifies opacity of the outline.
- **outline_width** (`lv_style_int_t`): Set the width of the outline.
- **outline_pad** (`lv_style_int_t`) Set the space between the object and the outline. 
- **outline_blend_mode** (`lv_blend_mode_t`): Set the blend mode of the outline. Can be `LV_BLEND_MODE_NORMAL/ADDITIVE/SUBTRACTIVE`). Default value: `LV_BLEND_MODE_NORMAL`.

```eval_rst
.. image:: /lv_examples/src/lv_ex_style/lv_ex_style_3.*
  :alt: Styling the outline in lvgl

.. literalinclude:: /lv_examples/src/lv_ex_style/lv_ex_style_3.c
  :language: c
```

### Shadow properties
The shadow is a blurred area under the object.
- **shadow_color** (`lv_color_t`) Specifies the color of the shadow.
- **shadow_opa** (`lv_opa_t`) Specifies opacity of the shadow.
- **shadow_width** (`lv_style_int_t`): Set the width (blur size) of the outline.
- **shadow_ofs_x** (`lv_style_int_t`): Set the an X offset for the shadow.
- **shadow_ofs_y** (`lv_style_int_t`): Set the an Y offset for the shadow.
- **shadow_spread** (`lv_style_int_t`): ake the shadow larger than the background in every direction by this value.
- **shadow_blend_mode** (`lv_blend_mode_t`): Set the blend mode of the shadow. Can be `LV_BLEND_MODE_NORMAL/ADDITIVE/SUBTRACTIVE`). Default value: `LV_BLEND_MODE_NORMAL`.

```eval_rst
.. image:: /lv_examples/src/lv_ex_style/lv_ex_style_4.*
  :alt: Styling the shadow in lvgl

.. literalinclude:: /lv_examples/src/lv_ex_style/lv_ex_style_4.c
  :language: c
```

### Pattern properties
The pattern is an image (or symbol) drawn in the middle of the background or repeated to fill the whole background.
- **pattern_image** (`const void *`): Pointer to an `lv_img_dsc_t` variable, a path to an image file or a symbol.
- **pattern_opa** (`lv_opa_t`): Specifies opacity of the pattern.
- **pattern_recolor** (`lv_color_t`): Mix this color to the pattern image. In case of symbols (texts) it will be the text color.
- **pattern_recolor_opa** (`lv_opa_t`): Intensity of recoloring. Default value: `LV_OPA_TRANSP` (no recoloring).
- **pattern_repeat** (`bool`): `true`: the pattern will be repeated as a mosaic. `false`: place the pattern in the middle of the background.
- **pattern_blend_mode** (`lv_blend_mode_t`): Set the blend mode of the pattern. Can be `LV_BLEND_MODE_NORMAL/ADDITIVE/SUBTRACTIVE`). Default value: `LV_BLEND_MODE_NORMAL`.

```eval_rst
.. image:: /lv_examples/src/lv_ex_style/lv_ex_style_5.*
  :alt: Styling the shadow in lvgl

.. literalinclude:: /lv_examples/src/lv_ex_style/lv_ex_style_5.c
  :language: c
```

### Value properties
Value is an arbitrary text drawn to the background. It can be a lightweighted replacement of the creating label objects.

- **value_str** (`const char *`): Pointer to text to display. Only the pointer is saved.
- **value_color** (`lv_color_t`): Color of the text. 
- **value_opa** (`lv_opa_t`): Opacity of the text.
- **value_font** (`const lv_font_t *`): Pointer to font of the text.
- **value_letter_space** (`lv_style_int_t`): Letter space of the text.
- **value_line_space** (`lv_style_int_t`): Line space of the text.
- **value_align** (`lv_align_t`): Alignment of the text. Can be `LV_ALIGN_...`.
- **value_ofs_x** (`lv_style_int_t`): X offset from the original position of the alignment.
- **value_ofs_y** (`lv_style_int_t`): Y offset from the original position of the alignment.
- **value_blend_mode** (`lv_blend_mode_t`): Set the blend mode of the text. Can be `LV_BLEND_MODE_NORMAL/ADDITIVE/SUBTRACTIVE`). Default value: `LV_BLEND_MODE_NORMAL`.

```eval_rst
.. image:: /lv_examples/src/lv_ex_style/lv_ex_style_6.*
  :alt: Styling the value text in lvgl

.. literalinclude:: /lv_examples/src/lv_ex_style/lv_ex_style_6.c
  :language: c
```

### Text properties
Properties for textual object.
- **text_color** (`lv_color_t`): Color of the text. 
- **text_opa** (`lv_opa_t`): Opacity of the text.
- **text_font** (`const lv_font_t *`): Pointer to font of the text.
- **text_letter_space** (`lv_style_int_t`): Letter space of the text.
- **text_line_space** (`lv_style_int_t`): Line space of the text.
- **text_decor** (`lv_text_decor_t`): Add text decoration. Can be `LV_TEXT_DECOR_NONE/UNDERLINE/STRIKETHROUGH`.
- **text_sel_color** (`lv_color_t`): Set background color of text selection.
- **text_blend_mode** (`lv_blend_mode_t`): Set the blend mode of the text. Can be `LV_BLEND_MODE_NORMAL/ADDITIVE/SUBTRACTIVE`). Default value: `LV_BLEND_MODE_NORMAL`.

```eval_rst
.. image:: /lv_examples/src/lv_ex_style/lv_ex_style_7.*
  :alt: Styling aline in lvgl

.. literalinclude:: /lv_examples/src/lv_ex_style/lv_ex_style_7.c
  :language: c
```

### Line properties
Properties of lines.
- **line_color** (`lv_color_t`): Color of the line. 
- **line_opa** (`lv_opa_t`): Opacity of the line.
- **line_width** (`lv_style_int_t`): Width of the line.
- **line_dash_width** (`lv_style_int_t`): Width of dash. Dashing is drawn only for horizontal or vertical lines. 0: disable dash.
- **line_dash_gap** (`lv_style_int_t`): Gap between two dash line. Dashing is drawn only for horizontal or vertical lines. 0: disable dash.
- **line_rounded** (`bool`): `true`: draw rounded line endings.
- **line_blend_mode** (`lv_blend_mode_t`): Set the blend mode of the line. Can be `LV_BLEND_MODE_NORMAL/ADDITIVE/SUBTRACTIVE`). Default value: `LV_BLEND_MODE_NORMAL`.


### Image properties
Properties of image.
- **image_recolor** (`lv_color_t`):  Mix this color to the pattern image. In case of symbols (texts) it will be the text color.
- **image_recolor_opa** (`lv_opa_t`): Intensity of recoloring. Default value: `LV_OPA_TRANSP` (no recoloring).
- **image_opa** (`lv_opa_t`): Opacity of the image.
- **image_blend_mode** (`lv_blend_mode_t`): Set the blend mode of the image. Can be `LV_BLEND_MODE_NORMAL/ADDITIVE/SUBTRACTIVE`). Default value: `LV_BLEND_MODE_NORMAL`.

```eval_rst
.. image:: /lv_examples/src/lv_ex_style/lv_ex_style_9.*
  :alt: Styling an image in lvgl

.. literalinclude:: /lv_examples/src/lv_ex_style/lv_ex_style_9.c
  :language: c
```

### Transition properties
Properties to describe state change animations.
- **transition_time** (`lv_style_int_t`): Time of the transition.
- **transition_delay** (`lv_style_int_t`): Delay before the transition.
- **transition_1** (`property name`): A property on which transition should be applied. Use the property name with upper case with `LV_STYLE_` prefix, e.g. `LV_STYLE_BG_COLOR`
- **transition_2** (`property name`): Same as *transition_1* just for an other property.
- **transition_3** (`property name`): Same as *transition_1* just for an other property.
- **transition_4** (`property name`): Same as *transition_1* just for an other property.
- **transition_5** (`property name`): Same as *transition_1* just for an other property.
- **transition_6** (`property name`): Same as *transition_1* just for an other property.
- **transition_path** (`lv_anim_path_cb_t`): An animation path for the transition. Built pats can be used, e.g. `lv_anim_path_overshoot`.

```eval_rst
.. image:: /lv_examples/src/lv_ex_style/lv_ex_style_10.*
  :alt: Styling an transitions in lvgl

.. literalinclude:: /lv_examples/src/lv_ex_style/lv_ex_style_10.c
  :language: c
```

### Scale properties
Auxiliary properties for scale like elements. Scales have a normal and and end region. 
As the name implies the end region is the end of the scale where can be critical values or inactive values. The normal region is before the end region. 
Both region could have different properties.
- **scale_grad_color** (`lv_color_t`):  In normal region make gradient to this color on the scale lines. 
- **scale_end_color** (`lv_color_t`):  Color of the scale lines in the end region. 
- **scale_width** (`lv_style_int_t`): Width of the scale. Default value: `LV_DPI / 8`.
- **scale_border_width** (`lv_style_int_t`): Width of a border drawn on the outer side of the scale in the normal region.
- **scale_end_border_width** (`lv_style_int_t`): Width of a border drawn on the outer side of the scale in the end region.
- **scale_end_line_width** (`lv_style_int_t`): Width of a scale lines in the end region.


## Themes
Themes are collection of styles. There is always an active theme whose styles are automatically applied when an object is created. It gives a default appearance to UI which can modified by adding further styles.

The default theme is set in `lv_conf.h` with `LV_THEME_...` defines. Every theme has the following properties
- primary color
- secondary color
- small font
- normal font
- subtitle font
- title font

The usage of these parameters depends on the given theme.

There are 3 built-in themes:
- empty: no default styles are added
- default: an impressive, modern theme 
- template: a very simple theme which can be copied to create  custom theme 


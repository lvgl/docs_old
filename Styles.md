_Written for v5.1_

To set the appearance of the objects styles can be used. A style is a structure variable with attributes like colors, paddings, visibility, and others. There is common style type: **lv_style_t**.

By setting the fields of an `lv_style_t` structure you can influence the appearance of the objects using that style.

The objects store only a pointer to a style so the style cannot be a local variable which is destroyed after the function exists. **You should use static, global or dynamically allocated variables.**
```c
lv_style_t style_1;             /*OK! Global variables for styles are fine*/
static lv_style_t style_2;      /*OK! Static variables outside the functions are fine*/
void my_screen_create(void) 
{
  static lv_style_t style_3;    /*OK! Static variables in the functions are fine*/
  lv_style_t style_1;           /*WRONG! Styles can't be local variables*/

  ...
}
```


## Style properties
A style has 5 main parts: common, body, text, image and line. An object will use that fields which are relevant for it. For example, Lines don't care about the letter_space. To see which fields are used by an object type see their documentation.

The fields of a style structure are the followings:

* **Common properties**
  * **glass** 1: Do not inherit this style (see below)
* **Body style properties** Used by the rectangle-like objects
  - **body.empty** Do not fill the rectangle (just draw border and/or shadow)
  - **body.main_colo**r Main color (top color)
  - **body.grad_color** Gradient color (bottom color)
  - **body.radius** Corner radius. (set to LV_RADIUS_CIRCLE to draw circle)
  - **body.opa** Opacity (0..255 or LV_OPA_TRANSP, LV_OPA_10, LV_OPA_20 ... LV_OPA_COVER)
  - **body.border.color** Border color
  - **body.border.width** Border width
  - **body.border.part** Border parts (LV_BORDER_LEFT/RIGHT/TOP/BOTTOM/FULL or 'OR'ed values)
  - **body.border.opa** Border opacity
  - **body.shadow.color** Shadow color
  - **body.shadow.width** Shadow width
  - **body.shadow.type** Shadow type (LV_SHADOW_BOTTOM or LV_SHADOW_FULL)
  - **body.padding.hor** Horizontal padding
  - **body.padding.ver** Vertical padding
  - **body.padding.inner** Inner padding
* **Text style properties** Used by the objects which show texts
  - **text.color** Text color
  - **text.font** Pointer to a font
  - **text.opa** Text opacity (0..255 or LV_OPA_TRANSP, LV_OPA_10, LV_OPA_20 ... LV_OPA_COVER)
  - **text.letter_space** Letter space
  - **text.line_space** Line space
* **Image style properties** Used by image-like objects or icons on objects
  - **image.color** Color for image re-coloring based on the pixels brightness
  - **image.intense** Re-color intensity (0..255 or LV_OPA_TRANSP, LV_OPA_10, LV_OPA_20 ... LV_OPA_COVER)
  - **image.opa** Image opacity (0..255 or LV_OPA_TRANSP, LV_OPA_10, LV_OPA_20 ... LV_OPA_COVER)
* **Line style properties** Used by objects containing lines or line-like elements
  - **line.color** Line color
  - **line.width** Line width
  - **line.opa** Line opacity (0..255 or LV_OPA_TRANSP, LV_OPA_10, LV_OPA_20 ... LV_OPA_COVER)

## Using styles
Every object type has a unique function to set its style or styles.

If the object has only one style - like a label - the `lv_label_set_style(label1, &style) `function can be used to set a new style.

If the object has more styles (like a button have 5 styles for each state) `lv_btn_set_style(obj, LV_BTN_STYLE_..., &rel_style`) function can be used to set a new style.

The styles and the style properties used by an object type are described in their documentation.

If you **modify a style which is used** by one or more objects then the objects have to be notified about the style is changed. You have two options to do that:

```c
void lv_obj_refresh_style(lv_obj_t * obj);		/*Notify an object about its style is modified*/
void lv_obj_report_style_mod(void * style);		/*Notify all object if a style is modified.(NULL to notify all objects)*/
```

If the **style of an object is NULL then its style will be inherited from its parent's style**. It makes easier to create a consistent design. Don't forget a style describes a lot of properties at the same time. So for example, if you set a button's style and create a label on it with NULL style then the label will be rendered according to the buttons styles. In other words, the button makes sure its children will look well on it.

Setting the //glass style property will prevent inheriting that style//. You should use it if the style is transparent so that its children use colors and others from its parent.

## Built-in styles
There are several built-in styles in the library:

![Built in styles in LittlevGL Embedded Graphics Library](http://docs.littlevgl.com/img/style-built-in.png)

As you can see there is a style for screens, for buttons, plain and pretty styles and transparent styles as well. The `lv_style_transp`, `lv_style_transp_fit` and `lv_style_transp_tight` differ only in paddings: for `lv_style_transp_tight` all padings are zero, for `lv_style_transp_fit` only hor and ver paddings are zero.

The built in styles are global lv_style_t variables so you can use them like: lv_btn_set_style(obj, LV_BTN_STYLE_REL, &lv_style_btn_rel)

You can modify the built-in styles or you can create new styles. When creating new styles it is recommended to first copy a built-in style to be sure all fields are initialized with a proper value. The lv_style_copy(&dest_style, &src_style) can be used to copy styles.

## Style animations
You can animate styles using `lv_style_anim_create(&anim)`. Before calling this function you have to initialize an `lv_style_anim_`t variable. The animation will fade a `style_1` to `style_2`.

```c
lv_style_anim_t a;    /*Will be copied, can be local variable*/
a.style_anim = & style_to_anim;     /*Pointer to style to animate*/
a.style_start = & style_1;          /*Pointer to the initial style (only pointer saved) */
a.style_end = & style_2;            /*Pointer to the target style (only pointer saved) */
a.act_time = 0;                     /*Set negative to make a delay*/
a.time = 1000;                      /*Time of animation in milliseconds*/
a.playback = 0;                     /*1: play the animation backward too*/
a.playback_pause = 0;               /*Wait before playback [ms]*/
a.repeat = 0;                       /*1: repeat the animation*/
a.repeat_pause = 0;                 /*Wait before repeat [ms]*/
a.end_cb = NULL;                    /*Call this function when the animation ready*/
```

## Style example
The example below demonstrates the above-described style usage

![Styles usage example in LittlevGL Embedded Graphics Library](http://docs.littlevgl.com/img/style-example.png)
```c
/*Create a style*/
static lv_style_t style1;
lv_style_copy(&style1, &lv_style_plain);    /*Copy a built-in style to initialize the new style*/
style1.body.main_color = LV_COLOR_WHITE;
style1.body.grad_color = LV_COLOR_BLUE;
style1.body.radius = 10;
style1.body.border.color = LV_COLOR_GRAY;
style1.body.border.width = 2;
style1.body.border.opa = LV_OPA_50;
style1.body.padding.hor = 5;            /*Horizontal padding, used by the bar indicator below*/
style1.body.padding.ver = 5;            /*Vertical padding, used by the bar indicator below*/
style1.text.color = LV_COLOR_RED;

/*Create a simple object*/
lv_obj_t *obj1 = lv_obj_create(lv_scr_act(), NULL);
lv_obj_set_style(obj1, &style1);                        /*Apply the created style*/
lv_obj_set_pos(obj1, 20, 20);                           /*Set the position*/

/*Create a label on the object. The label's style is NULL by default*/
lv_obj_t *label = lv_label_create(obj1, NULL);
lv_obj_align(label, NULL, LV_ALIGN_CENTER, 0, 0);       /*Align the label to the middle*/

/*Create a bar*/
lv_obj_t *bar1 = lv_bar_create(lv_scr_act(), NULL);
lv_bar_set_style(bar1, LV_BAR_STYLE_INDIC, &style1);    /*Modify the indicator's style*/
lv_bar_set_value(bar1, 70);                             /*Set the bar's value*/
```

## Themes
To create styles for your GUI is challenging because you need a deeper understanding of the library and you need to have some design skills. In addition, it takes a lot of time to create so many styles.

To speed up the design part themes are introduced. A theme is a style collection which contains the required styles for every object type. For example 5 styles for buttons to describe their 5 possible states. 
Check the [Existing themes](https://littlevgl.com/themes).

To be more specific a theme is a structure variable which contains a lot of lv_style_t * fields. For buttons:
```c
theme.btn.rel       /*Released button style*/
theme.btn.pr        /*Pressed button style*/
theme.btn.tgl_rel   /*Toggled released button style*/
theme.btn.tgl_pr    /*Toggled pressed button style*/
theme.btn.ina       /*Inactive button style*/
```

A theme can initialized by: `lv_theme_xxx_init(hue, font)`. Where xxx is the name of the theme, *hue* is a Hue value from HSV color space (0..360) and *font* is the font applied in the theme (`NULL` to use the `LV_FONT_DEFAULT` default font)

When a theme is initialized its styles can be used like this:

![Theme usage example in Littlev Embedded Graphics Library](http://docs.littlevgl.com/img/theme-example.png)
```c
/*Create a default slider*/
lv_obj_t *slider = lv_slider_create(lv_scr_act(), NULL);
lv_slider_set_value(slider, 70);
lv_obj_set_pos(slider, 10, 10);

/*Initialize the alien theme with a redish hue*/
lv_theme_t *th = lv_theme_alien_init(10, NULL);

/*Create a new slider and apply the themes styles*/
slider = lv_slider_create(lv_scr_act(), NULL);
lv_slider_set_value(slider, 70);
lv_obj_set_pos(slider, 10, 50);
lv_slider_set_style(slider, LV_SLIDER_STYLE_BG, th->slider.bg);
lv_slider_set_style(slider, LV_SLIDER_STYLE_INDIC, th->slider.indic);
lv_slider_set_style(slider, LV_SLIDER_STYLE_KNOB, th->slider.knob);
```

You can ask the library to apply the styles from a theme when you create new objects. To do this use `lv_theme_set_current(th)`;

_Written for v5.1_

The color module handles all color related functions like changing color depth, creating colors from hex code, converting between color depths, mixing colors etc. 

The following variable types are defined by the color module:

- **lv_color1_t** Store monochrome color. For compatibility it also has R,G,B fields but they are always the same (1 byte)
- **lv_color8_t** A structure to store R (3 bit),G (3 bit),B (2 bit) components for 8 bit colors (1 byte)
- **lv_color16_t** A structure to store R (5 bit),G (6 bit),B (5 bit) components for 16 bit colors (2 byte)
- **lv_color24_t** A structure to store R (8 bit),G (8 bit), B (8 bit) components for 24 bit colors (4 byte)
- **lv_color_t** Equal to color1/8/16/24_t according to color depth settings
- **lv_color_int_t** uint8_t, uint16_t or uint32_t according to color depth setting. Used to build color arrays from plain numbers.
- **lv_opa_t** A simple uint8_t type to describe opacity.

The _lv_color_t_, _lv_color1_t__lv_color8_t_, _lv_color16_t_ and _lv_color24_t_ types have got four fields:

- **red** red channel
- **green** green channel
- **blue** blue channel
- **full** red + green + blue as one number

You can set the **current color depth** in _lv_conf.h_ by setting the _LV_COLOR_DEPTH_ define to 1 (monochrome), 8, 16 or 24.

You can **convert a color from the current color depth** to an other. The converter functions return with a number so you have to use the _full_ field:

```c
lv_color_t c;
c.red   = 0x38;
c.green = 0x70;
c.blue  = 0xCC;

lv_color1_t c1;
c1.full = lv_color_to1(c);		/*Return 1 for light colors, 0 for dark colors*/

lv_color8_t c8;
c8.full = lv_color_to8(c);		/*Give a 8 bit number with the converted color*/ 

lv_color16_t c16;
c16.full = lv_color_to16(c); 	/*Give a 16 bit number with the converted color*/

lv_color24_t c24;
c24.full = lv_color_to24(c);	/*Give a 32 bit number with the converted color*/
```

You can **create a color** with the current color depth using the **LV_COLOR_MAKE** macro. It takes 3 arguments (red, green, blue) as 8 bit numbers. For example to create light red color: `my_color = COLOR_MAKE(0xFF,0x80,0x80)`. Colors can be created from **HEX codes** too: `my_color = LV_COLOR_HEX(0xFF8080)` or `my_color = LV_COLOR_HEX3(0xF88)`.

**Mixing two colors** is possible with `mixed_color = lv_color_mix(color1, color2, ratio)`. Ration can be 0..255. 0 results fully color2, 255 result fully color1. 

To describe **opacity** the _lv_opa_t_ type is created as wrapper to _uint8_t_. Some defines are also introduced: 

- **LV_OPA_TRANSP** Value: 0, means the opacity makes the color fully transparent
- **LV_OPA_10** Value: 25, means the color covers only a little
- **LV_OPA_20 ... OPA_80** come logically
- **LV_OPA_90** Value: 229, means the color near fully covers 
- **LV_OPA_COVER** Value: 255, means the color fully covers 

You can also use the _LV_OPA_*_ defines in _lv_color_mix() as ratio._

  

The color module defines the **most basic colors**:   

- ![#000000](https://placehold.it/15/000000/000000?text=+) `LV_COLOR_BLACK`
- ![#808080](https://placehold.it/15/808080/000000?text=+) `LV_COLOR_GRAY`
- ![#c0c0c0](https://placehold.it/15/c0c0c0/000000?text=+) `LV_COLOR_SILVER`
- ![#ff0000](https://placehold.it/15/ff0000/000000?text=+) `LV_COLOR_RED`
- ![#800000](https://placehold.it/15/800000/000000?text=+) `LV_COLOR_MARRON`
- ![#00ff00](https://placehold.it/15/00ff00/000000?text=+) `LV_COLOR_LIME`
- ![#008000](https://placehold.it/15/008000/000000?text=+) `LV_COLOR_GREEN`
- ![#808000](https://placehold.it/15/808000/000000?text=+) `LV_COLOR_OLIVE`
- ![#0000ff](https://placehold.it/15/0000ff/000000?text=+) `LV_COLOR_BLUE`
- ![#000080](https://placehold.it/15/000080/000000?text=+) `LV_COLOR_NAVY`
- ![#008080](https://placehold.it/15/008080/000000?text=+) `LV_COLOR_TAIL`
- ![#00ffff](https://placehold.it/15/00ffff/000000?text=+) `LV_COLOR_CYAN`
- ![#00ffff](https://placehold.it/15/00ffff/000000?text=+) `LV_COLOR_AQUA`
- ![#800080](https://placehold.it/15/800080/000000?text=+) `LV_COLOR_PURPLE`
- ![#ff00ff](https://placehold.it/15/ff00ff/000000?text=+) `LV_COLOR_MAGENTA`
- ![#ffa500](https://placehold.it/15/ffa500/000000?text=+) `LV_COLOR_ORANGE`
- ![#ffff00](https://placehold.it/15/ffff00/000000?text=+) `LV_COLOR_YELLOW`

as well as `LV_COLOR_WHITE`.
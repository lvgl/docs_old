```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/en/overview/indev.md
```
# Input devices

Input devices in general means:
- Pointer-like input devices like touchpad or mouse
- Keypads like a normal keyboard or simple numpad
- Encoders with left/right turn and push options
- External hardware buttons which are assigned to specific points on the screen


``` important:: Before reading further, please read the [Porting](/porting/indev) section of Input devices
```

## Pointers

Pointer input devices can have a cursor. (typically for mouses)

```c
...
lv_indev_t * mouse_indev = lv_indev_drv_register(&indev_drv);

LV_IMG_DECLARE(mouse_cursor_icon);                          /*Declare the image file.*/
lv_obj_t * cursor_obj =  lv_img_create(lv_scr_act(), NULL); /*Create an image object for the cursor */
lv_img_set_src(cursor_obj, &mouse_cursor_icon);             /*Set the image source*/
lv_indev_set_cursor(mouse_indev, cursor_obj);               /*Connect the image  object to the driver*/

``` 

Note that the cursor object should have `lv_obj_set_click(cursor_obj, false)`. 
For images *clicking* is disabled by default.

## Keypad and encoder

You can fully control the user interface without touchpad or mouse using a keypad or encoder(s). it works similarly when you press the *TAB* key on PC to select the element in an application or a web page. 

### Groups

The objects, you want to control with keypad or encoder, needs to be added to a *Group*. 
In every group, there is exactly one focused object which receives the pressed keys or the encoder actions. 
For example, if a [Text area](/object-types/ta) is focused and you press some letter on a keyboard, the keys will be sent and inserted into the Text area. 
Or if a [Slider](/object-types/slider) is focused and you press the left or right arrows the slider's value will be changed.

You need to associate an input device with a group. An input device can send the keys to only one group but a group can receive data from more than one input devices too.

To create a group use `lv_group_t g = lv_group_create()` and to add an object to the group use `lv_group_add_obj(g, obj)`.

The associate a group with an input device use `lv_indev_set_group(indev, g)`, where `indev` is the return value of `lv_indev_drv_register()`

#### Keys
There are some predefined keys which have special meaning:
- **LV_KEY_NEXT** Focus on the next object
- **LV_KEY_PREV** Focus on the previous object
- **LV_KEY_ENTER** Triggers `LV_EVENT_PRESSED/CLICKED/LONG_PRESSED` etc events
- **LV_KEY_UP** Increase value or move upwards 
- **LV_KEY_DOWN** Decrease value or move downwards
- **LV_KEY_RIGHT** Increase value or move the the right
- **LV_KEY_LEFT** Decrease value or move the the left
- **LV_KEY_ESC**  Close or exit (E.g. close a [Drop down list](/object-types/ddlist))
- **LV_KEY_DEL**  Delete (E.g. a character on the right in a [Text area](/object-types/ta))
- **LV_KEY_BACKSPACE** Delete a character on the left (E.g. in a [Text area](/object-types/ta))
- **LV_KEY_HOME** Go to the beginning/top (E.g. in a [Text area](/object-types/ta))
- **LV_KEY_END** Go to the end (E.g. in a [Text area](/object-types/ta)))

The most important special keys are: `LV_KEY_NEXT/PREV`, `LV_KEY_ENTER` and `LV_KEY_UP/DOWN/LEFT/RIGHT`. 
In your `read_cb` function you should translate some of your keys to these special keys to navigate in the group and interact with the selected object.

Usually, it's enough to use only `LV_KEY_LEFT/RIGHT` because most of the objects can be fully controlled with them. 

With an encoder, you should use only `LV_KEY_LEFT`, `LV_KEY_RIGHT` and `LV_KEY_ENTER`. 

#### Edit and navigate mode

With keypads, there are plenty of keys so it's easy to navigate among the objects and edit them. However, the encoders have a very limited number of "keys". To effectively support encoders too *Navigate* and *Edit* is created.

In *Navigate* mode the encoders `LV_KEY_LEFT/RIGHT` is translated to `LV_KEY_NEXT/PREV`. Therefore the next or previous object will be selected by turning the encoder.
Pressing `LV_KEY_ENTER` will change to *Edit* mode.

In *Edit* mode `LV_KEY_NEXT/PREV` is used normally to edit the object.
Depending on the object's type a short or long press of `LV_KEY_ENTER` changes back to *Navigate* mode. 
Usually object which can not be pressed (like a [Slider](/object-types/slider)) leaves *Edit* mode on short click but with object where short click has meaning (e.g. [Button](/object-types/btn)) long press is required.

#### Styling the focused object
To visually highlight the focused element its [Main style](/overview/style#use-the-styles) will be updated. 
By default, some orange color is mixed to the original colors of the style. 
A new style modifier callback be set by `lv_group_set_style_mod_cb(g, my_style_mod_cb)`. A style modifier callback receives a pointer to a caller group and pointer to a style to modify. 
The default style modifier looks like this (slightly simplified):
```c
static void default_style_mod_cb(lv_group_t * group, lv_style_t * style)
{
    /*Make the bodies a little bit orange*/
    style->body.border.opa   = LV_OPA_COVER;
    style->body.border.color = LV_COLOR_ORANGE;
    style->body.border.width = LV_DPI / 20;

    style->body.main_color   = lv_color_mix(style->body.main_color, LV_COLOR_ORANGE, LV_OPA_70);
    style->body.grad_color   = lv_color_mix(style->body.grad_color, LV_COLOR_ORANGE, LV_OPA_70);
    style->body.shadow.color = lv_color_mix(style->body.shadow.color, LV_COLOR_ORANGE, LV_OPA_60);

    /*Recolor text*/
    style->text.color = lv_color_mix(style->text.color, LV_COLOR_ORANGE, LV_OPA_70);

    /*Add some recolor to the images*/
    if(style->image.intense < LV_OPA_MIN) {
        style->image.color = LV_COLOR_ORANGE;
        style->image.intense = LV_OPA_40;
    }
}
```

This style modifier callback is used for keypads and encoder in *Navigate* mode. 
For the *Edit* mode and other callback is used which can be set with `lv_group_set_style_mod_edit_cb()`. By default, it has a greenish color.


### Live demo

Try this [Live demo](https://littlevgl.com/demo-touchpadless) to see how a group and touchpad-less navigation works in the practice.

## API


### Input device

```eval_rst

.. doxygenfile:: lv_indev.h
  :project: lvgl
        
```

### Groups

```eval_rst

.. doxygenfile:: lv_group.h
  :project: lvgl
        
```


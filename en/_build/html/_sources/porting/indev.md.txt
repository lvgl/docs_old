# Input device interface

To set up an input device an `lv_indev_drv_t` variable has to be initialized:

```c
lv_indev_drv_t indev_drv;
lv_indev_drv_init(&indev_drv);      /*Basic initialization*/
indev_drv.type =...                 /*See below.*/
indev_drv.read_cb =...              /*See below.*/
/*Register the driver in LittlevGL and save the created input device object*/
lv_indev_t * my_indev = lv_indev_drv_register(&indev_drv);
```

**type** can be 
- **LV_INDEV_TYPE_POINTER** touchpad or mouse
- **LV_INDEV_TYPE_KEYPAD** keyboard or keypad
- **LV_INDEV_TYPE_ENCODER** encoder with left, right, push options
- **LV_INDEV_TYPE_BUTTON** external buttons pressing the screen
  
**read_cb** is a function pointer which will be called periodically to report the current state of an input device. 
It can also buffer data and return `false` when no more data to be read or `true` when the buffer is not empty.


Visit [Input devices](/overview/indev) to learn more about input devices in general.


##  Touchpad, mouse or any pointer
Input devices which are able to click points of the screen belong to this category. 

```c
indev_drv.type = LV_INDEV_TYPE_POINTER;
indev_drv.read_cb = my_input_read;

...

bool my_input_read(lv_indev_drv_t * drv, lv_indev_data_t*data)
{
    data->point.x = touchpad_x; 
    data->point.y = touchpad_y;
    data->state = LV_INDEV_STATE_PR or LV_INDEV_STATE_REL;
    return false; /*No buffering now so no more data read*/
}
```

``` important::  Touchpad drivers must return the last X/Y coordinates even when the state is *LV_INDEV_STATE_REL*.
```

To set a mouse cursor use `lv_indev_set_cursor(my_indev, &img_cursor)`. (`my_indev` is the return value of `lv_indev_drv_register`) 

## Keypad or keyboard 

Full keyboards with all the letters or simple keypads with a few navigation buttons belong here.

To use a keyboard/keypad:
- Register a `read_cb` function with `LV_INDEV_TYPE_KEYPAD` type.
- Enable `LV_USE_GROUP` in *lv_conf.h*
- An object group has to be created: `lv_group_t * g = lv_group_create()`  and objects have to be added to it with `lv_group_add_obj(g, obj)`
- The created group has to be assigned to an input device: `lv_indev_set_group(my_indev, g)` (`my_indev` is the return value of `lv_indev_drv_register`)
- Use `LV_KEY_...` to navigate among the objects in the group. See `lv_core/lv_group.h` for the available keys.

```c
indev_drv.type = LV_INDEV_TYPE_KEYPAD;
indev_drv.read_cb = my_input_read;

...

bool keyboard_read(lv_indev_drv_t * drv, lv_indev_data_t*data){
  data->key = last_key();            /*Get the last pressed or released key*/
  
  if(key_pressed()) data->state = LV_INDEV_STATE_PR;
  else data->state = LV_INDEV_STATE_REL;
  
  return false; /*No buffering now so no more data read*/
}
```

## Encoder 
With an encoder you can do 4 things:
1. Press its button
2. Long press its button
3. Turn left
4. Turn right

In short, the Encoder input devices work like this:
- By turning the encoder you can focus on the next/previous object. 
- When you press the encoder on a simple object (like a button), it will be clicked. 
- If you press the encoder on a complex object (like a list, message box, etc.) the object will go to edit mode where by turning the encoder you can navigate inside the object. 
- To leave edit mode press long the button.


To use an *Encoder* (similarly to the *Keypads*) the objects should be added to groups.


```c
indev_drv.type = LV_INDEV_TYPE_ENCODER;
indev_drv.read_cb = my_input_read;

... 
 
bool encoder_read(lv_indev_drv_t * drv, lv_indev_data_t*data){
  data->enc_diff = enc_get_new_moves();
  
  if(enc_pressed()) data->state = LV_INDEV_STATE_PR;
  else data->state = LV_INDEV_STATE_REL;
  
  return false; /*No buffering now so no more data read*/
}
```

## Button 
*Buttons* mean external "hardware" buttons next to the screen which are assigned to specific coordinates of the screen. 
If a button is pressed it will simulate the pressing on the assigned coordinate. (Similarly to a touchpad)

To assign buttons to coordinates use `lv_indev_set_button_points(my_indev, points_array)`.   
`points_array` should look like `const lv_point_t points_array[] =  { {12,30},{60,90}, ...}`

```c
indev_drv.type = LV_INDEV_TYPE_BUTTON;
indev_drv.read_cb = my_input_read;

...

bool button_read(lv_indev_drv_t * drv, lv_indev_data_t*data){
    static uint32_t last_btn = 0;   /*Store the last pressed button*/ 
    int btn_pr = my_btn_read();     /*Get the ID (0,1,2...) of the pressed button*/
    if(btn_pr >= 0) {               /*Is there a button press? (E.g. -1 indicated no button was pressed)*/
       last_btn = btn_pr;           /*Save the ID of the pressed button*/
       data->state = LV_INDEV_STATE_PR;  /*Set the pressed state*/
    } else {
       data->state = LV_INDEV_STATE_REL; /*Set the released state*/
    }
  
    data->btn = last_btn;            /*Save the last button*/
   
    return false;                    /*No buffering now so no more data read*/
}
```

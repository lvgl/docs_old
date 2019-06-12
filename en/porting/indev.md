# Input device interface

To set up an input device an **lv_indev_drv_t** variable has to be initialized:

```c
lv_indev_drv_t indev_drv;lv_indev_drv_init(&indev_drv);  /*Basic initialization*/
indev_drv.type =.../*See below.*/
indev_drv.read =.../*See below.*/
lv_indev_drv_register(&indev_drv);  /*Register the driver in LittlevGL*/
```

**type** can be 
- LV_INDEV_TYPE_POINTER: touchpad or mouse
- LV_INDEV_TYPE_KEYPAD: keyboard
- LV_INDEV_TYPE_ENCODER: left, right, push
- LV_INDEV_TYPE_BUTTON: external buttons pressing the screen
  
**read** is a function pointer which will be called periodically to report the current state of an input device. It can also buffer data and return _false_ when no more data to be read or _true_ when the buffer is not empty.

##  Touchpad, mouse or any pointer

```c
indev_drv.type = LV_INDEV_TYPE_POINTER;
indev_drv.read = my_input_read;
```

The read function should look like this:

```c
bool my_input_read(lv_indev_data_t*data)
{
    data->point.x = touchpad_x;   
    data->point.y = touchpad_y;
    data->state = LV_INDEV_STATE_PR or LV_INDEV_STATE_REL;
    return false; /*No buffering so no more data read*/
}
```

> **IMPORTANT NOTE:** Touchpad drivers must return the last X/Y coordinates even when the state is `LV_INDEV_STATE_REL`.

## Keypad or keyboard 
```c
indev_drv.type = LV_INDEV_TYPE_KEYPAD;
indev_drv.read = my_input_read;
```
The read function should look like this:
```c
bool keyboard_read(lv_indev_data_t*data){
  data->key = last_key();            /*Set the last pressed or released key*/
  if(key_pressed()){
    data->state = LV_INDEV_STATE_PR;
  }
  else{
    data->state = LV_INDEV_STATE_REL;
  }
  return false; /*No buffering so no more data read*/
}
```
To use a keyboard:
-  Register a _read_ function (like above) with _LV_INDEV_TYPE_KEYPAD_ type.
- _USE_LV_GROUP_ has to be enabled in _lv_conf.h_
-  An object group has to be created: _lv_group_create()_ and objects have to be added: _lv_group_add_obj()_
-  The created group has to be assigned to an input device: _lv_indev_set_group(my_indev, group1);_
-  Use _LV_GROUP_KEY_..._ to navigate among the objects in the group

Visit [Touchpad-less navigation](Input-devices) to learn more.

## Encoder 
With an encoder you can do 4 things:
1. press its button
2. long press its button
3. turn left
4. turn right

By turning the encoder you can focus on the next/previous object. When you press the encoder on a simple object (like a button), it will be clicked. If you press the encoder on a complex object (like a list, message box etc.) the object will go to edit mode where by turning the encoder you can navigate inside the object. To leave edit mode press long the button.

```c
indev_drv.type = LV_INDEV_TYPE_ENCODER;
indev_drv.read = my_input_read;
```
The read function should look like this:
```c
bool encoder_read(lv_indev_data_t*data){
  data->enc_diff = enc_get_new_moves();
  if(enc_pressed()){
    data->state = LV_INDEV_STATE_PR;
  }
  else{
    data->state = LV_INDEV_STATE_REL;
  }

  return false; /*No buffering so no more data read*/
}
```

- To use an `ENCODER`, similarly to the `KEYPAD`, the objects should be added to groups

## Button 
```c
indev_drv.type = LV_INDEV_TYPE_BUTTON;
indev_drv.read = my_input_read;
```
The read function should look like this:
```c
bool button_read(lv_indev_data_t*data){
    static uint32_t last_btn = 0;   /*Store the last pressed button*/ 
    int btn_pr = my_btn_read();     /*Get the ID (0,1,2...) of the pressed button*/
    if(btn_pr >= 0) {               /*Is there a button press?*/  
       last_btn = btn_pr;           /*Save the ID of the pressed button*/
       data->state = LV_INDEV_STATE_PR;  /*Set the pressed state*/
    } else {
       data->state = LV_INDEV_STATE_REL; /*Set the released state*/
    }
  
    data->btn = last_btn;            /*Set the last button*/         
   
    return false;                    /*No buffering so no more data read*/
}
```

- The buttons need to be assigned to pixels on the screen using `lv_indev_set_button_points(indev, points_array)`. Where _points_array_ look like `const lv_point_t points_array[] =  { {12,30},{60,90}, ...}`   


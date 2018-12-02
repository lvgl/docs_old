_Written for v5.1_

To interact with the created object _Input devices_ are required. For example Touchpad, Mouse, Keyboard or even an Encoder. To learn how to add an input device, read the [Porting guide](/Porting_tr). 

When you register an input device driver the library adds some extra information to it to describe the state of the input device in more detail. When a user action (e.g. a button press) happens and an action (callback) function is triggered always there is an input device which triggered that action. You can get this input device with 

```c
lv_indev_t *indev = lv_indev_get_act();
```

It might be important when you need to know some special information about the input device like the currently pressed point, or dragging an object or not etc.  

The input devices have a very simple API:

```c
/*Get the last point on a display input*/
void lv_indev_get_point(lv_indev_t * indev, point_t * point);

/*Check if there is dragging on input device or not */
bool lv_indev_is_dragging(lv_indev_t * indev);

/*Get the vector of dragging on a input device*/
void lv_indev_get_vect(lv_indev_t * indev, point_t * point);

/*Do nothing until the next release*/
void lv_indev_wait_release(lv_indev_t * indev);

/*Do nothing until the next release*/
void lv_indev_wait_release(lv_indev_t * indev);

/*Reset one or all (use NULL) input devices*/
void lv_indev_reset(lv_indev_t * indev);

/*Reset the long pressed state of an input device*/
void lv_indev_reset_lpr(lv_indev_t * indev);

/*Set a cursor for a pointer input device*/
void lv_indev_set_cursor(lv_indev_t * indev, lv_obj_t * cur_obj);

/*Set a destination group for a keypad input device*/
void lv_indev_set_group(lv_indev_t * indev, lv_group_t * group);
```

* * *

### Touchpad-less navigation

The objects can be grouped in order to easily **control** them **without touchpad or mouse**. It allows you to use

- Keyboard or keypad
- Hardware buttons
- Encoder

to navigate among objects.

Firstly you have to **create an object group** with `lv_group_t *group = lv_group_create()` and add objects to it with `lv_group_add_obj(group, obj)`. In a group always there is a _focused_ object. All the button press will be "sent" to the currently focused object. 

To navigate among the objects in a group (change the focused object) and interact with them an _LV_INDEV_TYPE_KEYPAD_ typed input device is required. In its _read_ function you can tell the library which key is pressed or released. To learn how to add an input device, read the [Porting guide](/Porting_tr). 

Besides you have to **assign the group to the input device** with  

```c
lv_indev_set_group(indev, group)
```

There are some special **control characters** which can be used in the _read_ function:

- **LV_GROUP_KEY_NEXT** Focus on the next object
- **LV_GROUP_KEY_PREV** Focus on the previous object
- **LV_GROUP_KEY_UP** Increment the value, move up or click the focused object (move up means e.g. select an upper list element)
- **LV_GROUP_KEY_DOWN** Decrement the value or move down on the focused object (move down means e.g. select a lower list element)
- **LV_GROUP_KEY_RIGHT** Increment the value or click the focused object
- **LV_GROUP_KEY_LEFT** Decrement the value of the focused object
- **LV_GROUP_KEY_ENTER** Click the focused object or a selected element (e.g. list element)
- **LV_GROUP_KEY_ESC** Close the object (e.g. drop-down list)

In some cases (e.g. when a pop-up window appears) it is useful to freeze the focus on an object. It means the _LV_GROUP_KEY_NEXT/PREV_ will be ignored. You can do it with `lv_group_focus_freeze(group,true)`.

The **style of the object in focus** is modified by a function. By default, it makes the object's colors orangish but you can also specify your own style updater function in each group with 

```c
void lv_group_set_style_mod_cb(group, style_mod_cb). 
```

The _style_mod_cb_ needs an `lv_style_t *` parameter which is a copy of the focused object's style. In the callback, you can mix some colors to the current ones, and modify parameters but **it is not permitted to set attributes which modify the size** (like _letter_space_, _padding_ etc.)

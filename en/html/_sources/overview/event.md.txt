```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/en/overview/event.md
```
# Events

In LittlevGL events are triggered if something happens which might be interesting to the user. For example an object
- is clicked
- is dragged
- its value has changed, etc.

The user can assign a callback function to an object to see these event. In the practice it looks like this:
```c
lv_obj_t * btn = lv_btn_create(lv_scr_act(), NULL);
lv_obj_set_event_cb(btn, my_event_cb);   /*Assign an event callback*/

...

static void my_event_cb(lv_obj_t * obj, lv_event_t event)
{
    switch(event) {
        case LV_EVENT_PRESSED:
            printf("Pressed\n");
            break;

        case LV_EVENT_SHORT_CLICKED:
            printf("Short clicked\n");
            break;

        case LV_EVENT_CLICKED:
            printf("Clicked\n");
            break;

        case LV_EVENT_LONG_PRESSED:
            printf("Long press\n");
            break;

        case LV_EVENT_LONG_PRESSED_REPEAT:
            printf("Long press repeat\n");
            break;

        case LV_EVENT_RELEASED:
            printf("Released\n");
            break;
    }

       /*Etc.*/
}
```

More objects can use the same *event callback*.

## Event types

The following event types exist:

### Generic events
Any object can receive these events independently from their type. I.e. these events are sent to Buttons, Labels, Sliders, etc.

#### Input device related
Sent when an object is pressed, released, etc by the user. They are used for *Keypad*, *Encoder* and *Button* input devices as well not only for *Pointers*. Visit the [Overview of input devices](/overview/indev) section to learn more about them.
- **LV_EVENT_PRESSED** The object has been pressed
- **LV_EVENT_PRESSING** The object is being pressed (sent continuously while pressing)
- **LV_EVENT_PRESS_LOST** Still pressing but slid from the objects
- **LV_EVENT_SHORT_CLICKED** Released before l`LV_INDEV_LONG_PRESS_TIME`. Not called if dragged.
- **LV_EVENT_LONG_PRESSED**  Pressing for `LV_INDEV_LONG_PRESS_TIME` time.  Not called if dragged.
- **LV_EVENT_LONG_PRESSED_REPEAT** Called after `LV_INDEV_LONG_PRESS_TIME` in every `LV_INDEV_LONG_PRESS_REP_TIME` ms.  Not called if dragged.
- **LV_EVENT_CLICKED** Called on release if not dragged (regardless to long press)
- **LV_EVENT_RELEASED**  Called in every case when the object has been released even if it was dragged. Not called if slid from the object while pressing and released outside of the object. In this case, `LV_EVENT_PRESS_LOST` is sent. 

#### Pointer related
These events are sent only by pointer-like input devices (E.g. mouse or touchpad)
- **LV_EVENT_DRAG_BEGIN** Dragging of the object has started
- **LV_EVENT_DRAG_END** Dragging finished (including drag throw)
- **LV_EVENT_DRAG_THROW_BEGIN** Drag throw started (released after drag with "momentum")
 
#### Keypad and encoder related
These events are sent by keypad and encoder input devices. Learn more about *Groups* in [overview/indev](Input devices) section.
- **LV_EVENT_KEY** A *Key* is sent to the object. Typically when it was pressed or repeated after a long press 
- **LV_EVENT_FOCUSED** The object is focused in its group
- **LV_EVENT_DEFOCUSED** The object is defocused in its group

#### General events
Other general events sent by the library.
- **LV_EVENT_DELETE** The object is being deleted. Free the related user-allocated data.

### Special events
These events are specific to a particular object type. 
- **LV_EVENT_VALUE_CHANGED** The object value has changed (e.g. for a [Slider](/object-types/slider))
- **LV_EVENT_INSERT** Something is inserted to the object. (Typically to a [Text area](/object-types/ta))
- **LV_EVENT_APPLY**  "Ok", "Apply" or similar specific button has clicked. (Typically from a [Keyboard](/object-types/kb) object)
- **LV_EVENT_CANCEL** "Close", "Cancel" or similar specific button has clicked. (Typically from a [Keyboard](/object-types/kb) object)
- **LV_EVENT_REFRESH** Query to refresh the object. Never sent by the library but can be sent by the user.

To see exactly which events are used by an object type see the particular [Object type's documentation](/object-types/index).

## Custom data
Some events might contain custom data. For example `LV_EVENT_VALUE_CHANGED` in some cases tells the new value. For more info see the particular [Object type's documentation](/object-types/index).
To get the custom data in the event callback use `lv_event_get_data()`.

The type of the custom data depends on the sending object but if its a 
- single number then it's `uint32_t *` or `int32_t *`
- text then `char * ` or `const char *`


## Send events manually

To manually send events to an object use `lv_event_send(obj, LV_EVENT_..., &custom_data)`. 

It can be used for example to manually close a message box by simulating a button press:
```c
/*Simulate the press of the first button (indexes start from zero)*/
uint32_t btn_id = 0;
lv_event_send(mbox, LV_EVENT_VALUE_CHANGED, &btn_id);
```

Or to ask refresh in a generic way.
```c
lv_event_send(label, LV_EVENT_REFRESH, NULL);
```

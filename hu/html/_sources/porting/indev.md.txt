```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/hu/porting/indev.md
```
# Bemeneti eszköz interfész

## A bementi eszközök típusai

Egy bementi eszköz létrehozásához egy `lv_indev_drv_t` változót kell inicializálni:

```c
lv_indev_drv_t indev_drv;
lv_indev_drv_init(&indev_drv);      /*Alap inicializálás*/
indev_drv.type =...                 /*Lásd lent.*/
indev_drv.read_cb =...              /*Lásd lent.*/
/*A driver regisztrálása a LittlevGL-ben és a létrehozott bemeneti eszköz elmentése*/
lv_indev_t * my_indev = lv_indev_drv_register(&indev_drv);
```

**type** mező lehet: 
- **LV_INDEV_TYPE_POINTER** touchpad és egér
- **LV_INDEV_TYPE_KEYPAD** billentyűzet or keypad
- **LV_INDEV_TYPE_ENCODER** enkóder bal, jobb és gomb nyomás funkciókkal
- **LV_INDEV_TYPE_BUTTON** küldő gomb ami képernyőt nyomja
  
**read_cb** egy függvény, ami periodikusan meghívódik, hogy jelentse a bemeneti eszköz állapotát.
A függvény bufferel-het adatokat és `false`-sal térhet vissza, ha nincs több, `true`-val, ha még van adat a bufferben.


Több információ a [Bementi eszközök](/overview/indev) áttekintése fejezetben olvasható.


###  Touchpad, egér vagy más mutató eszköz
Azok a bemeneti eszközök tartoznak ebbe a kategóriába, melyek képesek egy pontra kattintani a képernyőn  .

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

``` important::  A touchpad driver-eknek az utolsó megnyomott  X/Y koordinátával kell visszatérni  *LV_INDEV_STATE_REL* állapotban.
```

Egér kurzor megjelenítéséhez a `lv_indev_set_cursor(my_indev, &img_cursor)` függvény használható. (`my_indev` `lv_indev_drv_register` visszatérési értéke) 

### Billentyűzet vagy keypad

Teljes értékű billentyűzetek minden karakterrel vagy egyszerű keypad-ok néhány navigációs gombbal tartoznak ide.

A billentyűzet/keypad használatához:
- `read_cb` regisztrálása `LV_INDEV_TYPE_KEYPAD` típussal.
- `LV_USE_GROUP` engedélyezése *lv_conf.h*-ban
- Egy objektum *group* (csoport) létrehozása: `lv_group_t * g = lv_group_create()`  és objektumok a csoporthoz adása a  `lv_group_add_obj(g, obj)` függvénnyel.
- A létrehozott *group* bemeneti eszközhöz rendelése: `lv_indev_set_group(my_indev, g)` (`my_indev` `lv_indev_drv_register` visszatérési értéke)
- Néhány gombok `LV_KEY_...` értékre konvertálása az objektumok közötti navigációhoz. A vezérlő gombok teljes listája `lv_core/lv_group.h`-ban látható.

```c
indev_drv.type = LV_INDEV_TYPE_KEYPAD;
indev_drv.read_cb = my_input_read;

...

bool keyboard_read(lv_indev_drv_t * drv, lv_indev_data_t*data){
  data->key = last_key();            /*Az utolsó lenyomott vagy felengedett gomb lekérdezése*/
  
  if(key_pressed()) data->state = LV_INDEV_STATE_PR;
  else data->state = LV_INDEV_STATE_REL;
  
  return false; /*Nincs bufferelés*/
}
```

### Encoder 
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
  
  return false; /*Nincs bufferelés*/
}
```

### Button 
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

## Other features

Besides `read_cb` a `feedback_cb` callback can be also specified in `lv_indev_drv_t`. 
`feedback_cb` is called when any type of event is sent by the input devices. (independently from its type). It gives the opportunity to make feedback for the user e.g. to play a sound on `LV_EVENT_CLICK`.

The default value of the following parameters can be set in *lv_conf.h* but the default value can be overwritten in `lv_indev_drv_t`:
- **drag_limit** Number of pixels to slide before actually drag the object
- **drag_throw**  Drag throw slow-down in [%]. Greater value means faster slow-down
- **long_press_time** Press time to send `LV_EVENT_LONG_PRESSED` (in milliseconds)
- **long_press_rep_time** Interval of sending `LV_EVENT_LONG_PRESSED_REPEAT` (in milliseconds)
- **read_task** pointer to the `lv_task` which reads the input device. It parameters can be changed by `lv_task_...()` functions 


Every Input device is associated with a display. By default, a new input device is added to the lastly created or the explicitly selected (using `lv_disp_set_default()`) display. 
The associated display is stored and can be changed in `disp` field of the driver.


## API 

```eval_rst

.. doxygenfile:: lv_hal_indev.h
  :project: lvgl
        
```

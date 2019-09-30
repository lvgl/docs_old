```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/en/overview/layer.md
```

# Layers

## Order of creation

By default, LittlevGL draw old objects on the background and new objects on the foreground.

For example, assume we added a layer by creating the first object named as button1 and second object as button2. Then the button1(with related objects on it) will be in the background and can be covered by the button2 and its children.


![](/misc/layers.png "Creating graphical objects in Littlev Graphics Library")  

```c
/*Create a screen*/
lv_obj_t * scr = lv_obj_create(NULL, NULL);
lv_scr_load(scr);          /*Load the screen*/

/*Create 2 buttons*/
lv_obj_t * btn1 = lv_btn_create(scr, NULL);         /*Create a button on the screen*/
lv_btn_set_fit(btn1, true, true);                   /*Enable to automatically set the size according to the content*/
lv_obj_set_pos(btn1, 60, 40);              	   /*Set the position of the button*/

lv_obj_t * btn2 = lv_btn_create(scr, btn1);         /*Copy the first button*/
lv_obj_set_pos(btn2, 180, 80);                    /*Set the position of the button*/

/*Add labels to the buttons*/
lv_obj_t * label1 = lv_label_create(btn1, NULL);	/*Create a label on the first button*/
lv_label_set_text(label1, "Button 1");          	/*Set the text of the label*/

lv_obj_t * label2 = lv_label_create(btn2, NULL);  	/*Create a label on the second button*/
lv_label_set_text(label2, "Button 2");            	/*Set the text of the label*/

/*Delete the second label*/
lv_obj_del(label2);
```

## Bring to the foreground

There are several ways to bring an object to the foreground:
- Use `lv_obj_set_top(obj, true)`. If `obj` or any of its children is clicked, then LittlevGL will automatically bring the object to the foreground.
It works similarly to the Windows on PC. When a window in the background is clicked, it will come to the foreground automatically.
- Use `lv_obj_move_foreground(obj)` to explicitly tell the library to bring an object to the foreground. Similarly, use `lv_obj_move_background(obj)` to move to the background.
- When `lv_obj_set_parent(obj, new_parent)` is used, `obj` will be on the foreground on the `new_parent`.


## Top and sys layer

LittlevGL uses two special layers named as `layer_top` and `layer_sys`.
Both are visible and common on all screens of a display. The `layer_top` is used to place on top of "normal screen" and `layer_sys` is on top of `layer_top`.

The `layer_top` can be used by the user to create some content visible everywhere. For example, a menu bar, a pop-up, etc. If the `click` attribute is enabled, then `layer_top` will absorb all user click and acts as a modal.
```c
lv_obj_set_click(lv_layer_top(), true);
```

The `layer_sys` is also using for similar purpose on LittlevGL. For example, it places the mouse cursor there to be sure it's always visible.

```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/hu/overview/layer.md
```

# Layers

## Order of creation

The earlier created object (and its children) will be drawn earlier (nearer to the background). In other words, the lastly created object will be on the top among its siblings. 
It is very important, the order is calculated among the objects on the same level ("siblings").

Layers can be added easily by creating 2 objects (which can be transparent). Firstly 'A' and secondly 'B'. 'A' and every object on it will be in the background and can be covered by 'B' and its children.

  
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
- Use `lv_obj_set_top(obj, true)`. If `obj` or any of its children is clicked then LittlevGL will automatically bring the object to the foreground. 
It works similarly to the windows on PC. When a window in the background is clicked it will come to the foreground automatically.
- Use `lv_obj_move_foreground(obj)` and `lv_obj_move_background(obj)` to explicitly tell the library to bring an object to the foreground or move to the background.
- When `lv_obj_set_parent(obj, new_parent)` is used `obj` will be on the foreground on the new parent.


## Top and sys layer

There are two special layers called `layer_top` and `layer_sys`. 
Both of them is visible and the same on all screens of a display. `layer_top` is on top of "normal screen" and `layer_sys` is on top of `layer_top` too.

`layer_top` can be used by the user to create some content visible everywhere. For example a menu bar, a pop-up, etc. If the `click` attribute is enabled then `layer_top` will absorb all user click and acts as a modal.
```c
lv_obj_set_click(lv_layer_top(), true);
``` 

`layer_sys` is used by LittlevGL. For example, it places the mouse cursor there to be sure it's always visible. 

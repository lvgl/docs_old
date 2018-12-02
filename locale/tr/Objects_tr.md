_Written for v5.1_

In the Littlev Graphics Library the **basic building blocks** of a user interface are the objects. For example:

- [Button](/Button_tr)
- [Label](/Label_tr)
- [Image](/Image_tr)
- [List](/List_tr)
- [Chart](/Chart_tr)
- [Text area](/Text-area_tr)

Click to check all the existing [Object types](Object-types_tr)

#### Object attributes

##### Basic attributes

The objects have basic attributes which are common independently from their type:

- Position
- Size
- Parent
- Drag enable
- Click enable etc.

You can set/get this attributes with `lv_obj_set_...` and `lv_obj_get_...` functions. For example:

```c
/*Set basic object attributes*/
lv_obj_set_size(btn1, 100, 50);						/*Button size*/
lv_obj_set_pos(btn1, 20,30);						/*Button position*/
```

To see all the available functions visit the Base object's [documentation](/Base-object_tr).

##### Specific attributes

The object types have special attributes. For example a slider have:

- Min. max. values
- Current value
- Callback function for new value set 
- Styles

For these attributes every object type have unique API functions. For example for a slider: 

```c
/*Set slider specific attributes*/
lv_slider_set_range(slider1, 0, 100);			/*Set min. and max. values*/
lv_slider_set_value(slider1, 40);			/*Set the current value (position)*/
lv_slider_set_action(slider1, my_action);		/*Set a callback function*/
```

#### Object's working mechanisms

##### Parent-child structure

A parent can be considered as the container of its children. Every object has exactly one parent object (except screens) but a parent can have unlimited number of children. There is no limitation for the type of the parent but there typically parent (e.g. button) and typical child (e.g. label) objects.

##### Screen – the most basic parent

The screen is a special object which has no parent object. Always there is an active screen. By default, the library creates and loads one. To get the currently active screen use the `lv_scr_act()` function.

A screen can be created with any object type, for example, a basic object or an image to make a wallpaper.

##### Moving together

If the position of the parent is changed the children will move with the parent. Therefore all positions are relative to the parent. So the (0;0) coordinates mean the objects will remain in the top left-hand corner of the parent independently from the position of the parent.

![Objects are moving together 1](https://littlevgl.com/docs/par_child1.png)  

```c
lv_obj_t * par = lv_obj_create(lv_scr_act(), NULL); 	/*Create a parent object on the current screen*/
lv_obj_set_size(par, 100, 80);		                /*Set the size of the parent*/

lv_obj_t * obj1 = lv_obj_create(par, NULL);	        /*Create an object on the previously created parent object*/
lv_obj_set_pos(obj1, 10, 10);			        /*Set the position of the new object*/
```

Modify the position of the parent:
  
![Graphical objects are moving togother 2](https://littlevgl.com/docs/par_child2.png)  

```c
lv_obj_set_pos(par, 50, 50);		/*Move the parent. The child will move with it.*/
```

##### Visibility only on parent

If a child partially or totally out of its parent then the parts outside will not be visible.
  
![A graphical object is visible on its parent](https://littlevgl.com/docs/par_child3.png)  

```c
lv_obj_set_x(obj1, -30);		/*Move the child a little bit of the parent*/
```

#### Create - delete objects

In the graphics library objects can be created and deleted dynamically in run-time. It means only the currently created objects consume RAM. For example, if you need a chart you can create it only when it is required and delete after it is used.

Every objects type has its own **create** function with an unified prototype. It needs two parameters: a pointer the parent object and optionally a pointer to an other object with the same type. If the second parameter is not _NULL_ then this objects will be copied to the new one. To create a screen give _NULL_ as parent. The return value of the create function is a pointer to the created object. Independently from the object type a common variable type **lv_obj_t** is used. This pointer can be used later to set or get the attributes of the object. The create functions look like this:

```c
lv_obj_t * lv_type_create(lv_obj_t * parent, lv_obj_t * copy);
```

There is a common **delete** function for all object types. It deletes the object and all of its children.

```c
void lv_obj_del(lv_obj_t * obj);
```

You can delete only the children of an object but leave the object itself "alive":

```c
void lv_obj_clean(lv_obj_t * obj);
```

#### Layers

The earlier created object (and its children) will be drawn earlier (nearer to the background). In other words, the lastly created object will be on the top among its siblings. It is very important, the order is calculated among the objects on the same level ("siblings").

Layers can be added easily by creating 2 objects (which can be transparent) firstly 'A' and secondly 'B'. 'A' and every object on it will be in the background and can be covered by 'B' and its children.

  
![Creating graphical objects in Littlev Graphics Library](https://littlevgl.com/docs/par_child4.png)  

```c
/*Create a screen*/
lv_obj_t * scr = lv_obj_create(NULL, NULL);
lv_scr_load(scr);       						    /*Load the screen*/

/*Create 2 buttons*/
lv_obj_t * btn1 = lv_btn_create(scr, NULL);         /*Create a button on the screen*/
lv_btn_set_fit(btn1, true, true);                   /*Enable to automatically set the size according to the content*/
lv_obj_set_pos(btn1, 60, 40);              		    /*Set the position of the button*/

lv_obj_t * btn2 = lv_btn_create(scr, btn1);         /*Copy the first button*/
lv_obj_set_pos(btn2, 180, 80);                 	    /*Set the position of the button*/

/*Add labels to the buttons*/
lv_obj_t * label1 = lv_label_create(btn1, NULL);	/*Create a label on the first button*/
lv_label_set_text(label1, "Button 1");          	/*Set the text of the label*/

lv_obj_t * label2 = lv_label_create(btn2, NULL);  	/*Create a label on the second button*/
lv_label_set_text(label2, "Button 2");            	/*Set the text of the label*/

/*Delete the second label*/
lv_obj_del(label2);
```

```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/en/overview/object.md
```
# Objects

In the LittlevGL the **basic building blocks** of a user interface are the objects, also called *Widgets*.
For example a [Button](/object-types/btn), [Label](/object-types/label), [Image](/object-types/img), [List](/object-types/list), [Chart](/object-types/chart) or [Text area](/object-types/ta).

Check all the [Object types](/object-types/index) here.

## Object attributes

### Basic attributes

All object types share some basic attributes:
- Position
- Size
- Parent
- Drag enable
- Click enable etc.

You can set/get these attributes with `lv_obj_set_...` and `lv_obj_get_...` functions. For example:

```c
/*Set basic object attributes*/
lv_obj_set_size(btn1, 100, 50);	 /*Button size*/
lv_obj_set_pos(btn1, 20,30);      /*Button position*/
```

To see all the available functions visit the Base object's [documentation](/object-types/obj).

### Specific attributes

The object types have special attributes too. For example, a slider has
- Min. max. values
- Current value
- Custom styles

For these attributes, every object type have unique API functions. For example for a slider:

```c
/*Set slider specific attributes*/
lv_slider_set_range(slider1, 0, 100);	   /*Set min. and max. values*/
lv_slider_set_value(slider1, 40, LV_ANIM_ON);	/*Set the current value (position)*/
lv_slider_set_action(slider1, my_action);     /*Set a callback function*/
```

The API of the object types are described in their [Documentation](/object-types/index) but you can also check the respective header files (e.g. *lv_objx/lv_slider.h*)

## Object's working mechanisms

### Parent-child structure

A parent object can be considered as the container of its children. Every object has exactly one parent object (except screens), but a parent can have an unlimited number of children.
There is no limitation for the type of the parent but, there are typical parent (e.g. button) and typical child (e.g. label) objects.

### Moving together

If the position of the parent is changed the children will move with the parent.
Therefore all positions are relative to the parent.

The (0;0) coordinates mean the objects will remain in the top left-hand corner of the parent independently from the position of the parent.

![](/misc/par_child1.png "Objects are moving together 1")

```c
lv_obj_t * par = lv_obj_create(lv_scr_act(), NULL); /*Create a parent object on the current screen*/
lv_obj_set_size(par, 100, 80);	                   /*Set the size of the parent*/

lv_obj_t * obj1 = lv_obj_create(par, NULL);	         /*Create an object on the previously created parent object*/
lv_obj_set_pos(obj1, 10, 10);	                   /*Set the position of the new object*/
```

Modify the position of the parent:

![](/misc/par_child2.png "Graphical objects are moving together 2")  

```c
lv_obj_set_pos(par, 50, 50);	/*Move the parent. The child will move with it.*/
```

(For simplicity the adjusting of colors of the objects is not shown in the example.)

### Visibility only on the parent

If a child is partially or fully out of its parent then the parts outside will not be visible.

![](/misc/par_child3.png "A graphical object is visible on its parent")  

```c
lv_obj_set_x(obj1, -30);	/*Move the child a little bit of the parent*/
```

### Create - delete objects

In LittlevGL objects can be created and deleted dynamically in run-time.
It means only the currently created objects consume RAM.
For example, if you need a chart, you can create it when required and delete it when it is not visible or necessary.

Every object type has its own **create** function with a unified prototype.
It needs two parameters:
- A pointer to the *parent* object. To create a screen give *NULL* as parent.
- Optionally, a pointer to *copy* object with the same type to copy it. This *copy* object can be *NULL* to avoid the copy operation.

All objects are referenced in C code using an `lv_obj_t` pointer as a handle. This pointer can later be used to set or get the attributes of the object.

The create functions look like this:

```c
lv_obj_t * lv_ <type>_create(lv_obj_t * parent, lv_obj_t * copy);
```

There is a common **delete** function for all object types. It deletes the object and all of its children.

```c
void lv_obj_del(lv_obj_t * obj);
```

`lv_obj_del` will delete the object immediately.
If for any reason you can't delete the object immediately you can use `lv_obj_del_async(obj)`.
It is useful e.g. if you want to delete the parent of an object in the child's `LV_EVENT_DELETE` signal.

You can remove all the children of an object (but not the object itself) using `lv_obj_clean`:

```c
void lv_obj_clean(lv_obj_t * obj);
```

### Screen – the most basic parent

The screens are special objects which have no parent object. So it is created like:
```c
lv_obj_t * scr1 = lv_obj_create(NULL, NULL);
```

There is always an active screen on each display. By default, the library creates and loads a "Base object" as the screen for each display.  
To get the currently active screen use the `lv_scr_act()` function. To load a new one, use `lv_scr_load(scr1)`.

Screens can be created with any object type. For example, a [Base object](/object-types/obj) or an image to make a wallpaper.


Screens are created on the currently selected *default display*.
The *default screen* is the last registered screen with `lv_disp_drv_register` or you can explicitly select a new default display using `lv_disp_set_default(disp)`.
`lv_scr_act()` and `lv_scr_load()` operate on the currently default screen.

Visit [Multi-display support](/overview/display) to learn more.

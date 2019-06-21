# Tile view (lv_tileview)

## Overview

The tileview a container obejct where its elements (called *tiles*) can be arranged in a grid form. By swiping the user can navigate between the tiles. 

If the Tileview is screen sized it gives a ueser inteface you might have seen on the smartwatches.

### Valid positons

The tiles don't has to form a full grid where every element exists. There can be holes in the grid but it has to continiuous, i.e. there can the be an emty row or culomn. 

With `lv_tileview_set_valid_positions(tileview, valid_pos_array, array_len)`the valid positions can be set. Scrolling will be possible only to this positions. the `0,0` index means the top left tile. 
E.g. `lv_point_t * valid_pos_array = {{0,0}, {0,1}, {1,1}, {{LV_COORD_MIN, LV_COORD_MIN}}` gives a Tile view with "L" shape. It idicates that there is no tile in `{1,1}` threfore the user can't scroll there.


In other words the `valid_pos_array` tells where the tiles are. It can be changed on the fly to the disable some positions on specific tiles. 
For example there can be a 2x2 grid where all tiles are added but the first row (y = 0) is a main row and the second row (y = 1) contains options for the tile above it. 
Let's say horizontal scrolling is possible only in the main row and bot possible between the option in the second row. In this case the `valid_pos_array` needs to changed when a new main tile is selected:
- for the first main tile: `{0,0}, {0,1}, {1,0}` to disable the `{1,1}` option tile
- for the second main tile `{0,0}, {1,0}, {1,1}` to disable the `{0,1}` option tile

### Add element

To add elements just craete an obejct on the Tileview and call `lv_tileview_add_element(tielview, element)`. 

The element should have the same size then the Tile view and needs to be positioned manually to the desired position.

The scroll propagation feature of page-like objects (like [List](/object-types/list)) can be used very well here. 
For example there can be a full sized List and when it reaches the top or bottom most position the user will scroll the tile view instead.

If you want other objects then the tile's container to scroll the Tile view when they are dragged thes also needs to be added with `lv_tileview_add_element`. 
For example if there is button on a tile, the button needs to be explictily added to the Tile view to enable the user scroll the tilview with the button too.

It true for the buttons on a List as well. Every list button needs to be added with `lv_tileview_add_element`.

### Set tile

To set the currently visibel tile use `lv_tileview_set_tile_act(tileview, x_id, y_id, LV_ANIM_ON/OFF)`. 

### Animation time

The animation time when a tile 
- is selected with `lv_tileview_set_tile_act`
- is scrolled a little and then released (revert the original tile)
- is scrolled more then a half size and  then release (move to the next tile)

can be set with `lv_tileview_set_anim_time(tileview, anim_time)`. 

### Edge flash

An "edge flash" effect can be added when the tile view reached hits an invalid position or the end of tile view when scrolled.

Use `lv_tileview_set_edge_flash(tileview, true)` to enable this feature.



## Styles
The tileview has on one style which van be changes with  `lv_tileview_set_style(slider, LV_TILEVIEW_STYLE_MAIN, &style)`.

- **LV_TILEVIEW_STYLE_MAIN** Style of the background. All `style.body` properties are used.

## Events
Besided the [Genreric events](/overview/event.html#generic-events) the following [Special events](/overview/event.html#special-events) are sent by the Slider:
- **LV_EVENT_VALUE_CHANGED** Sent when a new tile loaded either with scrolling or `lv_tileview_set_act`. The event data is set ti the index of the new tile in `valid_pos_array` (It's type is `uint32_t *`)

## Keys
- **LV_KEY_UP**, **LV_KEY_RIGHT** Increment the slider's value by 1
- **LV_KEY_DOWN**, **LV_KEY_LEFT** Decrement the slider's value by 1

Learn more about [Keys](/overview/indev).

## Example

### C

![](/examples/bar/bar_1.png "Slider in LittlevGL")

```eval_rst
.. container:: toggle

    .. container:: header
    
      code

    .. literalinclude:: /examples/slider/slider_1.c
      :language: c
 
```

### MicroPython
No examples yet.

## API 

```eval_rst

.. doxygenfile:: lv_tileview.h
  :project: lvgl
        
```


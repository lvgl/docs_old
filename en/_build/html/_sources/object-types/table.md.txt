# Table (lv_table)

## Overview

Table, as usual, are built from rows, columns and cells. You can add texts to the cells.

The Table object is very light weighted becasue onyl tehxt are stored. No real objects are created for cells but they are jst drwan on the fly.


### Rows and Columns

To set number of rows and colums use `lv_table_set_row_cnt(table, row_cnt)` and `lv_table_set_col_cnt(table, col_cnt)`

### Width and Height

The width of the colums can be set with `lv_table_set_col_width(table, col_id, width)`. The overall width of the Table object will be set to the sum of colum widths.

The height is calculated automatically from the cell styles (font, padding etc) and the number of rows.

### Set cell value

The cells can store on texts so need to convert numbers to text before displing them in a table.

`lv_table_set_cell_value(table, row, col, "Content")`. The text is saved by the table so it be even a local variable.

Line break can be used in the text like `"Value\n60.3"`.

### Align

The text alignment in cells can be adjuted individually with `lv_table_set_cell_align(table, row, col, LV_LABEL_ALIGN_LEFT/CENTER/RIGHT)`.

### Cell type

You can use 4 different cell types. Each has its owne style.

Cell types can be used to add difefrent style for example to:
- table header
- first column
- highlight a cell
- etc

The type can be selected with `lv_table_set_cell_type(table, row, col, type)` `type` can be 1, 2, 3 or 4.

### Merge cells

Cells can be merged horizontally with `lv_table_set_cell_merge_right(table, col, row, true)`. To merge more adjecent cells apply this function for each cell.


### Crop text

By deafult the the text are word wrapped to fit into the cells width and the cells height is set automatically. To isable this and keep the text as it is enable `lv_table_set_cell_crop(table, row, col, true)`.

### Scroll
The make the Table scrollable place it on a [Page](/object-types/page)

## Styles
  
Use `lv_table_set_style(page, LV_TABLE_STYLE_...,  &style)` to set a new style for an element of the page:

- **LV_PAGE_STYLE_BG** background's style which uses all `style.body` properties (default: `lv_style_plain_color`)
- **LV_PAGE_STYLE_CELL1/2/3/4** 4 for styles for the 4 cell types. All `style.body` properties are used. (default: `lv_style_plain`)

## Events
Only the [Genreric events](/overview/event.html#generic-events) are sent by the object type.

Learn more about [Events](/overview/event).

##Keys

No *Keys* are processed by the object type.

Learn more about [Keys](/overview/indev).

## Example

### C

![](/examples/table/table_1.png "Table obejct in LittlevGL")

```eval_rst
.. container:: toggle

    .. container:: header
    
      code

    .. literalinclude:: /examples/table/table_1.c
      :language: c
 
```

### MicroPython
No examples yet.

## API 

```eval_rst

.. doxygenfile:: lv_table.h
  :project: lvgl
        
```

```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/en/object-types/table.md
```
# Table (lv_table)

## Overview

Tables, as usual, are built from rows, columns, and cells containing texts.

The Table object is very light weighted because only the texts are stored. No real objects are created for cells but they are just drawn on the fly.

### Rows and Columns

To set number of rows and columns use `lv_table_set_row_cnt(table, row_cnt)` and `lv_table_set_col_cnt(table, col_cnt)`

### Width and Height

The width of the columns can be set with `lv_table_set_col_width(table, col_id, width)`. The overall width of the Table object will be set to the sum of columns widths.

The height is calculated automatically from the cell styles (font, padding etc) and the number of rows.

### Set cell value

The cells can store on texts so need to convert numbers to text before displaying them in a table.

`lv_table_set_cell_value(table, row, col, "Content")`. The text is saved by the table so it can be even a local variable.

Line break can be used in the text like `"Value\n60.3"`.

### Align

The text alignment in cells can be adjusted individually with `lv_table_set_cell_align(table, row, col, LV_LABEL_ALIGN_LEFT/CENTER/RIGHT)`.

### Cell type

You can use 4 different cell types. Each has its own style.

Cell types can be used to add different style for example to:
- table header
- first column
- highlight a cell
- etc

The type can be selected with `lv_table_set_cell_type(table, row, col, type)` `type` can be 1, 2, 3 or 4.

### Merge cells

Cells can be merged horizontally with `lv_table_set_cell_merge_right(table, col, row, true)`. To merge more adjacent cells apply this function for each cell.


### Crop text
By default, the texts are word-wrapped to fit into the width of the cell and the height of the cell is set automatically. To disable this and keep the text as it is enable `lv_table_set_cell_crop(table, row, col, true)`.

### Scroll
The make the Table scrollable place it on a [Page](/object-types/page)

## Styles
  
Use `lv_table_set_style(page, LV_TABLE_STYLE_...,  &style)` to set a new style for an element of the page:

- **LV_PAGE_STYLE_BG** background's style which uses all `style.body` properties (default: `lv_style_plain_color`)
- **LV_PAGE_STYLE_CELL1/2/3/4** 4 for styles for the 4 cell types. All `style.body` properties are used. (default: `lv_style_plain`)

## Events
Only the [Generic events](/overview/event.html#generic-events) are sent by the object type.

Learn more about [Events](/overview/event).

## Keys

No *Keys* are processed by the object type.

Learn more about [Keys](/overview/indev).

## Example

```eval_rst

.. include:: /lv_examples/src/lv_ex_table/index.rst

```

### MicroPython
No examples yet.

## API 

```eval_rst

.. doxygenfile:: lv_table.h
  :project: lvgl
        
```

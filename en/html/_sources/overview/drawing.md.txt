# Drawing

With LittlevGL you don't need to draw anything manually. Just create objects (like buttons and labels), move and change them and LittlevGL will refresh and redraw what is required.

However, it might be useful to have a basic understanding of how drawing happens in LittlevGL.

The basic concept is to not draw directly to screen but draw to an internal buffer first and then copy that buffer to screen when the rendering is ready. It has two main advantages:
1. **Avoids flickering** while layers of the UI are drawn. E.g. when drawing a *background + button + text* each "stage" would be visible for a short time.
2. **It's faster** because when pixels are redrawn multiple times (e.g. background + button + text) it's faster to modify a buffer in RAM and finally write one pixel once 
than read/write a display directly on each pixel access. (e.g. via a display controller with SPI interface).

## Buffering types

As you already might learn in the [Porting](/porting/display) section there are 3 types of buffering:
1. **One buffer** LittlevGL draws the content of the screen into a buffer and sends it to the display. The buffer can be smaller than the screen. In this case, the larger areas will be redrawn in multiple parts. If only small areas changes (e.g. button press) then only those areas will be refreshed.
2. **Two non-screen-sized buffers** having two buffers LittlevGL can draw into one buffer while the content of the other buffer is sent to display in the background.
DMA or other hardware should be used to transfer the data to the display to let the CPU draw meanwhile.
This way the rendering and refreshing of the display become parallel. Similarly to the *One buffer* LittlevGL will draw the display's content in chunks if the buffer is smaller than the area to refresh.
3. **Two screen-sized buffers**.
In contrast to *Two non-screen-sized buffers* LittlevGL will always provide the whole screen's content not only chunks. This way the driver can simply change the address of the frame buffer to the buffer received from LittlevGL.
Therefore this method works the best when the MCU has an LCD/TFT interface and the frame buffer is just a location in the RAM.

## Mechanism of screen refreshing

1. Something happens on the GUI which requires redrawing. E.g. a button has been pressed, a chart has been changed or an animation happened, etc.
2. LittlevGL saves the changed object's old and new area into a buffer, called *Invalid area buffer*. For optimization in some cases objects are not added to the buffer:
    - Hidden objects are not added
    - Objects completely out of their parent are not added
    - Areas out of the parent are cropped to the parent's area
    - The object on other screens are not added
3. In every `LV_DISP_DEF_REFR_PERIOD` (set in *lv_conf.h*):
    - LittlevGL checks the invalid areas and joins the adjacent or intersecting areas
    - Takes the first joined area if it's smaller the *display buffer* then simply draws the areas content to the *display buffer*. If the area doesn't fit into the buffer draw as many lines as possible to the *display buffer*. 
    - When the area is drawn call `flush_cb` from the display driver to refresh the display
    - If the area was larger than the buffer redraw the remaining parts too.
    - Do the same with all the joined areas.
 
While an area is redrawn the library searches the most top object which covers the area to redraw and starts to draw from that object. 
For example, if a button's label has changed the library will see that it's enough to draw the button under the text and it's not required to draw the background too. 
 
The difference between buffer types regarding the drawing mechanism is the following: 
1. **One buffer** LittlevGL needs to wait for `lv_disp_flush_ready()` (called at the end of `flush_cb`) before starting to redraw the next part.
2. **Two non-screen-sized buffers** LittlevGL can immediately draw to the second buffer when the first is sent to `flush_cb` because the flushing should be done by DMA (or similar hardware) in the background.
3. **Two screen-sized buffers** After calling `flush_cb` the first buffer if being displayed as frame buffer. Its content is copied to the second buffer and all the changes are drawn on top of it. 
 
 

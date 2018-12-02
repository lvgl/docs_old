_Written for v5.1_

In _LittlevGL_ you can think in graphical objects and don't care about how the drawing happens. You can set the size, position or any attribute of the object an the library will refresh the old (invalid) areas and redraw the new ones. However, you should know the basic drawing methods to know which one you should choose. 

### Buffered and unbuffered drawing

#### Unbuffered drawing

The unbuffered drawing puts the pixels directly to the display (frame buffer). Therefore during the drawing process, some flickering might be visible because firstly the background has to be drawn and then the objects on it. For this reason, this type is not suitable when scrolling, dragging and animations are used. On the other hand, it has the smallest memory footprint because no extra graphics buffer is required.   

To use unbuffered drawing set _LV_VDB_SIZE_ to 0 in _lv_conf.h_ and register the _disp_map_ and _disp_fill_functions. Here you can learn more about [Porting](/Porting_tr).

#### Buffered drawing

The buffered drawing is similar to double buffering when two screen sized buffers are used (one for rendering and an other to display the last ready frame). However, LittlevGL's buffered drawing algorithm uses only one frame buffer and a small graphical buffer called Virtual Display Buffer (VDB). For VDB size ~1/10 screen size is typically enough. For a 320 × 240 screen with 16-bit colors, it means only 15 kB extra RAM.   

With buffered drawing there is no flickering because the image is created firstly in the memory (VDB), therefore scrolling, dragging and animations can be used. In addition, it enables the use of other graphical effects like anti-aliasing, transparency (opacity) and shadows.   

To use buffered drawing set _LV_VDB_SIZE_ to &gt; LV_HOR_RES in _lv_conf.h_ and register a _disp_flush_ function. 

In buffered mode, you can use **double VDB** to parallelly execute rendering into one VDB and copying pixels to your frame buffer from an other. The copy should use DMA or other hardware acceleration to work in the background to let the CPU to do other things. In _lv_conf.h_ the _LV_VDB_DOUBLE 1_ enables this feature.

#### Buffered vs Unbuffered drawing

Keep in mind it's not sure that the unbuffered drawing is faster. During the rendering process, a pixel is overwritten multiple times (e.g. background, button, text are above each other). This way in unbuffered mode the library needs to access the external memory or display controller several times which is slower than writing/reading the internal RAM.

The following table summarizes the differences between the two drawing methods:

|               | Unbuffered drawing | Buffered drawing |
|---------------|--------------------|------------------|
|  Memory usage | No extra           | >~1/10 screen    |
| Quality       | Flickering         | Flawless         |
|  Antialiasing | Not supported      | Supported        |
| Transparency  | Not supported      | Supported        |
| Shadows       | Not supported      | Supported        |

### Anti-aliasing

In lv_conf.h you can enable the anti-aliasing with _LV_ANTIALIAS 1_. The anti-aliasing is supported only in buffered mode (LV_VDB_SIZE &gt; LV_HOR_RES). 

The anti-aliasing algorithm puts some translucent pixels (pixels with opacity) to make lines and curves (including corners with radius) smooth and even. Because it only puts some extra pixels anti-aliasing requires only a few extra computational power(~1,1x extra time compared to not anti-aliased configuration)

As described in [Font section](/Fonts_tr) the fonts can be anti-aliased by using a different font with higher bpp (Bit-Per-Pixel). This way the pixels of a font can be not only 0 or 1 but can be translucent. The supported bpp-s are 1, 2, 4 and 8. Keep in mind a font with higher bpp requires more ROM.

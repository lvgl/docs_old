/*Create label on the screen. By default it will inherit the style of the screen*/
lv_obj_t * title = lv_label_create(lv_scr_act(), NULL);
lv_label_set_text(title, "Title Label");
lv_obj_align(title, NULL, LV_ALIGN_IN_TOP_MID, 0, 20);  /*Align to the top*/

/*Create anew style*/
static lv_style_t style_txt;
lv_style_copy(&style_txt, &lv_style_plain);
style_txt.text.font = &lv_font_dejavu_40;
style_txt.text.letter_space = 2;
style_txt.text.line_space = 1;
style_txt.text.color = LV_COLOR_HEX(0x606060);

/*Create a new label*/
lv_obj_t * txt = lv_label_create(lv_scr_act(), NULL);
lv_obj_set_style(txt, &style_txt);                    /*Set the created style*/
lv_label_set_long_mode(txt, LV_LABEL_LONG_BREAK);     /*Break the long lines*/
lv_label_set_recolor(txt, true);                      /*Enable re-coloring by commands in the text*/
lv_label_set_align(txt, LV_LABEL_ALIGN_CENTER);       /*Center aligned lines*/
lv_label_set_text(txt, "Align lines to the middle\n\n"
                       "#000080 Re-color# #0000ff words of# #6666ff the text#\n\n"
                       "If a line become too long it can be automatically broken into multiple lines");
lv_obj_set_width(txt, 300);                           /*Set a width*/
lv_obj_align(txt, NULL, LV_ALIGN_CENTER, 0, 20);      /*Align to center*/

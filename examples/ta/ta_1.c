/*Create a scroll bar style*/
static lv_style_t style_sb;
lv_style_copy(&style_sb, &lv_style_plain);
style_sb.body.main_color = LV_COLOR_BLACK;
style_sb.body.grad_color = LV_COLOR_BLACK;
style_sb.body.border.color = LV_COLOR_WHITE;
style_sb.body.border.width = 1;
style_sb.body.border.opa = LV_OPA_70;
style_sb.body.radius = LV_RADIUS_CIRCLE;
style_sb.body.opa = LV_OPA_60;

/*Create a normal Text area*/
lv_obj_t * ta1 = lv_ta_create(lv_scr_act(), NULL);
lv_obj_set_size(ta1, 200, 100);
lv_obj_align(ta1, NULL, LV_ALIGN_CENTER, 0, - LV_DPI / 2);
lv_ta_set_style(ta1,LV_TA_STYLE_SB, &style_sb);                     /*Apply the scroll bar style*/
lv_ta_set_cursor_type(ta1, LV_CURSOR_BLOCK);
lv_ta_set_text(ta1, "A text in a Text Area\n"
               "You can scroll it if the text is long enough.");    /*Set an initial text*/
lv_ta_set_cursor_pos(ta1, 2);                                       /*Set the cursor position*/
lv_ta_add_text(ta1, "long ");                                       /*Insert a word at the current cursor position*/

static lv_style_t style_bg;
lv_style_copy(&style_bg, &lv_style_pretty);
style_bg.body.shadow.width = 8;
style_bg.text.color = LV_COLOR_MAKE(0x30, 0x60, 0xd0);              /*Blue label*/

/*Create a one lined test are with password mode*/
lv_obj_t * ta2 = lv_ta_create(lv_scr_act(), ta1);
lv_obj_align(ta2, ta1, LV_ALIGN_OUT_BOTTOM_MID, 0, 50);
lv_ta_set_style(ta2,LV_TA_STYLE_BG, &style_bg);                     /*Apply the background style*/
lv_ta_set_one_line(ta2, true);
lv_ta_set_cursor_type(ta2, LV_CURSOR_LINE);
lv_ta_set_pwd_mode(ta2, true);
lv_ta_set_text(ta2, "Password");

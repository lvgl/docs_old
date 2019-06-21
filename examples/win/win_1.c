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

/*Create a window*/
lv_obj_t * win = lv_win_create(lv_scr_act(), NULL);
lv_win_set_title(win, "Example window");                        /*Set the title*/
lv_win_set_style(win, LV_WIN_STYLE_SB, &style_sb);              /*Set the scroll bar style*/


/*Add control button to the header*/
lv_win_add_btn(win, SYMBOL_SETTINGS, my_setup_action);            /*Add a setup button*/
lv_win_add_btn(win, SYMBOL_CLOSE, lv_win_close_action);           /*Add close button and use built-in close action*/


/*Add some dummy content*/
lv_obj_t * txt = lv_label_create(win, NULL);
lv_label_set_text(txt, "This is the content of the window\n\n"
                       "You can add control buttons to\nthe window header\n\n"
                       "You can scroll it\n\n"
                       "See the scroll bar on the right!");

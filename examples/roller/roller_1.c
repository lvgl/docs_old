/*Create a default roller*/
lv_obj_t *roller1 = lv_roller_create(lv_scr_act(), NULL);
lv_roller_set_options(roller1, "Apple\n"
                               "Broccoli\n"
                               "Cabbage\n"
                               "Dewberry\n"
                               "Eggplant\n"
                               "Fig\n"
                               "Grapefruit");
lv_obj_set_pos(roller1, 50, 80);


/*Create styles*/
static lv_style_t bg_style;
lv_style_copy(&bg_style, &lv_style_pretty);
bg_style.body.main_color = LV_COLOR_WHITE;
bg_style.body.grad_color = LV_COLOR_HEX3(0xddd);
bg_style.body.border.width = 0;
bg_style.text.line_space = 20;
bg_style.text.opa = LV_OPA_40;

static lv_style_t sel_style;
lv_style_copy(&sel_style, &lv_style_pretty);
sel_style.body.empty = 1;
sel_style.body.radius = LV_RADIUS_CIRCLE;
sel_style.text.color = LV_COLOR_BLUE;

/*Create a roller and apply the new styles*/
lv_obj_t *roller2 = lv_roller_create(lv_scr_act(), NULL);
lv_roller_set_options(roller2, "0\n"
                               "1\n"
                               "2\n"
                               "3\n"
                               "4\n"
                               "5\n"
                               "6\n"
                               "7\n"
                               "8\n"
                               "9");
lv_roller_set_style(roller2, LV_ROLLER_STYLE_BG, &bg_style);
lv_roller_set_selected(roller2, 3, false);
lv_roller_set_style(roller2, LV_ROLLER_STYLE_SEL, &sel_style);
lv_roller_set_visible_row_count(roller2, 3);
lv_roller_set_hor_fit(roller2, false);
lv_obj_set_width(roller2, 40);
lv_obj_set_pos(roller2, 220, 50);

static void spinbox_value_changed(lv_obj_t * spinbox)
{

}

.
.
.
spinbox = lv_spinbox_create(lv_scr_act(), NULL);
lv_spinbox_set_style(spinbox, LV_SPINBOX_STYLE_BG, &spinBoxStyle);
lv_spinbox_set_style(spinbox, LV_SPINBOX_STYLE_CURSOR, &spinBoxCursorStyle);
lv_obj_set_size(spinbox, LV_HOR_RES, 80);
lv_obj_align(spinbox, NULL, LV_ALIGN_IN_TOP_LEFT, 4, 0);

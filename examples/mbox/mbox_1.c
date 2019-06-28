static const char * btns[] ={"Apply", "Close", ""};

lv_obj_t * mbox1 = lv_mbox_create(lv_scr_act(), NULL);
lv_mbox_set_text(mbox1, "A message box with two buttons.");
lv_mbox_add_btns(mbox1, btns);
lv_obj_set_width(mbox1, 200);
lv_obj_set_event_cb(mbox1, event_handler);
lv_obj_align(mbox1, NULL, LV_ALIGN_CENTER, 0, 0); /*Align to the corner*/

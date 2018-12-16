_Written for v5.1_

## Overview

The Tab view object can be used to **organize content in tabs**. You can **add a new tab** with `lv_tabview_add_tab(tabview, "Tab name")`. It will return with a pointer to a [Page](/Page_tr) object where you can add the tab's content.

To **select a tab** you can:

- Click on it on the header part
- Slide horizontally 
- Use `lv_tabview_set_tab_act(tabview, id, anim_en)` function

The **manual sliding** can be disabled with `lv_tabview_set_sliding(tabview, false)`.

The **animation time** is adjusted by `lv_tabview_set_anim_time(tabview, anim_time)`.

A **callback function** can be assigned to **tab load** event with `lv_tabview_set_tab_load_action(tabview, action)`. The callback function need to have the following prototype:

```c
void callback(lv_obj_t * tabview, uint16_t act_id);
```

Where _act_id_ means tab which will be loaded. In the action `lv_tabview_get_tab_act(tabview)` will give the id of the old tab.

## Style usage

Use `lv_tabview_set_style(tabview, LV_TABVIEW_STYLE_...,  &style)` to set a new style for an element of the tab view:

- **LV_TABVIEW_STYLE_BG** main background which uses all _style.body_ properties (default: lv_style_plain)
- **LV_TABVIEW_STYLE_INDIC** a thin rectangle on the top to indicate the current tab. Uses all _style.body_ properties. It height comes from _body.padding.inner_ (default: _lv_style_plain_color_)
- **LV_TABVIEW_STYLE_BTN_BG** style of the tab buttons' background. Uses all _style.body_ properties. The header height will be set automatically considering _body.padding.ver_ (default: _lv_style_transp_)
- **LV_TABVIEW_STYLE_BTN_REL** style of released tab buttons. Uses all _style.body_ properties.  (default: _lv_style_tbn_rel_)
- **LV_TABVIEW_STYLE_BTN_PR** style of released tab buttons. Uses all _style.body_ properties.  (default: _lv_style_tbn_rel_)
- **LV_TABVIEW_STYLE_BTN_TGL_REL** style of toggled released tab buttons. Uses all _style.body_ properties.  (default: _lv_style_tbn_rel_)
- **LV_TABVIEW_STYLE_BTN_TGL_PR** style of toggled pressed tab buttons. Uses all _style.body_ properties.  (default: _lv_style_btn_tgl_pr_)

## Notes

## Example
![Tabview image](http://docs.littlevgl.com/img/tab-view-lv_tabview.png)
```c
/*Create a Tab view object*/
lv_obj_t *tabview;
tabview = lv_tabview_create(lv_scr_act(), NULL);

/*Add 3 tabs (the tabs are page (lv_page) and can be scrolled*/
lv_obj_t *tab1 = lv_tabview_add_tab(tabview, "Tab 1");
lv_obj_t *tab2 = lv_tabview_add_tab(tabview, "Tab 2");
lv_obj_t *tab3 = lv_tabview_add_tab(tabview, "Tab 3");


/*Add content to the tabs*/
lv_obj_t * label = lv_label_create(tab1, NULL);
lv_label_set_text(label, "This the first tab\n\n"
                         "If the content\n"
                         "become too long\n"
                         "the tab become\n"
                         "scrollable\n\n");

label = lv_label_create(tab2, NULL);
lv_label_set_text(label, "Second tab");

label = lv_label_create(tab3, NULL);
lv_label_set_text(label, "Third tab");
```

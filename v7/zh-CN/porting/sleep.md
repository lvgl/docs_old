```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/zh-CN/porting/sleep.md
```
# 休眠管理

当没有用户输入时，MCU可以休眠。在这种情况下，main `while(1)` 应该是这样的:

```c
while(1) {
  /*Normal operation (no sleep) in < 1 sec inactivity*/
  if(lv_disp_get_inactive_time(NULL) < 1000) {
	  lv_task_handler();
  }
  /*Sleep after 1 sec inactivity*/
  else {
	  timer_stop();   /*Stop the timer where lv_tick_inc() is called*/
	  sleep();		    /*Sleep the MCU*/
  }
  my_delay_ms(5);
}
```

如果唤醒(按，触摸或点击等)发生，您还应该在您的输入设备中添加以下代码:
```c
lv_tick_inc(LV_DISP_DEF_REFR_PERIOD);  /*Force task execution on wake-up*/
timer_start();                         /*Restart the timer where lv_tick_inc() is called*/
lv_task_handler();                     /*Call `lv_task_handler()` manually to process the wake-up event*/
```

除了 ' lv__get_inactive_time() ' 之外，您还可以检查 ' lv_anim_count_running() '，看看是否每个动画都完成了。

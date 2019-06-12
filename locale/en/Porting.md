*Written for v6.0*

## System architecture




## Tick interface

The LittlevGL uses a system tick. Call the `lv_tick_inc(tick_period)` function periodically and tell the call period in milliseconds. For example if called in every milliseconds: `lv_tick_inc(1)`. 
It is required for LittlevGL to know the elapsed time. Therefore `lv_tick_inc` should be called in a higher priority then `lv_task_handler()`, for example in an interrupt.

## Task handling

To handle the tasks of LittlevGL you need to call `lv_task_handler()` periodically in one of the followings:
- *while(1)* of *main()* function 
- timer interrupt periodically (low priority then `lv_tick_inc()`)
- an OS task periodically

The timing is not critical but it should be about 5 milliseconds to keep the system responsive.

Example:
```c
while(1) {
  lv_task_handler();
  my_delay_ms(5);
}
```
## Handling sleep
The MCU can go to **sleep** when no user input happens. In this case the main `while(1)` should look like this:

```c
while(1) {
  /*Normal operation in < 1 sec inactivity*/ 
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

You should also add these lines to your input device read function if a press happens:
```c
lv_tick_inc(LV_REFR_PERIOD);  /*Force task execution on wake-up*/
timer_start();                /*Restart the timer where lv_tick_inc() is called*/
lv_task_handler();            /*Call `lv_task_handler()` manually to process the press event*/
``` 

In addition to `lv_disp_get_inactive_time()` you can check `lv_anim_count_running()` to see if every animations are finished.


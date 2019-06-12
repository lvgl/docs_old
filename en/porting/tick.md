# Tick interface

The LittlevGL uses a system tick. Call the `lv_tick_inc(tick_period)` function periodically and tell the call period in milliseconds. For example if called in every milliseconds: `lv_tick_inc(1)`. 
It is required for LittlevGL to know the elapsed time. Therefore `lv_tick_inc` should be called in a higher priority then `lv_task_handler()`, for example in an interrupt.


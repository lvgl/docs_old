```eval_rst
:github_url: https://github.com/littlevgl/docs/blob/master/zh-CN/porting/task-handler.md
```
# 任务处理程序

为了处理 LittlevGL 的任务，需要在以下代码中周期性调用 ' lv_task_handler() ':
main() 里的 while(1) 函数
周期性的定时中断（优先级要低于  `lv_tick_inc()` ）
一个周期性的 OS 任务

时间不是关键，但它应该是大约5毫秒，以保持系统的响应。

例子：
```c
while(1) {
  lv_task_handler();
  my_delay_ms(5);
}
```

了解更多访问 [Tasks](/overview/task)  章节


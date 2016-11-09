# -*- encoding: utf-8 -*-

import time,sched

#被调度触发的函数
def event_func(msg):
    print "Current Time:",time.time(),'msg:',msg

if __name__=="__main__":
    #初始化sched模块和scheduler类
    s=sched.scheduler(time.time,time.sleep)   #scheduler的两个参数用法复杂,可以不做任何更改
    #设置两个调度
    s.enter(1,2,event_func,("Small event",))
    s.enter(2,1,event_func,("Big event",))  ##四个参数分别为：间隔事件、优先级（用于同时间到达的两个事件同时执行时定序）、被调用触发的函数，给他
                                            #的参数（注意：一定要以tuple给如，如果只有一个参数就(xx,)）
    s.run()        #运行。注意sched模块不是循环的，一次调度被执行后就Over了，如果想再执行，请再次enter
    while True:
        time.sleep(100)
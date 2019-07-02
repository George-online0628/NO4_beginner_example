初学者简单事例整合

1.忽略子进程信号
　signal.signal(signal.SIGCHLD,signal.SIG_IGN)
 SIGCHLD  子进程状态改变时，父进程会收到这个信号
 SIG_IGN  忽略这个信号　　
 SIGINT   Ctrl-C
 SIGTSTP  Ctrl-Z
 SIGQUIT  Ctrl-\
 os.kill(pid,sig)  向目标进程pid，发送信号sig
 os.gitppid()父进程    p.pid  进程对象

 2.装饰器　decorators
 　　是指装饰的是一个函数，传入的是一个函数，返回的也是一个函数的函数(闭包函数)
   在不改变函数调用和定义的情况下，来改变函数的功能，
   即用一个装饰器的调用来代替原来的变量名，装饰器可以嵌套
   
   
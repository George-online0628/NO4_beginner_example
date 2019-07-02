# 司机和售票员的故事
# * 创建父子进程分别代表司机和售票员
# * 当售票员收到SIGINT信号，
#         给司机发送SIGUSR1信号此时司机打印"老司机开车了"
#  当售票员收到SIGQUIT信号，
#         给司机发送SIGUSR2信号此时司机打印"车速有点快，系好安全带"
#  当司机捕捉到SIGTSTP信号，给售票员发送SIGUSR1，
#         售票员打印"到站了，请下车"
# * 到站后 售票员先下车，司机下车 （子进程先退出）
# 说明 ： SIGINT  SIGQUIT SIGTSTP从键盘发出

from multiprocessing import Process
import time
import os
from signal import *

def saler_handler(sig,frame):
    if sig == SIGINT:
        os.kill(os.getppid(),SIGUSR1) #给父进程发SIGUSR1信号
    elif sig == SIGQUIT:
        os.kill(os.getppid(),SIGUSR2)
    elif sig == SIGUSR1:
        print('到站了，请下车')
        os._exit(0)


def drive_handler(sig,frame):
    if sig == SIGUSR1:
        print('老司机开车了')
    elif sig == SIGUSR2:
        print('车速有点快，系好安全带')
    elif sig == SIGTSTP:
        os.kill(p.pid,SIGUSR1)#给子进程发送信号

#子进程售票员创建
def saler():
    signal(SIGINT,saler_handler)
    signal(SIGQUIT,saler_handler)
    signal(SIGUSR1,saler_handler)
    signal(SIGTSTP,SIG_IGN)  #当Ctrl-Z时，子进程忽略
    while True:
        time.sleep(2)
        print('这里有诗和画．．．．．')

p = Process(target = saler)
p.start()

#父进程创建
signal(SIGUSR1,drive_handler)
signal(SIGUSR2,drive_handler)
signal(SIGTSTP,drive_handler)
signal(SIGINT,SIG_IGN)   #当Ctrl-C时，父进程忽略
signal(SIGQUIT,SIG_IGN)  #当Ctrl-\时，父进程忽略

p.join()
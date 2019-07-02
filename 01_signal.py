from signal import *
import time


alarm(3)

def handler(sig,frame):
    if sig == SIGALRM:
        print('接收到时钟信号')
    elif sig == SIGINT:
        print('就不结束')


signal(SIGALRM,handler)
signal(SIGINT,handler)

while True:
    print('waiting for a signal...')
    time.sleep(2)


#signal.signal(signal.SIGALRM,signal.SIG_DFL)  #默认
#signal.signal(signal.SIGINT,signal.SIG_IGN)  　#忽略

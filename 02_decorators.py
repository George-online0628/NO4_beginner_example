#装饰器示例--用一个装饰器的调用来代替原来的变量名，可以嵌套


#1.添加一个余额变动提醒的短信装饰器
def message_send(fn):   #一定传的是函数
    def fx(name,x):    #用fx(name,x)函数替换定义函数，参数个数相同
        print('发来消息:',name,'来银行办理业务了，欢迎短信．．．．．')
        fn(name,x)
        print('发来消息:',name,'来银行办了',x,'元，短信已发送．．．．．．．')
    return fx

#2.加一个权限验证功能的装饰器
def privileged_check(fn):
    def fx(name,x):
        print('正在检查权限......')
        if True:
            fn(name,x)
    return fx


#存钱
@privileged_check
@message_send
def savemoney(name,x):
    print(name,'存了',x,'元')


#取钱
@message_send
def withdraw(name,x):
    print(name,'取了',x,'元')


savemoney('小王',500)
savemoney('小李',300)
withdraw('小花',200)


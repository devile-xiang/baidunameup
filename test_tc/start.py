#encoding:utf-8
import time
import baidu_requst_parameter
def main():
    first=1
    yerday=0
    while True:
        # if first==1:
        #     # baidu_requst_parameter.starturl()
        #     first=2
        #     print("进入第一次")
        #     continue
        # else:
        if time.strftime('%H',time.localtime(time.time()))=="20" and int(time.strftime('%Y%m%d',time.localtime(time.time())))>yerday :
            a=int(time.strftime('%Y%m%d',time.localtime(time.time())))
            print(a)
            yerday=a
            baidu_requst_parameter.starturl()
            print("开始")
        else:
            print("还没有到启动时间！！")
            time.sleep(30)






if __name__ == '__main__':
    main()











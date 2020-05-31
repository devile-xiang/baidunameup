#encoding:utf-8

import time
from baidunameup import keyname
import requests
from lxml import etree

from requests.cookies import RequestsCookieJar

import random
def main():

    #访问链接
    # requests.adapters.DEFAULT_RETRIES = 15
    # # 设置连接活跃状态为False
    # s = requests.session()
    # s.keep_alive = False
    head={
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding":"gzip, deflate",
        "Accept-Language":"zh-CN,zh;q=0.9",
        "Referer":"http://www.baidu.com/",

        "Upgrade-Insecure-Requests":"1",
        # "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36",
        "Proxy-Switch-Ip": "yes"

    }


    # targetUrl="http://httpbin.org/get"
    targetUrl = "http://test.abuyun.com/"
    # targetUr1 = "http://www.baidu.com/s?wd=%e8%b6%b3%e7%90%83%e7%9b%b4%e6%92%ad"
    # targetUr2 = "http://www.baidu.com/s?wd=%e5%85%8d%e8%b4%b9NBA%e7%9b%b4%e6%92%ad"
    # targetUr3 = "http://www.baidu.com/s?wd=%e8%af%b4%e7%90%83%e5%90%a7"
    # targetUr4 = "http://www.baidu.com/link?url=IH-eyq-OPzY25nzv-TUSWwr-1qMNWK1ixNlNfq54Tzt2C1HbkjxGHeieQyLNzGCb"
    # targetUr5 = "http://www.baochengshangbiao.com"


    #ip申请网址
    proxyHost="http-pro.abuyun.com"
    #ip申请网址的端口
    proxyPort="9010"
    #账户登录账号
    proxyuser="H2S5599U2AHJ83LP"
    #账户登录密码
    proxypass="B096A6369FF333EC"

    # proxyMeta="http://%(user)s;%(pass)s@%(host)s:%(port)s"%{
    #     "host":proxyHost,
    #     "port":proxyPort,
    #     "user":proxyuser,
    #     "pass":proxypass
    # }
    proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
        "host": proxyHost,
        "port": proxyPort,
        "user": proxyuser,
        "pass": proxypass,
    }

    global proxies
    proxies={
        "http":proxyMeta,
        "http":proxyMeta
    }
    f = open("小号.txt")
    openurl=[]
    ct=["2097153","2097152","2097153"]
    #小说
    txtwebsite=[
        'www.15huang.com',
        "www.guiayi.com",
        "www.shjiangting.com",
        "www.167k.com" ,
        "www.sharjah.cc",
        "www.92kshu.com",
        "www.92kshu.cc",
        "www.kuaikanxs.cc",
        "www.zazhimall.com",
        "www.jdhs.cc",]
    #机械
    Mechanicswebsite=[
        "www.chinahuaji.com",
        "www.epoji.net",
        "www.suikuangji.com",
        "www.51xishaji.com",
        "www.meiqiuji.net",
        "www.bashihejinwang.com",
        "www.cngaoge.cn",
        "www.oupukeji.com",
        "www.taifuximadianji.com",
        "www.cnjly.com",
        "www.szbaoheng.cn",
    ]
    #工艺品
    technologywebsite=[
        "www.tcjpjt.net",
        "www.songtaogongyi.com",
        "www.jiawc.com",
        "guangxi.zhaobiao.cn",
        "www.duizhuang.com",
        "www.zgszys.com",
        "www.szhad.net ",
        "www.meishu163.com",
        "www.lvsongshi.org",
        "www.cmcat.com",

    ]


    getURL=[]

    for i in txtwebsite:

        url="http://www.baidu.com/baidu?wd=%s&tn=monline_4_dg&ie=utf-8&si=www.baochengshangbiao.com&ct=2097153"




    for i in f:
        line = f.readline()
        # print("当前使用的cookie%s" % line)
        cookie_jar = RequestsCookieJar()


        requ = requests.get(targetUrl,headers=head,cookies=cookie_jar,proxies=proxies,stream=True)
        html = requ.content
        HTML = etree.HTML(html)
        ip1 = HTML.xpath("//tr[3]/td/text()")
        print("当前使用的ip%s"%ip1)



        # cookie_jar.set("BDUSS", '%s' % line[6:-2],domain=".baidu.com")
        cookie_jar.set("BDUSS", '%s' % line[6:-2], domain=".baidu.com")

        txtname="key.textkey.txt"
        key=keyname.getkey(txtname)
        # print(key)
        targetUr1 = "http://www.baidu.com/baidu?wd=%s&tn=monline_4_dg&ie=utf-8&si=www.baochengshangbiao.com&ct=2097153" % key
        print(targetUr1)


        requ=requests.get(targetUr1,headers=head,proxies=proxies,cookies = cookie_jar,stream=True)
        print(requ.status_code)
        html = requ.content.decode()
        HTML = etree.HTML(html)
        # # print(html)
        user = HTML.xpath("//a[@class='username']/text()")
        print("当前用户是%s"%user)
        time.sleep(0.25)





        while True:

            requ = requests.get(targetUrl,headers=head,cookies=cookie_jar,proxies=proxies,stream=True)
            html = requ.content
            HTML = etree.HTML(html)
            ip2 = HTML.xpath("//tr[3]/td/text()")
            # print(requ.text)
            print("结束时的ip%s"%ip2,end="")
            if ip1!=ip2:
                print("ip已经更新")

                break
            else:
                print("继续等待ip更新！！！！再次执行访问关键词和访问页面操作")
                #
                try:
                    time.sleep(8)
                    txtname = ["gjc.textkey.txt", "key.textkey.txt"]
                    import random
                    number = random.randint(0, 1)
                    key = keyname.getkey(txtname[number])
                    targetUr1 = "http://www.baidu.com/baidu?wd=%s&tn=monline_4_dg&ie=utf-8&si=www.baochengshangbiao.com&ct=2097153" % key
                    print(targetUr1)
                    requ = requests.get(targetUr1, headers=head, proxies=proxies, cookies=cookie_jar, stream=True)

                    print(requ.status_code)
                    html = requ.content.decode()
                    HTML = etree.HTML(html)
                    user = HTML.xpath("//a[@class='username']/text()")
                    print("当前用户是%s" % user)

                    time.sleep(8)
                except:
                    time.sleep(8)
                    txtname = ["gjc.textkey.txt", "key.textkey.txt"]
                    import random
                    number = random.randint(0, 1)
                    key = keyname.getkey(txtname[number])
                    targetUr1 = "http://www.baidu.com/baidu?wd=%s&tn=monline_4_dg&ie=utf-8&si=www.baochengshangbiao.com&ct=2097153" % key
                    print(targetUr1)
                    requ = requests.get(targetUr1, headers=head, proxies=proxies, cookies=cookie_jar, stream=True)

                    print(requ.status_code)
                    html = requ.content.decode()
                    HTML = etree.HTML(html)
                    user = HTML.xpath("//a[@class='username']/text()")
                    print("当前用户是%s" % user)

                    time.sleep(8)
                #
                # ""
                #
                # "%e5%95%86%e6%a0%87%e6%b3%a8%e5%86%8c"
                # "http://www.baidu.com/baidu?wd=%e5%95%86%e6%a0%87%e6%b3%a8%e5%86%8c&tn=monline_4_dg&ie=utf-8&si=www.baochengshangbiao.com&ct=2097153"





if __name__ == '__main__':
    main()
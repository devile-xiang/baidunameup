#encoding:utf-8

import time
import requests
from lxml import etree

from requests.cookies import RequestsCookieJar

import random


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


def getkeywords(x):
    global fanhuizhi
    try:
        fanhuizhi = requests.get("http://%s" % x, headers=head, timeout=5)
    except:
        pass
    try:
        text = fanhuizhi.content.decode('utf-8')
    except:
        try:
            text = fanhuizhi.content.decode('gbk')
        except:
            try:
                text = fanhuizhi.content.decode('GBK')
            except:
                try:
                    text = fanhuizhi.content.decode('GB2312')
                except:
                    text = fanhuizhi.content.decode('gb2312')

    # print(text)
    html = etree.HTML(text)
    KEYWORDS = html.xpath("//meta[@name='keywords']/@content")

    if len(KEYWORDS) < 1:

        KEYWORDS = html.xpath("//meta[@name='Keywords']/@content")
    else:
        pass

    print(KEYWORDS[0].split(","))

    fanhuizhi=""

    return KEYWORDS[0].split(",")



def starturl():

    #访问链接
    # requests.adapters.DEFAULT_RETRIES = 15
    # # 设置连接活跃状态为False
    # s = requests.session()
    # s.keep_alive = False


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
        "m.kayege.vip" ,
        "www.sharjah.cc",
        "cxbz958.com",
        "www.2uxs.com",
        "6dxsw.com",
        "www.sj19.net",
        "www.242xs.com",]
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
    ]
    #工艺品
    technologywebsite=[
        "www.tcjpjt.net",
        "www.songtaogongyi.com",
        "www.jiawc.com",
        "www.zlsqlt.com",
        "www.duizhuang.com",
        "www.shouwjj.com",
        "www.szhad.net",
        "www.meishu163.com",
        "www.lvsongshi.org",
        "www.cmcat.com",

    ]


    getURL=[]

    for i,values in enumerate(ct):
        if i==0:
            for x in txtwebsite:
                print(x)
                keywords=getkeywords(x)
                keyname = keywords[random.randint(0, len(keywords) - 1)]
                for j in range(1000):
                    url="http://www.baidu.com/baidu?wd=%s&tn=monline_4_dg&ie=utf-8&si=%s&ct=%s"%(keyname,x,values)
                    # print("需要访问的url是%s"%url)
                    getURL.append(url)
                    url=""
        if i==1:
            for x in Mechanicswebsite:
                print(x)
                keywords = getkeywords(x)
                keyname = keywords[random.randint(0, len(keywords) - 1)]
                for j in range(1000):
                    url = "http://www.baidu.com/baidu?wd=%s&tn=monline_4_dg&ie=utf-8&si=%s&ct=%s" % (keyname, x, values)
                    # print("需要访问的url是%s"%url)
                    getURL.append(url)
                    url = ""
        if i==2:
            for x in technologywebsite:
                print(x)
                keywords = getkeywords(x)
                keyname = keywords[random.randint(0, len(keywords) - 1)]
                for j in range(1000):
                    url = "http://www.baidu.com/baidu?wd=%s&tn=monline_4_dg&ie=utf-8&si=%s&ct=%s" % (keyname, x, values)
                    # print("需要访问的url是%s"%url)
                    getURL.append(url)
                    url = ""
    print(len(txtwebsite))
    print(len(Mechanicswebsite))
    print(len(technologywebsite))
    print(len(getURL))


    for baiduurl in getURL:
        line = f.readline()
        # print("当前使用的cookie%s" % line)
        cookie_jar = RequestsCookieJar()


        requ = requests.get(targetUrl,headers=head,cookies=cookie_jar,proxies=proxies,stream=True)
        html = requ.content
        HTML = etree.HTML(html)
        ip1 = HTML.xpath("//tr[3]/td/text()")
        print("当前使用的ip%s"%ip1)



        # cookie_jar.set("BDUSS", '%s' % line[6:-2],domain=".baidu.com")

        #创建一个随机数，如果等于一，就是用cookie
        suijishu=random.randint(0,3)


        if suijishu==1:
            print("使用了cookie")
            cookie_jar.set("BDUSS", '%s' % line[6:-2], domain=".baidu.com")
        else:
            print("没有使用cookie")

        requ = requests.get(baiduurl, headers=head, proxies=proxies, cookies=cookie_jar, stream=True)
        print(requ.status_code)
        try:
            html = requ.content.decode()
            HTML = etree.HTML(html)
            user = HTML.xpath("//a[@class='username']/text()")
            print("当前用户是%s" % user)
            time.sleep(0.25)
        except:
            print(" ('Connection broken: IncompleteRead(0 bytes read)', IncompleteRead(0 bytes read))")
            time.sleep(0.5)
        # print(html)






        while True:
            try:

                requ = requests.get(targetUrl,headers=head,cookies=cookie_jar,proxies=proxies,stream=True)
                html = requ.content
                HTML = etree.HTML(html)
                ip2 = HTML.xpath("//tr[3]/td/text()")
                # print(requ.text)
                print("结束时的ip%s"%ip2,end="")
            except:
                ip2=""
            if ip1!=ip2:
                print("ip已经更新")

                break
            else:
                print("继续等待ip更新！！！！再次执行访问关键词和访问页面操作")
                #

                time.sleep(1)
                requ = requests.get(baiduurl, headers=head, proxies=proxies, cookies=cookie_jar, stream=True)
                print(requ.status_code)
                try:
                    html = requ.content.decode()
                    HTML = etree.HTML(html)
                    user = HTML.xpath("//a[@class='username']/text()")
                    print("当前用户是%s" % user)
                    time.sleep(0.25)
                except:
                    print(" ('Connection broken: IncompleteRead(0 bytes read)', IncompleteRead(0 bytes read))")
                    time.sleep(0.5)






if __name__ == '__main__':
    starturl()
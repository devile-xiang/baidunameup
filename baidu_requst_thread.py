#encoding:utf-8

import time
from baidunameup import keyname
import requests
from lxml import etree

from requests.cookies import RequestsCookieJar

import random
def main():

    #访问链接
    header={
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding":"gzip, deflate",
        "Accept-Language":"zh-CN,zh;q=0.9",
        "Referer":"http://www.baidu.com/",

        "Upgrade-Insecure-Requests":"1",
        # "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"

    }
    f = open("小号.txt")

    # targetUrl="http://httpbin.org/get"
    targetUrl = "http://test.abuyun.com/"
    # targetUr1 = "http://www.baidu.com/s?wd=%e8%b6%b3%e7%90%83%e7%9b%b4%e6%92%ad"
    # targetUr2 = "http://www.baidu.com/s?wd=%e5%85%8d%e8%b4%b9NBA%e7%9b%b4%e6%92%ad"
    # targetUr3 = "http://www.baidu.com/s?wd=%e8%af%b4%e7%90%83%e5%90%a7"
    targetUr4 = "http://www.baidu.com/link?url=IH-eyq-OPzY25nzv-TUSWwr-1qMNWK1ixNlNfq54Tzt2C1HbkjxGHeieQyLNzGCb"
    targetUr5 = "http://www.baochengshangbiao.com"


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
        "https":proxyMeta
    }

    for i in f:
        requ = requests.get(targetUrl,proxies=proxies,stream=True)
        html = requ.content
        HTML = etree.HTML(html)
        ip1 = HTML.xpath("//tr[3]/td/text()")
        print("当前使用的ip%s"%ip1)

        line = f.readline()
        #下一次要使用的cookie
        # print(line[6:-2])

        # cookies = {'domain': '.baidu.com',
        #            'httpOnly': True,
        #            'name': 'BDUSS',
        #            'path': '/',
        #            'secure': False,
        #            'value': '%s' % line[6:-2]}
        # 'NpaTZ2eE02bVRscU1XV2NtVmVDRzJjamdCZDFNR3lickZ6dWFDYVVVendBZlplRUFBQUFBJCQAAAAAAAAAAAEAAAAaY-VFy83E47TIz-m1xM6i0KYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPB0zl7wdM5eck'
        cookie_jar=RequestsCookieJar()
        # cookie_jar.set("httpOnly", "True",domain=".baidu.com")
        # cookie_jar.set("name", "BDUSS",domain=".baidu.com")
        # cookie_jar.set("path", '/',domain=".baidu.com")
        # cookie_jar.set("secure", "False",domain=".baidu.com")
        cookie_jar.set("BDUSS", '%s' % line[6:-2],domain=".baidu.com")

        # print(cookie_jar)
        # , cookies = cookie_jar
        txtname = ["gjc.txt", "key.txt"]
        import random
        number = random.randint(0, 1)
        key = keyname.getkey(txtname[number])
        targetUr1="http://www.baidu.com/s?wd=%s"%key
        print(targetUr1)
        requ=requests.get(targetUr1,proxies=proxies,cookies = cookie_jar,stream=True)
        print(requ.status_code)
        html = requ.content.decode()
        HTML = etree.HTML(html)
        # # print(html)
        user = HTML.xpath("//a[@class='username']/text()")
        print("当前用户是%s"%user)
        # time.sleep(1)
        # requ2 = requests.get(targetUr2, proxies=proxies, cookies=cookie_jar)
        # print(requ2.status_code)
        # time.sleep(1)
        # requ3 = requests.get(targetUr3, proxies=proxies, cookies=cookie_jar)
        # print(requ3.status_code)
        # time.sleep(1)

        requ4 = requests.get(targetUr4, proxies=proxies, cookies=cookie_jar,stream=True)
        print(requ4.status_code)

        requ5 = requests.get(targetUr5, proxies=proxies, cookies=cookie_jar,stream=True)
        print(requ5.status_code)


        while True:

            requ = requests.get(targetUrl, proxies=proxies,stream=True)
            html = requ.content
            HTML = etree.HTML(html)
            ip2 = HTML.xpath("//tr[3]/td/text()")
            # print(requ.text)
            print("结束时的ip%s"%ip2,end="")
            if ip1!=ip2:
                print("ip已经更新")
                time.sleep(8)
                break
            else:
                print("继续等待ip更新！！！！再次执行访问关键词和访问页面操作")
                #
                time.sleep(8)
                txtname = ["gjc.txt", "key.txt"]
                import random
                number = random.randint(0, 1)
                key = keyname.getkey(txtname[number])
                # print(key)
                targetUr1 = "http://www.baidu.com/s?wd=%s" % key
                print(targetUr1)
                requ = requests.get(targetUr1, proxies=proxies, cookies=cookie_jar,stream=True)
                print(requ.status_code)
                html = requ.content.decode()
                HTML = etree.HTML(html)
                user = HTML.xpath("//a[@class='username']/text()")
                print("当前用户是%s" % user)
                requ4 = requests.get(targetUr4, proxies=proxies, cookies=cookie_jar,stream=True)
                print(requ4.status_code)
                requ5 = requests.get(targetUr5, proxies=proxies, cookies=cookie_jar,stream=True)
                print(requ5.status_code)
                time.sleep(8)







if __name__ == '__main__':
    main()
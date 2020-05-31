#encoding：utf+8


import requests
def main():
    import requests

    # 要访问的目标页面
    targetUrl = "http://test.abuyun.com"
    # targetUrl = "http://proxy.abuyun.com/switch-ip"
    # targetUrl = "http://proxy.abuyun.com/current-ip"

    # 代理服务器
    proxyHost = "http-pro.abuyun.com"
    proxyPort = "9010"

    # 代理隧道验证信息
    proxyUser = "H2S5599U2AHJ83LP"
    proxyPass = "B096A6369FF333EC"

    proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
        "host": proxyHost,
        "port": proxyPort,
        "user": proxyUser,
        "pass": proxyPass,
    }

    proxies = {
        "http": proxyMeta,
        "https": proxyMeta,
    }


    #添加ip
    header={
        "Proxy-Switch-Ip":"yes"
    }
    resp = requests.get(targetUrl, proxies=proxies,headers=header)

    print(resp.status_code)
    print(resp.text)


    # a=resp.text.split(',')
    # print(a)
    # targetUrl1="http://test.abuyun.com"
    # https_proxies={
    #     "http":"%s:%s"%(a[0],proxyPort),
    #     "https":"%s:%s" % (a[0], proxyPort)
    # }
    #
    # print("代理IP为%s"%https_proxies)
    # resp1=requests.get(targetUrl1,proxies=https_proxies)
    #
    # print(resp1.status_code)
    # print(resp1.text)




    #



if __name__ == '__main__':
    main()
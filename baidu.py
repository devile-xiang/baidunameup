#encoding：utf-8

from selenium import webdriver

import time

from tkinter import *
import tkinter
import string
import zipfile

def stop():
    exit()
def start():

    #使用cookie和代理登陆账户

    proxyHost = "http-pro.abuyun.com"
    proxyPort = "9010"

    # 代理隧道验证信息
    proxyUser = "H2S5599U2AHJ83LP"
    proxyPass = "B096A6369FF333EC"

    def create_proxy_auth_extension(proxy_host, proxy_port,
                                    proxy_username, proxy_password,
                                    scheme='http', plugin_path=None):
        if plugin_path is None:
            plugin_path = r'D:/{}_{}@http-pro.abuyun.com_9010.zip'.format(proxy_username, proxy_password)

        manifest_json = """
               {
                   "version": "1.0.0",
                   "manifest_version": 2,
                   "name": "Abuyun Proxy",
                   "permissions": [
                       "proxy",
                       "tabs",
                       "unlimitedStorage",
                       "storage",
                       "<all_urls>",
                       "webRequest",
                       "webRequestBlocking"
                   ],
                   "background": {
                       "scripts": ["background.js"]
                   },
                   "minimum_chrome_version":"22.0.0"
               }
               """

        background_js = string.Template(
            """
            var config = {
                mode: "fixed_servers",
                rules: {
                    singleProxy: {
                        scheme: "${scheme}",
                        host: "${host}",
                        port: parseInt(${port})
                    },
                    bypassList: ["foobar.com"]
                }
              };

            chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

            function callbackFn(details) {
                return {
                    authCredentials: {
                        username: "${username}",
                        password: "${password}"
                    }
                };
            }

            chrome.webRequest.onAuthRequired.addListener(
                callbackFn,
                {urls: ["<all_urls>"]},
                ['blocking']
            );
            """
        ).substitute(
            host=proxy_host,
            port=proxy_port,
            username=proxy_username,
            password=proxy_password,
            scheme=scheme,
        )

        with zipfile.ZipFile(plugin_path, 'w') as zp:
            zp.writestr("manifest.json", manifest_json)
            zp.writestr("background.js", background_js)

        return plugin_path

    proxy_auth_plugin_path = create_proxy_auth_extension(
        proxy_host=proxyHost,
        proxy_port=proxyPort,
        proxy_username=proxyUser,
        proxy_password=proxyPass)

    option = webdriver.ChromeOptions()

    option.add_argument("--start-maximized")
    option.add_extension(proxy_auth_plugin_path)

    driver = webdriver.Chrome(chrome_options=option)


    f=open("小号.txt")


    for i in f:
        line=f.readline()
        print(line[6:-2])





        cookies={'domain': '.baidu.com',
                     'httpOnly': True,
                     'name': 'BDUSS',
                     'path': '/',
                     'secure': False,
                    'value':'%s'%line[6:-2]}
        # 'NpaTZ2eE02bVRscU1XV2NtVmVDRzJjamdCZDFNR3lickZ6dWFDYVVVendBZlplRUFBQUFBJCQAAAAAAAAAAAEAAAAaY-VFy83E47TIz-m1xM6i0KYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPB0zl7wdM5eck'

        print(cookies)
        driver.get("http://www.baidu.com")
        driver.add_cookie(cookies)
        driver.get("https://www.baidu.com/s?wd=%E5%BB%BA%E7%AB%99")
        time.sleep(3)
        driver.get("https://www.baidu.com/s?wd=%E4%BC%81%E4%B8%9A%E5%BB%BA%E7%AB%99")
        time.sleep(3)
        driver.get("https://www.baidu.com/s?wd=%E8%AE%AF%E6%B3%95%E7%BD%91")
        time.sleep(3)
        driver.refresh()
        driver.delete_all_cookies()

        for i in range(4):
            print("登录结束暂停%s"%i)
            time.sleep(1)



    for i in range(5):
        print("倒计时%s" % i)
        time.sleep(1)








    driver.close()
    driver.quit()


top=Tk()
top.title("测试百度快排")
top.geometry("600x600")


start1=tkinter.Button(top,text='启动',command=start)
start1.pack()
top.mainloop()








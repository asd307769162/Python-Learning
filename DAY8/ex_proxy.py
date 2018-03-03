import requests
import os
import random
import bs4


# 操作说明：先使用proxy_ip.py获取最新的可用代理ip，因文件使用的方法是续写，并且免费的代理并不可靠，所以建议一定时间后删除生成的txt文件并重新获取代理ip


def open_url():
    # 设置访问源
    url = "https://www.baidu.com"
      
    # 设置浏览器头部信息
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36}',}

    # 景点游标信息，非必须
    data = {}
   
    # 获取代理IP，并设置代理信息
    file = open("可用的代理IP.txt")
    all_lines = file.readlines()
    ips = []
    
    for line in all_lines:
        ips.append(line.split())

    proxies = {"http":(random.choice(ips))[0]}
    print("正在使用"+str(proxies))


    # 访问网页
    try:
        res = requests.get(url, headers=headers, proxies=proxies, timeout=2)
        if res == "":
            fail = True
            print("返回故障，重新获取中")
    except:
        print(str(proxies)+"连接故障，重新尝试中")
    else:
        print(res)
        status = do_other_things(res)
        return status

def do_other_things(res):
    # 此处可写代码

    
    # 此处加一个验证是否获取正确的条件，并返回status
    status = True
    return status
    

if __name__=="__main__":
    page = 1
    status = open_url()
    page = page + 1
      


        

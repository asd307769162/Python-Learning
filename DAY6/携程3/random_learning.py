import os
import random
import requests

# 获取代理IP

while True:
    file = open("可用的代理IP.txt")
    all_lines = file.readlines()
    ips = []
        
    for line in all_lines:
        ips.append(line.split())


    proxies = {"http":(random.choice(ips))[0]}

    print(proxies)

    url='http://www.whatismyip.com.tw'

    headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36 Maxthon/5.1.6.2000'}


    res = requests.get(url, proxies=proxies, headers=headers)

    print(res)
       

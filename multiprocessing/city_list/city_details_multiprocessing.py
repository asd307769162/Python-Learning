# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 16:11:47 2018

@author: busby
"""

import time
import requests
import bs4
from multiprocessing import Pool


def get_details(soup):
    try: #分别获取整张表、keys、values和注释符号
        table = soup.find('div', class_="basic-info cmn-clearfix")
        table_dts = table.find_all('dt', class_="basicInfo-item name")
        table_dds = table.find_all('dd', class_="basicInfo-item value")
        table_zs = table.find_all('sup', class_="sup--normal")
    except:
        return(None)
    
    
    i = 0
    max_i = len(table_dts) #获取循环次数
    keys = []
    values = []
    zss = []
    for each in table_zs: #将注释符号汇总为一个列表
        zss.append(each.text.strip().replace(" ", ""))
    while i < max_i:
        key = table_dts[i].text.strip().replace(" ", "") #先去除空格和换行符
        value = table_dds[i].text.strip().replace(" ", "") #同上
        for each in zss: #通过循环迭代，去除掉注释符号，如果没有则不会去除任何字符
            key = key.replace(each, "").strip()
            value = value.replace(each, "").strip()
        keys.append(key)   
        values.append(value)
        i += 1
        
    details = [keys, values, max_i] #组成列表，传参
    return(details)


def open_url(url):
    # 使用headers解决百科反爬虫的问题
    #return(url)
    headers = {
            'User-Agent':'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299',
            'Referer': 'https://baike.baidu.com/item/%E5%8C%97%E4%BA%AC/128981?fr=aladdin&fromid=126069&fromtitle=%E5%8C%97%E4%BA%AC%E5%B8%82'
            }

    res = requests.get(url, headers = headers).content.decode('utf-8')
    soup = bs4.BeautifulSoup(res, 'lxml')
    # print(soup)
    details = get_details(soup)
    return (details)

def save_details(details):
    max_i = details[2]
    i = 0
    file = open('中国县级以上城市信息简表2.txt', 'a', encoding = 'utf-8')
    while i < max_i: #输出完整信息
        file.write(details[0][i]+"："+details[1][i]+"\n")
        # print(details[0][i]+"："+details[1][i])
        i += 1
    file.write('\n\n')
    file.close
    return('Success')

def get_list():
    file = open("中华人民共和国县以上行政区划代码.txt", "r", encoding = "utf-8")
    all_lines = file.readlines()
    details = []
    provinces = []
    cities = []
   
    for line in all_lines:
        details.append(line.split())
    
    i = 0
    while i < len(details):
        if len(details[i]) != 0:
            cities.append(details[i])
        else:
            #print(cities)
            provinces.append(cities)
            cities = []
        i += 1
    return (provinces)

def make_urls(name):
    # print("正在拼凑")
    name = name[0]
    url = "https://baike.baidu.com/item/" + str(name)
    return (url)
    
def main():
    num = 1
    st = time.time()
    provinces_name = get_list()
    pool = Pool(processes = 8)
    for province in provinces_name:
        provinces_urls = pool.map(make_urls, province)
        provinces_txt = pool.map(open_url, provinces_urls)
        for each in provinces_txt:
            try:
                result = save_details(each)
                print(result, num)
            except:
                print('failed', each)
            num += 1

    print(time.time()-st)
    
if __name__ == '__main__':
    main()
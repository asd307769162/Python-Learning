# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 11:53:39 2018

@author: busby
"""

import requests
import bs4


def get_res(url):
    res = requests.get(url).content.decode('utf-8')
    soup = bs4.BeautifulSoup(res, 'lxml')
    content = soup.find_all('td',class_="xl7012452")
    id_ =[]
    name_ = []
    i = 0
    new_content = []
    for each in content:
        if each.text != "":
            new_content.append(each)
             
    while i < len(new_content):
        if i % 2 == 0:
            id_.append(new_content[i].text)
        else:
            name_.append(new_content[i].text)
        i += 1
    
    provinces = []
    cities = []
    i = 0
    while i < len(id_):
        if id_[i] == 0:
            cities.append(name_[i])
        elif id_[i][0:2] == id_[i-1][0:2]:
            cities.append(name_[i])
        else:
            # print(cities)
            provinces.append(cities)
            cities = []
            cities.append(name_[i])
        i += 1
    return(provinces)
    

def write_list(provinces):
    # print(provinces)
    file = open("中华人民共和国县以上行政区划代码.txt", 'a', encoding = 'utf-8')
    for province in provinces:
        for city in province:
            file.write(city + "\n")
        file.write("\n")
    file.close
    
    
def main():
    url = 'http://www.mca.gov.cn/article/sj/tjbz/a/2018/201803/201803191002.html'
    provinces = get_res(url)
    write_list(provinces)
    
if __name__ == '__main__':
    main()
import requests
import bs4
import re
import time
import os
import random

# 获取景点的详细信息
def open_url(page):
    # 访问源
    host = "http://you.ctrip.com/destinationsite/TTDSecond/SharedView/AsynCommentView"
   
    # 浏览器头部信息
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36}',
               'Referer':'http://you.ctrip.com/sight/chongming571/5681.html',
               'Cookie':'StartCity_Pkg=PkgStartCity=2; _abtest_userid=e74c1d70-50d9-43c3-8c86-0b21452c223f; UM_distinctid=16155888ba7a2-07430e799076d7-4353468-144000-16155888ba82fc; _RSG=mIa4qcNeaO2oqJerQlY88A; _RDG=28496414ac40d72e9532746a41ac46f315; _RGUID=2624a179-b412-44b0-a208-8af6b5a13d32; _ga=GA1.2.1140136322.1517558470; MKT_Pagesource=PC; CNZZDATA1256793290=157138234-1517557503-http%253A%252F%252Fwww.ctrip.com%252F%7C1517557503; bdshare_firstime=1517558477763; Customer=HAL=ctrip_gb; _gid=GA1.2.1290549758.1518148629; appFloatCnt=4; manualclose=1; ASP.NET_SessionSvc=MTAuOC4xODkuNTN8OTA5MHxqaW5xaWFvfGRlZmF1bHR8MTUxMTI1OTIwNzU5NQ; _RF1=116.224.215.31; Session=smartlinkcode=U130026&smartlinklanguage=zh&SmartLinkKeyWord=&SmartLinkQuary=&SmartLinkHost=; Union=AllianceID=4897&SID=130026&OUID=&Expires=1518782732056; __zpspc=9.4.1518177932.1518177932.1%232%7Cwww.baidu.com%7C%7C%7C%7C%23; _jzqco=%7C%7C%7C%7C%7C1.443470209.1517558469937.1518148629385.1518177932087.1518148629385.1518177932087.0.0.0.4.4; Mkt_UnionRecord=%5B%7B%22aid%22%3A%224897%22%2C%22timestamp%22%3A1518177945508%7D%5D; _bfi=p1%3D290510%26p2%3D290510%26v1%3D12%26v2%3D11; _bfa=1.1517558467111.2j1um.1.1518148624801.1518177680566.4.21; _bfs=1.11',
               'Content-Type':'application/x-www-form-urlencoded',
               'Accept-Encoding':'gzip, deflate',
               }
    # 景点游标信息
    data = {
        "poiID":76804,
        "districtId":571,
        "districtEName":"Chongming",
        "pagenow":page,
        "order":3.0,
        "star":0,
        "tourist":0.0,
        "resourceId":5681,
        "resoucetype":2,
        }
    print(data)

    # 获取代理IP
    file = open("可用的代理IP.txt")
    all_lines = file.readlines()
    
    file = open("可用的代理IP.txt")
    all_lines = file.readlines()
    ips = []
    
        
    for line in all_lines:
        ips.append(line.split())


    proxies = {"http":(random.choice(ips))[0]}
    print("正在使用"+str(proxies))

    fail = False
    
    # 访问携程
    try:
        res = requests.post(host, headers=headers, data=data, proxies=proxies, timeout=2)
        res = res.content.decode('utf-8')
    except:
        print(str(proxies)+"网络故障，重新尝试中")
        fail = True
    else:
        soup = bs4.BeautifulSoup(res, 'lxml')
        get_info(soup)
        fail = False
        return fail


def get_info(soup):
    # 用户名
    users = []
    targets = soup.find_all("span", class_="ellipsis")
    for each in targets:
        users.append('用户名：%s' %each.a['title'])
        # print(each.a['title'])

    # 评论内容，去除空格和换行
    comments = []
    targets = soup.find_all("span", class_="heightbox")
    for each in targets:
        comments.append(' 评论：%s' %each.text.replace("\n",""))
        # print(each.text)

    # 总分评价
    avg_marks = []
    targets = soup.find_all("span", itemtype="http://schema.org/Rating")
    for each in targets:
        if str(each.span)[21:22] == '%':
            avg_marks.append(' 总分：'+str(each.span)[19:21])
            # print(str(each.span)[19:21])
        else:
             avg_marks.append(' 总分：'+str(each.span)[19:22])
            # print(str(each.span)[19:22])

    # 汇总在一起，一行数据为一个用户的内容
    result = []
    length = len(users)

    # 写入文件
    for i in range(length):
        result.append(users[i]+comments[i]+avg_marks[i]+"\n")
        # print(result[i])
       
        file = open("东平国家森林公园.txt", "a", encoding='utf-8')
        file.write(result[i])
        file.close()


# 获取评论总页数
def get_max_page_num(url):
    
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36}',
               'Cookie':'StartCity_Pkg=PkgStartCity=2; _abtest_userid=e74c1d70-50d9-43c3-8c86-0b21452c223f; UM_distinctid=16155888ba7a2-07430e799076d7-4353468-144000-16155888ba82fc; _RSG=mIa4qcNeaO2oqJerQlY88A; _RDG=28496414ac40d72e9532746a41ac46f315; _RGUID=2624a179-b412-44b0-a208-8af6b5a13d32; _ga=GA1.2.1140136322.1517558470; MKT_Pagesource=PC; CNZZDATA1256793290=157138234-1517557503-http%253A%252F%252Fwww.ctrip.com%252F%7C1517557503; bdshare_firstime=1517558477763; Customer=HAL=ctrip_gb; _gid=GA1.2.1290549758.1518148629; appFloatCnt=4; manualclose=1; ASP.NET_SessionSvc=MTAuOC4xODkuNTN8OTA5MHxqaW5xaWFvfGRlZmF1bHR8MTUxMTI1OTIwNzU5NQ; _RF1=116.224.215.31; Session=smartlinkcode=U130026&smartlinklanguage=zh&SmartLinkKeyWord=&SmartLinkQuary=&SmartLinkHost=; Union=AllianceID=4897&SID=130026&OUID=&Expires=1518782732056; __zpspc=9.4.1518177932.1518177932.1%232%7Cwww.baidu.com%7C%7C%7C%7C%23; _jzqco=%7C%7C%7C%7C%7C1.443470209.1517558469937.1518148629385.1518177932087.1518148629385.1518177932087.0.0.0.4.4; Mkt_UnionRecord=%5B%7B%22aid%22%3A%224897%22%2C%22timestamp%22%3A1518177945508%7D%5D; _bfi=p1%3D290510%26p2%3D290510%26v1%3D12%26v2%3D11; _bfa=1.1517558467111.2j1um.1.1518148624801.1518177680566.4.21; _bfs=1.11',
               'Content-Type':'application/x-www-form-urlencoded',
               'Accept-Encoding':'gzip, deflate',
               }

    res = requests.get(url, headers=headers)

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    max_page_num = soup.find('b', class_="numpage").text

    return int(max_page_num)


# 主程序
def main():
    url = input("请输入需要爬取的景点链接：")
    page_num = get_max_page_num(url)

    
    i = 63
    while i <= page_num:
        fail = open_url(i)
        if fail == False:
            print("已完成"+str(i)+"页的爬取工作")
            time.sleep(0.5)
            i = i+1
        else:
            i = i

if __name__=="__main__":
    main()

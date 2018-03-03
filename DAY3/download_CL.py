import urllib.request
import urllib.error
import os
import random
import time
import re
from urllib.error import URLError,HTTPError

def url_open(url):

    try:     
        req=urllib.request.Request(url)
        req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299')
        req.add_header('Cookie','__jsluid=fcea67179f86ef04f1e472f19872b127')
       
        iplist=['127.0.0.1:1082']

        proxy_support = urllib.request.ProxyHandler({'http':random.choice(iplist)})

        opener=urllib.request.build_opener(proxy_support)
        opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36')]

        urllib.request.install_opener(opener)

        response=urllib.request.urlopen(url)
        html=response.read()
    except URLError as e:
        if hasattr(e,'reason'):
                print("打开时链接出错："+each)
                pass
        elif hasattr(e,'code'):
                print("打开时网络出错："+e.code)
                pass
    else:
        return html


def find_imgs(url):

    print("您要下载的CL链接为："+url)
    html=url_open(url).decode("gbk",errors = 'ignore')

    p=r"<input src='([^']+\.jpg)'"
    img_addrs=re.findall(p,html)

    '''
    for each in img_addrs:
        print(each)
    '''
    return img_addrs
   
def find_name(url):
    html=url_open(url).decode("gbk",errors = 'ignore')
    c=html.find("title")
    d=html.find("[",c)
    img_name=html[c+6:d]
    
    return img_name

def save_imgs(folder,img_addrs):

    '''
    for each in img_addrs:
        filename = each.split('/')[-1]
        with open(filename,'wb') as f:
                  img =url_open(each)
                  f.write(img)
        print(each+"下载完成")
        time.sleep(2)
    '''
    for each in img_addrs:
        try:
            filename=each.split('/')[-1]
            urllib.request.urlretrieve(each, filename,None)
            time.sleep(1)
        except URLError as e:
            if hasattr(e,'reason'):
                print("保存时链接出错："+each)
                pass
            elif hasattr(e,'code'):
                print("保存时网络出错："+e.code)
                pass
        else:
            print(each+"下载完成")
  

def download_mm():

    while True:
            
        page_url = input("请输入要下载的链接：")
        if page_url=="":
            break

        home=os.getcwd()
        
        img_addrs = find_imgs(page_url)
        img_name = find_name(page_url)
        folder=img_name
        try:
            os.mkdir(folder)
        except:
            print("该链接已经在当前目录中，无须再次下载！")
            download_mm()
        
        os.chdir(folder)
        save_imgs(folder, img_addrs)
        os.chdir(home)
        print("下载链接完成！")

            
if __name__ == '__main__':
    download_mm()



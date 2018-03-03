import urllib.request
import os
import random
import time


def url_open(url):

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
  
    return html


def find_imgs(url):
    html=url_open(url).decode("gb2312",errors = 'ignore')
    
    img_addrs=[]
    a=html.find('img alt=')

    while a!=-1:
        b=html.find('.jpg',a,a+255)
        c=html.find('http:',a,a+255)
        if b!=-1:
            if html[c:b+4]!="http://www.meizitu.com/images/erweima.jpg":
                img_addrs.append(html[c:b+4])
        else:
            b=a+25

        a=html.find('img alt=',b)

    return img_addrs

def find_name(url):
    html=url_open(url).decode("gb2312",errors = 'ignore')
    c=html.find("img alt=")
    d=html.find("，第",c)
    img_name=html[c+9:d]
    
    return img_name

def save_imgs(folder,img_addrs):
    for each in img_addrs:
        filename = each.split('/')[-1]
        with open(filename,'wb') as f:
                  img =url_open(each)
                  f.write(img)
        print(each+"下载完成")
        time.sleep(2)

def download_mm():

    url = "http://www.meizitu.com/"
    
    page_num=int(input("请输入要下载的页码："))

    home=os.getcwd()
    
    page_url = url + 'a/' + str(page_num) + '.html'
    img_addrs = find_imgs(page_url)
    img_name = find_name(page_url)
    folder=str(page_num)+str(img_name)
    os.mkdir(folder)
    os.chdir(folder)
    save_imgs(folder, img_addrs)
    os.chdir(home)

        
if __name__ == '__main__':
    download_mm()



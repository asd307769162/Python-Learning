import urllib.request
import random

url='http://www.whatismyip.com.tw'

iplist=['127.0.0.1:1082']

proxy_support = urllib.request.ProxyHandler({'http':random.choice(iplist)})

opener=urllib.request.build_opener(proxy_support)
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36')]

 
urllib.request.install_opener(opener)

response=urllib.request.urlopen(url)

html=response.read().decode('utf-8')

print(html)

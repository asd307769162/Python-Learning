import urllib.request
import urllib.parse
import json

translation=input('请输入要翻译的内容：')

url= 'http://fy.iciba.com/ajax.php?a=fy'

head={}
head['User-Agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'


data={}

data['f']='auto'
data['t']='auto'
data['w']=translation

data=urllib.parse.urlencode(data).encode('utf-8')


req =urllib.request.Request(url,data,head)
response=urllib.request.urlopen(req)

html=response.read().decode('utf-8')

target=json.loads(html)

answer=target['content']['out']


print('原文：'+translation)
print('结果：'+answer)
 

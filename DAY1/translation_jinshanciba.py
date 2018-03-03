import urllib.request
import urllib.parse
import json

translation=input('请输入要翻译的内容：')

url= 'http://fy.iciba.com/ajax.php?a=fy'

data={}

data['f']='auto'
data['t']='auto'
data['w']=translation

data=urllib.parse.urlencode(data).encode('utf-8')


response =urllib.request.urlopen(url,data)
html=response.read().decode('utf-8')

json.loads(html)
target=json.loads(html)

answer=target['content']['out']


print('原文：'+translation)
print('结果：'+answer)
 

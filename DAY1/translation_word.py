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

answer=target['content']['word_mean']

print('原文：'+translation)


n=len(answer)
i=0
while i<n:
    print('结果：'+answer[i])
    i=i+1
 

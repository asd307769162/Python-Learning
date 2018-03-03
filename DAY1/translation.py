import urllib.request
import urllib.parse

url= 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

data={}


data['i']='测试'
data['from']='AUTO'
data['to']='AUTO'
data['smartresult']='dict'
data['client']='fanyideskweb'
data['salt']='1517902138471'
data['sign']='07876224cf3755531b5e1cb003f714f7'
data['doctype']='json'
data['version']='2.1'
data['keyfrom']='fanyi.web'
data['action']='FY_BY_CLICKBUTTION'
data['typoResult']='false'
data=urllib.parse.urlencode(data).encode('utf-8')


response =urllib.request.urlopen(url,data)
html=response.read().decode('utf-8')

print(html)
 

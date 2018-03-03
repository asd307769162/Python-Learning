import urllib.request
import urllib.parse

url= 'http://fanyi.baidu.com/v2transapi'

data={}

data['from']='zh'
data['to']='en'
data['query']='测试'
data['transtype']='translang'
data['simple_means_flag']='3'
data['sign']='167486.421135'
data['token']='882ed058cd3aad45010de47cb7055175'


data=urllib.parse.urlencode(data).encode('utf-8')


response =urllib.request.urlopen(url,data)
html=response.read().decode('utf-8')

print(html)
 

import urllib.request

response=urllib.request.urlopen('https://www.baidu.com/img/bd_logo1.png')

baidu_img=response.read()


with open('baidu.jpg','wb') as f:
    f.write(baidu_img)


'''
>>> response.geturl()
'https://www.baidu.com/img/bd_logo1.png'
>>> response.info()
<http.client.HTTPMessage object at 0x000001880D41BA58>
>>> print(response.info())
Accept-Ranges: bytes
Cache-Control: max-age=315360000
Content-Length: 7877
Content-Type: image/png
Date: Tue, 06 Feb 2018 07:24:32 GMT
Etag: "1ec5-502264e2ae4c0"
Expires: Fri, 04 Feb 2028 07:24:32 GMT
Last-Modified: Wed, 03 Sep 2014 10:00:27 GMT
P3p: CP=" OTI DSP COR IVA OUR IND COM "
Server: Apache
Set-Cookie: BAIDUID=28544D03BB205896BEA7421B39EC8A17:FG=1; expires=Wed, 06-Feb-19 07:24:32 GMT; max-age=31536000; path=/; domain=.baidu.com; version=1
Connection: close


>>> response.getcode()
200
>>>

'''

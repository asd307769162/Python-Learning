import urllib.request
import urllib.parse
import json

def ip_Tencent(ip):
   

    url='http://apis.map.qq.com/ws/location/v1/ip?ip='+ip+'&key=LMKBZ-VORKG-GGEQ7-IFEQQ-MDYFS-V6FLY'
    
    response =urllib.request.urlopen(url)
    html=response.read().decode('utf-8')
    
    json.loads(html)
    target=json.loads(html)

    try:
        ip_ip=target['result']['ip']
        ip_lat=target['result']['location']['lat']
        ip_lng=target['result']['location']['lng']
        ip_nation=target['result']['ad_info']['nation']
        ip_province=target['result']['ad_info']['province']
        ip_city=target['result']['ad_info']['city']
        ip_district=target['result']['ad_info']['district']
        ip_adcode=target['result']['ad_info']['adcode']

        ip_info="ip地址："+ip_ip+"\n纬度："+str(ip_lat)+"\n经度："+str(ip_lng)+"\n地区："+ip_nation+" "+ip_province+" "+ip_city+" "+ip_district+"\n邮编："+str(ip_adcode)

    except:
        ip_status=target['status']
        ip_message=target['message']
        ip_info="错误代码："+str(ip_status)+"\n错误原因："+ip_message
        
    return ip_info

while True:
    ip=input("请输入需要查询的ip地址：")
    if ip=="":
        break
    ip_info=ip_Tencent(ip)
    print(ip_info)
 

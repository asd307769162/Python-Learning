# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 21:46:25 2018

@author: busby
"""

import requests
import json
import smtplib
from email.mime.text import MIMEText
from email import encoders
from email.header import Header
from email.utils import parseaddr, formataddr
      

def get_aqi():
    url = "http://wis.qq.com/weather/common?source=pc&weather_type=air%7Crise&province=%E4%B8%8A%E6%B5%B7&city=%E4%B8%8A%E6%B5%B7&callback=jQuery11130569730820780882_1520565502963&_=1520565502966"
    res= requests.get(url)
    a = res.text.find('{')
    content = res.text[a:-1]
    content = json.loads(content)
    weather_aqi = content["data"]["air"]
    aqi_num = weather_aqi["aqi"]
    aqi_level = weather_aqi["aqi_level"]
    aqi_name = weather_aqi["aqi_name"]
    pm2_5 = weather_aqi["pm2.5"]
    pm10 = weather_aqi["pm10"]
    update_mon = weather_aqi["update_time"][4:6]
    update_day = weather_aqi["update_time"][6:8]
    update_time = weather_aqi["update_time"][8:10]

    if int(aqi_num) > 100:
        weather_aqi = ("目前（%s月%s日%s时发布）的AQI指数为%s，等级为%s级，属于%s，其中PM2.5指数为%s，PM10指数为%s。"  %(update_mon, update_day, update_time, aqi_num, aqi_level, aqi_name, pm2_5, pm10))
        Send_Email(weather_aqi)
    else:
        print("天气正常")


def _format_addr(s):
    name, addr = parseaddr(s)
    return (formataddr((Header(name, 'utf-8').encode(), addr)))


def Send_Email(weather_aqi):
    from_addr = 'admin@admin.com'
    password = 'password'
    to_addr = 'user@user.com'
    smtp_server = 'smtp.qq.com'
    
    
    msg_body = weather_aqi
    msg_foot = "\n\n请减少户外停留时间哟，如需出门请戴好口罩！~\n\n\n本空气污染预报由Busby制作并提供服务\n版本号：0.1"
    msg = msg_body +msg_foot
    header = ("空气污染预警！")
     
    msg = MIMEText(msg,'plain','utf-8')
    msg['From'] = _format_addr('Busby<%s>' % from_addr)
    msg['To'] = _format_addr('尊敬的用户<%s>' % to_addr)
    msg['Subject'] = Header(header, 'utf-8').encode()
    
    server = smtplib.SMTP_SSL(smtp_server,465)
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()
    
    
get_aqi()

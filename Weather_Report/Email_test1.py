# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 21:42:33 2018

@author: busby
"""

import smtplib
from email.mime.text import MIMEText
from email import encoders
from email.header import Header
from email.utils import parseaddr, formataddr
from weather_test1 import get_tomorrow 

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

from_addr = 'admin@admin.com'
password = 'password'
to_addr = 'user@user.com'
smtp_server = 'smtp.qq.com'

weather = get_tomorrow()
tomorrow_date = weather[0]
tomorrow_tem = weather[1]
tomorrow_wea = weather[2]
tomorrow_win = weather[3]
msg = '尊敬的用户，明天是'+tomorrow_date+'日\n明天温度：'+tomorrow_tem+'\n天气：'+tomorrow_wea+"\n风力："+ tomorrow_win+"\n请注意照顾好自己哟~\n\n\n本天气预报由Busby制作并提供服务\n版本号：0.1"
header = '关于3月'+tomorrow_date+'日的天气预报'
 
msg = MIMEText(msg,'plain','utf-8')
msg['From'] = _format_addr('Busby<%s>' % from_addr)
msg['To'] = _format_addr('尊敬的用户<%s>' % to_addr)
msg['Subject'] = Header(header, 'utf-8').encode()

server = smtplib.SMTP_SSL(smtp_server,465)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()

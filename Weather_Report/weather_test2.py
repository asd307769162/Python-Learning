# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 11:02:45 2018

@author: busby
"""

import requests
import json


def get_hours():
    url = "http://wis.qq.com/weather/common?source=pc&weather_type=observe%7Cforecast_1h%7Cforecast_24h%7Cindex%7Calarm%7Climit%7Ctips%7Crise&province=%E4%B8%8A%E6%B5%B7&city=%E4%B8%8A%E6%B5%B7&county=%E9%BB%84%E6%B5%A6&callback=jQuery111309358002047979104_1520564434052&_=1520564434088"
    res= requests.get(url)  
    a = res.text.find('{')
    content = res.text[a:-1]
    content = json.loads(content)
    return(content["data"]["forecast_1h"])

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
    weather_aqi = ("目前（%s月%s日%s时发布）的AQI指数为%s，等级为%s级，属于%s，其中PM2.5指数为%s，PM10指数为%s。"  %(update_mon, update_day, update_time, aqi_num, aqi_level, aqi_name, pm2_5, pm10))
    return(weather_aqi)

def get_days():
    url= "http://wis.qq.com/weather/common?source=pc&weather_type=forecast_24h&province=%E4%B8%8A%E6%B5%B7%E5%B8%82&city=%E4%B8%8A%E6%B5%B7%E5%B8%82&county=&callback=jQuery11130569730820780882_1520565502963&_=1520565502967"    
    res= requests.get(url)
    a = res.text.find('{')
    content = res.text[a:-1]
    content = json.loads(content)
    weather_days = content["data"]["forecast_24h"]
    num = 0
    day_weather = []
    day_wind_direction = []
    day_wind_power = []
    max_degree = []
    min_degree = []
    night_weather = []
    night_wind_direction = []
    night_wind_power = []
    time = []
    weather_day = []
    while int(num) <= int(7):
        day_weather.append(weather_days["%s" %(num)]["day_weather"])
        day_wind_direction.append(weather_days["%s" %(num)]["day_wind_direction"])
        day_wind_power.append(weather_days["%s" %(num)]["day_wind_power"])
        max_degree.append(weather_days["%s" %(num)]["max_degree"])
        min_degree.append(weather_days["%s" %(num)]["min_degree"])
        night_weather.append(weather_days["%s" %(num)]["night_weather"])
        night_wind_direction.append(weather_days["%s" %(num)]["night_wind_direction"])
        night_wind_power.append(weather_days["%s" %(num)]["night_wind_power"])
        time.append(weather_days["%s" %(num)]["time"])
        weather_day.append([day_weather[num],
                       day_wind_direction[num],
                       day_wind_power[num],
                       max_degree[num],
                       min_degree[num],
                       night_weather[num],
                       night_wind_direction[num],
                       night_wind_power[num],
                       time[num]])
        num += 1
    # print(weather_day)
    weather_today = ("今天(%s)白天的天气为%s，%s，风力%s级，晚间的天气为%s，%s，风力%s级，最高温度%s℃，最低温度%s℃。" 
          % (weather_day[1][8], weather_day[1][0], weather_day[1][1], weather_day[1][2], weather_day[1][5],
          weather_day[1][6], weather_day[1][7], weather_day[1][3], weather_day[1][4]))
    weather_tomorrow = ("明天(%s)白天的天气为%s，%s，风力%s级，晚间的天气为%s，%s，风力%s级，最高温度%s℃，最低温度%s℃。" 
          % (weather_day[2][8], weather_day[2][0], weather_day[2][1], weather_day[2][2], weather_day[2][5],
          weather_day[2][6], weather_day[2][7], weather_day[2][3], weather_day[2][4]))
    weather_the_3rd_day = ("后天(%s)白天的天气为%s，%s，风力%s级，晚间的天气为%s，%s，风力%s级，最高温度%s℃，最低温度%s℃。" 
          % (weather_day[3][8], weather_day[3][0], weather_day[3][1], weather_day[3][2], weather_day[3][5],
          weather_day[3][6], weather_day[3][7], weather_day[3][3], weather_day[3][4]))
    weather_days = [weather_today, weather_tomorrow, weather_the_3rd_day]
    return(weather_days)
        
    
def main():
    info = input("请输入指令【1】获取24小时天气预报【2】获取当前AQI指数【3】获取未来三天天气预报：")
    if int(info) == 1:
        print(get_hours())
    elif int(info) == 2:
        print(get_aqi())
    elif int(info) == 3:
        print(get_days())
    else:
        print("请输入正确的指令！")
        main()
        
if __name__ == "__main__":
    main()
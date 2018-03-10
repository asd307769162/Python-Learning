import requests
import bs4
import time


def open_url(url):
    res = requests.get(url)
    res = res.content.decode('utf-8')
    # print(res.status_code)
    
    soup = bs4.BeautifulSoup(res, 'html.parser')
    return(soup)


def get_today():
    today_date = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    
    url = 'http://www.weather.com.cn/weather1d/101020400.shtml'
    soup = open_url(url)
    weather = soup.find('div', class_="sk")
    today_humidity = weather.find('div', class_="zs h")
    print(today_humidity)
    

    
    
def get_tomorrow():
    url = 'http://www.weather.com.cn/weather/101020400.shtml'
    soup = open_url(url)
    weather = soup.find('li',class_="sky skyid lv2")
    tomorrow_date = weather.find('h1').text[0:2].replace("\n","")
    tomorrow_wea = weather.find('p', class_ = "wea").text.replace("\n","")
    tomorrow_tem = weather.find('p', class_ = "tem").text.replace("\n","")
    tomorrow_win = weather.find('p', class_ = "win").text.replace("\n","")

    '''
    print(tomorrow_date)
    print(tomorrow_tem)
    print(tomorrow_wea)
    print(tomorrow_win)
    '''
    
    tomorrow_weather = [tomorrow_date,tomorrow_tem,tomorrow_wea,tomorrow_win]
    # print(tomorrow_weather)
    
    return(tomorrow_weather)

def get_the_day_after_tom():
    pass


def Main():
    date = input("请输入获取的天气日期（1为今天，2为明天，3为后天)：")
    if date == "1":
        get_today()
    elif date == "2":
        get_tomorrow()
    elif date == "3":
        get_the_day_after_tom()
        
if __name__ == "__Main__":
    Main()
    

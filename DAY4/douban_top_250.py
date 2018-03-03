import requests
import bs4
import re

def open_url(url):
    # proxies = {"http":"127.0.0.1:1082", "https":"127.0.0.1:1082"}
    headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36 Maxthon/5.1.6.2000'}

    # res = requests.get(url, headers=headers, proxies=proxies)
    res = requests.get(url, headers=headers)

    return res


def find_movies(res):
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    movies = []
    targets = soup.find_all("div",class_="hd")
    for each in targets:
        movies.append(each.a.span.text)
   

    ranks = []
    targets = soup.find_all("span",class_="rating_num")
    for each in targets:
        ranks.append(' 评分：%s'%each.text)

    messages = []
    targets = soup.find_all("div", class_="bd")
    for each in targets:
        try:
            messages.append(each.p.text.split('\n')[1].strip()+each.p.text.split('\n')[2].strip())
        except:
            continue

    result = []
    length = len(messages)

    for i in range(length):
        result.append(movies[i]+ranks[i]+messages[i]+'\n')

    return result

def find_depth(res):
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    depth = soup.find('span', class_="next").previous_sibling.previous_sibling.text

    return int(depth)

def main():
    host = "https://movie.douban.com/top250"
    res = open_url(host)
    depth = find_depth(res)

    result = []

    for i in range(depth):
        url = host+"?start="+str(25*i)
        res=open_url(url)
        result.extend(find_movies(res))

        with open("豆瓣电影Top250.txt", "w", encoding = "utf-8") as f:
            for each in result:
                f.write(each)
  
if __name__=="__main__":
    main()

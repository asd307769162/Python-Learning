import requests
import json

def get_hot_comments(res, name_id):
    comments_json = json.loads(res.text)
    hot_comments = comments_json['hotComments']
    with open('hot_comments_'+str(name_id)+'.txt', 'w', encoding='utf-8') as file:
        for each in hot_comments:
            file.write(each['user']['nickname']+':\n\n')
            file.write(each['content']+'\n')
            file.write("-----------------------------------------\n")


def get_name_id(url):
    name_id = url.split('=')[1]
    print(name_id)
    return name_id

def get_comments(url, name_id):
    headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36',
               'referer':url}

    params = "/uIpR7XTeEu5BO9pgI5jg1togXrbN5u9Myk/rGFXDylC+sO8YOK9k6atCmNmGFLCvNq8txmtCmDtKB4UAduLNjLBTqG6Da/C1ECMIT8uNsgegmCXbF7Q/Ub0bcsqorTUa5ySGBQfl0VZ3MnxoJ6nIcsVVUXEWN5x14vid8e/avUu2e7UthEbdipaffYxV+Pw"
    encSecKey = 'bd4f0c5d56bc3a6bee3466d303dfe8d43c7f9f3ae040c6edc890ca8940f7ad708bb6a3e13633b87e7172c2fb50b600c3d33e94c6e7ba45817387fe63783148367943c9842e573654d7dfe901f5f5cfa03e0323e79f29d2b5d70dde8ac674a3f80fd6d03eee7ecac2be5891dc8841f86ee70b83f56a6e91aaca40cbe0671f702f'

    data = {
        "params":params,
        "encSecKey":encSecKey}

    target_url="http://music.163.com/weapi/v1/resource/comments/R_SO_4_{}?csrf_token=".format(name_id)
    
    res = requests.post(target_url, headers=headers, data=data)

    return res

def main():
    url = input("请输入链接：")
    name_id = get_name_id(url)
 
    res = get_comments(url, name_id)
 
    hot_comments = get_hot_comments(res, name_id)



if __name__=="__main__":
    main()

import requests





url = "http://api.ltp-cloud.com/analysis/?"

args = {
        'api_key':'O1w6c8Q2I34QLSBMqezoEAbjRpzf3sab7NuvKCjU',
        'text':'测试',
        'pattern':'ws',
        'format':'json'
        }

res = requests.get(url, args)



content = res.content.decode('utf-8')

print(content)

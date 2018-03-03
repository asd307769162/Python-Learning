import requests
import bs4


url = "http://you.ctrip.com/sight/chongming571/5681.html"

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36}',
           'Cookie':'StartCity_Pkg=PkgStartCity=2; _abtest_userid=e74c1d70-50d9-43c3-8c86-0b21452c223f; UM_distinctid=16155888ba7a2-07430e799076d7-4353468-144000-16155888ba82fc; _RSG=mIa4qcNeaO2oqJerQlY88A; _RDG=28496414ac40d72e9532746a41ac46f315; _RGUID=2624a179-b412-44b0-a208-8af6b5a13d32; _ga=GA1.2.1140136322.1517558470; MKT_Pagesource=PC; CNZZDATA1256793290=157138234-1517557503-http%253A%252F%252Fwww.ctrip.com%252F%7C1517557503; bdshare_firstime=1517558477763; Customer=HAL=ctrip_gb; _gid=GA1.2.1290549758.1518148629; appFloatCnt=4; manualclose=1; ASP.NET_SessionSvc=MTAuOC4xODkuNTN8OTA5MHxqaW5xaWFvfGRlZmF1bHR8MTUxMTI1OTIwNzU5NQ; _RF1=116.224.215.31; Session=smartlinkcode=U130026&smartlinklanguage=zh&SmartLinkKeyWord=&SmartLinkQuary=&SmartLinkHost=; Union=AllianceID=4897&SID=130026&OUID=&Expires=1518782732056; __zpspc=9.4.1518177932.1518177932.1%232%7Cwww.baidu.com%7C%7C%7C%7C%23; _jzqco=%7C%7C%7C%7C%7C1.443470209.1517558469937.1518148629385.1518177932087.1518148629385.1518177932087.0.0.0.4.4; Mkt_UnionRecord=%5B%7B%22aid%22%3A%224897%22%2C%22timestamp%22%3A1518177945508%7D%5D; _bfi=p1%3D290510%26p2%3D290510%26v1%3D12%26v2%3D11; _bfa=1.1517558467111.2j1um.1.1518148624801.1518177680566.4.21; _bfs=1.11',
           'Content-Type':'application/x-www-form-urlencoded',
           'Accept-Encoding':'gzip, deflate',
           }

res = requests.get(url, headers=headers).content.decode('utf-8')


var_resourceid = res.find("var resourceid")
end = res.find('\"',var_resourceid + 18, var_resourceid + 60)
resourceid = res[var_resourceid + 18: end]


var_resourcetype = res.find("var resourcetype")
end = res.find('\"',var_resourcetype + 20, var_resourcetype + 60)
resourcetype = res[var_resourcetype + 20: end]

var_districtid = res.find("var districtid")
end = res.find('\"',var_districtid + 18, var_districtid + 60)
districtid = res[var_districtid + 18: end]

var_districtename = res.find("var districtename")
end = res.find('\"', var_districtename +21, var_districtename + 60)
districtename = res[var_districtename + 21: end]

star = "0.0"

tourist = "0.0"

order = "3.0"

var_poiid = res.find("var poiid")
end = res.find('\"', var_poiid + 14, var_poiid + 60)
poiid = res[var_poiid + 14: end]

page = "1"

resoucetype = "2"


data = {"poiID":poiid,
        "districtId":districtid,
        "districtEName":"districtename",
        "pagenow":page,
        "order":order,
        "star":star,
        "tourist":tourist,
        "resourceId":resourceid ,
        "resoucetype":resoucetype,
        }

print(data)


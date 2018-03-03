import urllib.request
import urllib.parse
import json


def translate(translation):
    url= 'http://fy.iciba.com/ajax.php?a=fy'

    data={}

    data['f']='auto'
    data['t']='auto'
    data['w']=translation

    data=urllib.parse.urlencode(data).encode('utf-8')


    response =urllib.request.urlopen(url,data)
    html=response.read().decode('utf-8')
    
    json.loads(html)
    target=json.loads(html)

    try:
        answer=target['content']['out']
        print('原文：'+translation)
        print('结果：'+answer)
    except:
        answer=target['content']['word_mean']
        print('原文：'+translation)
        n=len(answer)
        i=0
        while i<n:
            print('结果：'+answer[i])
            i=i+1
    else:
        pass
    
        
    translation=input('请输入要翻译的内容：')
    if translation =='':
        input ("请再次回车退出程序")
    else:
        translate(translation)
  

translation=input('请输入要翻译的内容：')
translate(translation)
    

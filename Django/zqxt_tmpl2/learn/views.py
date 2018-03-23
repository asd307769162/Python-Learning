from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def home(request):
    TutorialList = ["HTML", "CSS", "jQuery", "Python", "Django"]

    string = u"这是我的第一个Django网站"


    info_dict = {'site': u'自强学堂', 'content': u'各种IT技术教程'}
    
    List = map(str, range(100))# 一个长度为100的 List


    # return render(request, 'home.html', {'string':string})
    # return render(request, 'home.html', {'TutorialList': TutorialList})
    # return render(request, 'home.html', {'info_dict': info_dict})
    return render(request, 'home.html', {'List': List})



def add(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))

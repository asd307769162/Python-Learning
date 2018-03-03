import thulac


comment = "去过不止一次了，想逛遍森林公园建议还是租个自行车较为明智，不过只有单人或前后双人的，没有适合一家三口或多人的带蓬自行车，希望能增设呢。公园内有不小的房车营地，价格也不低，如果想体验一把的话可以一试。当天是带了娃去看灯光秀的，效果不错，就是排队安排很不人性化，导致人流人为拥堵，管理能力有待加强啊！"


thu = thulac.thulac(seg_only = True)
text = thu.cut(comment, text = True)
print(text)

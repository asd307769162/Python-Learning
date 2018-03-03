import re

while True:

    num = input("请输入一个数字：")

    re1 = re.compile(r'[0-9]{2,4}')

    re2 = re.compile(r'2018-')

    if re1.match(num):
        if re2.match(num):
            print("False")
        else:
            print("True")
    else:
        print("False")

    if num == "-1":
        break
        

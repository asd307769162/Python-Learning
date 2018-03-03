import pymssql
import os

while True:
    name = input("请输入旅游目的地：")
    num = int(input("总计评论数量："))
    i = 1


    server = "localhost"
    user = "sa"
    password = "19980501."
    database = "ChongMing"


    file = open(name+"ERROR.txt", encoding = 'utf-8')
    all_lines = file.readlines()

    origin_info = []
    for line in all_lines:
        origin_info.append(line.split())
        

    info = []
    for each in origin_info:
        if len(each) == 0:
            pass
        else:
            info.append(each)
    

    for each in info:
        # print(each)
        pass
            
    usernames = []
    usercomments = []
    scores = []
    times = []

    t = 0
    while t < num:
        username = info[t][0]
        usercomment = info[num+t][0]
        score = info[2*num+t][0]
        time = info[3*num+t][0]
        
        try:
            conn = pymssql.connect(server, user, password, database)
            cursor = conn.cursor()
            SQL = "insert into origin (username, destination, usercomment, score, time, platform) values ('{0}', '{1}', '{2}', {3}, '{4}', '{5}')".format(username, name, usercomment, score, time, "驴妈妈")
            # print(SQL+";\n")
            t = t+1
            cursor.execute(SQL)
            conn.commit()
            conn.close()
        except:
            file = open(name+"ERROR.txt", "a", encoding = 'utf-8')
            file.write(SQL)
            file.close()
        else:
            pass

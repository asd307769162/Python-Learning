import collections
import pymssql
import os
import time

server = "localhost"
user = "sa"
password = "19980501."
database = "ChongMing"

SQL = "select min(commentID), max(commentID) from analyst"
conn = pymssql.connect(server, user, password, database)
cursor = conn.cursor()
cursor.execute(SQL)
result = cursor.fetchall()
conn.close()
commentID = result[0][0]
commentID_MAX = result[0][1]

time_start_original = time.time()
while commentID <= commentID_MAX:
    time_start = time.time()
    conn = pymssql.connect(server, user, password, database)
    cursor = conn.cursor()
    SQL = "select * from analyst where commentID = {0}".format(commentID)
    cursor.execute(SQL)
    rows = cursor.fetchall()
    conn.close()

    for row in rows:
        word = row[2].replace(" ","")
        SQL = "select * from counts where word = '{0}'".format(word)
        conn = pymssql.connect(server, user, password, database)
        cursor = conn.cursor()
        cursor.execute(SQL)
        word_counted = cursor.fetchall()
        conn.close()
        if len(word_counted) == 0:
            SQL = "select count(*) from analyst where word = '{0}'".format(word)
            conn = pymssql.connect(server, user, password, database)
            cursor = conn.cursor()
            cursor.execute(SQL)
            count = cursor.fetchall()
            conn.close()

            SQL = "insert into counts (word, times) values('{0}', {1})".format(word, count[0][0])
            # print(SQL)
            conn = pymssql.connect(server, user, password, database)
            cursor = conn.cursor()
            cursor.execute(SQL)
            conn.commit()
            conn.close()
    commentID = commentID + 1
    time_used = time.time()-time_start
    time_used_all = time.time()-time_start_original
    print("总耗时："+str(time_used_all)+"\n单项耗时："+str(time_used)+"\n")
     

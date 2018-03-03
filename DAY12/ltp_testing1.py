#encoding=utf-8
import requests
import bs4
import re
import time
import os
import random
import pymssql
import json
import jieba


def get_comments_maxid():
    server = "localhost"
    user = "sa"
    password = "19980501."
    database = "ChongMing"

    try:
        conn = pymssql.connect(server, user, password, database)
        cursor = conn.cursor()
        SQL = "select max(id) from origin"
        # print(SQL)
        cursor.execute(SQL)
        rows = cursor.fetchall()  
        conn.close()
        num = (rows[0][0])
        print(num)
    except:
        print("查询时数据库链接故障")

    return int(num)


def get_comments(num):
    time_start = time.time()
    server = "localhost"
    user = "sa"
    password = "19980501."
    database = "ChongMing"


    # print(SQL)
    i = int(input("请输入开始的评论id："))

    while i < num:
        conn = pymssql.connect(server, user, password, database, charset='utf8')
        cursor = conn.cursor()
        SQL = "select * from origin where id >= {0} and id <= {1}".format(i, i+99).encode("utf8")
        print(SQL)
        cursor.execute(SQL)
        rows = cursor.fetchall() 
        conn.close()
        for row in rows:
            # print(row[3])
            print("\n正在分句")
            details = fenju(row[3])
            commentID = row[0]
            for each in details:
                # print("正在分词")
                results = fenci(each)
                write(results, commentID)
            time_end = time.time()
            time_use = time_end - time_start
            print("第"+str(commentID)+"条评论写入完成，已耗时"+str(time_use)+"秒")  
            commentID = commentID + 1
        i = i + 100

    
def fenju(comment):
    details = comment.split("。")
    # print("分句完成")
    # for each in details:
        # print(each)
    return details


def fenci(detail):
    seg_list = jieba.cut(detail)
    return seg_list

def write(results, commentID):
    compile_comment = re.compile(r'(^[\u4e00-\u9fa5]{0,}$)+')
    for each in results:
        if compile_comment.match(each):
            # print("\n\n\n"+each)
            server = "localhost"
            user = "sa"
            password = "19980501."
            database = "ChongMing"
            
            conn = pymssql.connect(server, user, password, database)
            cursor = conn.cursor()
            SQL = "insert into analyst (commentID, word) values('{0}', '{1}')".format(commentID, each)
            # print(SQL)
            cursor.execute(SQL)
            conn.commit()
            conn.close()
                
def main():


    num = get_comments_maxid()
    comments = get_comments(num)
    
if __name__ == "__main__":
    main()

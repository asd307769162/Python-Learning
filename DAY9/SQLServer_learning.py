import pymssql

server = "localhost"
user = "sa"
password = "19980501."
database = "Ctrip"

conn = pymssql.connect(server, user, password, database)

cursor = conn.cursor()


# 增加
SQL = "insert into Ctrip (username, destination, usercomment, score) values ('SQL测试用户', 'SQL测试目的地','SQL测试评论',60)"

cursor.execute(SQL)

conn.commit()

# 选择
SQL = "select * from Ctrip"

cursor.execute(SQL)

rows = cursor.fetchall()

conn.close()

for row in rows:
    print(row[4])

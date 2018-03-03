import pymssql
import time

server = "localhost"
user = "sa"
password = "19980501."
database = "ChongMing"

SQL = 'select * from analyst'

conn = pymssql.connect(server, user, password, database)
cursor = conn.cursor()
cursor.execute(SQL)
results = cursor.fetchall()
conn.close()


num = (len(results))
i = 0

word = []
commentID = []

for each in results:
     word.append((each[2].replace(" ","")))
     commentID.append(each[1])
  


while i < num:
    i0 = i
    list1= ['很不','很','非常','有点','还','不','没有','没','挺','比较','蛮','没什么','总体','更','不能','实在','不是','不太']

    while word[i] in list1:
        new_word = word[i] + word[i+1]
        i = i + 1
    
    if i0 != i:
        print(new_word)
    else:
        print(word[i])

    i = i + 1

        
    '''
    try:
        SQL = "insert into analysted (commentID, word) values ({0},'{1}')".format(commentID[i], new_word)
    except:
        SQL = "insert into analysted (commentID, word) values ({0},'{1}')".format(commentID[i], word[i])

    print(SQL)        
    i = i + 1
    '''


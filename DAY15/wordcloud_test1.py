from wordcloud import WordCloud
import pymssql

server = "localhost"
user = "sa"
password = "19980501."
database = "ChongMing"

SQL = 'select * from counts2'

conn = pymssql.connect(server, user, password, database)
cursor = conn.cursor()
cursor.execute(SQL)
results = cursor.fetchall()
conn.close()

myWords = []
for result in results:
    myWords.append((result[1].replace(" ",""), result[2]))
    # print(myWords)

wc = WordCloud(
            # 设置字体
            font_path = r'C:\Windows\Fonts\SimHei.ttf',
            # 设置背景色
            background_color='white',
            # 允许最大词汇
            max_words=20,
            # 词云形状
            # mask=bg_pic,
            # 最大号字体
            max_font_size=100,
            # 设置宽度
            width = 500,
            # 设置高度
            height = 500
            )


# 生成词云
wc.generate_from_frequencies(dict(myWords))

import matplotlib.pyplot as plt
plt.imshow(wc)
plt.axis("off")
plt.show()
wc.to_file('test2.png')

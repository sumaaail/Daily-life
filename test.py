# import sqlite3
# from flask import jsonify
# conn = sqlite3.connect('database.db')
# c = conn.cursor()
# print('connected successfully')
# # print([0 == len(''.join(node)) for node in c.execute("SELECT pwd FROM user WHERE uid = 5")])
# data = []
# # for row in c.execute("SELECT pwd FROM user WHERE uid = 5"):
# #     data.append(row)
# # print(jsonify(data))
# # print('xhr' in [node[0] for node in c.execute("SELECT uname FROM user ")])
# c.execute("INSERT INTO user [('uname', 'pwd', 'phone')] VALUES ('maomao', '1234', '1333')")
# conn.commit()
# print('inserted successfully')
# conn.close()

# data = b'{"password":"12313","username":"33"}'
# st = str(data,encoding="utf-8")
# print(st)
# dic = eval(st)
# print(dic['username'])

# data = ['asd', '123', 'xxx']
# print(type(tuple(data)))
# print(type(str(tuple(data))))
import time
from operation.operation import Operation
import newspaper
from newspaper import Article
from newspaper import news_pool
from newspaper import fulltext

def get_news(paper, num):
    print("begin to fetch {}".format(paper.brand))
    news_title = []
    news_text = []

    table = "news"
    columns = str(('title', 'text'))
    print("{} length".format(paper.brand),len(paper.articles))
    for article in paper.articles[:num]:
        time.sleep(0.01)

        for i in range(6):
            try:

                print(i)
                atc = Article(article.url)
                atc.download()
                atc.parse()
                print(atc.title)
                values = str((atc.title,atc.text))
                op = Operation
                op.db_insert(table, columns, values)
                # news_title.append(atc.title)
                # news_text.append(atc.text)
                break
            except Exception as e:
                if i > 5:

                    print(e)
                    continue
                else:
                    time.sleep(0.5)
    print("cache complete")
print("start caching")
# <newspaper.source.Source object at 0x7f9a82393d10> by print
qq_paper = newspaper.build('https://www.news.qq.com/', language='zh', memorize_articles=False)
print("qq build complete")
wired_paper = newspaper.build('https://wired.com', language='en', memorize_articles=False)
print("wired build complete")
cnet_paper = newspaper.build('https://cnet.com', language='en', memorize_articles=False)
print("cnet build complete")
south_paper = newspaper.build('http://southcn.com', language='zh', memorize_articles=False)
print("southcn build complete")
papers = [south_paper, qq_paper, wired_paper, cnet_paper]

# 4 * 2 = 8 threads
# news_pool.set(papers, threads_per_source=2)
# news_pool.join()
# print("pool join complete")

for paper in papers:
    get_news(paper,20)    # the 2th param means the maximum news in one fetch of one paper

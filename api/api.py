from operation.operation import Operation





# UserLogin and registration


# input the uname for uid
def select_id_by_uname(cmd):
    table = 'user'
    column = ['uid']
    constraint = ' WHERE uname = "{}"'.format(cmd)
    op = Operation()
    data = op.db_select(table, column, constraint)
    print(type(data))
    return data


# input the table name for selection
def select_all(cmd):
    table = cmd
    columns = '*'
    op = Operation()
    data = op.db_select(table, columns)
    print(type(data))
    return data


# input the uname for check
def select_uname(cmd):
    table = 'user'
    column = ['uname']
    op = Operation()
    data = op.db_select(table, column)
    print(type(data), data)
    return data


# input the uname to login
def select_pwd_by_uname(cmd):
    table = 'user'
    column = ['pwd']
    constraint = ' WHERE uname = "{}"'.format(cmd)
    op = Operation()
    data = op.db_select(table, column, constraint)
    print(type(data), data)
    return data


# input the values for registration
def user_register(cmd):
    table = 'user'
    columns = str(('uname', 'pwd', 'phone'))
    values = str(tuple(cmd))
    op = Operation()
    op.db_insert(table, columns, values)
    return 1


# input the uname for delete account
def delete_account_by_uname(cmd):
    table = 'user'
    constraint = ' WHERE uname = "{}"'.format(cmd)
    op = Operation()
    op.db_delete(table,constraint)
    return 1
################################################################################################

# favourite table

# input the values for save favourites
def insert_fav(cmd):
    table = 'fav'
    columns = str(('uid', 'fav'))
    values = str(tuple(cmd))
    op = Operation()
    op.db_insert(table, columns, values)
    return 1


# input the uid to fetch the fav
def select_fav_by_uid(cmd):
    table = 'fav'
    column = str(('fav',))
    constraint = ' WHERE uid = {}'.format(cmd)
    op = Operation()
    data = op.db_select(table, column, constraint)
    return data


#########################################################################################################

import time
import pandas as pd
import newspaper
from newspaper import Article
from newspaper import news_pool
from newspaper import fulltext

def get_news(paper, num):
    print("begin to fetch {}".format(paper.brand))
    news_title = []
    news_text = []
    op = Operation
    table = "news"
    columns = str(('title', 'text'))

    for article in paper.articles[:num]:
        time.sleep(0.01)

        for i in range(6):
            try:

                atc = Article(article.url)
                atc.download()
                atc.parse()
                print(atc.title)
                values = str((atc.title,atc.text))
                op.db_insert(table, columns, values)
                # news_title.append(atc.title)
                # news_text.append(atc.text)
                break
            except Exception as e:
                if i > 5:

                    print(e)
                    break
                else:
                    time.sleep(0.5)
    print("cache complete")
    # paper_data = pd.DataFrame({'title': news_title, 'text': news_text})
    # return paper_data
    # paper_data.to_csv('{}_news.txt'.format(paper.brand))
    # print("news saved")



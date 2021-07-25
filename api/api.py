from operation.operation import Operation
import requests
from datetime import datetime, timedelta
from lxml import etree
from time import sleep
from random import randint
from nlp import *


# 测试数据库能否连接的demo
def demo_select(cmd):
    table = 'students'
    columns = ['NAME', 'ADDRESS']
    constraint = ' where ' + 'ID = 2'
    op = Operation()
    data = op.db_select(table, columns, constraint)
    return data


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
    op.db_delete(table, constraint)
    return 1


def changepassword(cmd):
    table = 'user'
    columns = 'pwd'
    values = "{}".format(cmd[1])
    print("values: ", values)
    constraint = ' WHERE uname = "{}"'.format(cmd[0])
    op = Operation()
    op.db_update(table, columns, values, constraint)
    print("update pwd successfully")
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
    column = ['fav']
    constraint = ' WHERE uid = {}'.format(cmd)
    op = Operation()
    data = op.db_select(table, column, constraint)
    return data


# get keywords of fav


def getKeywords():
    table = 'fav'
    column = ['fav']
    op = Operation()
    data = op.db_select(table, column)

    pos = False
    text = str(data)
    seg_list = seg_to_list(text, pos)
    filter_list = word_filter(seg_list, pos)

    print("the result of TF-IDF model: ")
    tfidf_extract(filter_list)
    return tfidf_extract(filter_list)


#########################################################################################################

# news
# spyder


news = []


def parseTime(unformatedTime):
    if '分钟' in unformatedTime:
        minute = unformatedTime[:unformatedTime.find('分钟')]
        minute = timedelta(minutes=int(minute))
        return (datetime.now() -
                minute).strftime('%Y-%m-%d %H:%M')
    elif '小时' in unformatedTime:
        hour = unformatedTime[:unformatedTime.find('小时')]
        hour = timedelta(hours=int(hour))
        return (datetime.now() -
                hour).strftime('%Y-%m-%d %H:%M')
    else:
        return unformatedTime


def dealHtml(html):
    results = html.xpath('//div[@class="result-op c-container xpath-log new-pmd"]')

    for result in results:
        try:
            link = result.xpath('.//@mu')[0]

            title = result.xpath('.//h3/a')[0]

            title = title.xpath('string(.)').strip()

            summary = result.xpath('.//span[@class="c-font-normal c-color-text"]')[0]
            summary = summary.xpath('string(.)').strip()

            # ./ 是直接下级，.// 是直接/间接下级

            infos = result.xpath('.//div[@class="news-source_Xj4Dv"]')[0]
            source, dateTime = infos.xpath(".//span[last()-1]/text()")[0], \
                               infos.xpath(".//span[last()]/text()")[0]

            dateTime = parseTime(dateTime)

            # print('标题', title)
            # print('来源', source)
            # print('时间', dateTime)
            # print('概要', summary)
            # print('链接', link)

            news.append({
                'title': title,
                'source': source,
                'time': dateTime,
                'summary': summary,
                'link': link
            })
        except Exception as e:
            print(e)
            continue


from fake_useragent import UserAgent

ua = UserAgent()
headers = {

    'User-Agent': ua.random,
    'Referer': 'https://www.baidu.com/s?rtt=1&bsst=1&cl=2&tn=news&word=%B0%D9%B6%C8%D0%C2%CE%C5&fr=zhidao'
}

url = 'https://www.baidu.com/s'

params = {
    'ie': 'utf-8',
    'medium': 0,
    # rtt=4 按时间排序 rtt=1 按焦点排序
    'rtt': 1,
    'bsst': 1,
    'rsv_dl': 'news_t_sk',
    'cl': 2,
    'tn': 'news',
    'rsv_bp': 1,
    'oq': '',
    'rsv_btype': 't',
    'f': 8,
}


def doSpider(keyword, sortBy='focus'):
    '''
    :param keyword: 搜索关键词
    :param sortBy: 排序规则，可选：focus(按焦点排序），time(按时间排序），默认 focus
    :return:
    '''

    params['wd'] = keyword
    if sortBy == 'time':
        params['rtt'] = 4

    with requests.get(url=url, params=params, headers=headers, timeout=2) as response:

        html = etree.HTML(response.text)

    dealHtml(html)
    total = html.xpath('//div[@id="header_top_bar"]/span/text()')[0]

    total = total.replace(',', '')
    try:
        total = int(total[7:-1])
    except Exception as e:
        print(e)
        return [-1, ]

    pageNum = total // 10
    print("total news num: {}\n page num: {}".format(total, pageNum))  # 十条资讯一页
    # for page in range(1, pageNum):
    for page in range(1, 2):  # 只爬取第一页
        print('第 {} 页\n\n'.format(page))
        headers['Referer'] = response.url
        params['pn'] = page * 10

        with requests.get(url=url, params=params, headers=headers, timeout=2) as response:
            html = etree.HTML(response.text)

        dealHtml(html)

        sleep(randint(2, 4))

    return news


##############################################################################################################



from api.api import *
from flask import Blueprint, request, Response, render_template, make_response,jsonify

news = Blueprint('news',__name__)



@news.route('/getnews')
def newsCache():
    print("start caching")
    # <newspaper.source.Source object at 0x7f9a82393d10> by print
    lifehacker_paper = newspaper.build('https://www.lifehacker.com/', language='en')
    print("lifehacker build complete")
    wired_paper = newspaper.build('https://wired.com', language='en')
    print("wired build complete")
    cnet_paper = newspaper.build('https://cnet.com', language='en')
    print("cnet build complete")
    south_paper = newspaper.build('http://southcn.com', language='zh')
    print("southcn build complete")
    papers = [south_paper, lifehacker_paper, wired_paper, cnet_paper]

    # 4 * 2 = 8 threads
    # news_pool.set(papers, threads_per_source=2)
    # news_pool.join()
    # print("pool join complete")

    for paper in papers:
        get_news(paper,10)    # the 2th param means the maximum news in one fetch of one paper



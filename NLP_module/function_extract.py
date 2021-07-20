from topic_model import TopicModel
from contract_method import *
from tf_idf import Tf_Idf


def tfidf_extract(word_list, pos=False, keyword_num=10):
    doc_list = load_data(pos)
    idf_dic, default_idf = train_idf(doc_list)
    tfidf_model = Tf_Idf(idf_dic, default_idf, word_list, keyword_num)
    tfidf_model.get_tfidf()

def textrank_extract(text, pos=False, keyword_num=10):
    textrank = analyse.textrank
    keywords = textrank(text, keyword_num)
    # extract some keyword
    for keyword in keywords:
        print(keyword+'/',end='')
    print()

def topic_extract(word_list, model, pos=False, keyword_num=10):
    doc_list = load_data(pos)
    topic_model = TopicModel(doc_list,keyword_num,model=model)
    topic_model.get_simword(word_list)
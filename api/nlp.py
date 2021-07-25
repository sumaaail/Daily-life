import math
import jieba
import jieba.posseg as psg
import functools
import numpy as np


class Tf_Idf(object):
    def __init__(self, idf_dic, default_idf, word_list, keyword_num):
        """

        :param idf_dic: trained idf dictionary
        :param default_idf: default idf dictionary
        :param word_list: processed document for selecting important words
        :param keyword_num: number of the importance words
        """
        self.idf_dic, self.default_idf = idf_dic, default_idf
        self.word_list = word_list
        self.tf_dic = self.get_tf_dic()  # calculate the tf value
        self.keyword_num = keyword_num

    def get_tf_dic(self):
        # calculate the tf value
        tf_dic = {}
        for word in self.word_list:
            tf_dic[word] = tf_dic.get(word, 0.0) + 1.0
        tt_count = len(self.word_list)
        for k, v in tf_dic.items():
            tf_dic[k] = float(v) / tt_count
        return tf_dic

    def get_tfidf(self):
        # calculate the tf-idf value
        tfidf_dic = {}
        for word in self.word_list:
            idf = self.idf_dic.get(word, self.default_idf)
            tf = self.tf_dic.get(word, 0)
            tfidf = tf * idf
            tfidf_dic[word] = tfidf
        tfidf_dic.items()
        k_word = []
        for k, v in sorted(tfidf_dic.items(), key=functools.cmp_to_key(cmp), reverse=True)[:self.keyword_num]:
            k_word.append(k)

        return k_word


def get_stopword_list():
    stop_word_path = 'api/stopword.txt'
    stopword_list = [sw.replace('\n', '') for sw in open(stop_word_path, encoding="utf-8").readlines()]
    return stopword_list


# token
def seg_to_list(sentence, pos=False):
    """

    :param sentence:
    :param pos: if mark the lexical category
    :return:
    """
    if not pos:
        seg_list = jieba.cut(sentence)
    else:
        seg_list = psg.cut(sentence)
    return seg_list


# filter the interruption
def word_filter(seg_list, pos=False):
    """

    1: filter according to the token result
    2: consider whether to filter other lexical category than nouns according to @param pos
    3: judge whether in stop_word_list and the length
    """
    stopword_list = get_stopword_list()
    filter_list = []
    for seg in seg_list:
        if not pos:
            word = seg
            flag = 'n'  # if pos=False, all the words are marked as 'nouns' and kept
        else:
            word = seg.word
            flag = seg.flag
        if not flag.startswith('n'):
            continue
        if not word in stopword_list and len(word) > 1:
            filter_list.append(word)
    return filter_list


# load the dataset, do tokenization and filter
def load_data(pos=False, corpus_path='api/corpus.txt'):
    """
    process the dataset, after it only interference words remain in each doc
    :param pos: if mark the word
    :param corpus_path: path to dataset
    :return:
    """
    doc_list = []
    for line in open(corpus_path, 'r', encoding="utf-8"):
        content = line.strip()  # get data of each line
        seg_list = seg_to_list(content, pos)  # tokenization
        filter_list = word_filter(seg_list, pos)  # filter the stopword
        doc_list.append(filter_list)
    return doc_list


def train_idf(doc_list):
    """

    generate the IDF dictionary according to 'doc_list' for get 'TF-IDF' later
    """
    idf_dic = {}
    tt_count = len(doc_list)  # total count of doc in doc_list
    # count the number of occurrences of each word in the doc
    for doc in doc_list:
        for word in set(doc):
            idf_dic[word] = idf_dic.get(word, 0.0) + 1.0
    # transform to idf value and add 1 to dominator for flatten process
    for k, v in idf_dic.items():
        idf_dic[k] = math.log(tt_count / (v + 1.0))
    # for those which doesnt occur in the dictionary, by default its best to appear in a document and get the default
    # idf value
    default_idf = math.log(tt_count / 1.0)
    return idf_dic, default_idf


def tfidf_extract(word_list, pos=False, keyword_num=5):
    doc_list = load_data(pos)
    idf_dic, default_idf = train_idf(doc_list)
    tfidf_model = Tf_Idf(idf_dic, default_idf, word_list, keyword_num)
    return tfidf_model.get_tfidf()


def cmp(e1, e2):
    res = np.sign(e1[1] - e2[1])
    if res != 0:  # sort by importance value
        return res
    else:  # if the numbers equal, sort by word
        a = e1[0] + e2[0]
        b = e2[0] + e1[0]
        if a > b:
            return 1
        elif a == b:
            return 0
        else:
            return -1

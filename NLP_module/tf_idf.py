from contract_method import *

class Tf_Idf(object):
    def __init__(self, idf_dic, default_idf, word_list, keyword_num):
        '''

        :param idf_dic: trained idf dictionary
        :param default_idf: default idf dictionary
        :param word_list: processed document for selecting important words
        :param keyword_num: number of the importance words
        '''
        self.idf_dic, self.default_idf = idf_dic, default_idf
        self.word_list = word_list
        self.tf_dic = self.get_tf_dic() # calculate the tf value
        self.keyword_num = keyword_num

    def get_tf_dic(self):
        # calculate the tf value
        tf_dic = {}
        for word in self.word_list:
            tf_dic[word] = tf_dic.get(word,0.0)+1.0
        tt_count = len(self.word_list)
        for k, v in tf_dic.items():
            tf_dic[k] = float(v)/tt_count
        return tf_dic

    def get_tfidf(self):
        # calculate the tf-idf value
        tfidf_dic = {}
        for word in self.word_list:
            idf = self.idf_dic.get(word,self.default_idf)
            tf = self.tf_dic.get(word,0)
            tfidf = tf*idf
            tfidf_dic[word] = tfidf
        tfidf_dic.items()
        for k, v in sorted(tfidf_dic.items(), key=functools.cmp_to_key(cmp),reverse=True)[:self.keyword_num]:
            print(k + '/', end='')
        print()

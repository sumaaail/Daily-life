import functools
import math

from contract_method import *
# realize LSI, LDA method
class TopicModel(object):
    def __init__(self, doc_list, keyword_num, model='LSI', num_topics=4):
        '''

        :param doc_list: dataset processed after function 'load_data'
        :param keyword_num: number of important words
        :param model: LSI or LDA
        :param num_topics: numbers of topics
        '''
        # using gensim interface to transform doc to vector
        # generate dictionary
        self.dictionary = corpora.Dictionary(doc_list)
        # using BOW model to vectorize
        corpus = [self.dictionary.doc2bow(doc) for doc in doc_list]
        self.tfidf_model = models.TfidfModel(corpus)
        self.corpus_tfidf = self.tfidf_model[corpus]
        self.keyword_num = keyword_num
        self.num_topics = num_topics

        # select the model to load
        if model == 'LSI':
            self.model = self.train_lsi()
        else:
            self.model = self.train_lda()

        # get the topic word of the dataset
        word_dic = self.word_dictionary(doc_list)
        self.wordtopic_dic = self.get_wordtopic(word_dic)

    def train_lsi(self):
        lsi = models.LsiModel(self.corpus_tfidf, id2word=self.dictionary, num_topics=self.num_topics)
        return lsi

    def train_lda(self):
        lda = models.LdaModel(self.corpus_tfidf, id2word=self.dictionary, num_topics=self.num_topics)
        return lda

    def get_wordtopic(self, word_dic):
        wordtopic_dic = {}
        for word in word_dic:
            single_list = [word]
            wordcorpus = self.tfidf_model[self.dictionary.doc2bow(single_list)]
            wordtopic = self.model[wordcorpus]
            wordtopic_dic[word] = wordtopic
        return wordtopic_dic

    # cosin simularity
    def calsim(self, l1, l2):
        a, b, c = 0.0, 0.0, 0.0
        for t1, t2 in zip(l1, l2):
            x1 = t1[1]
            x2 = t2[1]
            a += x1 * x1
            b += x1 * x1
            c += x2 * x2
        sim = a / math.sqrt(b * c) if not (b * c) == 0.0 else 0.0
        return sim
    def get_simword(self, word_list):
        # calculate the simularity between word and doc, pick the most similar as  keyword based on keyword_num
        sentcorpus = self.tfidf_model[self.dictionary.doc2bow(word_list)]
        senttopic = self.model[sentcorpus]


        # calculate the simularity between word of input text and topics
        sim_dic = {}
        for k, v in self.wordtopic_dic.items():
            if k not in word_list:
                continue
            sim = self.calsim(v, senttopic)
            sim_dic[k] = sim
        for k, v in sorted(sim_dic.items(), key=functools.cmp_to_key(cmp), reverse=True)[:self.keyword_num]:
            print(k+'/',end='')
        print()

    def word_dictionary(self, doc_list):
        # generate the space of word and vectorization without gensim interface
        dictionary = []
        for doc in doc_list:
            dictionary.extend(doc)
        dictionary = list(set(dictionary))
        return dictionary

    def doc2bowvec(self, word_list):
        vec_list = [1 if word in word_list else 0 for word in self.dictionary]
        return vec_list




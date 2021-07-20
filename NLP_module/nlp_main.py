from function_extract import *
if __name__ == '__main__':
    with open('testdata.txt','r') as f:
        lines = f.readlines()
    text = ''
    for line in lines:
        text += line.strip()



    pos = False
    seg_list = seg_to_list(text,pos)
    filter_list = word_filter(seg_list,pos)

    print("the result of TF-IDF model: ")
    tfidf_extract(filter_list)
    print("the result of TextRank: ")
    textrank_extract(text)
    print("the result of LSI model: ")
    topic_extract(filter_list, 'LSI', pos)
    print("the result of LDA model: ")
    topic_extract(filter_list, 'LDA', pos)
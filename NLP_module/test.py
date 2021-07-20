import jieba.analyse
with open('corpus.txt','r') as f:
    lines = f.readlines()
text = ''
for line in lines:
    text += line.strip()

result = " ".join(jieba.analyse.textrank(sentence=text, topK=5, withWeight=False, allowPOS=('ns', 'n', 'vn', 'v')))
print(result)
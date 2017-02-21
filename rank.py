#coding=utf8
import re
import jieba
from gensim import corpora,models,similarities,utils

etlregex = re.compile(ur"[^\u4e00-\u9f5a0-9]")
def etl(content):
    content = etlregex.sub('',content)
    return content

output = './'

dictionary = corpora.Dictionary.load("./models/all.dic")

tfidfModel = models.TfidfModel.load("./models/allTFIDF.mdl")
indexTfidf = similarities.MatrixSimilarity.load("./models/allTFIDF.idx")

ldaModel = models.LdaModel.load("./models/allLDATopic.mdl")
indexLDA = similarities.MatrixSimilarity.load("./models/allLDATopic.idx")

# query test
query = ''

query_bow = dictionary.doc2bow(filter(lambda x: len(x)>1,map(etl,jieba.cut(query,cut_all=False))))
tfidfvect = tfidfModel[query_bow]
ldavec = ldaModel[tfidfvect]
simstfidf = indexTfidf[tfidfvect]
simlda = indexLDA[ldavec]

# print(simstfidf)
print(simlda)

sort_sims = sorted(enumerate(simlda), key=lambda item: -item[1])
print sort_sims[0:10]

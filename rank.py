# coding=utf8
import jieba
from gensim import corpora, models, similarities

from utils import Utils

docinfo = Utils.loadObject('./data/raw_info')    # load raw doc info to map to real data

dictionary = corpora.Dictionary.load("./models/all.dic")

tfidfModel = models.TfidfModel.load("./models/allTFIDF.mdl")
indexTfidf = similarities.MatrixSimilarity.load("./models/allTFIDF.idx")

ldaModel = models.LdaModel.load("./models/allLDATopic.mdl")
indexLDA = similarities.MatrixSimilarity.load("./models/allLDATopic.idx")

# query test
query = ''

query_bow = dictionary.doc2bow(filter(lambda x: len(x) > 1, map(Utils.sanitize, jieba.cut(query, cut_all=False))))
tfidfvect = tfidfModel[query_bow]
ldavec = ldaModel[tfidfvect]
simstfidf = indexTfidf[tfidfvect]
simlda = indexLDA[ldavec]

# print(simstfidf)
# print(simlda)

sort_sims = sorted(enumerate(simlda), key=lambda item: -item[1])

print sort_sims

print 'top 10 similar: '
for sim in sort_sims[0:10]:
    print docinfo[sim[0]]

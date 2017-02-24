# coding=utf8
import jieba
from gensim import corpora, models, similarities

from utils import Utils

docinfo = Utils.loadObject('./data/raw_info')    # load raw doc info to map to real data

dictionary = corpora.Dictionary.load("./models/all.dic")

tfidfModel = models.TfidfModel.load("./models/allTFIDF.mdl")
indexTfidf = similarities.MatrixSimilarity.load("./models/allTFIDF.idx")


"""
Load LDA models (passes 10 and passes 0)

"""
ldaModel = models.LdaModel.load("./models/allLDATopic.mdl")
indexLDA = similarities.MatrixSimilarity.load("./models/allLDATopic.idx")

# LDA passes = 10
ldaModelP10 = models.LdaModel.load("./models/allLDATopicPass10.mdl")
indexLDAP10 = similarities.MatrixSimilarity.load("./models/allLDATopicPass10.idx")

# query test
query = ''

query_bow = dictionary.doc2bow(filter(lambda x: len(x) > 1, map(Utils.sanitize, jieba.cut(query, cut_all=False))))
tfidfvect = tfidfModel[query_bow]
simstfidf = indexTfidf[tfidfvect]

ldavec = ldaModel[tfidfvect]
simlda = indexLDA[ldavec]
# ldavec = ldaModelP10[tfidfvect]
# simlda = indexLDAP10[ldavec]

# print ldavec    # get topic probability distribution for a document
# print simlda    # similarity matrix result, similarity with all other docs

"""
print all topics with word distribution
"""
# for topic in ldaModelP10.show_topics(10, 10, formatted=True):
#     print topic[1]
#
# print '------------------------华丽的分割线----------------------------'
#
# for topic in ldaModel.show_topics(10, 10, formatted=True):
#     print topic[1]


# sort_sims = sorted(enumerate(simlda), key=lambda item: -item[1])
#
# print 'top 10 similar: '
# for sim in sort_sims[0:10]:
#     print docinfo[sim[0]]

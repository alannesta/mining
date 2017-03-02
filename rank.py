# coding=utf8
import jieba
from gensim import corpora, models, similarities
from utils.utils import Utils

base = './models_v2'

docinfo = Utils.loadObject('./data/raw_info')    # load raw doc info to map to real data

dictionary = corpora.Dictionary.load(base + "/all.dic")

tfidfModel = models.TfidfModel.load(base + "/allTFIDF.mdl")
indexTfidf = similarities.MatrixSimilarity.load(base + "/allTFIDF.idx")


"""
Load LDA models (passes 10 and passes 0)

"""
ldaModel = models.LdaModel.load(base + "/allLDATopic.mdl")
indexLDA = similarities.MatrixSimilarity.load(base + "/allLDATopic.idx")

# LDA passes = 10
ldaModelP10 = models.LdaModel.load(base + "/allLDATopicPass10.mdl")
indexLDAP10 = similarities.MatrixSimilarity.load(base + "/allLDATopicPass10.idx")

# query test
query = ''

query_bow = dictionary.doc2bow(filter(lambda x: Utils.filter_stopwords(x), map(Utils.sanitize, jieba.cut(query, cut_all=False))))
tfidfvect = tfidfModel[query_bow]
simstfidf = indexTfidf[tfidfvect]

# pass 0 LDA models
ldavec = ldaModel[tfidfvect]
simlda = indexLDA[ldavec]

# pass 10 LDA models
ldavecP10 = ldaModelP10[tfidfvect]
simldaP10 = indexLDAP10[ldavecP10]

# print ldavec    # get topic probability distribution for a document
# print simlda    # similarity matrix result, similarity with all other docs

"""
print all topics with word distribution
"""
print 'topic and keywords LDA pass=0: '

for topic in ldaModelP10.show_topics(10, 10, formatted=True):
    print topic[1]

print '------------------------华丽的分割线----------------------------'

print 'topic and keywords LDA pass=10: '

for topic in ldaModel.show_topics(10, 10, formatted=True):
    print topic[1]

print '------------------------华丽的分割线----------------------------'

"""
Finally: top 10 similar content
"""
sort_sims = sorted(enumerate(simlda), key=lambda item: -item[1])

print 'top 10 similar LDA pass=0: '
for sim in sort_sims[0:10]:
    print docinfo[sim[0]]

print '------------------------华丽的分割线----------------------------'

sort_simsP10 = sorted(enumerate(simldaP10), key=lambda item: -item[1])

print 'top 10 similar LDA pass=10: '
for sim in sort_simsP10[0:10]:
    print docinfo[sim[0]]
# coding=utf-8
from gensim import corpora, models, similarities

from utils.utils import Utils

base = './models_v2'

train_set = Utils.loadObject('./data/jieba_fenci')

dictionary = corpora.Dictionary(train_set)
dictionary.save(base + '/all.dic')

# TF-IDF
print('start generating TF-IDF data...')
corpus = [dictionary.doc2bow(text) for text in train_set]
tfidf = models.TfidfModel(corpus)
tfidf.save(base + '/allTFIDF.mdl')
tfidfVectors = tfidf[corpus]

indexTfidf = similarities.MatrixSimilarity(tfidfVectors)
indexTfidf.save(base + '/allTFIDF.idx')

# LDA model training, topic = 10, pass=10
print('start training LDA model (pass=5)...')
lda = models.LdaModel(tfidfVectors, id2word=dictionary, num_topics=10, passes=5)
lda.save(base + "/allLDATopicPass10.mdl")

corpus_lda = lda[tfidfVectors]
indexLDA = similarities.MatrixSimilarity(corpus_lda)
indexLDA.save(base + "/allLDATopicPass10.idx")

# LDA model training, topic = 10, pass=0
print('start training LDA model (pass=0)...')
lda = models.LdaModel(tfidfVectors, id2word=dictionary, num_topics=10)
lda.save(base + "/allLDATopic.mdl")

corpus_lda = lda[tfidfVectors]
indexLDA = similarities.MatrixSimilarity(corpus_lda)
indexLDA.save(base + "/allLDATopic.idx")

from gensim import corpora,models,similarities,utils
import pickle;

fenci = open('./jieba_fenci', 'r')

train_set = pickle.load(fenci);
dictionary = corpora.Dictionary(train_set);
dictionary.save('./all.dic')

# TF-IDF
corpus = [dictionary.doc2bow(text) for text in train_set]
tfidf = models.TfidfModel(corpus)
tfidf.save("./allTFIDF.mdl")

tfidfVectors = tfidf[corpus]
indexTfidf = similarities.MatrixSimilarity(tfidfVectors)
indexTfidf.save("./allTFIDF.idx")

# LDA model training, topic = 10
lda = models.LdaModel(tfidfVectors, id2word=dictionary, num_topics=10)
lda.save("./allLDA50Topic.mdl")

corpus_lda = lda[tfidfVectors]
indexLDA = similarities.MatrixSimilarity(corpus_lda)
indexLDA.save("./allLDA50Topic.idx")


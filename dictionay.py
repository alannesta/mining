# coding=utf-8
import jieba
import codecs
from utils.utils import Utils

raw = codecs.open('./data/raw', encoding='utf-8')
jieba.load_userdict('./data/custom_user_dict')
train_set = []

try:
    for line in raw:
        sList = map(Utils.filter_keywords, jieba.cut(line, cut_all=False))
        # TODO: len > 1 should not be the criteria, should just filter the stop word
        filtered = filter(lambda x: Utils.filter_stopwords(x), sList)
        train_set.append(filtered)
finally:
    raw.close()

Utils.saveObject('./data/jieba_fenci', train_set)    # use pickle to serialize object in binary file

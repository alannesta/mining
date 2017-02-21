import jieba
import pickle
from utils import Utils

raw = open('./data/raw')
fenci = open('./data/jieba_fenci', 'w')
train_set = []

try:
    for line in raw:
        sList = map(Utils.sanitize, jieba.cut(line, cut_all=False))
        # TODO: len > 1 should not be the criteria, should just filter the stop word
        filtered = filter(lambda x: len(x) > 1, sList)
        train_set.append(filtered)
        # print '\\'.join(final)
        # train_set = train_set + filtered;
finally:
    raw.close()

pickle.dump(train_set, fenci)  # serialize to file


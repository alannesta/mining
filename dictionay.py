import jieba
import re
import pickle

raw = open('./raw')
fenci = open('./jieba_fenci', 'w')
train_set = []

# remove useless characters
etlregex = re.compile(ur"[^\u4e00-\u9f5a0-9]")
def etl(content):
    content = etlregex.sub('',content)
    return content

try:
    for line in raw:
        list = map(etl, jieba.cut(line, cut_all=False))
        filtered = filter(lambda x: len(x) > 1, list)
        train_set.append(filtered)
        # print '\\'.join(final)
        # train_set = train_set + filtered;
finally:
    raw.close()

pickle.dump(train_set, fenci)  # serialize to file


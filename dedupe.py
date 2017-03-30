# coding=utf-8
import codecs
from utils.utils import Utils

word_list = []
dictionary_raw = ''
ids = ''
util_instance = Utils()
count = 0

dupe_ids = codecs.open('./data/dupe_ids', mode='w+', encoding='utf-8')
deduped_list = codecs.open('./data/deduped_list', mode='w+', encoding='utf-8')

with codecs.open('./data/raw_mapped', mode='r', encoding='utf-8') as raw:
    for line in raw:
        if count < 500:
            word_list.append(line.strip('\n'))
            count += 1
# print len(wordList)

filter_words = util_instance.generateHightFreq(word_list)
deduped_result = util_instance.remove_dup(word_list, filter_words)

for title in deduped_result['word_list']:
    dictionary_raw += title + '\n'

for id in deduped_result['deleted_ids']:
    ids += id + '\n'

deduped_list.write(dictionary_raw)
dupe_ids.write(ids)

deduped_list.close()
dupe_ids.close()

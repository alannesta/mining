# coding=utf-8
import re
import codecs
from utils.utils import Utils

f = codecs.open('./data/data.sql', mode='r', encoding='utf-8')
raw = codecs.open('./data/raw_dedupe_2', mode='w+', encoding='utf-8')

pattern = re.compile("\(\d+,\'(.*?)\'")

utilInstance = Utils()
result = []
docinfos = []
jointResult = ''

try:
    for line in f:
        result = re.findall(pattern, line)
        if len(result) > 0:
            # since collection is mutated in this function
            filter_words = utilInstance.generateHightFreq(re.findall(pattern, line))
            deduped = utilInstance.remove_dup(re.findall(pattern, line), filter_words)
            for title in deduped:
                docinfos.append(title)
                jointResult += title+'\n'
finally:
    f.close()

Utils.saveObject('./data/raw_info_dedupe', docinfos)     # save a copy of raw info for future reference
raw.write(jointResult)
raw.close()

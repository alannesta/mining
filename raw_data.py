# coding=utf-8
import re
import codecs
from utils.utils import Utils

f = codecs.open('./data/data.sql', mode='r', encoding='utf-8')
raw = codecs.open('./data/raw_mapped', mode='w+', encoding='utf-8')

pattern = re.compile("\((\d+),\'(.*?)\'")

utilInstance = Utils()
result = []
docinfos = []
jointResult = ''

# raw data in the format of: id [tab] title
def build_raw(matches):
    return matches[0] + '\t' + matches[1]

try:
    for line in f:
        result = re.findall(pattern, line)
        if len(result) > 0:
            construct = map(build_raw, result)
            for nline in construct:
                jointResult += nline+'\n'
finally:
    f.close()

# Utils.saveObject('./data/raw_info_dedupe', docinfos)     # save a copy of raw info for future reference
raw.write(jointResult)
raw.close()

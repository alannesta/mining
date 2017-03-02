# coding=utf-8
import re
import codecs
from utils.utils import Utils

f = codecs.open('./data/data.sql', mode='r', encoding='utf-8')
raw = codecs.open('./data/raw', mode='w+', encoding='utf-8')

pattern = re.compile("\(\d+,\'(.*?)\'")

result = []
docinfos = []
jointResult = ''

try:
    for line in f:
        result = re.findall(pattern, line)
        if len(result) > 0:
            # jointResult = jointResult + '\n'.join(result)
            for title in result:
                docinfos.append(title)
                jointResult += title+'\n'
finally:
    f.close()

Utils.saveObject('./data/raw_info', docinfos)     # save a copy of raw info for future reference
raw.write(jointResult)
raw.close()

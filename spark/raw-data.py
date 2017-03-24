# coding=utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf8')

import codecs
import re
from pyspark import SparkContext
from operator import add
import copy

sc = SparkContext("local", "de-deupe task") # replace local with master url

# add dependency modules
sc.addPyFile('/Users/sijin.cao/git/mining/utils/utils.py')
sc.addPyFile('/Users/sijin.cao/git/mining/utils/lcs.py')
# need to reload sys encoding, otherwise utf8 encoded bytes will be decoded via ascii
sqlRaw = sc.textFile('/Users/sijin.cao/git/mining/data/data.sql')
raw = codecs.open('/Users/sijin.cao/Desktop/raw_dedupe_spark', mode='w+', encoding='utf-8')


import utils

utilInstance = utils.Utils()
pattern = re.compile("\(\d+,\'(.*?)\'")

def extract(line):
    return re.findall(pattern, line)

def dedupe(collection):
    jointResult = ''
    part = collection[0:400]
    temp = copy.copy(part)    # shallow copy suffices here
    filter_words = utilInstance.generateHightFreq(temp)
    deduped = utilInstance.remove_dup(part, filter_words)
    for title in deduped:
        jointResult += title+'\n'
    return jointResult

result = sqlRaw.map(extract).filter(lambda x: len(x) > 0).map(dedupe).reduce(add)
raw.write(result)

# result = sqlRaw.map(extract).filter(lambda x: len(x) > 0).collect()
# for matches in result:
#     for title in matches:
#         print title


sc.stop()

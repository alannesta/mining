import re
from utils import Utils

f = open('./data/data.sql')
raw = open('./data/raw', 'w+')

pattern = re.compile("\(\d+,\'(.*?)\'")
# pattern = re.compile(u"[\u4e00-\u9fa5]+")

result = []
docinfos = []
jointResult = ''

try:
    for line in f:
        result = re.findall(pattern, line)
        if (len(result) > 0):
            # jointResult = jointResult + '\n'.join(result)
            for title in result:
                docinfos.append(title)
                jointResult += title+'\n'
finally:
    f.close()

Utils.saveObject('./data/raw_info', docinfos)     # save a copy of raw info for future reference
# jointResult = jointResult + '\n'.join(result)
raw.write(jointResult)
raw.close()

# for word in result:
#     print(word.decode('utf8'))

# coding=utf-8

# http://stackoverflow.com/questions/11536764/how-to-fix-attempted-relative-import-in-non-package-even-with-init-py/27876800#27876800
if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from utils.utils import Utils
import codecs

utilsInstance = Utils()
f = codecs.open('../data/raw', mode='r', encoding='utf-8')
collection = []
dedupe = []
# collection = ['a112233b',
#               'a11d22343b',
#               '12344a',
#               'vvwdweqwqe',
#               'qewqeqd122',
#               'bb112233dd']
count = 0
for line in f:  # each line still contains the line feed '\n'
    if count < 1000:
        collection.append(line)
        dedupe.append(line)
        count += 1

# print len(collection)
# print len(Utils.remove_dup(collection))

filter = utilsInstance.generateHightFreq(collection)
result = utilsInstance.remove_dup(dedupe, filter)
# result = utilsInstance.remove_dup(utilsInstance, dedupe, [])

print len(result)

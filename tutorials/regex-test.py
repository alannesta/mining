# coding=utf-8
import re

# http://stackoverflow.com/questions/11536764/how-to-fix-attempted-relative-import-in-non-package-even-with-init-py/27876800#27876800
if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from utils.utils import Utils

# print(Utils.filter_stopwords)
sList = [u'云盘', u'谷歌', u'百度']
filtered = filter(lambda x: Utils.filter_stopwords(x), sList)
print ','.join(filtered)






# coding=utf-8
import re

# http://stackoverflow.com/questions/11536764/how-to-fix-attempted-relative-import-in-non-package-even-with-init-py/27876800#27876800
if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from utils.utils import Utils

# print(Utils.filter_stopwords)
sList = [u'云盘', u'谷歌', u'百度']
filtered = filter(Utils.filter_stopwords, sList)
print ','.join(filtered)

content = u'测试3?p<>!!卡,?3P?哈'
print Utils.filter_keywords(content)

# coding=utf-8
import re
import pickle
import codecs

class Utils:

    stop_words = [u'的', u'和', u'了', u'是', u'而', u'都', u'与', u'微信', u'QQ', u'qq', u'简介', u'福利', u'打包', u'白菜价', u'网盘', u'验证', u'手势', u'认证', u'购买', u'云盘', u'资源']
    regex_qq = re.compile(r'\d{5,}')

    # only match chinese characters (by unicode range)
    @staticmethod
    def sanitize(content):
        etlregex = re.compile(ur'[^\u4e00-\u9fff]', re.UNICODE)
        content = etlregex.sub('', content)
        return content

    @staticmethod
    def filter_stopwords(word):
        return word not in Utils.stop_words and Utils.regex_qq.match(word) == None and len(word) > 0

    @staticmethod
    def saveObject(filename, obj):
        f = codecs.open(filename, mode='wb')
        pickle.dump(obj, f)
        f.close()
        return True

    @staticmethod
    def loadObject(filename):
        f = codecs.open(filename, mode='rb')
        obj = pickle.load(f)
        f.close()
        return obj
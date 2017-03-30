# coding=utf-8
import re
import pickle
import codecs
import time
import copy

from lcs import DFLCS


class Utils:
    stop_words = [u'的', u'和', u'了', u'是', u'而', u'都', u'与', u'微信', u'QQ', u'qq', u'简介', u'福利', u'打包', u'白菜价', u'网盘',
                  u'验证', u'手势', u'认证', u'购买', u'云盘', u'资源']
    regex_qq = re.compile(r'\d{5,}')

    # only match chinese characters (by unicode range)
    @staticmethod
    def sanitize(content):
        etlregex = re.compile(ur'[^\u4e00-\u9fff]', re.UNICODE)
        content = etlregex.sub('', content)
        return content

    @staticmethod
    def filter_keywords(content):
        wordReg = re.compile(ur'[\u4e00-\u9fff]|3[pP]', re.UNICODE)
        result = re.findall(wordReg, content)  # a list of matching strings
        return ''.join(result)

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

    def remove_dup(self, raw_list, filter_words):
        # each line in the collection contains the id and title in the form of: id [\t] title
        collection = copy.copy(raw_list)

        result = dict() # a map of
        deleted_ids = []

        print('start deduping collection of size: ' + str(len(collection)))
        timestamp = time.time()
        for index1, word1 in enumerate(collection):
            if len(word1) == 0:
                continue
            for index2, word2 in enumerate(collection):
                if index2 > index1 and len(word2) > 0:
                    (maxLen, endIndex) = DFLCS(self.filterHighFreq(word1.split('\t')[1], filter_words), word2.split('\t')[1])
                    if maxLen > 7:
                        deleted_ids.append(word2.split('\t')[0])
                        collection[index2] = ''

        print('time used: ' + str((time.time() - timestamp)))
        result['word_list'] = filter(lambda x: len(x) > 0, collection)
        result['deleted_ids'] = deleted_ids
        return result

    def generateHightFreq(self, raw_list):
        # for generate frequency map, just need words without ids
        collection = copy.copy(map(lambda x: x.strip().split('\t')[1], raw_list))
        timestamp = time.time()
        highFreq = dict()
        for index1, word1 in enumerate(collection):
            if len(word1) == 0:
                continue
            for index2, word2 in enumerate(collection):
                if index2 > index1:
                    (maxLen, endIndex) = DFLCS(word1, word2)
                    commonSub = word1[int(endIndex - maxLen + 1):int(endIndex + 1)]
                    if maxLen > 7:
                        if commonSub in highFreq:
                            highFreq[commonSub] += 1
                        else:
                            highFreq[commonSub] = 1
                        collection[index2] = ''

        print('generate freq time used: ' + str((time.time() - timestamp)))
        return self.extractHighFreq(highFreq)

    def extractHighFreq(self, freq_dict):
        result = []
        for key in freq_dict.keys():
            if freq_dict[key] > 10:
                result.append(key)
        return result

    def filterHighFreq(self, word, filter_list):
        for filter_word in filter_list:
            if filter_word in word:
                return word.replace(filter_word, '')
        return word

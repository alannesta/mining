import re
import pickle

class Utils:
    # remove irrelevant characters
    @staticmethod
    def sanitize(content):
        etlregex = re.compile(ur"[^\u4e00-\u9f5a0-9]")
        content = etlregex.sub('', content)
        return content

    @staticmethod
    def saveObject(filename, obj):
        f = open(filename, 'wb')
        pickle.dump(obj, f)
        f.close()
        return True

    @staticmethod
    def loadObject(filename):
        f = open(filename, 'r')
        obj = pickle.load(f)
        f.close()
        return obj

# coding=utf-8
# -*- coding: utf-8 -*- # 重要的事说两遍

tUnicode = u'卡卡'

print type(tUnicode)
# print tUnicode
print repr(tUnicode)    # underline representation is unicode which could be encoded(via utf8) and persisted as bytes(utf8 bytes)
# print tUnicode.encode('utf-8')
print repr(tUnicode.encode('utf-8'))    # => repr(tStr)
print type(tUnicode.encode('utf-8'))    # from unicode type to str(bytes) type

print '-------------华丽的分割线--------------'

tStr = '卡卡'
print type(tStr)
# print tStr
print repr(tStr)    # underline representation is bytes(utf8 bytes) which could be decoded(via utf8) to meaningful unicode
# print tStr.decode('utf-8')
print repr(tStr.decode('utf-8'))    # => repr(tUnicode)
print type(tStr.decode('utf-8'))    # form str(bytes) type to unicode type

tArr = [u'卡卡', u'拉拉']
print(tArr)
print(str(tArr))
print(repr(tArr))

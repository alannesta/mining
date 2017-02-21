import re;

f = open('./data/data.sql')
raw = open('./data/raw', 'w')

pattern = re.compile("\(\d+,\'(.*?)\'")
# pattern = re.compile(u"[\u4e00-\u9fa5]+")

result = []
jointResult = ''

try:
    for line in f:
        result = re.findall(pattern, line)
        if (len(result) > 0):
            jointResult = jointResult + '\n'.join(result)
finally:
    f.close()

# jointResult = jointResult + '\n'.join(result)
raw.write(jointResult)
raw.close()

# for word in result:
#     print(word.decode('utf8'))



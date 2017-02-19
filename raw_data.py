f = open('./data.sql');
raw = open('./raw', 'w');
import re;

pattern = re.compile("\(\d+,\'(.*?)\'")
# pattern = re.compile(u"[\u4e00-\u9fa5]+")

try:
    for line in f:
        result = re.findall(pattern, line)
finally:
    f.close()

jointResult = '\n'.join(result);
raw.write(jointResult);
raw.close();

# for word in result:
#     print(word.decode('utf8'))



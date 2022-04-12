import re
import string
from collections import Counter

# 全小写
doc = "Everybody in this country should learn how to program a computer, because it teaches you how to think.".lower()

# 用正则表达式提取所有单词并存储为列表
matchObj = re.findall('[a-z]+', doc)
# 初始化字符串
my_str = ''
# 创建迭代器
it = iter(matchObj)
# 遍历迭代器并叠加到字符串
for x in it:
    my_str += x
# a-z26个小写字母存储为列表并创建迭代器
az = [x for x in string.ascii_lowercase]
azit = iter(az)
# 用字符串创建计数器，for循环遍历字母表写入字典
counter = Counter(my_str)
my_dict = {}
for x in azit:
    my_dict[x] = counter[x]
print(
    sorted(my_dict.items(), key=lambda x: x[1], reverse=True)
)


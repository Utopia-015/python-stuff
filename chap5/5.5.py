import re


doc = "Everybody in this country should learn how to program a computer, because it teaches you how to think."
matchList = re.findall('[a-z]+', doc, re.I)
print('输入的句子：\n' + doc)
sortedMatch = sorted(matchList, key=len, reverse=True)
print('最长的5个单词：\n' + str(sortedMatch[:5]))

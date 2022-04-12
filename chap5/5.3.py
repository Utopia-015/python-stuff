import re
my_str = input('输入字符串：')
letter_num = re.findall('[a-zA-Z]', my_str)
digit_num = re.findall(r'\d', my_str)
space_num = re.findall(' ', my_str)
other_num = re.findall('[^a-zA-Z0-9 ]', my_str)
print("""
        你输入了 
        %d 个字母,
        %d 个数字,
        %d 个空格,
        %d 个其他字符。
        """ % (len(letter_num), len(digit_num), len(space_num), len(other_num))
      )

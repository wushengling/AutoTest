# 边界匹配

import re
a = '100000001'
# ^ 匹配输入字符串的开始位置
# $ 匹配输入字符串的结束位置
r = re.findall('^000',a)
r1 = re.findall('000$',a)
print(r)
print(r1)

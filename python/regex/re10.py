# re.sub  字符串替换
# 可以把函数当作参数

import re 
a= 'A83C72D1D86E67'

def convert(value):
    matched = value.group()
    if int(matched) >= 6:
        return '9'
    return '0'

r = re.sub('\d',convert,a)
print(r)
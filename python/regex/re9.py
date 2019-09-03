# re.sub  字符串替换

import re 
a = 'PythonC#JavaPHPC#C#'
def convert(value):
    matched = value.group()
    return '!!'+matched+'!!'

r = re.sub('C#',convert,a)  #count = 0 为全部替换
# b = a.replace('C#','GO')
# print(b)
print(r)


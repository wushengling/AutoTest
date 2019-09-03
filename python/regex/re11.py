# re.match 从字符串的首字母开始匹配，没有则返回None 
# re.search 搜索整个字符串，直到找到，则返回第一个结果
import re
a= 'A83C72D1D8E67'

r = re.match('\d',a)
print(r)
r1 = re.search('\d',a)
print(r1)
r2 = re.findall('\d',a)
print(r2)
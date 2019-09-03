import re
# 'Python' 普通字符   '\d' 元字符
a = 'C0C++7Java8C#9Python6Javascript'
r = re.findall('\d',a)
print(r)
#元字符查询手册
# https://www.runoob.com/regexp/regexp-metachar.html

R = re.findall('\D',a)
print(R)

# 数量词

import re
a = 'python 1111java678php'
r = re.findall('[a-z]{3,6}',a)
# 贪婪 与 非贪婪 ?
print(r)

# * 匹配0次或者无限多次
# + 匹配一次或无限多次
# ? 匹配零次或一次
b = 'pytho0python1pythonn2'
r1 = re.findall('python*',b)
print(r1)
# 概括字符集
# \d  匹配一个数字字符  等价于 [0-9]
# \D 匹配一个非数字字符  等价于 [^0-9]

# \w 匹配字母、数字、下划线  等价于[A-Za-z0-9_]
# \W 匹配非字母、数字、下划线  等价于 [^A-Za-z0-9_]

# \s 匹配任何空白字符，包括空格、制表符、换页符等等 等价于[\f\n\r\t\v]
# \S 匹配任何非空白字符。等价于 [^ \f\n\r\t\v]

# . 匹配除换行符（\n、\r）之外的任何单个字符
import re
a = 'python 1111java&678p\n\r\t\fhp'
r = re.findall('\w',a)
print(r)
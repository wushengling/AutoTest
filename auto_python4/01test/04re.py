#coding:utf-8
"""
re模块
findall:查找,并返回所有符合规则的数据,返回一个list


"""
import re
#findall方法使用
# s1 ="asdasds123asdas123sdasdas123"
# res1 =re.findall("123",s1)
# print(res1)

#单字符
#\d:表示匹配一个数字
# s2 ="asdasds123asdas123sdasdas123"
# res2 = re.findall(r"\d",s2)
# print(res2)
#\D:表示匹配一个非数字
# s3 ="asdasd__s123asdas123sda?!sdas123"
# res3 = re.findall(r"\D",s3)
# print(res3)
#\w:表示匹配一个单词字符(数字,字母,下划线)
# s4 ="asdQWERTYasd__s123asdas123sd # a?!sdas123"
# res4 = re.findall(r"\w",s4)
# print(res4)
#\W:表示匹配一个非单词字符(数字,字母,下划线)
# s5 ="asdQWERTYasd__s123asdas123sd # a?!sda  s123"
# res5 = re.findall(r"\W",s5)
# print(res5)
#\s:表示匹配一个空白(空格键,tab键)
# s6 ="asdQWERTYasd__s123asdas123sd # a?!sda  s123"
# res6 = re.findall(r"\s",s6)
# print(res6)
#\S:表示匹配一个非空白(空格键,tab键)
# s7 ="asdQWERTYasd__s123asdas123sd # a?!sda  s123"
# res7 = re.findall(r"\S",s7)
# print(res7)

# . 表示一个任意字符
# s2 = "adc123ADC?>* ()#  "
# res2 = re.findall(r".",s2)
# print(res2)

#[],匹配[]列举的字符
# s3 = "adc123ADC?>* ()#  "
# res3 = re.findall(r"[123a?D]",s3)
# print(res3)

#表示数量
# s1 ="asdasds12399999999asdas12399999999sdasdas12399999999"
# res1 = re.findall(r'\d{11}',s1)
# print(res1)

#{N,}:表示前面一个字符连续出现N次及以上
# s2 ="asdasds12399999999asdas12399999999111111sdasdas12399999999"
# res2 = re.findall(r'\d{4,}',s2)
# print(res2)
#{N,M}:表示前面一个字符连续出现N到M次
# s3 ="asdasds12399999999asdas12399999999111111sdasdas12399999999"
# res3 = re.findall(r'\d{5,12}',s3)
# print(res3)

#python中正则匹配的时候,默认是开启贪婪模式的
#关闭贪婪模式:?(表示数量,范围的后面加?,就可以关闭贪婪模式)
# s4 ="asdasds12399999999asdas12399999999111111sdasdas12399999999"
# res4 = re.findall(r'\d{5,12}?',s4)
# print(res4)

# * :表示前面的这个字符出现任意次(包括0次)
# s5 = "1234abc123b"
# res5 = re.findall(r"\d*",s5)
# print(res5)

# +: 表示前面的这个字符至少出现一次
# s6 = "1234abc123b"
# res6 = re.findall(r"\d+",s6)
# print(res6)

# ? :表示前一个字符出现0次或者1次
# ? 前是字符,则表示前一个字符出现0次或者1次
# ? 前是表示范围,则是关闭贪婪模式 {n,} {n,m} * +
# s7 = "1234abc123b"
# res7 = re.findall(r"\d?",s7)
# print(res7)

#表示边界
#^:表示字符串开头
#$:表示字符串结尾
# s = "python666java777php888python"
# res = re.findall(r"^python$",s)
# print(res)
#\b:表示单词边界  
# s = "python666 java777php?888python"

# # res = re.findall(r"\bjava",s)
# res = re.findall(r"php\b",s)
# print(res)
# \B:表示非单词的边界
# s = "python 666 java777php?888python"
# res = re.findall(r"python\B",s)
# print(res)


#表示分组
#需求:匹配连续三个数字或者连续aaa或者hhh

# | 用来隔开多个匹配规则
# s = "121hhh678aaa"
# res = re.findall(r"\d{3}|aaa|hhh",s)
# print(res)

#表示分组
#():
s="12345#phone#7878758473#pwd#sakjdks#member_id#5555"
res = re.findall(r"#(.+?)#",s)
print(res)

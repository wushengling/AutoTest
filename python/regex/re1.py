# 正则表达式
# JSON(xml)
'''
正则表达式是一个特殊的字符序列,检测一个字符串是否与
我们所设定的这样的字符序列相匹配

快速检索文本,实现一些替换文本的操作
1.检查一串数字是否是电话号码
2.检查一个字符串是否符合email
3.把一个文本里指定的单词替换为另外一个单词

'''
import re

a = 'C|C++|Java|C#|Python|Javascript'
r =re.findall('Python', a)
# 规则
if len(r)>0:
    print("YES")
else:
    print("NO")

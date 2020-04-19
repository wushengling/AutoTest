#coding:utf-8
"""
re模块
findall:查找,并返回所有符合规则的数据,返回一个list
search: 匹配出第一个符合规范的数据,返回一个匹配对象
    group() 方法可以获取匹配到的数据
macth :从字符串的头部开始匹配第一个符合规范的数据,返回一个匹配对象
        (如果数据不再字符串头部,则匹配不到)
        
        
"""
import re
# s = "123#python#1234#python#11111#pwd#python"
# res = re.findall(r"python",s)
# print(res)
# res = re.search(r"#(python)#1234#(python)#11111#(pwd)#",s)
# print(res)
# print(res.group())
# print(res.group(1))
# print(res.group(2))
# print(res.group(3))

#macth 从字符串的头部开始匹配
# s = "123#python#1234#python#11111#pwd#python"
# res= re.match(r"1111",s)
# print(res)

#sub:替换的方法
# s = "123#python#1234#python#11111#pwd#python"
# res= re.sub(r"#.+?#",r"java",s)
# print(res)X
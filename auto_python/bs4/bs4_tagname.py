# coding:utf-8
from bs4 import BeautifulSoup

youdao = open("bs4\\youdao.html","rb")
print(youdao)
soup = BeautifulSoup(youdao,"html.parser")
# print(soup.find_all("li"))
# print(soup.find(class_="rengong__guide--sub").string)

a=soup.find(class_="select clear")
# print(a)
# print(a.contents)
print(len(a.contents))
for i in a.contents:
    print(i.string.replace("\n",""))
'''
find_all()查找的是一个list对象
get_text()获取tag标签吓所有的文本
replace替换字符串里面的特殊字符

find()只查找一个(返回第一个)
Contents返回所有的子元素(list)
'''

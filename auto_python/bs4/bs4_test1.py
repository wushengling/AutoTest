# coding:utf-8
from bs4 import BeautifulSoup

youdao = open("bs4\\youdao.html","rb")
print(youdao)
soup = BeautifulSoup(youdao,"html.parser")
# print(type(soup))

# print(soup.prettify())

# print(soup.html)

# print(soup.title)  #Tag
# print(type(soup.title))

# print(soup.title.string)   #String
# print(type(soup.title.string))

'''
所有对象可以归纳为4种:
Tag:标签对象
NavigableString:字符对象
BeautifulSoup:就是整个html对象
Comment:注释对象(特殊的NavigableString)
'''




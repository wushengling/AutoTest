#coding:utf-8
"""
os模块:python内置的模块之一,它的作用是用来与操作系统进行交互的

os模块需要掌握的内容:处理路径

os.path.dirname :获取给定文件路径 所在的目录路径(获取父级目录)

os.path.json :进行路径拼接

window 中的路径使用的是\
linux 中的路径使用的是/

"""
import os
#当前文件的路径
path = __file__
print(path)
#当前文件在哪个路径下方
d1_path = os.path.dirname(path)
print(d1_path)
#os模块拼接出来的路径如果出现/和\都出现的情况(不用管,可以使用)
file_path = os.path.join(d1_path,"test.txt")
print(file_path)

with open(file_path,"r",encoding="utf-8") as f : 
    content = f.read()
    print(content)
    
#coding:utf-8
"""
os模块:python内置的模块之一,它的作用是用来与操作系统进行交互的

os模块需要掌握的内容:处理路径

os.path.dirname :获取给定文件路径 所在的目录路径(获取父级目录)

os.path.json :进行路径拼接

os.path.abspath :获取当前操作系统下的绝对路径表达方式 获取绝对路径

window 中的路径使用的是\
linux 中的路径使用的是/

"""
import os
# #如何在当前文件中获取项目路径
# d1 = os.path.dirname(__file__)
# print(d1)
# d2 = os.path.dirname(d1)
# print(d2)

# base_dir = os.path.dirname(os.path.dirname(__file__))
# print("项目目录的路径:",base_dir)

# file_path = os.path.join(base_dir,r"文件操作\test.txt")
# print(file_path)
# with open(file_path,"r",encoding="utf-8") as f : 
#     content = f.read()
#     print(content)


#Linux下的路径表示
print(__file__)
#获取当前操作系统下的绝对路径表达方式
print(os.path.abspath(__file__))

#后面项目中获取项目绝对路径的方式
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(base_dir)
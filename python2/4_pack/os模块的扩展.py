#coding:utf-8
"""
"""
import os
#获取当前工作路径 等同于linux下的pwd
p1 = os.getcwd()
print(p1)

# #切换路径 cd 
# os.chdir("../../..")
# print(os.getcwd())

# #创建文件夹 mkdir
# os.mkdir("pack2")

# #删除文件夹 rmdir
# os.rmdir("pack2")

#获取当前目录下的文件及文件夹信息: listdir
#可以接受一个参数(默认为当前工作目录)
print(os.listdir())

#判断给定的路径是否为文件
res = os.path.isfile()

#判断给定的路径是否为路径
res1 = os.path.isdir()
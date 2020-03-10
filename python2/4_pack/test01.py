#coding:utf-8
"""
模块导入的时候,同级目录导入,可能会出现代码标红(不代表报错)
在进行模块导入的时候,会将导入的模块从上到下执行一遍
"""
# vscode读取不到了包路径解决方案
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

#名称更改暂时无法导入
from pack import register
register.register()

#coding:utf-8
"""
第一种:导入模块
import 模块名

第二种:导入模块中的某个函数或者变量
from 模块名 import 变量/函数

第三种:导入的时候给导入的内容起别名
from 模块名 import 变量/函数 as 别名
import 模块 as 别名

第四种:几乎不用也不推荐的导入方式
from 模块 import *
import *
"""
# 读取不到了路径解决方案
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

#给导入的内容起别名
from pack.login import login as a
a()
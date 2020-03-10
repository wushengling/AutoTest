#coding:utf-8
import os
'''
# 获取当前文件的绝对路径
res = os.path.abspath(__file__)
print(res)
#获取当前文件的父级目录路径
res1 = os.path.dirname(res)
print(res1)
#获取当前文件的项目目录路径
res2 = os.path.dirname(res1)
print(res2)
'''
#获取项目目录路径
BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#用例模块目录的路径
CAESDIR = os.path.join(BASEDIR,"testcases")

#用例数据目录的路径
DATADIR = os.path.join(BASEDIR,"data")

#测试报告目录的路径
REPORTDIR = os.path.join(BASEDIR,"reports")

#配置文件目录的路径
CONFDIR = os.path.join(BASEDIR,"conf")

#日志文件目录的路径
LOGDIR = os.path.join(BASEDIR,"logs")

# print(BASEDIR,CAESDIR,DATADIR,REPORTDIR,CONFDIR,LOGDIR)

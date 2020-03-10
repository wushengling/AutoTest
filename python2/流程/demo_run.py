#coding:utf-8
"""
"""
# vscode读取不到了包路径解决方案
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

import unittest
from HTMLTestRunner import HTMLTestRunner
from testcase_ddt import LoginTest

#创建测试套件
suite = unittest.TestSuite()

# 通过测试用例类进行添加
#创建一个用例加载对象
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(LoginTest))

#创建测试运行程序
runner = HTMLTestRunner(stream=open(r"C:\wsl\AutoTest\python2\流程\report.html","wb"))

#执行测试套件
runner.run(suite)

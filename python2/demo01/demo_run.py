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
from demo01.excl import OperationExcel
from demo01.demo import LoginTest
from demo01.HTMLTestRunner import HTMLTestRunner
#创建测试套件
suite = unittest.TestSuite()

#获取excel测试用例的数据
excel = OperationExcel(filename=r"C:\wsl\AutoTest\python2\demo01\cases.xlsx",sheet_name="login")
cases = excel.read_excel()
for i in cases:
    #创建一条用例
    case = LoginTest("test_login",case_data=i)
    #添加到套件
    suite.addTest(case)

#创建测试运行程序
runner = HTMLTestRunner(stream=open(r"C:\wsl\AutoTest\python2\demo01\report.html","wb"))

#执行测试套件
runner.run(suite)


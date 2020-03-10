#coding:utf-8
# vscode读取不到了包路径解决方案
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)


from HTMLTestRunner import HTMLTestRunner
from operation_excel import OperationExcel
from demo import LoginTest 
import unittest
#创建测试套件
suite = unittest.TestSuite()

#读取用例中的数据
exl = OperationExcel(r"C:\wsl\AutoTest\python2\unittest框架\demo\cases.xlsx","login")
cases = exl.read_excel()
#通过循环来遍历用例数据
for i in cases:
    #创建一条测试用例
    case1 = LoginTest("test_login",i)
    #加载测试用例到套件
    suite.addTest(case1)
    
# 执行测试套件(创建测试运行程序)
runner = HTMLTestRunner(stream=open(r"C:\wsl\AutoTest\python2\unittest框架\demo\report.html","wb"))
runner.run(suite)





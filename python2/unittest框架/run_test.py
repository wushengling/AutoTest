#coding:utf-8
# vscode读取不到了包路径解决方案
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

import unittest
from unittest框架.testcases import LoginTest 
from unittest框架.HTMLTestRunner import HTMLTestRunner

#第一步:创建测试套件
suite = unittest.TestSuite()
#第二步:加载用例到套件
loader = unittest.TestLoader()
suite.addTest(loader.discover(r"C:\wsl\AutoTest\python2\unittest框架"))
#第三步:执行测试套件(创建测试运行程序)
runner = HTMLTestRunner(stream=open(r"C:\wsl\AutoTest\python2\unittest框架\report\report.html","wb"))
runner.run(suite)
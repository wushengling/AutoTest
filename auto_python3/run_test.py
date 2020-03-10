#coding:utf-8
# vscode读取不到了包路径解决方案
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

import unittest
from library.HTMLTestRunner import HTMLTestRunner
from common.handlepath import REPORTDIR,CAESDIR
#创建测试套件
suite = unittest.TestSuite()
#加载用例
loader = unittest.TestLoader()
suite.addTest(loader.discover(CAESDIR))
#执行用例
runner = HTMLTestRunner(stream=open(os.path.join(REPORTDIR,"report.html"),"wb"))
runner.run(suite)
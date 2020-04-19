#coding:utf-8
# vscode读取不到了包路径解决方案
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

import unittest
from common.handlepath import CAESDIR,REPORTDIR
from library.HTMLTestRunner import HTMLTestRunner
from common.handleemail import send_email

suite = unittest.TestSuite()

loader = unittest.TestLoader()
suite.addTest(loader.discover(CAESDIR))

report_file = os.path.join(REPORTDIR,"report.html")
runner = HTMLTestRunner(stream=open(report_file,"wb"))
runner.run(suite)

# send_email(filename=report_file,title="接口自动化报告")
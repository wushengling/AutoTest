#coding:utf-8
# vscode读取不到了包路径解决方案
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

import unittest
import datetime
from common.handlepath import CAESDIR,REPORTDIR
from library.HTMLTestRunner import HTMLTestRunner
from BeautifulReport import BeautifulReport
from common.handleemail import send_email

suite = unittest.TestSuite()

loader = unittest.TestLoader()
suite.addTest(loader.discover(CAESDIR))

date = datetime.datetime.now().strftime("%Y%m%d%H%M")

# #HTMLTestRunner报告
# report_file = os.path.join(REPORTDIR,date+"report.html")
# runner = HTMLTestRunner(stream=open(report_file,"wb"))
# runner.run(suite)

#BeautifulReport报告
br = BeautifulReport(suite)
br.report("接口自动化报告",filename=date+"report.html",report_dir=REPORTDIR)

# send_email(filename=report_file,title="接口自动化报告")
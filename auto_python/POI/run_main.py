# coding:utf-8
import unittest
from common import HTMLTestRunner

casePath = "D:\\Testing tools\\muke\\AutoTest\\auto_python\\POI\\testcase"
discover = unittest.defaultTestLoader.discover(casePath, "test*.py")
print(discover)

# runner = unittest.TextTestRunner()
# runner.run(discover)

reportPath = "D:\\Testing tools\\muke\\AutoTest\\auto_python\\POI\\report\\"+"result.html"
fp = open(reportPath,"wb")
runner = HTMLTestRunner.HTMLTestRunner(fp,verbosity=2,title="测试报告",description="POI模拟测试报告")
runner.run(discover)
fp.close()
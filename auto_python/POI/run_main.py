# coding:utf-8
import unittest
from common import HTMLTestRunner
#待执行用例的目录
casePath = "D:\\Testing tools\\muke\\AutoTest\\auto_python\\POI\\testcase"

#dixcover方法刷选出来的用例,循环添加到测试套件中
discover = unittest.defaultTestLoader.discover(casePath, "test*.py")
print(discover)

# runner = unittest.TextTestRunner()
# runner.run(discover)

#报告路径
reportPath = "D:\\Testing tools\\muke\\AutoTest\\auto_python\\POI\\report\\"+"result.html"
fp = open(reportPath,"wb")
runner = HTMLTestRunner.HTMLTestRunner(fp,verbosity=2,title="接口测试报告",description="POI模拟测试报告")
runner.run(discover)
fp.close()
if __name__ == '__main__':
    unittest.main()
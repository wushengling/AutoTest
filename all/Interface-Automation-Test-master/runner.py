import sys
sys.path.append("..")
import unittest
from TestCases.Api import ApiTest
from Base.BaseRunner import ParametrizedTestCase
from Base.BaseGetExcel import buit_report
from Base.BaseInit import BaseInit

def runner_case():#运行测试初始化
    BaseInit().mk_file()#创建文件
    suite = unittest.TestSuite()
    suite.addTest(ParametrizedTestCase.parametrize(ApiTest))
    unittest.TextTestRunner(verbosity=2).run(suite)#执行测试用例


if __name__ == '__main__':
    runner_case()#初始化
    buit_report()#写入报告
    print("执行完毕！")
    input("=====请查阅控制台执行日志=====")

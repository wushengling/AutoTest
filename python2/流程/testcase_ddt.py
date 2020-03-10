#coding:utf-8
"""
DDT:Data Driver Test (数据驱动测试)
数据驱动思想:数据和用例进行分离,通过外部数据去生成测试用例

ddt:源码优化 284行

"""
# vscode读取不到了包路径解决方案
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

import unittest
from login import login_check
from excl import OperationExcel
from ddt import ddt,data
from handlelog import log

@ddt
class LoginTest(unittest.TestCase):
    excel = OperationExcel(r"C:\wsl\AutoTest\python2\deme_ddt\cases.xlsx","login")
    cases = excel.read_excel()
    @data(*cases)
    def test_login(self,case):
        #参数
        data = eval(case["data"])
        #预期结果
        expected = eval(case["expected"])
        #实际结果
        res = login_check(*data)
        #用例所在行号
        row = case["case_id"]+1
        
        try:
            self.assertEqual(expected,res)
        except AssertionError as e:
            self.excel.write_excel(row=row,column=5,value="FAIL")
            log.error("用例:{},测试未通过".format(case["title"]))
            #抛出异常
            raise e
        else:
            self.excel.write_excel(row=row,column=5,value="PASS")
            log.info("用例:{},测试通过".format(case["title"]))
    
    
    
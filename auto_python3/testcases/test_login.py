#coding:utf-8
# vscode读取不到了包路径解决方案
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

import unittest
from library.ddt import ddt,data
from common.excel import OperationExcel
from login import login_check
from common.handlelog import log
from common.handlepath import DATADIR
@ddt
class LoginTest(unittest.TestCase):
    excel = OperationExcel(os.path.join(DATADIR,"cases.xlsx"),"login")
    cases = excel.read_excel()
    @data(*cases)
    def test_login(self,case):
        #传参
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
            log.error("用例:{},执行未通过".format(case["title"]))
            #捕获的异常对象输出到日志
            log.exception(e)
            #抛出异常
            raise e
        else:
            self.excel.write_excel(row=row,column=5,value="PASS")
            log.info("用例:{},执行通过".format(case["title"]))
        
    
    
    
        

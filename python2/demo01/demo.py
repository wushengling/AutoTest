#coding:utf-8
"""

"""
# vscode读取不到了包路径解决方案
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

import unittest
from demo01.login import login_check
from demo01.excl import OperationExcel  
class LoginTest(unittest.TestCase):
    excel = OperationExcel(filename=r"C:\wsl\AutoTest\python2\demo01\cases.xlsx",sheet_name="login")
    def __init__(self,methodName,case_data):
        self.case_data = case_data
        super().__init__(methodName)
    def test_login(self):
        res = login_check(*eval(self.case_data["data"]))
        #用例所在行号
        row = self.case_data["case_id"]+1
        try:
            self.assertEqual(eval(self.case_data["expected"]),res)
        except AssertionError as e:
            self.excel.write_excel(row=row,column=5,value="FAIL")
            #抛出异常
            raise e
        else:
            self.excel.write_excel(row=row,column=5,value="PASS")
            

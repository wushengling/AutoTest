#coding:utf-8
# vscode读取不到了包路径解决方案
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

import unittest
from unittest框架.login import login_check

class LoginTest(unittest.TestCase):
    def __init__ (self,methodName,case_data):
        #调用父类的__init__方法
        self.case_data = case_data
        super().__init__(methodName)
    def test_login(self):
        
        res = login_check(*self.case_data["data"])
        #断言
        self.assertEqual(self.case_data["expected"],res)

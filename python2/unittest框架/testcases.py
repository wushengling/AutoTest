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
    def test_login_pass(self):
        #正常登陆
        #入参
        data = ("root","123456")
        #预期结果
        expected = {"code":0,"msg":"登录成功"}
        #实际结果     *data 对元组进行拆包
        res = login_check(*data)
        #断言
        self.assertEqual(expected,res)

    def test_user_is_none(self):
        #账号为空
        #入参
        data = (None,"123456")
        #预期结果
        expected = {"code":1,"msg":"所有的参数不能为空"}
        #实际结果 ##data 对元组进行拆包
        res = login_check(*data)
        #断言
        self.assertEqual(expected,res)
        
    def test_user_is_none1(self):
        #账号为空
        #入参
        data = (None,"123456")
        #预期结果
        expected = {"code":1,"msg":"所有的参数不能为空1111"}
        #实际结果 ##data 对元组进行拆包
        res = login_check(*data)
        #断言
        self.assertEqual(expected,res)

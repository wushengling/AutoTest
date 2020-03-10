#coding:utf-8
"""
定义测试用例类:只要定义的类继承于unittest.TestCase 那么这个类就是测试用例类

测试用例怎么写:在测试用例类中定义以test开头的方法就是一条测试用例

unittest中评判 断言是否通过的标准:是否出现断言错误


"""
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
        #实际结果 ##data 对元组进行拆包
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
    
#创建测试用例对象的时候,必须要传入用例的方法名   
case1 = LoginTest("test_login_pass")
  
# if __name__ == '__main__':
#     t = LoginTest()
#     t.test_login_pass()
#     t.test_user_is_none()
    
 
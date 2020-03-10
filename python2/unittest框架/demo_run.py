#coding:utf-8
# vscode读取不到了包路径解决方案
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

import unittest
from unittest框架.demo01 import LoginTest
from unittest框架.HTMLTestRunner import HTMLTestRunner
#单独一条用例数据
case = {"data":("root","123456"),"expected":{"code":0,"msg":"登录成功"}}

#多条用例数据
cases = [{"data":("root","123456"),"expected":{"code":0,"msg":"登录成功"}},
             {"data":(None,"123456"),"expected":{"code":1,"msg":"所有的参数不能为空"}},
             {"data":(None,"123456"),"expected":{"code":1,"msg":"所有的参数不能为空111"}}
             ]
#创建测试套件
suite = unittest.TestSuite()

#通过循环来遍历用例数据
for i in cases:
    #创建一条测试用例
    case1 = LoginTest("test_login",i)
    #加载测试用例到套件
    suite.addTest(case1)
    
# 执行测试套件(创建测试运行程序)
runner = HTMLTestRunner(stream=open(r"C:\wsl\AutoTest\python2\unittest框架\report\report.html","wb"))
runner.run(suite)





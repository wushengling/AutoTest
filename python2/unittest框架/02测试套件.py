#coding:utf-8
"""
测试套件:使用unittest.TestSuite这个类创建出来的对象就是测试套件

测试运行程序:使用unittest.TextTestRunner这个类创建出来的对象就是测试运行程序(执行用例的入口)
    --测试运行程序后面会用第三方的,不用unittest自带的

用例加载对象:unittest.TestLoader 创建一个用例加载对象

测试用例执行的顺序:不是按照先后顺序进行执行,通过埃斯科马来排序

"""
# vscode读取不到了包路径解决方案
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

import unittest
from unittest框架.testcases import LoginTest 
#第一步:创建一个测试套件
suite = unittest.TestSuite()

#第二步:将测试用例加载到测试套件中
#第一种:一条一条添加
#创建一条测试用例
case1 = LoginTest("test_login_pass")
# case2 = LoginTest("test_user_is_none")
#将用例添加套件
# suite.addTest(case1)
# suite.addTest(case2)

#第二种:通过测试用例类进行添加
#创建一个用例加载对象
# loader = unittest.TestLoader()
# suite.addTest(loader.loadTestsFromTestCase(LoginTest))

#第三种:通过用例模块去加载测试用例
# from unittest框架 import testcases
#创建一个用例加载对象
# loader = unittest.TestLoader()
# suite.addTest(loader.loadTestsFromModule(testcases))


#第四种:通过路径去进行加载(默认会加载该路径下面所有以test开头的模块中的测试用例,可以通过pattern来指定模块名匹配规则)
#创建一个用例加载对象
loader = unittest.TestLoader()
suite.addTest(loader.discover(r"C:\wsl\AutoTest\python2\unittest框架",pattern="*.py"))

# unittest.defaultTestLoader.discover   默认加载器

#第三步:执行测试用例(需要先创建一个测试运行程序)
#创建测试运行程序
runner = unittest.TextTestRunner()

#执行测试套件中的测试用例
runner.run(suite)
#coding:utf-8
'''
Unittest是python里面的单元测试框架,方便组建测试用例
,执行用例,并生成报告
注意:
    1.测试类,继承单元测试unittest.TestCase这个类
    2.测试方法(用例)必须以test开头
    3.测试类就是多个用例的一个集合,相当于是测试用例的一个模版

用例执行顺序:
    setUpClass > setUp > testAdd > tearDown > setUp > testMultiply > tearDown > tearDownClass
'''
import unittest
# print(help(unittest))

def login():
    print("走登录流程,登录啦!!!")

class Test(unittest.TestCase):
    u'''用例总和'''
    @classmethod
    def setUpClass(cls): # 前置条件,所有用例只执行一次这个
        print("前置条件,所有用例只执行一次这个")
        login()

    @classmethod
    def tearDownClass(cls):
        print("后置,所有的用例执行完之后,最后执行这个")

    def setUp(self):  # 前置条件,每个用例都会先执行这个
        print("前置条件,每个用例都会先执行这个")
        login() #先走登录

    def tearDown(self): # 后置,每次用例执行完,都会执行这个
        print("后置,每次用例执行完,都会执行这个")
    
    def testAdd(self):  # test method names begin with 'test' #测试的名称必须以test开头
        u'''用例一'''
        a = 1
        b = 2
        c = a + b # 测试结果
        self.assertEqual(c, 3) # 断言是测试结果与预期结果对比
        print("test1")
    
    def testMultiply(self):
        u'''用例二'''
        a = 2
        b = 3
        c = a*b
        self.assertEqual(c, 5)  # 期望结果是5,失败的用例
        print("test2")


if __name__ == '__main__':
    unittest.main()
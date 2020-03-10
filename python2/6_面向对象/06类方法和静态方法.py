#coding:utf-8
"""
对象方法(实例方法):
    定义:通过对象去调用的:对象.方法名()
    对象方法的第一个参数是self,self代表的是对象本身
    
    
类方法:
    定义:在定义的方法上面加个@classmethod
    类方法的第一个参数是cls,cls代表的是类本身
    既可以通过对象去调用和可以通过类去调用
应用场景:
如果这个方法以类为主体去调用,方法内部不会涉及到对象属性和对象的使用,那么该方法应该使用类方法
    
静态方法:
    定义:在定义的方法上面加个@staticmethod
    没有必须要定义的固定参数
    既可以通过对象去调用和可以通过类去调用
应用场景:
方法内部既不会使用类属性和类方法,也不会使用对象属性和对象属性,使用静态方法

"""

class TestCase ():
    def func(self):
        print("方法一")
    
    @classmethod
    def func111(cls):
        print("这个是类方法:func111")
        
    @staticmethod
    def func222():
        print("这个是静态方法:func222")
    
t1 = TestCase()
t1.func111()
#类直接去调用类方法
TestCase.func111()
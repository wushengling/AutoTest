#coding:utf-8
"""
类里面的方法

方法(对象方法):
类里面的定义的函数叫方法:
    方法的第一个参数必须写成self(这个是规范)

self:代表的是对象本身,那个对象去调用方法,self代表就是那个对象
"""
class Car:
    #类属性
    a= "1"
    b= "2"
    def __init__(self,name,age,gender):
        #通过类去创建对象的时候,改方法会自动调用
        #初始化对象属性
        self.name = name
        self.age = age
        self.gender = gender
    def skill1(self):
        # print("通过self获取name属性:",self.name)
        print("{}正在吃鱼".format(self.name))
        
    def skill2(self):
        print("{}正在爬树".format(self.name))
        
car1 = Car("喵喵",1,"公")
# #通过对象获取属性
# print(car1.a)
# print(car1.b)

# #使用对象去调用方法: 对象.方法名()
# car1.skill1()
# car1.skill2()

#属性的访问和方法的调用

# #1.对象可不可以访问类属性
# print(car1.a)   #可以
# #2.对象可不可以访问对象属性
# print(car1.name)   #可以
# #3.对象可不可以直接调用方法
# print(car1.skill1())   #可以

# #1.类可不可以访问类属性
# print(Car.a)    #可以
# #2.类可不可以访问对象属性
# print(Car.name)    #不可以
# #3.类可不可以直接调用方法
# Car.skill1()    #不可以
#coding:utf-8
"""
动态属性的设置:

内置函数setattr:设置属性
参数一:类名/对象
参数二:属性名
参数三:属性值

内置函数getattr:获取属性
参数一:类名/对象
参数二:属性名


内置函数delattr:删除属性
参数一:类名/对象
参数二:属性名

"""
class MyClass(object):
    ttt = 111
    pass
    def __init__(self,gender):
        self.gender = gender

m = MyClass("女")
#__________________setattr_________________
#在类外面设置类属性
#方式一:
# MyClass.attr = 100
# print(m.attr)
#方式二:
# setattr(MyClass,"attr",100)
# print(m.attr)


#在类外面设置对象属性
# m.name = "小红"
# setattr(m,"age",8)
# print(m.name,m.age)

#__________________getattr_________________
#在类外面获取类属性
#方式一:
# print(MyClass.ttt)
#方式二:
# print(getattr(MyClass,"ttt"))

#在类外面获对象属性
#方式一:
# print(m.gender)
#方式二:
# print(getattr(m,"gender"))

#__________________delattr_________________
#在类外面删除类属性
#方式一:
# print(MyClass.ttt)
# del MyClass.ttt
# print(MyClass.ttt)
#方式二:
# print(MyClass.ttt)
# delattr(MyClass,"ttt")
# print(MyClass.ttt)

#在类外面删除对象属性
#方式一:
# print(m.gender)
# del m.gender
# print(m.gender)
#方式二:
# print(m.gender)
# delattr(m,"gender")
# print(m.gender)
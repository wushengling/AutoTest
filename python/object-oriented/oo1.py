#面向对象
#有意义的面向对象的代码
# 类 = 面向对象
# 类,对象

#类
#类基本的作用:封装
#类和对象

#模版

# class classname(object):
#     pass

class Student():
    #一个班级里所有学生的总数
    sum=0
    # name = '~~~~' 
    # age = 0
    #类变量和实例变量
    #类变量和类关联在一起
    #实例变量与对象关联在一起
    def __init__(self,name,age):
        #构造函数
        #自动运行
        #只能返回NONE
        #初始化对象的属性
        self.name = name
        self.age = age
        print('student')
    #行为 与 特征
    def do_homework(self):
        print('homework')

# class Printer(): 
#     def print_file(self):       #没有参数列表时,一定要加self
#         print('name='+ self.name)   #用使用类定义的变量,需要使用sel引用
#         print('age='+ str(self.age))

# student = Student()     # 实例化
# student.print_file()

# print(Student.name)

student1= Student(name='a',age=1)
# student1.__init__()
print(student1.name)
print(student1.age)
student2= Student('b',2)
print(student2.name)
print(student2.age)

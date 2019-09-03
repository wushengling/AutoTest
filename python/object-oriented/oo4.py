
class Student():
    sum1 =0
    def __init__(self,name,age):
        #this
        #显胜于隐
        self.name = name
        self.age = age
        self.__score= 0
        self.__class__.sum1 +=1
        print("总人数为"+str(self.__class__.sum1))
        # print(name)
        # print(age)
        # print('student')

    def marking(self,__score):
        if __score>=0:
            self.__score = __score
            print(self.name+'同学本次考试分数为:'+str(self.__score))
        else:
            return print('成绩输入有误')

    #行为 与 特征
    #实例方法
    def do_homework(self):   #self 代表对象本身
        self.do_english_homeword()
        print('homework')

    def do_english_homeword(self):
        print()
    
    #类方法
    @classmethod
    def plus_sum(cls):      #cls 代表类本身
        cls.sum1 +=1
        print(cls.sum1)
    #静态方法
    @staticmethod
    def add(x,y):
        print(Student.sum1)
        print('this is static method')

student_1 = Student('张三',18)
student_1.marking(-1)



# print(Student.name)
# print(Student.__dict__) 

# student1= Student('a',1)
# student1.plus_sum()
# Student.plus_sum()
# student1.add(1,2)
# Student.add(1,2)
# student2= Student('b',2)
# Student.plus_sum()
# student2= Student('c',3)
# Student.plus_sum()
# print(student1.__dict__) 


# print(student1.name)
# print(student1.age)

# student2= Student('b',2)
# print(student2.name)
# print(student2.age)


# 总结
# python类:
    # 变量:类变量
    #     实例变量

    # 方法:实例方法
    #      类方法
    #      静态方法
    # 构造函数

    #成员的可见性
        # public 公开的  方法无__
        # private 私有的 方法名称前加__

    #面向对象三大特性:
    #        继承性
    #        封装性
    #        多态性
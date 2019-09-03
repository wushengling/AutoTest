#参数
# 1.必须参数
# 2.关键字参数
from asyncio.windows_events import NULL
def add(x,y):
    result = x + y
    return result

z = add(y = 2,x = 1)  #关键字参数,指定参数赋值

#3.默认参数
#形参没有设置默认参数必须传参
#形参设置了默认参数,可不传,为默认参数
#默认参数后不能没有设置默认参数的形参

def print_student_files(name,gender='男',age=18,college='中国高中'):
    print('我叫'+name)
    print('我今年'+str(age)+'岁')
    print('我是'+gender+'生')
    print('我在'+college+'上学')

print_student_files('张三','女',18,'中国高中')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print_student_files('王五')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print_student_files('赵四',age=17)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
# print_student_files('孙六',gender='女',17,college='中国大学')    不能混淆赋值
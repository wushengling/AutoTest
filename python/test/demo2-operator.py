#变量    名字
from curses.has_key import python
A = [1,2,3,4,5,6]
B = [1,2,3]
print(3*A+B+A)

#变量名规范
#首字符不能为数字
#字母、数字、下划线
#系统保留关键字,不能用在变量名中
#区分大小写
#不用定义变量类型

#int  str tuple (不可变)值类型 list  set dict (可变)引用类型
a=[1,2,3,4,5]
a.append(6)
print(a)

a=(1,2,3,[1,2,4])
print(a[3][2])

# 算术运算符
# 多立方 **   2**2   2***2
# + - * / % // ** 

#赋值运算符
#= += *= /= %= **= //=

#比较(关系)运算符
#== != > < >= <=

#逻辑运算符
#and or not 

#成员运算符
#in not in 

#身份运算符
#is not is 

#位运算符
#&  按位与
a = 100
b = 11
print(a&b)

#|  按位或
a = 100
b = 11
print(a|b)

#^  按位异或

#~  按位取反
#<<  左移动
#>>  右移动
#把数字当做二进制数字进行运算



# == 值判断  is id身份判断   type 类型判断
#对象的三个特征  id \ value \ type
a=1 
# print(type(a) == int)
b=isinstance(a,int)
c=isinstance(a,(str,float))
print(c)



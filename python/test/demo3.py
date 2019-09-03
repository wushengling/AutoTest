#表达式(Expression)是运算符(Operator)和操作数(Operand)所构成的序列
# 优先级  ()
#流程控制语句
'''
条件控制      循环控制       分支
if else    for   while 
选择性问题
'''
mood = False
if mood :
    print('正确')
else:
    print('错误')


a = 1
b = 2
if a>b:
    print("False")
else:
    print("true")



print('请输入用户名:')
user_name = input()
print('请输入密码:')
user_password = input()

NAME = 'wsl'
PASSWORD = '123456'

if NAME == user_name and PASSWORD == user_password:
    print('登录成功')
else:
    print('用户名或密码错误')

""" 
snippet 片段
if condition:
    pass
else:
    pass
for target_list in expression_list:
    pass
class classname(object):
    pass 
"""
if True:
    pass #空语句/占位语句


a=input()
a= int(a)
if a==1:
    print("1")
elif a==2:
    print("2")
elif a==3:
    print("3")
else:
    print("0")

#while 循环
#递归
expression = 1
while expression<10:
    print(expression)
    expression +=1
else:
    print("两位数")

#for 循环
#主要是用来遍历/循环 序列或者集合\字典
a = [['a','b','c','d'],(1,2,3)]
for x in a:
    for y in x:
        print(y,end ='')
else:
    print("木有了")

#break 中止
a = [['a','b','c','d'],(1,2,3)]
for x in a:
    for y in x:
        if y==2:
            break
        print(y,end ='')
else:
    print("木有了")
#continue 跳出继续
a = [['a','b','c','d'],(1,2,3)]
for x in a:
    for y in x:
        if y==2:
            continue
        print(y,end ='')
else:
    print("木有了")

# range
for x in range(0,10,2):   #[0,10)
    print(x,end=" | ")
for x in range(10,0,-2):  
    print(x,end=" | ")

a = [1,2,3,4,5,6,7,8]
for x in a[0::2]:
    print(x,end=' | ')
for x in range(0,len(a),2):
    print(a[x],end=" | ")


#高性能  封装性(可复用),抽象
#coding:utf-8

"""
函数的参数

形参:在定义函数的时候,定义的参数,叫形参(形式上的参数,并不确定实际值为多少)
1,必需参数(必备参数) 定义了几个就要传几个,不能多,也不能少 def 函数名(a,b)
2,默认参数(缺省参数) 可以不传,不传时为设置的默认值  def 函数名(a,b=999)
3,不定长参数(动态参数) 可以用来接收0个,或者多个参数(可接收的参数不限定个数)
    *args:可以用来接收0个,或者多个参数(只能接收以位置传参的方式),以元组形式保存
    **kwargs:可以用来接收0个,或者多个参数(只能接收以关键字参数的方式),以字典的形式保存
    
    #规范写*args 可以改名,但不要改名
    #不定长参数必需定义在默认参数和必需参数后面
    
#拆包和打包 *  **
#拆包
*:可以用来对元组/列表/字符串进行拆包(只能在调用函数传递函数的时候)
**:可以用来对字典进行拆包(只能在调用函数传递函数的时候)

#打包
定义参数的时候在参数前面,加个*,或者**,那么这个参数就是一个不定长参数
带有一个*的不定长参数,会将接收到的参数,打包成一个元组
带有一个**的不定长参数,会将接收到的参数,打包成一个字典

#

实参:在调用函数的时候,传入进入的参数叫实参(实际的参数)
形参用来接收实参传递的值
1,按位置顺序进行传递--位置参数
2,通过参数名指定参数进行传递--关键字参数

"""
# #不定长参数
# def func(a,b=99,*args):
#     print("a为{}".format(a))
#     print("b为{}".format(b))
#     print("*args为{}".format(args))
#     return a+b
# res = func(11,22,33,444,5555)
# print(res)

# def func(a,b=99,*aaaa):
#     print("a为{}".format(a))
#     print("b为{}".format(b))
#     print("*aaaa为{}".format(aaaa))
#     return a+b
# res1 = func(11,22,33,444,5555)
# print(res1)
    
# #**kwargs
# def func(a,b=99,**kwargs):
#     print("a为{}".format(a))
#     print("b为{}".format(b))
#     print("*kwargs为{}".format(kwargs))
#     return a+b
# res = func(a= 11,b = 22,c = 33,d = 444,e = 5555)
# print(res)

#拆包和打包 * , **
#拆包
li = [1,2,3]
tu = (11,22,33)
dic = {"a":"111","b":222,"c":"333"}

# #不能这样用
# a,b,c = *li
# *li = 11,22,33

#正确的用法
def func(a,b,c):
    print(a)
    print(b)
    print(c)
# func(li[0],li[1],li[2])
func(*li)
func(*tu)

func(**dic)
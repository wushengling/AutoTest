#-*- coding:utf-8 -*-

# Number:数字
# int:整数
# 其它语言:float:浮点数   单精度(float)  双精度(double)
# 其它语言: short,int,long
print(type(1+0.1))
print(type(1*1))
print(type(1*0.1))
print(type(2/2)) #结果为浮点型
print(type(2//2)) #结果为整型

#/除,//整除
print(2/2)
print(2//2)
print(1/2)
print(1//2)

# 10进制,2进制,8进制,16进制
# 进制转换
print(0b10) #2进制表示0b
print(0o11) #8进制表示0o
print(0x1F) #16进制表示0x

print(bin(10)) #10进制转化为2进制  bin向2进制转化
print(int(0b111)) #2进制转化为10进制  int向10进制转化
print(oct(0b111))#2进制转化为8进制  oct向8进制转化
print(hex(888)) #10进制转化为16进制  hex向16进制转化


#bool布尔类型:表示真\假
# complex 复数  非重点,自行了解
True
False
print(type(True))
print(type(False))
print(int(True))
print(int(False))
print(bool(1))
print(bool(0)) #bool非0则为True,0或null\None则为False

# str字符串
# 用单引号,双引号,三引号表示

print(type('helloworld'))
print("let's go")
print('let"s go')
print('let\'s go')  #转义字符
print('''
hello world,hello world,hello world,hello world,
hello world,hello world
''')
print("""
hello world,hello world,hello world,hello world,
hello world,hello world
""")
print('hello world\nhello world\nhello world\nhello world')
print('hello\
world')

#转义字符--特殊的字符,tab,空格,换行,与语言本身语法有冲突的字符
# \n 换行
# \' 单引号
# \t 横向制表符
#\n 换行与\r 回车

print('hello \\n world')
print(R'c:\northwind\northwet') #字符串,不是一个普通字符串,而是一个原始字符串

#字符串运算
print("hello"+"world")
print("helloworld"*3)
print("hello world"[0])
print("hello world"[-1])
print("hello world"[0:2])  #[0:2)
print("hello world"[0:])

#数组 []
print(['one',2,'三',4,True])
print(type(['one',2,'三',4,True]))
print(['one',2,'三',4,True][-1:])

#元组
print(('one',2,'三',4,True))
print(type(('one',2,'三',4,True)))
print(('one',2,'三',4,True)[-1:])
print(type((1,)))
print(("hello world")[0:8:2])


print(7 in [1,2,3,4,5,6])
print(7 not in [1,2,3,4,5,6])

print(len([1,2,3,4,5,6]))
print(len('hello world'))

print(max([1,2,3,4,5,6]))
print(min([1,2,3,4,5,6]))
print(max('hello world'))
print(min('helloworld'))

print(ord('w'))
print(ord('d'))
print(ord(' '))

#集合 set ---无序{} 无下标索引
#集合 set ---不重复
print(type({1,2,3,4,5,6}))
print({1,1,1,2,2,2,2})
#差集
print({1,2,3,4,5,6}-{3,4})
#交集
print({1,2,3,4,5,6}&{3,4})
#合集
print({1,2,3,4,5,6}|{3,4,7})
#空集合
print(type(set()))

#字典 dict  集合序列
# key value
#{key1:value,key2:value2...} set
#key为不可变
print(type({1:1,2:2}))
print({'q':'第一','w':'第二','e':'第三','r':'第三'})
print({'q':'第一','w':'第二','e':'第三','r':'第三'}['w'])
print(type({}))


# 总结:
# 数字(Number): 整型 int
#              浮点型 float
#              布尔型 bool
#              复数 complex
# 组:
# 序列: 字符串 str 不可变
#       列表 list
#       元组 tuple     有序,可用下标索引来访问,切片操作[0:5]
# 集合: set 无序,没有索引,不能切片
# 字典: dict key:value 键值对是其最基本的概念



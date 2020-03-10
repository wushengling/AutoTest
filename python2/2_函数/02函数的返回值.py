#coding: utf-8
"""
函数的返回值
关键字:return
函数调用之后返回值是由return来决定的
函数没有写return,函数返回的内容为None(为空)
return 后面写什么,函数返回的就是什么

注意点:
一个函数中只能有一个return,
函数执行到return之后就不会再继续执行,会直接跳出函数,返回结果
可以写对个return 但注意一个分支只能写一个
返回多个值,直接写在return后面,用逗号隔开
返回两个及以上,会被放到元组中
"""

#拆包
def a():
    return 111,222,333
a,b,c = a()
print(a)
print(b)
print(c)
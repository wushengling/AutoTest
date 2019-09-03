# 函数式编程
# 闭包

# 函数 一切皆对象--结构
# 只是一段可执行的代码,并不是对象  C#

def a():
    pass

print(type(a))

# 闭包
# 函数+环境变量(函数定义时候)(函数需引用环境变量)
def curve_pre():
    a = 25
    def curve(x):
        return a*x*x
    return curve    #返回为curve函数
a = 100000   
f = curve_pre()
print(f.__closure__)
print(f.__closure__[0].cell_contents)
print(f(2))


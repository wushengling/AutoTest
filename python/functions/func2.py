# 1.实现两个数字的相加
# 2.打印输入的参数
# import sys
# sys.setrecursionlimit(99999999)   设置最大递归层数

def add(x,y):      #x,y为形式参数 形参
    result = x + y
    return result
def print_code(code):
    print(code)
    return
    print(code)   #return 后不运行

a = add(1,2)      #实际参数 实参
b = print_code('python')
print(a,b)


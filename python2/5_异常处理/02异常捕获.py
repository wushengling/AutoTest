#coding:utf-8
"""
异常捕获:
try:监测有可能出现异常的代码
except:捕获异常,对异常进行处理
else:没有发送异常的处理方式,放在else中
finally:不管代码是否发送异常都会执行


try:
    #try 下面放有可能会出现异常的代码
except:
    #except 下面放捕获到异常之后处理的代码
else:
    #else 代码没有发生异常,会执行else中的代码
finally:
    #finally 不管代码是否出现异常都会执行
    
"""
try:
    with open(r"C:\wsl\AutoTest\python2\异常处理\666.txt","r") as f:
        conetent = f.read()
except:
    print("except---获取异常之后的处理方式")
    with open(r"C:\wsl\AutoTest\python2\异常处理\666.txt","w") as f:
        pass
else:
    print("else---没有出现异常")
    print(conetent)
finally:
    print("finally---不管代码是否出现异常都会执行")
    
print("______________!!!!!_____________")

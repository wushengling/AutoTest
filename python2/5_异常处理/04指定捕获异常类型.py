#coding:utf-8
"""
异常捕获时,语法错误是捕获不到的
    
在except 后面可以指定捕获的异常类型
except NameError 变量不存在
except FileNotFoundError 文件目录不存在
如果要捕获多个异常类型:
方式一:
    使用多个except,每个except都是可以指定捕获的异常类型,适合不同类型的异常做不同的的处理
方法二:
    使用一个except捕获多个类型的异常,适用多个类型的不同异常采用相同的处理方式
方式三:
    捕获所有的异常类型(语法错误除外)
    except Exception as e:   Exception 基础的异常类型
    一些第三放模块自定义的异常使用except:
"""

# try:
#     print(a)
#     with open("123.txt","r",encoding="utf-8") as f:
#         content = f.read()
# except (NameError,FileNotFoundError,KeyError,ValueError) as e:
#     print("代码发生异常")
#     print("异常信息:",e)
# else:
#     print("代码没有异常")
# finally:
#     print("代码不管有没有异常都会执行")

try:
    print(a)
    with open("123.txt","r",encoding="utf-8") as f:
        content = f.read()
except Exception as e:
    print("代码发生异常")
    print("异常信息:",e)
else:
    print("代码没有异常")
finally:
    print("代码不管有没有异常都会执行")
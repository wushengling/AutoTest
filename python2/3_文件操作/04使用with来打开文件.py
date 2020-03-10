#coding:utf-8
"""
with 的使用
使用with打开文件,会自动帮我们关闭文件

with 可以开启文件操作的上下文管理器

"""
#例子:
def func():
    with open(r"C:\wsl\AutoTest\python2\文件操作\test.txt","r",encoding="utf-8") as f:
        content = f.readlines()
        # print(content)
        dic = {}
        for a,b in enumerate(content):
            key = "data{}".format(a)
            value = b.replace("\n", "")
            dic[key] = value
    return dic
res = func()
print(res)
    

    

    

#coding:utf-8
"""
python操作文件

open的常用参数:
第一个参数:要打开的文件名字或者文件路径
第二个参数:文件打开的模式
    r:只读模式
    rb:只读模式,以二进制的编码格式去打开文件

第三个参数:
    encoding:用来指定打开文件的编码格式(使用rb时,不需要用到这个参数)
"""
# #打开文件
# #读取文件一致使用文件的完整路径 前面加r,防转译
# f = open(r"C:\wsl\AutoTest\python2\文件操作\test.txt","r",encoding="utf-8")
# #读取内容
# content = f.read()
# #打印读取出来的内容
# print(content)
# #关闭文件
# f.close()

#读取图片,视频等文件
f = open(r"C:\wsl\AutoTest\python2\文件操作\test.txt","rb")
content = f.read()
print(content)
f.close()

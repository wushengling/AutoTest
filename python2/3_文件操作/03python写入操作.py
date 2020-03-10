#coding:utf-8
"""
python操作文件

open的常用参数:
第一个参数:要打开的文件名字或者文件路径
第二个参数:文件打开的模式
    r:只读模式,如果打开的文件不存在,会报错
    rb:只读模式,以二进制的编码格式去打开文件
    a:以追加写入的模式打开文件,如果打开的文件不存在,不会报错(会自动创建一个)
    ab:以追加写入的模式打开文件,以二进制的编码格式去打开文件,如果打开的文件不存在,不会报错(会自动创建一个)
    w:以覆盖写入的模式打开文件,如果打开的文件不存在,不会报错(会自动创建一个)
    wb:以覆盖写入的模式打开文件,以二进制的编码格式去打开文件,如果打开的文件不存在,不会报错(会自动创建一个)
    
    注意点:a,ab,w,wb,只能写入内容,不能读取
第三个参数:
    encoding:用来指定打开文件的编码格式(使用rb时,不需要用到这个参数)
    
    
关于文件写入的方法
"""
# #追加写入
# f = open(r"C:\wsl\AutoTest\python2\文件操作\test1.txt","a",encoding="utf-8")
# f.write("你是的小苹果")
# f.close()

# #覆盖写入
# f = open(r"C:\wsl\AutoTest\python2\文件操作\test1.txt","w",encoding="utf-8")
# f.write("123456")
# f.close()

# #文件读写的方式去复制一张图片
# f = open(r"C:\wsl\AutoTest\python2\文件操作\test.txt","r",encoding="utf-8")
# f1 = open(r"C:\wsl\AutoTest\python2\文件操作\test1.txt","a",encoding="utf-8")
# f1.write(f.read())
# f.close()
# f1.close()
#coding:utf-8
'''
魔法变量
__name__:直接运行这个文件,__name__的值为"__main__";在导入的时候__name__的值为"模块名称"
'''
def register():
    print("register")

#这个条件只有在直接运行这个文件的时候才会成立,模块导入的时候该条件不会成立
if __name__ == '__main__':
    register()
        

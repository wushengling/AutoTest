#coding:utf-8
class Count():
    def __init__(self,a=0,b=0): #初始化
        self.a = a
        self.b = b
    def add(self):   #默认值
        '''加法函数'''
        c = self.a+self.b
        return c

if __name__ == "__main__":
    a = Count(a=1,b=2)  # 实例化
    print(a.add())

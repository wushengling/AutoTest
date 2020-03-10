#coding:utf-8
"""
在子类中定义和父类同名的方法,这个操作叫重写父类方法

关于方法的调用:
    子类可以继承父类的方法,意味着子类可以调用父类的方法(父类不能调用子类的方法)
    如果子类重写了父类的方法,那么调用方法该方法时,使用子类的方法

在子类中调用父类中被重写的方法:
    第一种:父类名.方法名(self)
    第二种:super().方法名()
"""
import time
class BasePhone(object):
    def tell(self):
        print("这个是打语音电话的功能")

class PhoneV1(BasePhone):
    def send_msg(self):
        print("这个是发送短信的功能")
    def music(self):
        print("这个是播放音乐的功能")
        
class PhoneV2(PhoneV1):
    def new(self):
        print("这个是新增的其他功能")
    def tell(self):
        print("这个是打视频电话的功能")
        time.sleep(5)
        #调用父类被重写的方法
        #第一种:父类名.方法名(self)
        BasePhone.tell(self)
        #第二种:super().方法名()
        super().tell()

t = PhoneV2()
# t.send_msg()
t.tell()
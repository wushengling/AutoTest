#coding:utf-8
"""
继承关系:
通过继承可以获得父类的方法和属性
父类的私有属性,子类无法获取
"""
class BasePhone(object):
    def tell(self):
        print("这个是打电话的功能")

class PhoneV1(BasePhone):
    def send_msg(self):
        print("这个是发送短信的功能")
    def music(self):
        print("这个是播放音乐的功能")
        
class PhoneV2(PhoneV1):
    def new(self):
        print("这个是新增的其他功能")

t = PhoneV2()
t.send_msg()
t.tell()
#coding:utf-8
"""
python常用配置文件格式
.ini
.conf
.cfg

ConfigParser 模块

"""

from configparser import ConfigParser

#第一步:创建一个配置文件解析对象
conf = ConfigParser()

conf.read(r"C:\wsl\AutoTest\python2\配置文件的使用\conf.ini")

#读取配置文件中的内容
#第一种get方法:读取出来的都是字符串类型(不是int)
#参数一:配置区域(块) 参数二:配置项
# res = conf.get("mysql","port")
# print(res)

#第二种getint方法:获取数字类型的数据(不能为浮点数和字符串)
#参数一:配置区域(块) 参数二:配置项
# res = conf.getint("mysql","port")
# print(res)

#第三种getfloat方法:获取float类型的数据(不能为int和str)
#参数一:配置区域(块) 参数二:配置项
# res = conf.getfloat("mysql","port")
# print(res)

#第四种getboolean方法:获取bool值(不能为int\float\str)
#参数一:配置区域(块) 参数二:配置项
# res = conf.getboolean("mysql","port")
# print(res)

#扩展:
#获取所有的配置区域(块)
res1 = conf.sections()
print(res1)

#获取配置块下的所有配置项
res2 = conf.options("mysql")
print(res2)

#获取配置块下的所有配置项([(option,value),(option,value),(option,value)]))
res3 = conf.items("mysql")
print(res3)

#数据写入:set方法
conf.set("mysql","name","test")
#写入到文件: 注意点,使用w模式去写入
conf.write(fp =open(r"C:\wsl\AutoTest\python2\配置文件的使用\conf.ini","w"))
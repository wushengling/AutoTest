#coding:utf-8
"""
创建一个日志收集器
"""
import logging

#第一步:创建一个日志收集器对象
mylog = logging.getLogger("mylog")

#第二步:设置日志收集器收集的等级(没有设置之前,默认是warning等级)
mylog.setLevel("DEBUG")

#第三步:日志输出渠道的等级(没有设置之前,默认是warning等级)
#1.输出到控制台的渠道
#创建输出渠道
sh = logging.StreamHandler()
#设置输出渠道的输出等级
sh.setLevel("DEBUG")
#将输出渠道添加到收集器中
mylog.addHandler(sh)

#2.输出到文件的渠道
#创建输入渠道(输出到文件)
fh = logging.FileHandler(filename=r"C:\wsl\AutoTest\python2\日志\log.log",encoding="utf-8")

fh.setLevel("DEBUG")
mylog.addHandler(fh)

#第四步:日志输出格式的设置
"""
%(asctime)s:代表的是日志输出的时间
%(filename)s:日志输出的文件名
%(lineno)d:行号
%(levelname)s:日志等级
%(message)s:日志内容
"""
formater = '%(asctime)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s:%(message)s'
#创建一个输出格式
fm = logging.Formatter(formater)
#将输出格式和输出渠道绑定
sh.setFormatter(fm)  #控制台
fh.setFormatter(fm)  #文件
mylog.debug("这个是debug等级的日志")
mylog.info("这个是info等级的日志")
mylog.warning("这个是warning等级的日志")
mylog.error("这个是error等级的日志")
mylog.critical("这个是critical等级的日志")
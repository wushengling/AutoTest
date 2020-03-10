#coding:utf-8
"""
"""
import logging
from logging.handlers import RotatingFileHandler,TimedRotatingFileHandler

#第一步:创建一个日志收集器对象
mylog = logging.getLogger("mylog")

#第二步:设置日志收集器收集的等级(没有设置之前,默认是warning等级)
mylog.setLevel("DEBUG")

#第三步:日志输出渠道的等级(没有设置之前,默认是warning等级)
# 创建一个按文件大小轮转的输出渠道
fh_Bytes = RotatingFileHandler(filename=r"C:\wsl\AutoTest\python2\日志\log.log",
                         encoding="utf-8",
                         maxBytes=1024,
                         backupCount=3
                         )

fh_time = TimedRotatingFileHandler(filename=r"C:\wsl\AutoTest\python2\日志\log.log",
                                   encoding="utf-8",
                                   when = "D",
                                   interval=1,
                                   backupCount=30
                                   )
#设置输出等级
fh_Bytes.setLevel("DEBUG")
#添加到收集器中
mylog.addHandler(fh_Bytes)
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
fh.setFormatter(fm)  #文件
mylog.debug("这个是debug等级的日志")
mylog.info("这个是info等级的日志")
mylog.warning("这个是warning等级的日志")
mylog.error("这个是error等级的日志")
mylog.critical("这个是critical等级的日志")
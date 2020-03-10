#coding:utf-8
"""
封装日志
"""
import logging
class MyLog(object):
    @staticmethod
    def mylog():
        #创建日志收集器,设置收集器的等级
        mylog = logging.getLogger("mylog")
        mylog.setLevel("DEBUG")
        #创建日志输出到控制台渠道,设置等级
        sh = logging.StreamHandler()
        sh.setLevel("DEBUG")
        mylog.addHandler(sh)
        #创建日志输出到文件渠道,设置等级
        fh = logging.FileHandler(filename=r"C:\wsl\AutoTest\python2\日志\log.log",encoding="utf-8")
        fh.setLevel("DEBUG")
        mylog.addHandler(fh)

        #设置日志输出格式的设置
        formater = '%(asctime)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s:%(message)s'
        fm = logging.Formatter(formater)
        sh.setFormatter(fm)  #控制台
        fh.setFormatter(fm)  #文件
        return mylog

log = MyLog.mylog()

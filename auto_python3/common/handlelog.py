#coding
import logging
import os
from common.myconfig import conf
from common.handlepath import LOGDIR
class MyLog(object):
    @staticmethod
    def mylog():
        #创建日志收集器,设置收集器等级
        mylog = logging.getLogger("mylog")
        mylog.setLevel(conf.get("log","level"))
        #创建日志输出到控制台,设置等级
        sh = logging.StreamHandler()
        sh.setLevel(conf.get("log","sh_level"))
        mylog.addHandler(sh)
        #创建日志输出到文件,设置等级
        fh = logging.FileHandler(filename=os.path.join(LOGDIR,"log.log"),encoding="utf-8")
        fh.setLevel(conf.get("log","fh_level"))
        mylog.addHandler(fh)
        #设置日志输出格式
        formater = '%(asctime)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s:%(message)s'
        fm = logging.Formatter(formater)
        sh.setFormatter(fm)
        fh.setFormatter(fm)
        return mylog
log = MyLog.mylog()
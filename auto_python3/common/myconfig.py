#coding:utf-8
import os
from configparser import ConfigParser
from common.handlepath import CONFDIR
class Config(ConfigParser):
    def __init__(self,filename):
        super().__init__()
        self.filename = filename
        self.read(filename,encoding="utf-8")
    def write_data(self,section,option,value):
        """写入数据的方法"""
        self.set(section=section,option=option,value=value)
        self.write(fp=open(self.filename,"w"))
        
conf = Config(os.path.join(CONFDIR,"config.ini"))
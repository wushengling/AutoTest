#coding:utf-8
"""
"""

from configparser import ConfigParser

class Config(ConfigParser):
    def __init__(self,filename):
        super().__init__()
        self.filename = filename
        self.read(filename)
    def write_data(self,section,option,value):
        """" 写入数据的方法"""
        self.set(section,option,value)
        self.write(fp=open(self.filename,"w"))
        
        
        

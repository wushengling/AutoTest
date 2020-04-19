#coding:utf-8
# vscode读取不到了包路径解决方案
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

import pymysql
from common.myconfig import conf
class DB:
    def __init__(self):
        #连接数据库
        self.conn = pymysql.connect(host=conf.get("mysql","host"),
                                    port=conf.getint("mysql","port"),
                                    user=conf.get("mysql","user"),
                                    password=conf.get("mysql","pwd"),
                                    charset="utf8",
                                    cursorclass=pymysql.cursors.DictCursor
                                    )
        #创建一个游标对象
        self.cur = self.conn.cursor()
    def find_one(self,sql):
        '''获取查询出来的第一条数据'''
        self.conn.commit()
        self.cur.execute(sql)
        data = self.cur.fetchone()
        return data
    def find_all(self,sql):
        '''获取查询出来的所有数据'''
        self.conn.commit()
        self.cur.execute(sql)
        data = self.cur.fetchall()
        return data
    def find_count(self,sql):
        '''返回查询出来的数量'''
        self.conn.commit()
        data = self.cur.execute(sql)
        return data
    def close(self):
        '''关闭游标,断开连接'''
        self.cur.close()
        self.conn.close()
            
    
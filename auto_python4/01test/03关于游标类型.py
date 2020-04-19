#coding:utf-8
# vscode读取不到了包路径解决方案
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

import pymysql
#连接数据库
conn = pymysql.connect(host="120.78.128.25",
                port=3306,
                user="future",
                password="123456",
                #通过设置游标类型,可以控制查询出来的数据类型
                cursorclass=pymysql.cursors.DictCursor,
                charset="utf8")
#创建一个游标对象
cur = conn.cursor()
#执行sql语句
sql = "select * from futureloan.member limit 3"
cur.execute(sql)
#获取查询数据
# fetchone 查询一条
data = cur.fetchone()
print(data)  

#coding:utf-8
# vscode读取不到了包路径解决方案
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

import pymysql
from common.myconfig import conf
"""
数据库地址:120.78.128.25
端口:3306
账号:future
密码:123456
"""
#连接数据库
conn = pymysql.connect(host="120.78.128.25",
                port=3306,
                user="future",
                password="123456",
                charset="utf8")
#创建一个游标对象
cur= conn.cursor()
#执行sql语句
sql = "select * from futureloan.member limit 3"
#返回的是查询到的数据条数
res = cur.execute(sql)
print(res)
#获取查询的数据
#1.获取一条数据(返回的查询集中的第一条数据,元组类型)
data = cur.fetchone()
print(data)
print(cur.fetchone())
print(cur.fetchone())
print(cur.fetchone())
#2.获取查询集中的所有数据
datas = cur.fetchall()
print(datas)

#关于增加,删除,修改等相关涉及到数据库中数据变动的sql语句执行
#在执行完sql语句后,要多一步:调用commit提交事务
#conn.commit()

# pymssql  操作sqlserver
# cx_oracle 操作oracle
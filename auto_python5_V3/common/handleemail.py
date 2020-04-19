#coding:utf-8
# vscode读取不到了包路径解决方案
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

import smtplib
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from common.myconfig import conf
"""
smtp服务器:
smtp服务器地址:
    qq邮箱:smtp.qq.com  端口:465
    163邮箱:smtp.163.com  端口:465

账号:740776409@qq.com
授权码:ogfsbowjnvfpbbgc
"""
def send_email(filename,title):
    #第一步:连接邮箱smtp服务器,并登陆
    smtp = smtplib.SMTP_SSL(host=conf.get("email","host"),port=conf.getint("email","port"))
    smtp.login(user=conf.get("email","user"),password=conf.get("email","password"))
    
    #第二步:构建一封邮件
    #创建一封多组件的邮件
    msg = MIMEMultipart()
    with open(filename,"rb") as f:
        content = f.read()
    #创建邮件文本内容
    text_msg = MIMEText(content,_subtype="html",_charset="utf8")
    #添加到多组件的邮件中
    msg.attach(text_msg)
    #创建邮件的附件
    report_file = MIMEApplication(content)
    report_file.add_header('content-disposition', 'attachment',
                        filename= title)
    #将附件添加到多组件的邮件中
    msg.attach(report_file)
    
    #主题
    msg["Subject"] = title
    #发件人
    msg["From"] = conf.get("email","from_addr")
    #收件人
    msg["To"] = conf.get("email","to_addrs")

    #第三步:发送邮件
    smtp.send_message(msg,from_addr=conf.get("email","from_addr"),to_addrs=conf.get("email","to_addrs"))
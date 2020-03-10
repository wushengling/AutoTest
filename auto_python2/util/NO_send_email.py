#coding:utf-8
# 读取不到了路径解决方案
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import smtplib
from email.mime.text import MIMEText
from email.header import Header
class SendEmail:
    def send_email(self,user_list,sub,content):
        send_user = 'autotest975@163.com'
        email_host = 'smtp.163.com'
        password = 'qazwsx123456'
        
        user = "autotest975"+"<"+send_user+">"
        message =MIMEText(content,_subtype='plain',_charset='utf-8')
        message['Subject'] = sub
        message['From'] = user
        message['To'] = ";".join(user_list)
        server = smtplib.SMTP_SSL(email_host,465)
        server.login(send_user,password)
        server.send_message(user,user_list,message.as_string())
        server.close()
if __name__ == '__main__':
    sen = SendEmail()
    user_list = ['740776409@qq.com']
    sub = "这个是测试邮件"
    content = "这个是第一封测试邮件"
    sen.send_email(user_list,sub,content)
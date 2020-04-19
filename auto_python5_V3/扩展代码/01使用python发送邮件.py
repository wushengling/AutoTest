#coding:utf-8
import smtplib
from email.mime.text import MIMEText
"""
smtp服务器:
smtp服务器地址:
    qq邮箱:smtp.qq.com  端口:465
    163邮箱:smtp.163.com  端口:465

账号:740776409@qq.com
授权码:ogfsbowjnvfpbbgc
"""
#第一步:连接邮箱smtp服务器,并登陆
smtp = smtplib.SMTP_SSL(host="smtp.qq.com",port=465)
smtp.login(user="740776409@qq.com",password="ogfsbowjnvfpbbgc")

#第二步:构建一封邮件
with open(r"C:\wsl\AutoTest\auto_python5_V3\扩展代码\report.html","r",encoding="utf8") as f:
    content = f.read()
msg = MIMEText(content,_subtype="html",_charset="utf8")
#主题
msg["Subject"] = "接口自动化报告"
#发件人
msg["From"] = "740776409@qq.com"
#收件人
msg["To"] = "740776409@qq.com"

#第三步:发送邮件
smtp.send_message(msg,from_addr="740776409@qq.com",to_addrs="740776409@qq.com")
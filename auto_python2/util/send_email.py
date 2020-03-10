#coding:utf-8
# 读取不到了路径解决方案
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import smtplib
from email.mime.text import MIMEText
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
        server = smtplib.SMTP(email_host,25)
        server.login(send_user,password)
        server.send_message(user,user_list,message.as_string())
        server.close()
        
    def send_main(self,pass_list,fail_list):
        pass_num = len(pass_list)
        fail_num = len(fail_list)
        count_num = pass_num + fail_num
        pass_result = "%.2f%%" % (float(pass_num)/float(count_num)*100)
        fail_result = "%.2f%%" % (float(fail_num)/float(count_num)*100)
        
        user_list = ['740776409@qq.com']
        sub = "接口自动化测试报告"
        content = "此次一共运行接口个数为%d个，通过个数为%d个，失败个数为%d，通过率为%s，失败率为%s" %(count_num,pass_num,fail_num,pass_result,fail_result)
        print(content)
        # self.send_email(user_list,sub,content)
if __name__ == '__main__':
    sen = SendEmail()
    sen.send_main([1,2,3,4],[4,5,6])
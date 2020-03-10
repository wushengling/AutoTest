#coding:utf-8
import unittest
import re
import json
import HTMLTestRunner
from demo1 import RunMain
class TestMethod(unittest.TestCase):
    u'''demo'''
    def setUp(self):
        self.run = RunMain()
    def test_01(self):
        u'''验证码登录接口'''
        host = "http://192.168.1.238:9998"
        url = host+"/poipoi/users/login/phone"
        headers = {
            'Content-Type':'application/json',
            "Accept": "*/*"
            }
        body = {
            "deviceType": 1,
            "phone": "12000000001",
            "verifyCode": "120000"
            }
        res = self.run.run_main('POST',url,headers,body)
        # print(res)
        self.assertEqual(res.json()['status'],200,'测试失败')
        #globals()['变量名称']=值   设置为全局变量
        globals()['userId']=re.findall('"userId":(.+?),',res.text)[0]
        globals()['token']=re.findall('"token":"(.+?)"',res.text)[0]
        # print(userId,token)
    # @unittest.skip('test_02')   #容器  跳过
    def test_02(self):
        u'''访问个人信息接口'''
        host = "http://192.168.1.238:9998"
        url = host+"/poipoi/users/info"
        headers = {
            'Content-Type':'application/json',
            "Accept": "*/*",
            'userId':userId,
            'token':token
            }
        res = self.run.run_main('GET',url,headers)
        # print(res.text)
        # print(res.content.decode("UTF-8"))
        self.assertEqual(res.json()['status'],200,'测试失败')
if __name__ == "__main__":
    # unittest.main()

    #报告地址
    filepath = "C:\\wsl\\AutoTest\\\\auto_python2\\report\\html_report.html"
    fp = open(filepath,'wb')
    #创建容器,进行运行
    suite = unittest.TestSuite()
    suite.addTest(TestMethod('test_01'))
    suite.addTest(TestMethod('test_02'))
    # unittest.TextTestRunner().run(suite)
    runner = HTMLTestRunner.HTMLTestRunner(fp,verbosity=2,title="接口测试报告",description="demo_POI接口测试报告")
    runner.run(suite)


'''
unittest面试:
1.如何使用python开发测试框架?
-使用request包
-unittest框架  断言,判断  case的跳过skip\依赖\执行范围
-生成测试报告 HtmlTestRunner
-数据的存储  表格,数据库
-集成 git+jenkins
2.如何管理case?
-unittest框架  断言,判断  case的跳过\依赖\执行范围
-excel管理
3.简述Case的执行
setUp
tearDown
setUpClass
tearDownClass
test_01
test_02
4.如何解决case的依赖
-设置全局变量  通过正则表达式或引用的方式,输出为全局变量 globals()['变量名称']=值 
或存储数据库/配置文件
5.如何生成测试报告
下载HtmlTestRunner文件,放置在python安装目录的lib下
结合unittest,设置报告目录,输出报告
'''
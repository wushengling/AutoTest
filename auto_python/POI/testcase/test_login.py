#coding:utf-8
import unittest
import requests
import re
url = "http://192.168.1.238:9998/poipoi/users/login/phone"
headers = {
    'Content-Type':'application/json',
    'Accept':'*/*'
}
#body为json格式
body_pass = {
    'phone':'12000000001',
    'verifyCode':'120000',
    'deviceType':1
}
body_fail = {
    'phone':'12000000001',
    'verifyCode':'123456',
    'deviceType':1
}

class test_login(unittest.TestCase):
    u'''登录测试集合'''
    def setUp(self):
        # web端使用requests.session()
        # self.s = requests.session()
        pass
    def test_login_pass(self):
        u'''验证码登录成功'''
        result_pass = requests.post(url=url,headers=headers,json=body_pass)
        #打印结果
        print(result_pass.text)
        a = re.findall('"status":(.+?),',result_pass.text)

        self.assertEqual(a[0],'200')
    def test_login_fail(self):
        u'''验证码登录失败_验证码错误'''
        result_fail = requests.post(url=url,headers=headers,json=body_fail)
        #打印结果
        print(result_fail.text)
        a = re.findall('"message":"(.+?)"',result_fail.text)
        self.assertEqual(a[0],'验证码误')

        # #提取userId与token
        # userId_1 = re.findall('"userId":(.+?),',result.text)
        # token_1 = re.findall('"token":"(.+?)"',result.text)
        # # print(userId_1)
        # # print(token_1)
        # #访问个人中心
        # url_info = "http://192.168.1.238:9998/poipoi/users/info"
        # headers_info = {
        #             'Content-Type':'application/json',
        #             'Accept': '*/*',
        #             'userId':userId_1[0],
        #             'token':token_1[0]
        #             }
        # result_info = requests.get(url=url_info,headers=headers_info)
        # print(result_info.content) 


# if __name__ == '__main__':
#     unittest.main()
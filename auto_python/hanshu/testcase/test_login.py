#coding: utf-8
import requests
import re
import unittest
# 读取不到了路径解决方案
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

from common.postapi import Login 
class TestLogin(unittest.TestCase):
    def setUp(self):
        pass

    def test_login_01(self):
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
        result = Login.post(self,url,headers,body)
        # print(result.content)
        userId = re.findall('"userId":(.+?),',result.text)
        token = re.findall('"token":"(.+?)"',result.text)
        # print(userId,token)

        yuqi = '"status":200,'
        a = Login.is_login_success(self,yuqi,result.text)
        # print(a)
        self.assertTrue(a)

    def test_login_02(self):
        host = "http://192.168.1.238:9998"
        url = host+"/poipoi/users/login/phone"
        headers = {
            'Content-Type':'application/json',
            "Accept": "*/*"
            }
        body = {
            "deviceType": 1,
            "phone": "12000000001",
            "verifyCode": "123456"
            }
        result = Login.post(self,url,headers,body)
        # print(result.content)
        userId = re.findall('"userId":(.+?),',result.text)
        token = re.findall('"token":"(.+?)"',result.text)
        # print(userId,token)

        yuqi = '"status":200,'
        a = Login.is_login_success(self,yuqi,result.text)
        # print(a)
        self.assertFalse(a)
    
if __name__ == "__main__":
    unittest.main()

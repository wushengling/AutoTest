#coding:utf-8
import requests
import re
import json
class UpdateHeader:
    def update_header(self,data):
        #登录获取userId和token
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
        res = requests.post(url=url,headers=headers,json=body)
        res_json = res.json()
        return res_json["test"][data]
        
        # #正则提取方式，待验证
        # if data == "userId":
        #     return re.findall('"userId":(.+?),',res.text)[0]
        # else:
        #     return re.findall('"token":"(.+?)"',res.text)[0]
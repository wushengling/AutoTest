#coding:utf-8
import requests
import json
url = "http://192.168.1.238:9998/poipoi/users/login/phone"
headers = {'Content-Type':'application/json',
            "Accept": "*/*"}
#body为json
body ={
  "deviceType": 1,
  "phone": "12000000001",
  "verifyCode": "120000"
}
#json格式用json,data用data
# content-type 为json 传的json参数
# content-tpye 为urlencode 传的data参数
r = requests.post(url=url,headers=headers,json=body).json()

print(json.dumps(r,indent=2))  #格式化响应数据
# print(r.json()['data']['token'])
# print(r.content)


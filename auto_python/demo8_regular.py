#coding:utf-8
import requests
import re
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
# content-type 为urlencode 传的data参数
r = requests.post(url=url,headers=headers,json=body)
print(r.json()['data']['token'])
# # 正则表达式提取token的参数值
token_1 = re.findall('"token":"(.+?)"',r.text)  #结果格式为List
userId_1 = re.findall('"userId":(.+?),',r.text)  #结果格式为List
print(userId_1[0])
print(token_1[0])
print(r.json())


url_info= "http://192.168.1.238:9998/poipoi/users/info"
headers_info = {'Content-Type':'application/json',
                    'Accept': '*/*',
                    'userId':userId_1[0],
                    'token':token_1[0]}
r_info = requests.get(url=url_info,headers=headers_info)
print(r_info.json())
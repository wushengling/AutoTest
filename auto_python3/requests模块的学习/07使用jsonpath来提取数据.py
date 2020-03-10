#coding:utf-8
import requests
import jsonpath
"""
jsonpath     描述

"""
#登录
url = "http://api.lemonban.com/futureloan/member/login"
data = {
    "mobile_phone":"15099999999",
    "pwd":"12345678"
}
headers = {
    "X-Lemonban-Media-Type":"lemonban.v2"
}
res = requests.post(url=url,headers=headers,json=data)
data = res.json()
token_type =jsonpath.jsonpath(data,"$..token_type")[0]
token = jsonpath.jsonpath(data,"$..token")[0]
reg_name = jsonpath.jsonpath(data,"$..reg_name")[0]
code = jsonpath.jsonpath(data,"$..code")[0]
print(token_type)
print(token)
print(reg_name)
print(code)
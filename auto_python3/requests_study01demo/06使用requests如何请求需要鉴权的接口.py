#coding:utf-8
import requests
import json

#使用cookie+session鉴权
#使用requests中的session对象来发送请求
#使用session对象先登录,登录之后session对象会自动记录cookie信息,在请求需要登录的接口就可以通过鉴权
# s = requests.session()

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
a = res.content
b = json.loads(res.text)
print(b,type(b))
print(b['data']['token_info'])
token_type = data["data"]["token_info"]["token_type"]
token = data["data"]["token_info"]["token"]
token_value = token_type+" "+token

# 充值
re_url = "http://api.lemonban.com/futureloan/member/recharge"
re_data = {
    "member_id":7790183,
    "amount":"2000"
}
headers["Authorization"]=token_value
res = requests.post(url=re_url,headers=headers,json=re_data)
print(res.json())
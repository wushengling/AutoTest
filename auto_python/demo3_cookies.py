#coding:utf-8
import requests

#requests.session()  保持会话
session = requests.session()
url = "http://47.95.200.170/api/login"
headers = {"Content-Type":"application/json"}
body = {"username":"zhphuang",
        "password":"123456"}
r =session.post(url=url,headers=headers,json=body)
print(r.cookies)
print(r.json())
print(r.json()['data']['token'])


# 添加cookies
# c = requests.cookies.RequestsCookieJar
# c.set("key","value")
# c.set("key","value")
#添加cookies 到 session
# session.cookies.update(c)

url1= "http://47.95.200.170/api/role/roleList?offset=0&limit=50"
r1 = session.get(url=url1)
print(r1.json())

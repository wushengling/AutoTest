#coding:utf-8
import requests
session =requests.session()
url1= "http://47.95.200.170/api/role/roleList?offset=0&limit=50"
r1 = session.get(url=url1)   # 添加 allow_redirects=False 可以禁止重定向(默认为True)
print(r1.status_code)
print(r1.history)  #历史请求记录
print(r1.headers)
for i in r1.history:
    print(i.url)
    print(i.status_code)
    print(i.text)
    print(i.headers["Location"])
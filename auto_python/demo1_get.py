#coding:utf-8
import requests
from email.mime import application
url = "http://192.168.1.238:9998/poipoi/main/content/newest"
params = {'cursor':'1'} #参数存的格式为字典
headers ={'content-type':'application/json'} #header存的格式为字典
r = requests.get(url=url,params=params,headers=headers,verify=False)#verify=False 忽略ssl认证
print(r.status_code)    #查看响应状态码
print(r.headers)        #查看响应头
print(r.text)          #查看响应文本  运用utf-8 的格式
print(r.url)            #返回url地址
print(r.cookies)        #返回cookies值
print(r.headers)        #返回头部信息
print(r.encoding)       #返回编码格式
print(r.content)        #二进制流返回内容,用于返回值内容(自动解码gzip)
print(r.json())         #requests 中内置的JSON解码器,解析为字典(dict)格式
print(r.raise_for_status())#查看异常信息

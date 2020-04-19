#coding:utf-8
import requests
url = ""
data = {
    
}
requests.patch(url=url,json=data)
"""
get:用于获取资源（没有请求体）
post:向指定资源提交数据进行处理请求(例如提交表单或者上传文件),数据被包含在请求体中
    post请求可能会导致新的资源的建立和/或已有资源的修改
patch:用于更新服务器的数据(局部更新)
delete:用于服务器删除指定的数据
put:用于更新服务器的数据(数据整体更新)
""" 
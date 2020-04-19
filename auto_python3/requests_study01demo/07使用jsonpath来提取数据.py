#coding:utf-8
import requests
import jsonpath
"""
jsonpath     描述
 $          根节点
 .or[]      取子节点
 ..         子孙节点
 *          匹配所有元素节点
 []         如数组下标,根据内容选值等

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

#扩展
# json.loads()  将字符串中的json,转换为对应的python字典
# json.dumps()  将python中的字典,转化为对应的json字符串
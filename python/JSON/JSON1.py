'''
json         python
object   =   dict
array    =   list
string   =   str
number   =   int
number   =   float
true     =   True
false    =   False
null     =   None
'''

# 序列化
import json
import JSON

student = [
    {'name':'zhangsan','age':18,'flag':False},
    {'name':'zhaosi','age':17}
]

json_str = json.dumps(student)
print(json_str)
print(type(json_str))


# JSON对象 , JSON , JSON字符串
# ECMASCRIPT 


# A语言    <==   JSON   ==>     B语言    
#             中间数据类型

# JSON有自己的数据类型
# 虽然它和Javascript的数据类型
# 有些相似
# REST 服务的标准格式

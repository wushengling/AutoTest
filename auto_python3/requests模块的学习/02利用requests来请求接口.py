#coding:utf-8
import requests
url = "http://api.lemonban.com/futureloan/member/register"
headers = {
    "X-Lemonban-Media-Type":"lemonban.v1"
}
data = {
    "mobile_phone":"15099999999",
    "pwd":"12345678",
    "type":1,
    "reg_name":"test_01"
}
response = requests.post(url=url,headers=headers,json=data)
print(response.content.decode("utf-8"))
#参数使用json传递的时候,会自动加上请求头, Content-type:application/json
#参数使用data传递的时候,会自动加上请求头, Content-type:x-www-form-urlencoded
#参数使用file传递的时候,会自动加上请求头, Content-type:multipart/form-data  一般用于上传文件
# file_data = {"参数名":("文件名,open("文件地址","rb"),"text/py")}



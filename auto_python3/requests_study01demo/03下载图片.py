#coding:utf-8
import requests

url = "https://www.baidu.com/img/bd_logo1.png"
response = requests.get(url=url)
with open("baidu.png","wb") as f :
    f.write(response.content)

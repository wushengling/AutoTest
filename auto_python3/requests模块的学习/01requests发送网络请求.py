#coding:utf-8
"""
User-Agent:   反爬虫
"""
import requests
url = "https://www.baidu.com"
headers = {
    
}
response = requests.get(url=url,headers=headers)
# text属性:自动识别返回内容的解码方式,进行解码(有可能出现乱码)
# print(response.text)

#content属性:需要使用decode方法,指定解码方式进行解码
print(response.content.decode("utf-8"))

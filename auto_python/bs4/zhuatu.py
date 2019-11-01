#coding:utf-8
from bs4 import BeautifulSoup
import requests
import os
r = requests.get("http://m.699pic.com/tupian/chahua-so.html")
# print(r.content)
soup = BeautifulSoup(r.content,"html.parser")
# print(soup)
images = soup.find_all(class_="lazy")
# print(images)
path = "D:\\Testing tools\\muke\AutoTest\\auto_python\\bs4\\images\\"
for i in images:
    try:
        url = i['src']
        name = i['alt']
        # print(url,name)
        ima = requests.get(url)
        
        with open(path+name+".jpg","wb") as f:
            f.write(ima.content)
    except Exception as msg:
        print(msg)
    


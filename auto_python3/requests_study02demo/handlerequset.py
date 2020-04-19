#coding:utf-8
import requests
#使用token鉴权的
class SendRequest(object):
    @staticmethod
    def send_request(url,mehtod,headers=None,params=None,data=None,json=None,files=None):
        if mehtod == "get":
            res = requests.get(url=url,params=params,headers=headers)
        elif mehtod == "post":
            res = requests.post(url=url,data=data,json=json,files=files,headers=headers)
        elif mehtod == "patch":
            res = requests.patch(url=url,data=data,json=json,files=files,headers=headers)
        
        return res
    
#如果项目使用cookie+session鉴权的
class SendRequest2(object):
    def __init__(self):
        self.session = requests.session()
    def send_request(self,url,mehtod,headers=None,params=None,data=None,json=None,files=None):
        if mehtod == "get":
            res = self.session.get(url=url,params=params,headers=headers)
        elif mehtod == "post":
            res = self.session.post(url=url,data=data,json=json,files=files,headers=headers)
        elif mehtod == "patch":
            res = self.session.patch(url=url,data=data,json=json,files=files,headers=headers)
            
        return res


    
    
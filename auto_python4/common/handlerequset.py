#coding:utf-8
import requests
class SendRequest(object):
    def __init__(self):
        self.session = requests.session()
    def send_request(self,url,method,headers=None,params=None,data=None,json=None,files=None):
        method = method.lower()
        if method == "get":
            response = self.session.get(url=url,params=params,headers=headers)
        elif method == "post":
            response = self.session.post(url=url,data=data,json=json,files=files,headers=headers)
        elif method == "patch":
            response = self.session.patch(url=url,data=data,json=json,files=files,headers=headers)
        return response


    
    
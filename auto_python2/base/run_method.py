#coding:utf-8
import requests
class RunMethod:
    def __init__(self):
        self.host = "http://192.168.1.238:9998"
    def get_main(self,url,data=None,header=None):
        res =None
        if header != None:
            res = requests.get(url=self.host+url,json=data,headers=header)
        else:
            res = requests.get(url=self.host+url,headers=header,json=data)
        return res

    def post_main(self,url,data=None,header=None):
        res =None
        if header != None:
            res = requests.post(url=self.host+url,json=data,headers=header)
        else:
            res = requests.post(url=self.host+url,json=data)
        return res
    
    def run_main(self,method,url,data=None,header=None):
        res = None
        if method == 'get':
            res = self.get_main(url,data,header)
        else:
            res = self.post_main(url,data,header)
        return res
if __name__ == "__main__":
    method = 'post'
    url = '/poipoi/users/login/phone'
    data = {'deviceType': 1, 'phone': '12000000001', 'verifyCode': '120000'}
    header = {'Accept': '*/*', 'Content-Type': 'application/json'}
    a = RunMethod()
    b = a.run_main(method,url,data,header)
    print(b.json())

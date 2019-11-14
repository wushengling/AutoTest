#coding:utf-8
import requests
import json
class RunMain():

    # def __init__(self,method,url,headers=None,body=None):    #方法二
    #     self.res = self.run_main(method,url,headers,body)

    def api_get(self,url,headers,body):
        res = requests.get(url=url,headers=headers,json=body)
        # json.dumps(res,indent=2,ensure_ascii=False)   格式化结果
        return res

    def api_post(self,url,headers,body):
        #返回响应为JSON格式
        res = requests.post(url=url,headers=headers,json=body) #.json()
        # json.dumps(res,indent=2,ensure_ascii=False)    格式化结果
        return res

    def run_main(self,method,url,headers=None,body=None):
        res = None
        if method == 'GET':
            res = self.api_get(url,headers,body)
        else:
            res = self.api_post(url,headers,body)
        return res

if __name__ == "__main__":
    run = RunMain()
    host = "http://192.168.1.238:9998"
    url = host+"/poipoi/users/login/phone"
    headers = {
        'Content-Type':'application/json',
        "Accept": "*/*"
        }
    body = {
        "deviceType": 1,
        "phone": "12000000001",
        "verifyCode": "123456"
        }
    a = run.run_main('POST',url,headers,body)
    print(a)

    # #方法二
    # host = "http://192.168.1.238:9998"
    # url = host+"/poipoi/users/login/phone"
    # headers = {
    #     'Content-Type':'application/json',
    #     "Accept": "*/*"
    #     }
    # body = {
    #     "deviceType": 1,
    #     "phone": "12000000001",
    #     "verifyCode": "120000"
    #     }
    # a = RunMain('POST',url,headers,body)
    # print(a.res)
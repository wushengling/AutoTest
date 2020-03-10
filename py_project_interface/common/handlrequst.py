'''
 AUTH:RODDY
 DATE:2020/2/22
 TIME:19:46
 FILE:handlrequst.py
 '''
import requests
class SendRequest():
    def __init__(self):
        self.send=requests.session()
    def sendrequest(self,method,url,headers=None,data=None,json=None,param=None):
        method=method.lower()
        if method == 'post':
            response=self.send.post(url=url,headers=headers,data=data,json=json,)
        elif method =='get':
            response=self.send.get(url=url,headers=headers,param=param)
        return response

if __name__ == '__main__':
    register_api = r'http://api.lemonban.com/futureloan/member/register'
    heads={
    'X-Lemonban-Media-Type':'lemonban.v2'}
    regster_data ={
        'mobile_phone':13011110001,
        'pwd':'12345678',
        'type':'1',
        'reg_name':'roody'
    }
    send =SendRequest()
    res=send.sendrequest(method='Post',url=register_api,headers=heads,json=regster_data)
    print(res.json())


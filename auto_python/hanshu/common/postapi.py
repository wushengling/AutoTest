#coding:utf-8
import requests
import re
class Login():
    def __init__(self,s):
        pass
    def post(self,url,headers,body):
        result = requests.post(url=url,json=body,headers=headers)
        return result

    def is_login_success(self,yuqi,res):
        if yuqi in res:
            return True
        else:
            return False
    
if __name__ == "__main__":
    pass
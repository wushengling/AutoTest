#coding:utf-8
import requests
import re
class Login():
def post(url,headers,body):
    result = requests.post(url=url,json=body,headers=headers)
    return result

def is_login_success(yuqi,res):
    if yuqi in res:
        return True
    else:
        return False
    

#coding:utf-8
from unittest import mock

res_data = {"code":0,
            "msg":"OK"
            }
request = mock.Mock(return_value=res_data)

data = {'user':'python01',
        'pay_pwd':123456,
        'money':88.88}

res = request(data)
print(res)
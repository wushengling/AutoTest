'''
 AUTH:RODDY
 DATE:2020/2/22
 TIME:21:55
 FILE:testcase_change.py
 '''
import os
import unittest
import jsonpath
from common.readexcel import ReadExcel
from common.config import conf
from libray.ddt import ddt,data
from common.handlrequst import SendRequest
from common.dirpath import DATAPATH
from common.handlelog import log

@ddt
class TestCaseRecharge(unittest.TestCase):
    #读取测试数据
    excel=ReadExcel(filename=os.path.join(DATAPATH,conf.get('workbook','name')),sheetname=conf.get('workbook','sheet03'))
    cases=excel.read_excel()
    base_url='http://api.lemonban.com/futureloan'
    headers={'X-Lemonban-Media-Type':'lemonban.v2'}
    login_api = 'http://api.lemonban.com/futureloan/member/login'
    login_data ={
        'mobile_phone':13011110001,
        'pwd':'12345678'
    }
    send=SendRequest()
    @classmethod
    def setUpClass(cls):
        login=cls.send.sendrequest(method='post',url=cls.login_api,headers=cls.headers,json=cls.login_data)
        login_info=login.json()
        token=jsonpath.jsonpath(login_info,'$..token')[0]
        token_type=jsonpath.jsonpath(login_info,'$..token_type')[0]
        cls.headers['Authorization']='{} {}'.format(token_type,token)
        cls.uid=jsonpath.jsonpath(login_info,'$..id')[0]
        #print(cls.uid,type(cls.uid))
    @data(*cases)
    def test_recharge(self,case):
        #获取测试数据
        ##title method url  data  expected
        title=case['title']
        method=case['method']
        url=self.base_url+case['url']
        data=case['data']
        data=eval(data.replace('#member_id#',str(self.uid)))
        expected=case['expected']
        #发送请求
        respose=self.send.sendrequest(method=method,url=url,headers=self.headers,json=data)
        log.info(respose.json())



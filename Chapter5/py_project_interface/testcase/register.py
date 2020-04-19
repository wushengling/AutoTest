'''
 AUTH:RODDY
 DATE:2020/2/16
 TIME:14:54
 FILE:testcase.py
 '''
import unittest
import os
import random
from libray.ddt import ddt,data
from common.readexcel import ReadExcel
from common.dirpath import DATAPATH
from common.config import conf
from common.handlrequst import SendRequest
from common.handlelog import log
@ddt
class Test_register(unittest.TestCase):
    #获取测试数据
    base_url='http://api.lemonban.com/futureloan'
    excel=ReadExcel(filename=os.path.join(DATAPATH,conf.get('workbook','name')),
                    sheetname=conf.get('workbook','sheet01'))
    cases=excel.read_excel()
    headers={'X-Lemonban-Media-Type':'lemonban.v2'}
    print(cases[0])
    send=SendRequest()
    @data(*cases)
    def test_register(self,case):
        #第一步,准备测试数据
        #title  case_id
        print(case)
        row=case['case_id']+1
        method=case['method']
        url=self.base_url+case['url']
        data=case['data']
        ####phone#
        data=eval(data.replace('#phone#',self.telnum()))
        expected=eval(case['expected'])
        #第二部,发送请求
        response=self.send.sendrequest(method=method,url=url,headers=self.headers,json=data)
        res=response.json()
        #第三步,进行断言,回写数据
        try :
            self.assertEqual(res['code'],expected['code'])
            self.assertEqual(res['msg'],expected['msg'])
        except AssertionError as e :
            log.exception(e)
            log.error('用例{}测试未通过'.format(case['title']))
            self.excel.write_excel(row=row,column=8,value='未通过')
            raise  e
        else:
            log.info('用例{}测试通过'.format(case['title']))
            self.excel.write_excel(row=row,column=8,value='通过')

    def telnum(self):
        ram=(random.randint(100000000,999999999))
        ram_str=str(ram)[0:8]
        tel='136'+ram_str
        return tel






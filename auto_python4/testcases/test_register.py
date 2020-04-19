#coding:utf-8
# vscode读取不到了包路径解决方案
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import unittest
import random
from library.ddt import ddt,data
from common.handlerequset import SendRequest
from common.excel import OperationExcel
from common.handlepath import DATADIR
from common.myconfig import conf
from common.handlelog import log
from common.connectdb import DB
@ddt
class TestRegister(unittest.TestCase):
    excel =OperationExcel(filename=os.path.join(DATADIR,"apicases.xlsx"),sheet_name="register")
    cases = excel.read_excel()
    request = SendRequest()
    db = DB()
    @data(*cases)
    def test_register(self,case):
        url = conf.get("env","base_url")+case["url"]
        method = case["method"]
        #生成一个手机号码
        phone = self.random_phone()
        #替换用例数据中的手机号码(替换replace)
        case["data"] = case["data"].replace("#phone#",phone)
        
        data = eval(case["data"])
        headers = eval(conf.get("env","headers"))
        expected = eval(case["expected"])
        row = case["case_id"]+1
        
        response = self.request.send_request(url=url,method=method,json=data,headers=headers)
        res = response.json()
        try:
            self.assertEqual(expected["code"],res["code"])
            self.assertEqual(expected["msg"],res["msg"])
            if case["check_sql"]:
                sql = "SELECT * FROM futureloan.member WHERE mobile_phone={}".format(data["mobile_phone"])
                count = self.db.find_count(sql)
                self.assertEqual(1,count)
        except AssertionError as e:
            print("预期结果: ",expected)
            print("实际结果: ",res)
            self.excel.write_excel(row=row,column=8,value="FAIL")
            log.error("用例:{},执行未通过".format(case["title"]))
            log.exception(e)
            #抛出异常
            raise e            
        else:
            self.excel.write_excel(row=row,column=8,value="PASS")
            log.info("用例:{},执行通过".format(case["title"]))
    def random_phone(self):
        for i in range(1000):
            phone = "136"
            for i in range(8):
                n = random.randint(0,9)
                phone +=str(n)
            #查看随机生成的手机号是否存在
            sql = "SELECT * FROM futureloan.member WHERE mobile_phone={}".format(phone)
            count = self.db.find_count(sql)
            if count == 0:
                return phone
@ddt
class TestLogin(unittest.TestCase):
    excel =OperationExcel(filename=os.path.join(DATADIR,"apicases.xlsx"),sheet_name="login")
    cases = excel.read_excel()
    request = SendRequest()
    @data(*cases)
    def test_login(self,case):
        url = conf.get("env","base_url")+case["url"]
        method = case["method"]
        data = eval(case["data"])
        headers = eval(conf.get("env","headers"))
        expected = eval(case["expected"])
        row = case["case_id"]+1
        
        response = self.request.send_request(url=url,method=method,json=data,headers=headers)
        res = response.json()
        try:
            self.assertEqual(expected["code"],res["code"])
            self.assertEqual(expected["msg"],res["msg"])
        except AssertionError as e:
            print("预期结果: ",expected)
            print("实际结果: ",res)
            self.excel.write_excel(row=row,column=8,value="FAIL")
            log.error("用例:{},执行未通过".format(case["title"]))
            log.exception(e)
            #抛出异常
            raise e            
        else:
            self.excel.write_excel(row=row,column=8,value="PASS")
            log.info("用例:{},执行通过".format(case["title"]))
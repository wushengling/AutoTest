#coding:utf-8
# vscode读取不到了包路径解决方案
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

import unittest
import jsonpath
from decimal import Decimal
from library.ddt import ddt,data
from common.excel import OperationExcel
from common.handlepath import DATADIR
from common.handlerequset import SendRequest
from common.myconfig import conf
from common.handlelog import log
from common.connectdb import DB
from common.handledata import CaseData,replace_data
@ddt
class TestRecharge(unittest.TestCase):
    excel = OperationExcel(filename=os.path.join(DATADIR,"apicases.xlsx"),sheet_name="recharge")
    cases = excel.read_excel()
    request = SendRequest()
    db = DB()
    @classmethod
    def setUpClass(cls):
        #这个方法在该测试类的用例执行之前会执行
        #在这个方法里面进行登录
        url = conf.get("env","base_url")+"/member/login"
        data = {
            "mobile_phone":conf.get("test_data","phone"),
            "pwd":conf.get("test_data","pwd")
        }
        headers = eval(conf.get("env","headers"))
        response = cls.request.send_request(url=url,method="post",json=data,headers=headers)
        res = response.json()
        #提取token,token_type,保存为CaseData类的类属性
        token = jsonpath.jsonpath(res,"$..token")[0]
        token_type = jsonpath.jsonpath(res,"$..token_type")[0]
        CaseData.token_value = token_type+" "+token
        CaseData.token = token
        #提取member_id,保存为CaseData类的类属性
        CaseData.member_id = str(jsonpath.jsonpath(res,"$..id")[0])
        
    @data(*cases)
    def test_recharge(self,case):
        url = conf.get("env","base_url") + case["url"]
        method = case["method"]
        #在请求头中加入setUpClass中提取出来的token
        headers = eval(conf.get("env","headers"))
        headers["Authorization"]=getattr(CaseData,"token_value")
        #替换用例数据中的手机号码(替换replace)
        case["data"]=replace_data(case["data"])
        data = eval(case["data"])
        #在请求体中加入,时间戳和签名
        
        expected = eval(case["expected"])
        row = case["case_id"] + 1
        #发送请求之前获取用户余额
        if case["check_sql"]:
            sql = "SELECT leave_amount FROM futureloan.member WHERE mobile_phone={}".format(conf.get("test_data","phone"))
            #查询当前用户的余额
            start_money = self.db.find_one(sql)["leave_amount"]
            
        response = self.request.send_request(url=url,method=method,json=data,headers=headers)
        res = response.json()
        try:
            self.assertEqual(expected["code"],res["code"])
            self.assertEqual(expected["msg"],res["msg"])
            #判断是否需要进行sql校验
            if case["check_sql"]:
                sql = "SELECT leave_amount FROM futureloan.member WHERE mobile_phone={}".format(conf.get("test_data","phone"))
                #查询当前用户的余额
                end_money = self.db.find_one(sql)["leave_amount"]
                self.assertEqual(Decimal(str(data["amount"])),end_money-start_money)
        except AssertionError as e:
            print("预期结果: ",expected)
            print("实际结果: ",res)
            self.excel.write_excel(row=row,column=8,value="FAIL")
            log.error("用例:{},执行未通过".format(case["title"]))
            log.exception(e)
            raise e
        else:
            self.excel.write_excel(row=row,column=8,value="PASS")
            log.info("用例:{},执行通过".format(case["title"]))
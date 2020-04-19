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
from common.myconfig import conf
from common.handlerequset import SendRequest
from common.connectdb import DB
from common.handlelog import log
@ddt
class TestWithdraw(unittest.TestCase):
    excel = OperationExcel(filename=os.path.join(DATADIR,"apicases.xlsx"),sheet_name="withdraw")
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
        response = cls.request.send_request(url=url,method="post",headers=headers,json=data)
        res = response.json()
        #提取token,保存为类属性
        token = jsonpath.jsonpath(res,"$..token")[0]
        token_type = jsonpath.jsonpath(res,"$..token_type")[0]
        cls.token_value = token_type+" "+token
        #提取member_id,保存为类属性
        cls.member_id = jsonpath.jsonpath(res,"$..id")[0]
        
    @data(*cases)
    def test_withdraw(self,case):
        url = conf.get("env","base_url")+case["url"]
        method = case["method"]
        #在请求头中加入setUpClass中提取出来的token
        headers = eval(conf.get("env","headers"))
        headers["Authorization"]=self.token_value
        #替换用例数据中的手机号码(替换replace)
        case["data"]=case["data"].replace("#member_id#", str(self.member_id))
        data = eval(case["data"])
        expected = eval(case["expected"])
        row = case["case_id"]+1
        #发送请求之前获取用户余额
        if case["check_sql"]:
            sql = case["check_sql"].format(conf.get("test_data","phone"))
            start_money = self.db.find_one(sql)["leave_amount"]
        response = self.request.send_request(url=url,method=method,json=data,headers=headers)
        res = response.json()
        try:
            self.assertEqual(expected["code"],res["code"])
            self.assertEqual(expected["msg"],res["msg"])
            #判断是否需要进行sql校验
            if case["check_sql"]:
                sql = case["check_sql"].format(conf.get("test_data","phone"))
                end_money = self.db.find_one(sql)["leave_amount"]
                self.assertEqual(Decimal(str(data["amount"])),start_money-end_money)
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
            
        
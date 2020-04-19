#coding:utf-8
# vscode读取不到了包路径解决方案
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

import unittest
import jsonpath
from common.excel import OperationExcel
from common.handlepath import DATADIR
from common.myconfig import conf
from library.ddt import ddt,data
from common.handlerequset import SendRequest
from common.handledata import CaseData,replace_data
from common.handlelog import log
from common.connectdb import DB

@ddt
class TestAudit(unittest.TestCase):
    excel = OperationExcel(filename=os.path.join(DATADIR,"apicases.xlsx"),sheet_name="audit")
    cases = excel.read_excel()
    request = SendRequest()
    db = DB()
    @classmethod
    def setUpClass(cls):
        """管理员登录"""
        url = conf.get("env","base_url")+"/member/login"
        data = {
            "mobile_phone":conf.get("test_data","admin_phone"),
            "pwd":conf.get("test_data","admin_pwd")
        }
        headers = eval(conf.get("env","headers"))
        response = cls.request.send_request(url=url,method="post",headers=headers,json=data)
        res = response.json()
        token = jsonpath.jsonpath(res,"$..token")[0]
        token_type = jsonpath.jsonpath(res,"$..token_type")[0]
        CaseData.admin_token_value = token_type+" "+token
        CaseData.admin_member_id = str(jsonpath.jsonpath(res,"$..id")[0])

    def setUp(self):
        """新增项目"""
        url = conf.get("env","base_url")+"/loan/add"
        data = {
            "member_id":getattr(CaseData,"admin_member_id"),
            "title":"借钱实现财富自由",
            "amount":2000,
            "loan_rate":12.0,
            "loan_term":3,
            "loan_date_type":1,
            "bidding_days":5
        }
        headers = eval(conf.get("env","headers"))
        headers["Authorization"] = getattr(CaseData,"admin_token_value") # == CaseData.admin_token_value 
        response = self.request.send_request(url=url,method="post",headers=headers,json=data)
        res = response.json()
        CaseData.loan_id = str(jsonpath.jsonpath(res,"$..id")[0])
    @data(*cases)
    def test_audit(self,case):
        url = conf.get("env","base_url")+case["url"]
        method = case["method"]
        headers = conf.get("env","headers")
        headers["Authorization"]= getattr(CaseData,"admin_token_value")
        data = eval(replace_data(case["data"]))
        excepted = case["expected"]
        row = case["case_id"]+1
        response = self.request.send_request(url=url,method=method,headers=headers,json=data)
        res = response.json()
        #判断是否审核通过的用例,并且审核通过,保存其loan_id给后面接口使用
        if excepted["code"]==0 and case["title"]=="审核通过":
            CaseData.pass_loan_id = str(data["loan_id"])
        try:
            self.assertEqual(excepted["code"],res["code"])
            self.assertEqual(excepted["msg"],res["msg"])
            if case["check_sql"]:
                sql = replace_data(case["check_sql"])
                status_sql = self.db.find_one(sql=sql)["status"]
                #断言数据库中的标状态是否与预期的一致
                self.assertEqual(excepted["status"],status_sql)
                
        except AssertionError as e:
            print("预期结果: "+excepted)
            print("实际结果: "+res)
            self.excel.write_excel(row=row,column=8,value="FAIL")
            log.error("用例{},未通过".format(case["title"]))
            log.exception(e)
        else:
            self.excel.write_excel(row=row,column=8,value="PASS")
            log.info("用例{},通过".format(case["title"]))

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
"""
投资接口:
1.需要有标:管理员登录,加标,审核
2.用户登录
3.投资用例

#关于投资的sql语句校验
1.用户表--校验用户余额,是否发生变化,变化金额等于所投金额(根据用户id,去查member表)
2.根据用户id和标id去投资表中查用户的投资记录(查invest表)
3.根据用户id去流水表中查询流水记录(查询用户投资之后是否多一条记录)
4.在刚好投满的情况下,可以根据投资记录的id,去汇款计划表中查询是否,生成汇款计划

"""
@ddt
class TestInvest(unittest.TestCase):
    excel = OperationExcel(filename=os.path.join(DATADIR,"apicases.xlsx"),sheet_name="invest")
    cases = excel.read_excel()
    request = SendRequest()
    db = DB()
    @data(*cases)
    def test_invest(self,case):
        url = conf.get("env","base_url")+case["url"]
        method = case["method"]
        if case["interface"].lower() != "login":   
            headers = conf.get("env","headers")
            headers["Authorization"]= getattr(CaseData,"admin_token_value")
        data = eval(replace_data(case["data"]))
        excepted = case["expected"]
        row = case["case_id"]+1
        response = self.request.send_request(url=url,method=method,headers=headers,json=data)
        res = response.json()
        #发送请求之后,判断是否是登陆接口
        if case["interface"].lower() == "login":
            token = jsonpath.jsonpath(res,"$..token")[0]
            token_type = jsonpath.jsonpath(res,"$..token_type")[0]
            CaseData.token_value = token_type+" "+token
            CaseData.member_id = str(jsonpath.jsonpath(res,"$..id")[0])
        #发送请求之后,判断是否是新增项目
        if case["interface"].lower() == "add":
            CaseData.loan_id = str(jsonpath.jsonpath(res,"$..id")[0])
        try:
            self.assertEqual(excepted["code"],res["code"])
            # self.assertEqual(excepted["msg"],res["msg"])
            #成员断言
            self.assertIn(excepted["msg"],res["msg"])
            # if case["check_sql"]:
            #     sql = replace_data(case["check_sql"])
            #     # self.db.find_one(sql)[]
                
        except AssertionError as e:
            print("预期结果: "+excepted)
            print("实际结果: "+res)
            self.excel.write_excel(row=row,column=8,value="FAIL")
            log.error("用例{},未通过".format(case["title"]))
            log.exception(e)
        else:
            self.excel.write_excel(row=row,column=8,value="PASS")
            log.info("用例{},通过".format(case["title"]))

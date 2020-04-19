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
from library.ddt import ddt,data
from common.myconfig import conf
from common.handlerequset import SendRequest
from common.handledata import CaseData,replace_data
from common.handlelog import log
class TestAdd(unittest.TestCase):
    excel = OperationExcel(filename=os.path.join(DATADIR,"apicases.xlsx"),sheet_name="add")
    cases = excel.read_excel()
    request = SendRequest()
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
        #提取token,token_type,保存为CaseData类的类属性
        token = jsonpath.jsonpath(res,"$..token")[0]
        token_type = jsonpath.jsonpath(res,"$..token_type")[0]
        # 保存为CaseData类的类属性
        CaseData.admin_token_value = token_type+" "+token
        # 保存为CaseData类的类属性
        CaseData.admin_member_id = str(jsonpath.jsonpath(res,"$..id")[0]) 
    @data(*cases)
    def test_add(self,case):
        #第一步 获取测试数据
        url = conf.get("env","base_url")+case["url"]
        method = case["method"]
        headers = eval(conf.get("env","headers"))
        headers["Authorization"] = getattr(CaseData,"admin_token_value")
        data = eval(replace_data(case["data"]))
        expected = eval(case["expected"])
        row = case["case_id"]+1
        #第二步 发送请求获取实际结果
        response = self.request.send_request(url=url,method=method,headers=headers,json=data)
        res = response.json()
        #第三步 断言
        try:
            self.assertEqual(expected["code"],res["code"])
            self.assertEqual(expected["msg"],res["msg"])
        except AssertionError as e:
            print("预期结果: ",expected)
            print("实际结果: ",res)
            self.excel.write_excel(row=row,column=8,value="FAIL")
            log.error("用例{},执行未通过".format(case["title"]))
            log.exception(e)
        else:
            self.excel.write_excel(row=row,column=8,value="PASS")
            log.info("用例{},执行通过".format(case["title"]))
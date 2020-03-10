#coding:utf-8
# 读取不到了路径解决方案
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from util.operation_excel import OperationExcel
from base.run_method import RunMethod
from data.get_data import GetData
from jsonpath_rw import jsonpath,parse
import json
class DependentData:
    def __init__(self,case_id):
        self.case_id = case_id
        self.opera_excel = OperationExcel()
        self.run_method = RunMethod()
        self.data = GetData()
    #通过依赖id去获取该依赖id的整行数据
    def get_case_line_data(self):
        rows_data = self.opera_excel.get_rows_data(self.case_id)
        return rows_data
    #执行依赖测试，获取结果
    def run_dependent(self):
        row_num = self.opera_excel.get_row_num(self.case_id)
        request_url = self.data.get_request_url(row_num)
        request_method = self.data.get_request_method(row_num)
        request_header = self.data.is_header(row_num)
        request_data = self.data.get_data_for_json(row_num)
        res = self.run_method.run_main(request_method,request_url,request_data,request_header)
        res_str = json.dumps(res.json(),ensure_ascii=False)
        return json.loads(res_str)
    #根据依赖的返回数据去获取执行依赖测试case的响应，然后返回
    def get_data_for_key(self,row):
        depend_data = self.data.get_depend_key(row)
        response_data = self.run_dependent()
        json_exe = parse(depend_data)
        madle = json_exe.find(response_data)
        a = type(response_data)
        return [math.value for math in madle][0]
if __name__ == "__main__":
    a = DependentData(1)
    b = a.get_data_for_key(3)
    print(b)
        
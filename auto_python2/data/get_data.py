#coding:utf-8
# 读取不到了路径解决方案
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from util.operation_excel import OperationExcel
import data.data_config
from util.operation_json import OperetionJson
class GetData:
    def __init__(self):
        self.opera_excel = OperationExcel()
    #获取excel行数,就是我们的case个数
    def get_case_line(self):
        return self.opera_excel.get_lines()
    #获取名称
    def get_name(self,row):
        col = data.data_config.get_name()
        name = self.opera_excel.get_value(row,col)
        return name
    #获取是否执行
    def get_is_run(self,row):
        flag = None
        col = data.data_config.get_run()
        run_status = self.opera_excel.get_value(row,col)
        if run_status == 'yes':
            flag = True
        else:
            flag = False
        return flag
    #是否携带header
    def is_header(self,row):
        col = data.data_config.get_is_header()
        header = self.opera_excel.get_value(row,col)
        if header == 'yes':
            return data.data_config.get_header_value()
        else:
            return None
    #获取请求方式
    def get_request_method(self,row):
        col = data.data_config.get_request_way()
        request_method = self.opera_excel.get_value(row,col)
        return request_method
    #获取url
    def get_request_url(self,row):
        col = data.data_config.get_url()
        url = self.opera_excel.get_value(row,col)
        return url
    #获取请求数据关键字
    def get_request_data(self,row):
        col = data.data_config.get_data()
        value = self.opera_excel.get_value(row,col)
        if value =='':
            return None
        else:
            return value
    #通过获取关键字拿到 data数据
    def get_data_for_json(self,row):
        opera_json = OperetionJson()
        request_data = opera_json.get_data(self.get_request_data(row))
        return request_data
    #获取预期结果
    def get_expect(self,row):
        col = data.data_config.get_expect()
        expect = self.opera_excel.get_value(row,col)
        if expect == '':
            return None
        else:
            return expect

if __name__ == "__main__":
    a = GetData()
    print(a.get_case_line())

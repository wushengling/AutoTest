#coding:utf-8
import json
# 读取不到了路径解决方案
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from base.run_method import RunMethod
from data.get_data import GetData

class RunTest:
    def __init__(self):
        self.run_method = RunMethod()
        self.data = GetData()
    #执行程序的主入口
    def go_on_run(self):
        res =None
        rows_count = self.data.get_case_line()
        for i in range(1,rows_count):
            url = self.data.get_request_url(i)
            method = self.data.get_request_method(i)
            is_run = self.data.get_is_run(i)
            data = self.data.get_data_for_json(i)
            header = self.data.is_header(i)
            name = self.data.get_name(i)
            if is_run :
                res = self.run_method.run_main(method,url,data,header)
                print(name+'\n'+json.dumps(res.json(),indent=2,ensure_ascii=False))

if __name__ == "__main__":
    a = RunTest()
    a.go_on_run()


#coding:utf-8
import json
# 读取不到了路径解决方案
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from data.get_data import GetData
from util.common import CommonUtil
from base.run_method import RunMethod
from data.dependent_data import DependentData
class RunTest:
    def __init__(self):
        self.run_method = RunMethod()
        self.data = GetData()
        self.common = CommonUtil()
    #执行程序的主入口
    def go_on_run(self):
        res =None
        pass_count = []
        fail_count = []
        rows_count = self.data.get_case_line()
        for i in range(1,rows_count):
            is_run = self.data.get_is_run(i)
            if is_run :
                url = self.data.get_request_url(i)
                method = self.data.get_request_method(i)
                data = self.data.get_data_for_json(i)
                header = self.data.is_header(i)
                name = self.data.get_name(i)
                expect = self.data.get_expect(i)
                depend_case = self.data.is_depend(i)
                if depend_case != None:
                    self.depend_data = DependentData(depend_case)
                    # 获取依赖的value
                    depend_value = self.depend_data.get_data_for_key(i)
                    #获取依赖的key
                    depend_key = self.data.get_depend_field(i)
                    data[depend_key] = depend_value
                    print(data)
                res = self.run_method.run_main(method,url,data,header)
                if self.common.is_contain(expect,json.dumps(res.json(),indent=2,ensure_ascii=False)):
                    self.data.write_result(i,"PASS")
                    pass_count.append(i)
                    # print(res.json())
                else:
                    self.data.write_result(i,json.dumps(res.json(),indent=2,ensure_ascii=False))
                    fail_count.append(i)
                    # print(res.json())
                # print(json.dumps(res.json(),indent=2,ensure_ascii=False))
        print(len(pass_count))
        print(len(fail_count))
        
if __name__ == "__main__":
    a = RunTest()
    a.go_on_run()


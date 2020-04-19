#coding:utf-8
# vscode读取不到了包路径解决方案
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

import re
from common.myconfig import conf
class CaseData():
    ''''这个类专门用来保存,用例执行过程中提取出来,给其他用例用的数据'''
    pass
def replace_data(s):
    r1= r"#(.+?)#"
    while re.search(r1,s):
        res = re.search(r1,s)
        data = res.group()
        key = res.group(1)
        try:
            value = conf.get("test_data",key)
        except Exception:
            value = getattr(CaseData,key)
        finally:
            s = re.sub(data,value,s,1)
    return s
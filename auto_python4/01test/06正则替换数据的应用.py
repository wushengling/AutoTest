#coding:utf-8
# vscode读取不到了包路径解决方案
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

import re
from common.myconfig import conf
# s = '{"mobile_phone":"#phone#","pwd":"#pwd#","type":1,"reg_name":"34254sdfs"}'
#使用字符串的替换方法进行替换
# s = s.replace("#phone#", conf.get("test_data","phone"))
# s = s.replace("#pwd#", conf.get("test_data","pwd"))
# print(s)

# s = '{"mobile_phone":"#phone#","pwd":"#pwd#","type":1,"reg_name":"34254sdfs"}'
# r1= r"#(.+?)#"
# res = re.search(r1,s)
# data = res.group()
# key = res.group(1)
# # print(data)
# # print(key)
# s = s.replace(data, conf.get("test_data",key))
# print(s)
# res = re.search(r1,s)
# data = res.group()
# key = res.group(1)
# s = s.replace(data, conf.get("test_data",key))
# print(s)


s = '{"mobile_phone":"#phone#","pwd":"#pwd#","type":1,"reg_name":"34254sdfs"}'
def replace_data(s):
    r1= r"#(.+?)#"
    while re.search(r1,s):
        res = re.search(r1,s)
        data = res.group()
        key = res.group(1)
        s = s.replace(data, conf.get("test_data",key))
    return s
s = replace_data(s)
print(s)

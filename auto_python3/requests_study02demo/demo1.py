#coding:utf-8
# vscode读取不到了包路径解决方案
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

from common.handlepath import DATADIR
from requests_study02demo.handlerequset import SendRequest
from common.excel import OperationExcel

base_url = "http://api.lemonban.com/futureloan"

data = OperationExcel(os.path.join(DATADIR,"apicases.xlsx"),"login")
cases = data.read_excel()
method = cases[0]["method"]
url = base_url+cases[0]["url"]
data = eval(cases[0]["data"])
headers = {
    "X-Lemonban-Media-Type":"lemonban.v1"
}
res = SendRequest.send_request(url=url,mehtod=method,json=data,headers=headers)
print(res.json())

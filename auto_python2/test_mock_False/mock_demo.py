#coding:utf-8
from mock import mock
# 读取不到了路径解决方案
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from base.demo1 import RunMain
def mock_test(mock_method,request_body,method,response_data):
    mock_method = mock.Mock(response_data)
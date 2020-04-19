'''
 AUTH:RODDY
 DATE:2020/2/16
 TIME:15:25
 FILE:run_all.py
 '''
import unittest
import os
from common.dirpath import TESTCASEPATH,REPORTPATH
from libray.HTMLTestRunner_cn import HTMLTestRunner
from common.config import conf
suit = unittest.TestSuite()

loader= unittest.TestLoader()

suit.addTest(loader.discover(TESTCASEPATH))

runner= HTMLTestRunner(stream=open(os.path.join(REPORTPATH,conf.get('report','name')),'wb'),
                       title=conf.get('report','title'),
                       description=conf.get('report','title'))
runner.run(suit)



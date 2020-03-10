#coding:utf-8
"""
"""
import openpyxl
wb = openpyxl.load_workbook(r"C:\wsl\AutoTest\python2\unittest框架\excel_test\demo1\cases.xlsx")
sh = wb["login"]

datas = list(sh.rows)

title = [i.value for i in datas[0]]
cases = []
for i in datas[1:]:
    values = [c.value for c in i]
    print(values)
    case = dict(zip(title,values))
    cases.append(case)
print(cases)
    
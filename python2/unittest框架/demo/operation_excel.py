#coding:utf-8
"""
"""
import openpyxl
class OperationExcel(object):
    def __init__(self,filename,sheet_name):
        self.filename = filename
        self.wb = openpyxl.load_workbook(self.filename)
        self.sh = self.wb[sheet_name]
        
    def read_excel(self):
        datas = list(self.sh.rows)
        title = [i.value for i in datas[0]]
        cases = []
        for i in datas[1:]:
            values = [j.value for j in i]
            # print(values)
            case = dict(zip(title,values))
            cases.append(case)
        return cases
    
    def write_excel(self,row,column,value):
        self.sh.cell(row=row,column=column).value=value
        self.wb.save(self.filename)

if __name__ == '__main__':
    a = OperationExcel(filename =r"C:\wsl\AutoTest\python2\unittest框架\excel_test\demo1\cases.xlsx",sheet_name = "login")
    print(a.read_excel())
    a.write_excel(row=6,column=6,value="66666666")
    
    
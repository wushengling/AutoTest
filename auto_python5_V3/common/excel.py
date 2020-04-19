#coding:utf-8
"""
操作excel类
"""
import openpyxl

class OperationExcel(object):
    def __init__(self,filename,sheet_name):
        self.filename = filename
        self.sheet_name = sheet_name
        
    def open_excel(self):
        #读取excel文件,返回一个工作薄对象
        self.wb = openpyxl.load_workbook(self.filename)
        #选取工作薄中的表单
        self.sh = self.wb[self.sheet_name]
        
    def read_excel(self):
        self.open_excel()
        #获取表单中所有格子中的数据
        datas = list(self.sh.rows)
        #获取第一列的数据的value值
        titles = [i.value for i in datas[0]]
        cases=[]
        for i in datas[1:]:
            data = [j.value for j in i]
            case = dict(zip(titles,data))
            cases.append(case)
        return cases
    
    def write_excel(self,row,column,value):
        self.open_excel()
        self.sh.cell(row=row,column=column).value=value
        self.wb.save(self.filename)
    
# if __name__ == '__main__':
#     a = OperationExcel(r"C:\wsl\AutoTest\auto_python3\data\cases.xlsx","login")
#     b = a.read_excel()
#     # a.write_excel(9,9,123456)
#     print(b)
    
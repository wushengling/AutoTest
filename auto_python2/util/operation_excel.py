#coding:utf-8
import xlrd
'''
# 设置excel路径
path = "D:\\Testing tools\\muke\\AutoTest\\auto_python2\\dataconfig\\interface.xlsx"

# 打开excel
data = xlrd.open_workbook(path)

# 通过索引获取获取sheet内容
tables = data.sheets()[0]  #0开始

# 获取sheet行数
print(tables.nrows)  
# 获取sheet列数
print(tables.ncols)
#获取单元格内容
print(tables.cell_value(2,3))  #(行,列) 0开始
print(tables.cell_value(1,2))
print(tables.cell_value(2,2))
'''

class OperationExcel:
    def __init__(self,file_name=None,sheet_id=None):
        if file_name:
            self.file_name = file_name        
            self.sheet_id = sheet_id
        else:
            self.file_name = "D:\\Testing tools\\muke\\AutoTest\\auto_python2\\dataconfig\\interface.xlsx"
            self.sheet_id = 0
        self.data = self.get_data()
    #获取sheets的内容
    def get_data(self):
        data = xlrd.open_workbook(self.file_name)
        tables = data.sheets()[self.sheet_id]
        return tables
    #获取单元格的行数
    def get_lines(self):
        return self.data.nrows
    #获取某一个单元格的内容
    def get_value(self,row,col):
        return self.data.cell_value(row,col)
        
        
if __name__ == '__main__':
    opers = OperationExcel()
    #获取单元格的行数
    print(opers.get_lines())
    #获取某一个单元格的内容
    print(opers.get_value(1,1))
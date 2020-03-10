#coding:utf-8
import json
class OperetionJson:
    def __init__(self):
        self.data = self.read_data()
    #读取json文件
    def read_data(self):
        path = "C:\\wsl\\AutoTest\\auto_python2\\dataconfig\\test.json"
        with open(path) as fp :
            data = json.load(fp)
            return data
    
    #根据关键字获取数据
    def get_data(self,id):
        if id != None:
            return self.data[id]
        return None
    
    #写json
	def write_data(self,data):
		with open('C:\\wsl\\AutoTest\\auto_python2\\dataconfig\\header.json','w') as fp:
			fp.write(json.dumps(data))
        
if __name__ == '__main__':
    a = OperetionJson() 
    print(a.get_data(None))


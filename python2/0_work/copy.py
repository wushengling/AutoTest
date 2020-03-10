#coding:utf-8
import os
def copy_file(path):
    try:
        file_list = os.listdir(path)
    except:
        print("路径输入有误")
    else:
        for i in file_list:
            file_path = os.path.join(path,i)
            if os.path.isfile(file_path):
                with open(file_path,"r",encoding="utf-8") as f:
                    content = f.read()
                copy_path = os.path.join(os.path.dirname(__file__),"cp"+i)
                with open(copy_path,"a",encoding="utf-8") as f:
                    f.write(content)

if __name__ == '__main__':
    copy_file(r"C:\wsl\AutoTest\python2\函数")
    
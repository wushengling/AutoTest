#coding:utf-8
def login_check(username=None,password=None):
    if username != None and password != None:
        if username == "root" and password == "123456":
            return {"code":0,"msg":"登录成功"}
        else:
            return {"code":1,"msg":"用户名或密码错误"}
    else:
        return {"code":1,"msg":"所有的参数不能为空"}
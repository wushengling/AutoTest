#coding:utf-8
def login_check(username=None,password=None):
    if username != None and password != None:
        if username == "root" and password == "123456":
            return {"code":0,"msg":"登录成功"}
        else:
            return {"code":1,"msg":"用户名或密码错误"}
    else:
        return {"code":1,"msg":"所有的参数不能为空"}
    

# a = login_check("root","123456")
# print(a)
# res = a
# expected = {"code":0,"msg":"登录成功"}

#断言 assert 条件语句
"""
断言条件不通过,会报错(断言异常)
断言添加通过,不会有任何返回,直接执行下一行代码
"""
# assert res == expected
# print("断言通过")
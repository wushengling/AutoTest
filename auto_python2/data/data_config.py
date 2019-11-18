#coding:utf-8
class global_var:
    #case_id
    Id = 0
    name = 1
    url = 2
    run = 3
    request_way = 4
    header = 5
    id_depend = 6
    data_depend = 7
    field_depend = 8
    data = 9
    expect = 10
    result = 11
#获取case_id
def get_id():
    return global_var.Id
#获取获取名称
def get_name():
    return global_var.name
#获取url
def get_url():
    return global_var.url
#获取是否执行
def get_run():
    return global_var.run
#获取请求方式
def get_request_way():
    return global_var.request_way
#获取是否携带header
def get_is_header():
    return global_var.header
#获取header值
def get_header_value():
    header = {
            'Content-Type':'application/json',
            "Accept": "*/*"
            }
    return header
#获取依赖id
def get_id_depend():
    return global_var.id_depend
#获取依赖数据
def get_data_depend():
    return global_var.data_depend
#获取依赖数据所需字段
def get_field_depend():
    return global_var.field_depend
#获取请求数据关键字
def get_data():
    return global_var.data
#获取预期结果
def get_expect():
    return global_var.expect
    
if __name__ == "__main__":
    print(type(get_request_way()))
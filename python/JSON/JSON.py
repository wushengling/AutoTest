# JavaScript Object Notation
#  JavaScript 对象标记
# 是一种轻量级的数据交换格式
# 字符串是JSON的表现形式

import json
# 反序列化
json_str = '{"name":"zhangsan","age":18,"flag":false}'
student = json.loads(json_str)
print(type(student))    # dict
print(student)
print(student['name'])
print(student['age'])

json_str1 = '[{"name":"zhangsan","age":18,"flag":false},{"name":"zhaosi","age":17,"flag":false}]'
students = json.loads(json_str1)
print(type(students))
print(students[1]['name'])


#coding:utf-8
import random
#生成0-1之间的随机数
a = random.random()
print(a)
#在指定范围内，生成一个整数（包括范围的边界值）
b = random.randint(1,3)
print(b)


a = """你"""
b = "好"
c = '吗'
print(a+b+c)
#join() 拼接字符串
d = "_".join((a,b,c))
print(d)

f = "adjaskda\\nasdasd\\t"
print(f)
#在字符串前面使用r  不会进行转译 用于路径
e = r"adjaskda\nasdasd\t"
print(e)
#格式化输入 format()
s1 = "我是{}，今年{}，性别{}".format('小红',18,'女')
print(s1)
#format()高级用法
#下标来控制传入的数据,显示位置
s2 = "我是{1}，今年{2}，性别{0}".format('小红',18,'女')
print(s2)
#可以指定占的位置的长度  <>^来控制左右居中显示
s3 = "sdasda:{:^10}asdsad".format(123)
print(s3)

#最好用的一种,目前不流行,F表达式
age = 18
sex = "男"
name = "小明"
a1 = F"年龄:{age},性别:{sex},姓名:{name}"
print(a1)


#列表插入元素
li = [1,2,3]
#append 插入到列表的尾部
li.append(999)
#insert 插入到指定位置
li.insert(0,666)
#extend : 一次性插入多个数据到列表尾部
li.extend([11,22,33,44])

#列表删除元素
#remove 删除指定的元素
li.remove(1)
#pop 根据下标删除对应的元素 不传参数,默认为最后一个
li.pop(1)
#clear  清空列表
li.clear()
print(li)

#元组 ()
#元组只有一个元素,(11,)
#元组只能读取,不能修改

#字典 {}
#每一个元素都是有一个键值对(key : value)组成
#key 不能重复,只能是不可变类型的数据(字符串,数值,元组),建议key使用字符串
#value 可以为任意类型的数据

user_info = {"name" : "张三" , "age" : 18 , "gender" : "男"}
#第二种表达
#user_info = dict(name="张三",age=18,gender="男")
print(type(user_info))
#查找,查找不到报错
res1 = user_info['name']
#get查找不到返回none
res2 = user_info.get('name1')
print(res1,res2)

#获取字典中所有的键
res3 =list(user_info.keys())
print(res3)
#获取字典中所有的值
res4 =list(user_info.values())
print(res4)
#获取字典中的键值对
res5 = list(user_info.items())
print(res5)
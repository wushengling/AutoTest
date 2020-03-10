#coding:utf-8
# li = [11,22,33,44,55,66,77]
# res = max(li)#获取最大值
# res1 = min(li)#获取最小值
# res2 = sum(li)#求和
# print(res,res1,res2)

#高级内置函数
# enumerate 获取目标内所有的元素和下标值
li = [11,22,33,44,55,66,77]
res = enumerate(li)
for i in res :
    print(i)


#eval:识别字符串中有效的python表达式
str1 = "{'a':11,'b':22}"
str2 = "[11,22,33,44]"
#str1转换为字典,str2转换为列表
dic1 = eval(str1) #==={'a':11,'b':22}
li2 = eval(str2)  #===[11,22,33,44]
print(dic1,type(dic1))
print(li2,type(li2))

a = 100
b = 10
s1 = "a>b"
print(eval(s1),s1)

#zip:聚合打包  以最短的稳准,多余的去掉
#注意点:zip打包之后返回的数据,只能使用一次
# li = [1,2,3,4]
# li2 = [11,22,33,44]
# li3 = [111,222,333,444]
# res =zip(li,li2,li3)
# print(list(res))
#常见应用
# title = ["aa","bb","cc"]
# value = [11,22,33]
# res = zip(title,value)
# print(dict(res))
#例子
users_title = ["name","age","gender"]
users_info = [['小明',18,'男'],['小李',19,'男'],['小红',17,'女']]
users = []
def func(users_title,users_info):
    for i in users_info:
        data = zip(users_title,i)
        users.append(dict(data))
func(users_title,users_info)
print(users)

#filter:过滤器
#第一个参数是一个函数
#第二个参数是可迭代对象
#iterable 
#可以使用for循环进行遍历的都是可迭代对象
# 可迭代对象 字符串,元组,字典,range创建的数据

# def a(a):
#     if a>13:
#         return a
# b = [12,13,14,15]
# res = filter(a,b)
# print(list(res))

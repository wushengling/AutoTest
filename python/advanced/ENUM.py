# 枚举  标签  常量
# 不可变
# 不能出现相同标签
from enum import Enum
from enum import IntEnum,unique   #值必须为int类型    

class VIP(Enum):
    YELLOW = 1
    YELLOW_ALIAS =1
    GREEN = 2
    BLACK = 3
    RED = 4
#别名
class Common():
    YELLOW = 5
print(Common.YELLOW)

# 枚举类型,枚举名字,枚举的值
print(VIP.YELLOW)  
print(VIP.YELLOW.value)
print(VIP['YELLOW']) 
print(VIP.YELLOW.name)

for v in VIP:
    print(v)

for v1 in VIP.__members__:
    print(v1)

# 身份比较  ==  is  
# 不能做大小比较 <> 

#枚举的转换
a = 1
print(VIP(a))



'''
注意事项:
    不能出现相同标签
    别名不会被遍历出来
    
'''
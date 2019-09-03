#返回多个值
def damage(skill1,skill2):
    damage1 = skill1*2
    damage2 = skill2*3
    return damage1,damage2

# A = damage(1,1)
# print(type(A))   #返回为元组
# print(A[0])
# print(A[1])

#序列解包
#元素的个数要相等

skill1_damage1,skill2_damage2 = damage(1,1)
print(skill1_damage1,skill2_damage2)

# a = 1 
# b = 2
# c = 3
# a,b,c = 1,2,3

d = 1,2,3
a,b,c = d

#链式赋值
a=b=c=1


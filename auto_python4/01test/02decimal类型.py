#coding:utf-8
from decimal import Decimal
t =1.1
t2 = 9.3
print(t,type(t))
#浮点数进行相减,小数位会出现精度问题
print(t2-t)

d1 = Decimal("9.3")
d2 = Decimal("1.1")
d3 = d1-d2
print(d3,type(d3))

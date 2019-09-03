import one.demo1 as t
print(t.a)

from one.demo1 import a
print(a)

from one import demo1
print(demo1.a)

from one.demo1 import *
print(a)
print(b)
# print(c)

from one.demo1 import a,b,c
print(a)
print(b)
print(c)
 
import one

from one.demo1 import a

from one import *
print(demo2.d)

import one
print(one.sys.path)


#包和模块是不会被重复导入的

#避免循环导入(引用),文件循环引用

#入口文件的概念
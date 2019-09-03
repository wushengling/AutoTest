#字符集
import re
a = 'abc,acc,adc,aec,afc,ahc'

r = re.findall('a[cfd]c',a)   #中间为c或者为f或者为d
print(r)

r1 = re.findall('a[^c-f]c',a) #取反  ^
print(r1)


# group 组
import re 

a = 'life is short,i use python i love python'

r = re.search('life(.*)python(.*)python',a)
print(r.group(0,1,2))
print(r.groups())

r1 = re.findall('life(.*)python(.*)python',a)
print(r1)




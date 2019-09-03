#匹配模式
import re
a = 'PythonC#JavaPHP'
r = re.findall('c#',a,re.I | re.S)  # re.I 不区分大小写   re.S 
print(r)
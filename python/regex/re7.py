#组
import re
a = 'PythonPythonPythonPythonPython'
r = re.findall('(Python){6}',a)
print(r)
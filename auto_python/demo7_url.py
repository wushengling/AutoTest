#coding:utf-8
import urllib.parse
# import urllib
a = "中文"
b = urllib.parse.quote(a)   #转url编码
print(b)
url = "http://zzk.cnblogs.com/s/blogpost?Keywords=%s"%b
print(url)

import requests
# requests 自动转
r = requests.get("http://zzk.cnblogs.com/s/blogpost?Keywords=%s"%a)
print(r.url)

# url 解码
c = "%E4%B8%AD%E6%96%87"
d = "NGlZ7gInT8Lqg0tnETU1Pw=="
print(urllib.parse.unquote(d))
print(urllib.parse.unquote(r.url))

import base64
print(base64.b64encode(d))
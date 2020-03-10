import json
import re
class test1:
    def test(self,data):
        a = {"id":123}
        b = re.findall('"id":(.+?),',a.text)[0]
        
if __name__ == '__main__':
    a = test1()
    a.test("sms_code")
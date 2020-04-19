'''
 AUTH:RODDY
 DATE:2020/2/22
 TIME:21:20
 FILE:test_ram.py
 '''
import random
data='{"mobile_phone":#phone#,"pwd":"12345688","reg_name":"mmc"}'
####phone#

def telnum():
    ram=(random.randint(100000000,999999999))
    ram_str=str(ram)[0:8]
    tel='136'+ram_str
    return tel
print(telnum())
data=data.replace('#phone#',telnum())
print(data,type(data))
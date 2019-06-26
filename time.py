# -*- coding: utf-8 -*-
'''
Created on 25.06.2019

@author: yu03
'''


import datetime
import time
import pytz

now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print('Local time:     ', now)

now_utc = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
print('UTC time:      ', now_utc)

timezone = pytz.timezone('Asia/Shanghai')
now_timezone = datetime.datetime.now(timezone).strftime("%Y-%m-%d %H:%M:%S")
print('China time:     ', now_timezone)

# timestamp = int(time.time())
timestamp = 1561564380
print('Timestamp:     ', timestamp)

time = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
print('Convert Local:     ', time)
 
time_utc = datetime.datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
print('Convert UTC:     ', time_utc)

timezone = pytz.timezone('Asia/Harbin')
time_timezone = datetime.datetime.fromtimestamp(timestamp, tz=timezone).strftime('%Y-%m-%d %H:%M:%S')
print('China time:     ', time_timezone)

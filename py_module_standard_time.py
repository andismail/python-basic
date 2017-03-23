import time as _time

# measure of how fast your program is running
print(_time.clock() - _time.clock())
#
# time tuple
y, m, d, hh, mm, ss, weekday, jday, dst = _time.localtime(595785600)
print(y, m, d)  # 1988 11 18
type(_time.localtime(595785600))  # <class 'time.struct_time'>
#
# timestamp
_time.time()  # 1490257660.435193
#
# get format string from time
_time.strftime('%Y-%m-%d', _time.localtime(595785600))  # 1988-11-18 <class 'str'>
_time.strftime('%Y-%m-%m')  # 2017-03-03 (default current time)
#
# format string parse to time
fs3 = _time.strptime('1988-11-18', '%Y-%m-%d')
# time.struct_time(tm_year=1988, tm_mon=11, tm_mday=18, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=4, tm_yday=323, tm_isdst=-1) <class 'time.struct_time'>
#
# convert timestamp to time str
_time.ctime(595785600)  # Fri Nov 18 00:00:00 1988 <class 'str'>
#
# convert time tuple to time str
_time.asctime((y, m, d, hh, mm, ss, weekday, jday, dst))  # <class 'time.struct_time'>
#
#
#
#
#
#
#
from datetime import time as _d_time

dt1 = _d_time(18, 0, 1)  # 18:00:01 <class 'datetime.time'>
print(dt1.hour, dt1.minute, dt1.second)  # 18 0 1
print(dt1.max, dt1.min)  # 23:59:59.999999 00:00:00
dt2 = dt1.replace(hour=19)  # 19:00:01, return a new time

#
#
#
#
#
#
#
from datetime import date as _date

#
# construct a date
d1 = _date(2017, 3, 23)  # 2017-03-23 <class 'datetime.date'>
print(d1.year, d1.month, d1.day)  # 2017 3 23
d1.isoformat()  # 2017-03-23
d1.__format__('%Y/%m/%d')  # 2017/03/23 <class 'str'>
d1.weekday()  # (周)3
d1.isoweekday()  # (周)4
#
# use timestamp construct date
_date.fromtimestamp(_time.time())  # 2017-03-23 <class 'datetime.date'>
#
# date of today
_date.today()  # 2017-03-23 <class 'datetime.date'>
#
#
#
#
#
#
#

from datetime import datetime as _datetime

_datetime(2017, 3, 23, 18, 23, 19)

now = _datetime.now()
print(now.strftime('%Y-%m-%d %H:%M:%S'))
print('now', now)
print(now.time())
print(now.date())
print(_datetime.today())
#
#
#
#
#
#
from datetime import timedelta as _timedelta

d01 = _datetime(2017, 1, 1)
d02 = _datetime.now()
t01 = d02 - d01  # 81 days, 18:13:11.699427 <class 'datetime.timedelta'>
print(t01.days)  # 81
print(d02 > d01)  # True
ttt = _timedelta(days=40)
d01 + ttt  # 2017-02-10 00:00:00 <class 'datetime.datetime'>

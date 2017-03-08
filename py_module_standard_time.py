import time

sz = 10000000
td = range(sz)
t0 = time.clock()
su = sum(td)
t1 = time.clock()
print(t1 - t0) # measure of how fast your program is running
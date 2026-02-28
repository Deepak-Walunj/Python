import time
print(time.time())
print(time.localtime(100))
print(time.gmtime(100))
t=time.localtime()
f=time.strftime("%Y-%m-%d %H:%M:%S", t)
time.sleep(3)
print(f)
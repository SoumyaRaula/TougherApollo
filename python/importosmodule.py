import os
import datetime 
import sys
print(os.getcwd())
print(os.listdir())
print(datetime.datetime.fromtimestamp(os.stat('my_module.py').st_mtime))

for t, l, k in os.walk(sys.path[0]):
    print ('{} {} {}'.format(t,l,k))


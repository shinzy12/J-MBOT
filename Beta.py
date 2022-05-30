import os, platform
os.system('git pull')
try:
    import requests
except:
    os.system('pip2 install requests')

import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from justnow import bnsbuy
    bnsbuy()
elif bit == '32bit':
    os.system('clear')
    exit('\x1b[0;91m[*] Your Mobile Not Support This Tools \n Try Another Tools')

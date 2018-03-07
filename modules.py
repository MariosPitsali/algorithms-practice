#problems with time,date 1) timezones 2)daylight savings
#store dates as UTC instead of local time, unless you wanna use it only in your country (dumm)

import time
import datetime

print(time.gmtime(0))
print (time.localtime(time.time()))
time_now = time.localtime()
print ("year now is %4d for %2d" %(time_now[0], 20))
months = {1:"January",
          2: "Febrauary",
          3: "March",
         4:"April",
         5:'May'}
print (time_now[1] in months.keys())
print ("month now is %s" %(months.get(time_now[1])))

metallica = "Metallica", 'No Life Till Leather', 1981, ("Hit The Lights", 1), ("No Remorse", 2)
print (metallica)




import time


# Current time seconds since epoch
# currtime = time.time()
# print(currtime)

# Complete Current time
currtime = time.ctime()
print(currtime)

currtime = time.strftime('%H:%M:%S')
print(currtime)

currHour = int(currtime[0:2])
currHourOld = int(time.strftime('%H'))
print(currHourOld)
print(type(currHour))

if(currHourOld<12):
    print("Good Morning Sir")
elif(currHourOld>12 and currHourOld<17):
    print("Good Afternoon Sir")
else:
    print("Good Evening Sir")



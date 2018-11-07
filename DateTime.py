#TICK
#Floating-point numbers in units of seconds for time interval are indicated by Tick in python. They are expressed in seconds since 12.00am, Jan 1, 1970(epcoh).
#The function time.time() returns the current system time in ticks since 12:00am, Jan 1, 1970(Epoch).
import time
ticks=time.time()
print("Number of ticks since 12:00am, Jan 1,1970",ticks)

#TIME TUPLE
#Python's time functions handle time as a tuple of 9 numbers:
